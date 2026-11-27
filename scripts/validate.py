#!/usr/bin/env python3
"""Zero-dependency structural, parity, and hygiene validator for Awesome Antigravity Plugins."""

from __future__ import annotations

import argparse
from collections import Counter
import concurrent.futures
from pathlib import Path
import re
import sys
import unicodedata
import urllib.parse
import urllib.request

ROOT = Path(__file__).resolve().parent.parent

REQUIRED_FILES = [
    "README.md",
    "README_CN.md",
    "CONTRIBUTING.md",
    "LICENSE",
    "assets/banner.svg",
    ".github/ISSUE_TEMPLATE/submit-plugin.yml",
    ".github/PULL_REQUEST_TEMPLATE.md",
    ".github/workflows/validate.yml",
]

# Repositories staged locally by the maintainer prior to public GitHub push.
PENDING_PUBLIC_URLS: set[str] = set()

HEADING_RE = re.compile(r"^(#{2,3})\s+(.+?)\s*$", re.MULTILINE)
BULLET_RE = re.compile(
    r"^- \*\*\[([^\]]+)\]\((https://[^)]+)\)\*\*(?:\s*(?:\(|（)\[(?:Repo|源码仓库|源码)\]\((https://[^)]+)\)(?:\)|）))?\s+—\s+(.+)$"
)
TABLE_ROW_RE = re.compile(
    r"^\|\s*\*\*([^*]+)\*\*\s*\|\s*`((?:antigravity-plugins-(?:official|partners))/plugin/[a-z0-9_-]+)`[^|]*\|\s*(.+?)\s*\|$"
)
ANCHOR_LINK_RE = re.compile(r"\]\(#([^)]+)\)")
BADGE_EN_RE = re.compile(r"badge/curated-(\d+)%2B%20plugins")
BADGE_CN_RE = re.compile(r"badge/已收录-(\d+)%2B%20精选插件")


def github_slug(heading: str) -> str:
    """Compute GitHub-compatible Markdown heading anchor slug."""
    text = re.sub(r"`([^`]*)`", r"\1", heading.strip()).lower()
    out: list[str] = []
    for ch in text:
        if ch == " ":
            out.append("-")
        elif ch in "-_":
            out.append(ch)
        else:
            cat = unicodedata.category(ch)
            if cat.startswith(("L", "N")):
                out.append(ch)
    return "".join(out)


def parse_readme(path: Path, errors: list[str]) -> dict:
    raw = path.read_text(encoding="utf-8")
    lines = raw.splitlines()
    name = path.name

    headings: list[tuple[str, str, str]] = []
    slug_counts: Counter[str] = Counter()
    slugs: set[str] = set()
    for m in HEADING_RE.finditer(raw):
        level, title = m.group(1), m.group(2)
        base_slug = github_slug(title)
        idx = slug_counts[base_slug]
        slug_counts[base_slug] += 1
        final_slug = base_slug if idx == 0 else f"{base_slug}-{idx}"
        headings.append((level, title, final_slug))
        slugs.add(final_slug)

    # Check internal anchor links
    for anchor in ANCHOR_LINK_RE.findall(raw):
        decoded = urllib.parse.unquote(anchor)
        if decoded not in slugs and anchor not in slugs:
            errors.append(f"[{name}] Broken internal TOC/anchor link: #{anchor}")

    bullets: list[tuple[int, str, str]] = []
    table_rows: list[tuple[int, str, str]] = []
    all_http_urls: set[str] = set()

    for lineno, line in enumerate(lines, start=1):
        for u in re.findall(r"https?://[^\s)>\]\"']+", line):
            if "<" not in u and ">" not in u and "..." not in u:
                all_http_urls.add(u)

        if line.startswith("- **["):
            bm = BULLET_RE.match(line)
            if not bm:
                errors.append(
                    f"[{name}:{lineno}] Malformed plugin bullet (expected `- **[Name](https://...)** — Description`): {line[:90]}"
                )
            else:
                title = bm.group(1)
                primary_url = bm.group(2).rstrip("/")
                repo_override = (bm.group(3) or "").rstrip("/")
                canonical = (repo_override or primary_url).lower()
                bullets.append((lineno, title, canonical))

        elif line.startswith("| **"):
            tm = TABLE_ROW_RE.match(line)
            if not tm:
                errors.append(
                    f"[{name}:{lineno}] Malformed Marketplace table row: {line[:90]}"
                )
            else:
                table_rows.append((lineno, tm.group(1), tm.group(2)))

        # Catch accidental blank lines right between two plugin bullets or blank-less transitions
        if line.strip() == "---" and lineno >= 3:
            if lines[lineno - 2].strip() != "":
                errors.append(f"[{name}:{lineno}] Missing blank line before `---` divider.")
            if lineno >= 4 and lines[lineno - 3].strip() == "":
                errors.append(f"[{name}:{lineno}] Consecutive blank lines before `---` divider.")

    # Check duplicates within file
    bullet_counts = Counter(url for _, _, url in bullets)
    for url, count in bullet_counts.items():
        if count > 1:
            errors.append(f"[{name}] Duplicate community plugin repository URL ({count}x): {url}")

    catalog_counts = Counter(cid for _, _, cid in table_rows)
    for cid, count in catalog_counts.items():
        if count > 1:
            errors.append(f"[{name}] Duplicate Marketplace Catalog ID ({count}x): {cid}")

    return {
        "raw": raw,
        "headings": headings,
        "bullets": bullets,
        "table_rows": table_rows,
        "all_http_urls": all_http_urls,
    }


def check_url(url: str) -> tuple[str, int | str]:
    req = urllib.request.Request(
        url,
        method="HEAD",
        headers={"User-Agent": "awesome-antigravity-plugins-validator/1.0"},
    )
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            return url, resp.status
    except Exception:
        req_get = urllib.request.Request(
            url,
            method="GET",
            headers={"User-Agent": "awesome-antigravity-plugins-validator/1.0"},
        )
        try:
            with urllib.request.urlopen(req_get, timeout=10) as resp:
                return url, resp.status
        except Exception as exc:
            return url, str(exc)


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate Awesome Antigravity Plugins")
    parser.add_argument(
        "--check-links",
        action="store_true",
        help="Also verify live HTTP reachability of external URLs",
    )
    args = parser.parse_args()

    errors: list[str] = []

    for rel in REQUIRED_FILES:
        if not (ROOT / rel).is_file():
            errors.append(f"Missing required repository file: {rel}")

    if errors:
        for err in errors:
            print(f"ERROR: {err}", file=sys.stderr)
        return 1

    en = parse_readme(ROOT / "README.md", errors)
    cn = parse_readme(ROOT / "README_CN.md", errors)

    # Structural & entry parity checks between README.md and README_CN.md
    en_levels = [lvl for lvl, _, _ in en["headings"]]
    cn_levels = [lvl for lvl, _, _ in cn["headings"]]
    if en_levels != cn_levels:
        errors.append(
            f"[Parity] Heading structure mismatch: README.md has {len(en_levels)} headings vs README_CN.md {len(cn_levels)}."
        )

    en_urls = [u for _, _, u in en["bullets"]]
    cn_urls = [u for _, _, u in cn["bullets"]]
    if set(en_urls) != set(cn_urls):
        only_en = sorted(set(en_urls) - set(cn_urls))
        only_cn = sorted(set(cn_urls) - set(en_urls))
        if only_en:
            errors.append(f"[Parity] Repos in README.md but missing from README_CN.md: {only_en}")
        if only_cn:
            errors.append(f"[Parity] Repos in README_CN.md but missing from README.md: {only_cn}")
    elif en_urls != cn_urls:
        for idx, (u_en, u_cn) in enumerate(zip(en_urls, cn_urls), start=1):
            if u_en != u_cn:
                errors.append(
                    f"[Parity] Entry order mismatch at bullet #{idx}: README.md has {u_en} vs README_CN.md {u_cn}"
                )
                break

    en_cids = [c for _, _, c in en["table_rows"]]
    cn_cids = [c for _, _, c in cn["table_rows"]]
    if en_cids != cn_cids:
        errors.append(
            f"[Parity] Marketplace Catalog ID list/order mismatch between README.md ({len(en_cids)}) and README_CN.md ({len(cn_cids)})."
        )

    total_entries = len(en["bullets"]) + len(en["table_rows"])
    m_en = BADGE_EN_RE.search(en["raw"])
    m_cn = BADGE_CN_RE.search(cn["raw"])
    if not m_en or not m_cn:
        errors.append("[Badge] Curated count badge missing in README.md or README_CN.md.")
    else:
        b_en, b_cn = int(m_en.group(1)), int(m_cn.group(1))
        if b_en != b_cn:
            errors.append(f"[Badge] Badge floor mismatch: EN={b_en}+ vs CN={b_cn}+.")
        if total_entries < b_en:
            errors.append(
                f"[Badge] Badge claims {b_en}+ plugins, but only {total_entries} entries exist."
            )

    if args.check_links:
        urls_to_check = sorted(
            u
            for u in (en["all_http_urls"] | cn["all_http_urls"])
            if u.rstrip("/").lower() not in PENDING_PUBLIC_URLS
            and not u.startswith("https://img.shields.io/")
            and not u.endswith("/actions/workflows/validate.yml/badge.svg")
        )
        print(f"Checking {len(urls_to_check)} live URLs...")
        with concurrent.futures.ThreadPoolExecutor(max_workers=16) as pool:
            for url, status in pool.map(check_url, urls_to_check):
                if not (isinstance(status, int) and 200 <= status < 400):
                    errors.append(f"[Link] Unreachable URL ({status}): {url}")

    if errors:
        print(f"Validation FAILED with {len(errors)} error(s):", file=sys.stderr)
        for err in errors:
            print(f"  - {err}", file=sys.stderr)
        return 1

    print(
        f"OK: {len(en['bullets'])} community plugins + {len(en['table_rows'])} Marketplace plugins = "
        f"{total_entries} total curated entries (100% EN/ZH parity, {len(en_levels)} headings verified)."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
