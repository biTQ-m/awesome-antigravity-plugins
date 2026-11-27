# Contributing to Awesome Antigravity Plugins

Thank you for helping curate the **Google Antigravity** plugin ecosystem! Contributions in both English and Simplified Chinese are warmly welcome.

---

## Submission Criteria

Before opening a Pull Request or Issue, please verify that the project meets the following standards:

1. **Purpose-Built for Google Antigravity**: The project must ship a valid Antigravity `plugin.json` bundle, Auxiliary Pane / Sidebar `UI Sidecar`, interactive `MCP App` (`ui://`), CLI `statusLine`, `SKILL.md` suite, Lifecycle Hook, or ACP/MCP integration explicitly designed for Antigravity (`agy` CLI or Antigravity 2.0 Desktop/IDE).
2. **Clear Documentation & Install Path**: The repository must include a clear `README.md` with installation steps, supported platforms/runtimes, and an open-source license (or be an official/verified Antigravity Marketplace plugin).
3. **Author Disambiguation**: If your plugin shares a generic name with an existing entry (e.g. `AGY Usage` or `AGY MCP`), append your GitHub handle in parentheses: `**[AGY Usage (\`your-handle\`)](https://github.com/your-handle/agy-usage)**`.
4. **Security & Transparency**:
   - Open-source repositories must have inspectable source code with clear documentation of any local files or settings they touch.
   - Unofficial client patchers (such as localization packs or environment managers) must support clean backup/restore and state their caveats clearly.
   - **Zero tolerance** for malware, credential/token harvesting, or hidden telemetry.

---

## How to Add a Plugin via Pull Request

1. Fork this repository and create a new branch (`git checkout -b add-<plugin-name>`).
2. Add your entry to **both** [`README.md`](./README.md) (English) and [`README_CN.md`](./README_CN.md) (Simplified Chinese) at the **same relative position** under the most fitting category and sub-section.
3. Follow the concise single-bullet format (using an em-dash `—` surrounded by spaces):
   ```markdown
   - **[Plugin Name](https://github.com/owner/repo)** — Concise 1–2 sentence objective description highlighting what it solves and supported platforms. `Sidecar + Skill + MCP`
   ```
   *(If the primary link points to a homepage or configurator, include `([Repo](https://github.com/owner/repo))` in `README.md` and `（[源码仓库](https://github.com/owner/repo)）` in `README_CN.md` immediately before `—`.)*
4. Keep descriptions objective, crisp, and free of marketing superlatives ("the best", "ultimate", "revolutionary", etc.).
5. Run the zero-dependency validator locally before committing:
   ```bash
   python3 scripts/validate.py
   ```
6. Open a Pull Request describing your plugin—screenshots or short demo GIFs are encouraged for UI Sidecars, MCP Apps, and Desktop HUDs!

---

## 中文投稿简明规范

1. **双语同步更新**：请在 [`README.md`](./README.md) 与 [`README_CN.md`](./README_CN.md) 对应分类子标题下的**同一顺序位置**同时补充英文与简体中文条目。
2. **标准单行格式**：使用破折号 ` — `（前后各保留一个半角空格）连接标题与客观简介，并在句末附上扩展形态标签（如 `` `Aux Pane Sidecar + Skill` ``、`` `MCP App + CLI` `` 等），避免主观夸大宣传用语。
3. **本地一键校验**：提交前运行 `python3 scripts/validate.py`，确保双语条目数量、GitHub 仓库 URL 顺序、目录锚点与排版规范 100% 通过校验。
