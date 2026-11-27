<div align="center">

<img src="assets/banner.svg" width="100%" alt="Awesome Antigravity Plugins Banner" />

<br />

[![Awesome](https://awesome.re/badge-flat2.svg)](https://awesome.re)
[![Plugins Curated](https://img.shields.io/badge/curated-170%2B%20plugins-6366f1.svg)](#contents)
[![Validate Curated List](https://github.com/biTQ-m/awesome-antigravity-plugins/actions/workflows/validate.yml/badge.svg)](./.github/workflows/validate.yml)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-10b981.svg)](./CONTRIBUTING.md)
[![License: CC0-1.0](https://img.shields.io/badge/License-CC0%201.0-f59e0b.svg)](./LICENSE)

**English** · [简体中文](./README_CN.md)

*A curated directory of open-source plugins, Auxiliary Pane UI sidecars, interactive MCP Apps, macOS/Desktop HUDs, CLI statuslines, multi-agent workflows, and official Marketplace extensions for **Google Antigravity (`agy` CLI & Antigravity 2.0 Desktop/IDE)**.*

</div>

---

> [!NOTE]
> **What is an Antigravity Plugin?**
> In Google Antigravity, a **plugin** (`plugin.json`) is a single namespaced bundle that installs, enables, and disables as one unit—combining **UI Sidecars** (`sidecars/`), **Interactive MCP Apps** (`ui://` resources rendered inline, in `aux_pane`, or full-page in `global`), **Skills** (`skills/<name>/SKILL.md`), **MCP Servers** (`mcp_config.json`), **Lifecycle Hooks** (`hooks.json`), **Rules** (`rules/AGENTS.md`), and **Subagents** (`agents/`).

## Contents

- [Desktop UI, Auxiliary Pane & HUDs](#desktop-ui-auxiliary-pane--huds)
- [Telemetry, Context Window & Statuslines](#telemetry-context-window--statuslines)
- [Performance, Memory, Workflow & Swarm Orchestration](#performance-memory-workflow--swarm-orchestration)
- [Browser, Computer Use & Creative Automation](#browser-computer-use--creative-automation)
- [Cross-Agent Bridges, ACP & Remote Control](#cross-agent-bridges-acp--remote-control)
- [Official & Partner Marketplace Catalog](#official--partner-marketplace-catalog)
  - [Google Ecosystem, Cloud & Science](#google-ecosystem-cloud--science)
  - [Databases, Cloud & App Platforms](#databases-cloud--app-platforms)
  - [Observability, Security, Code Review & Testing](#observability-security-code-review--testing)
  - [Design, Productivity, Search & Business](#design-productivity-search--business)
- [Skill Suites & Plugin Authoring Toolkits](#skill-suites--plugin-authoring-toolkits)
- [Environment & Multi-Account Managers](#environment--multi-account-managers)
- [Localization, Themes & Accessibility](#localization-themes--accessibility)
- [Quick Install & Plugin Anatomy](#quick-install--plugin-anatomy)
- [Contributing](#contributing)

---

## Desktop UI, Auxiliary Pane & HUDs

*Native `UI Sidecar` (`SIDECAR_UI_ENTRYPOINT_AUX_PANE` & `SIDEBAR`) workbenches, interactive `MCP Apps`, macOS Dynamic Island HUDs, voice triggers, and desktop enhancements built for Antigravity 2.0.*

### Native HUDs, Voice & Workspace Launchers

- **[AGY Floating HUD](https://github.com/biTQ-m/agy-floating-hud)** — Always-on-top macOS Dynamic Island & multi-beacon (`NSPanel`) HUD for Antigravity 2.0 Desktop: adapts automatically between native MacBook Notch G1 fusion (`e05`) and external-display floating obsidian capsules (`island`) with magnetic drag & re-docking, offers 12 dual-state `Active × Done` micro-beacons (`E01`–`E10`), 120Hz single-shell liquid hover morph (`M1`–`M4`), 3 style modes × 5 liquid-glass themes, read-only SQLite WAL multi-session tracking, `<5ms` session jump, and an Auxiliary Pane Control Center + `floating-hud` Skill. `macOS` `Swift + Sidecar + Skill + Hooks`
- **[Project Pinboard (`agy-pin-projects`)](https://github.com/biTQ-m/agy-pin-projects)** — Persistent workspace launchpad & 4-in-1 Custom Icon Studio (`AUX_PANE` + `SIDEBAR`) for Antigravity 2.0 Desktop: pins favorite projects from `conversation_summaries.db` or local directories, organizes collapsible visual groups with cross-group drag-and-drop and List/Grid views, customizes icons via 32 built-in SVGs, Emoji/monograms, image/clipboard paste, or auto-detected repo logos, switches conversations in `<5ms`, and syncs live with the `pin-projects` Skill. `Aux Pane + Sidebar Sidecar + Skill`
- **[Voice Reader (`agy-voice-reader`)](https://github.com/biTQ-m/agy-voice-reader)** — Immersive English pronunciation & bilingual vocabulary workbench for Antigravity Desktop (macOS): double-tap `⌥` or Force Click any word/sentence to speak via a ~120ms hot dictionary socket + Microsoft Edge Neural HD voices, auto-injects vocabulary & code-switching rules (`rules/AGENTS.md`), and extracts clickable word cards with bilingual example drawers in the side panel. `macOS` `Aux Pane Sidecar + Rules + Skill`
- **[Voice Wake (`voice-wake`)](https://github.com/rmqg/antigravity-voice-wake)** — Offline macOS wake-word and global hotkey launcher for Google Antigravity: detects English phrases (`sherpa-onnx` Zipformer) or recorded voice samples (`EfficientWord-Net` INT8 ONNX) locally while protecting Bluetooth audio via built-in mic routing, opens a target project/model chat, triggers native dictation with Silero VAD auto-submit, and ships a bilingual 3-tab Auxiliary Pane UI. `macOS` `Swift + Aux Pane Sidecar + Skill`
- **[Antigravity Pet](https://github.com/Wlaeg/antigravity-pet)** — Zero-dependency native Windows & macOS pixel-art desktop companion plugin featuring 8 animated characters (including Android Bugdroid & Flutter Dash), live Agent state bubbles, and click interactions. `Windows / macOS` `Desktop Companion`

### Auxiliary Pane Workbenches & MCP Apps

- **[Postman Studio (`agy-postman`)](https://github.com/biTQ-m/agy-postman)** — Zero-dependency visual HTTP, REST & SSE API workbench inside Antigravity's Auxiliary Pane featuring a zero-CORS local Node proxy, DNS/TCP/TLS/TTFB timing waterfall, live `transcript.jsonl` cURL/endpoint sniffer, Postman Collection v2.1 import/export, mini concurrency load tester, and two-way AI Skill integration. `Aux Pane Sidecar + Skill`
- **[Antigravity Sidecar Studio](https://github.com/burnerous/antigravity-sidecar-studio)** — Three-in-one Auxiliary Pane workspace combining a project file tree, offline high-fidelity Word/Excel/PPT/PDF preview & editing, text-selection quoting to AI, and a read-only trajectory viewer. `Aux Pane Sidecar`
- **[Antigravity Doc Preview](https://github.com/Cl-Ask47/antigravity-doc-preview)** — Preview PDF, Word, PowerPoint, and Excel documents directly inside the Antigravity sidecar and inline chat. `Aux Pane Sidecar`
- **[Antigravity Inline Editor](https://github.com/mustafaakben/antigravity-inline-editor)** — Unofficial inline Edits tab for Antigravity Desktop with autosave, find & replace, comment, and quote actions. `Aux Pane Sidecar`
- **[Finder Explorer (`finder-explorer`)](https://github.com/jinxingtaire/finder-explorer)** — Zero-dependency macOS MCP App plugin rendering interactive inline file cards and an `aux_pane` directory browser that reveals workspace or `.gemini` artifact files directly in Finder (`open -R`) on double-click. `macOS` `MCP App + Rules`
- **[Antigravity Codex Monitor](https://github.com/Lyl101010/antigravity-codex-monitor)** — Native MCP App right-pane Mission Control monitor and cross-platform `codex-worker` delegation bundle for local OpenAI Codex CLI (`codex exec`): streams live commands, syntax-colored diffs, and token/cache metrics every 0.8s via local read-only polling with Git `--worktree` isolation, no-workspace scratch fallback, and zero `.asar`/CDP patching. `MCP App + Skill`

### Interface Suites & Step Experience

- **[Antigravity Max (`agy-max`)](https://github.com/wangbingnan136/agy-max)** — All-in-one workbench enhancement plugin for Antigravity 2.0 combining an optional `agy-fast` turn accelerator, auxiliary file-tree views, Codex-inspired search/Git/goal workflows, Prism optical styling, context/quota telemetry, and multi-account switching. `Sidecar + MCP + Hooks`
- **[AGY Powertools](https://github.com/WhiteBr1ck/agy-powertools)** — Native Antigravity 2.0 interface enhancement plugin featuring compact Codex-inspired typography, structured phase reporting, context & cache monitoring, session branching, and local usage views. `Desktop UI`
- **[Obsidian Prism](https://github.com/RMvdesi/obsidian-prism)** — Optical UI suite for Google Antigravity featuring 4 light/dark themes, damped-spring choreography, a breathing 512K context vial, reasoning-effort slider, pixel companions, and dual chat/coding modes. `Desktop UI`
- **[AGY Console (`agy-monitor`)](https://github.com/aishadiaodeqishui/agy-monitor)** — Zero-dependency non-invasive sidecar console combining live context/quota telemetry, multi-agent collaboration topology & Codex-style timeline tracking, composer ring HUDs, themes, and a pluggable desktop pet studio. `Aux Pane Sidecar + HUD`
- **[AGY Claude Style](https://github.com/0DNANCY/agy-claude-style)** — Cross-platform (`Windows` / `macOS` / `Linux`) UI restyling, multilingual localization, Token HUD telemetry, and interactive pixel mascot (`Clawd`) plugin for Antigravity. `Desktop UI + HUD`
- **[Antigravity Pulse](https://github.com/yangyu2004/antigravity-pulse)** — Inline chat step cards, lifecycle stall detector, and real-time token throughput & quota dashboard. `Desktop UI + Telemetry`
- **[Anti-Claude](https://github.com/hongqi7/Anti-Claude)** — Brings Claude.app-inspired interleaved step narration, live `TodoWrite` progress cards, and desktop UI rhythm to Antigravity Desktop via zero-patch runtime CDP injection. `Desktop UI`
- **[Antigravity Action Launchpad](https://github.com/404kidwiz/antigravity-action-launchpad)** — Zero-framework inline MCP App (`ui://`) and rules plugin that replaces repetitive `"go"` replies with 1-line keyboard command pills (`1`–`3`, `d` to expand), a fixed-height zero-jump hover `Why`/`What` Decision Inspector, A2UI-inspired `ChoicePicker` chips and inline short text fields, 2-step crimson `Click to confirm` arming guardrails, Warm Light/Dark native polarity, and a 1-paste 2-question Slim/Full agent setup (zero `npm install`). `macOS / Linux / Windows` `MCP App + Rules`

---

## Telemetry, Context Window & Statuslines

*Local-first observability tools for tracking token throughput (`tok/s`), context compaction budgets, prompt cache efficiency, model quotas, and `agy` CLI statuslines.*

### Desktop Sidecars, MCP Apps & Floating Monitors

- **[AGY Vitals (`agy-vitals`)](https://github.com/2fa0/agy-vitals)** — Zero-dependency, 100% local read-only telemetry suite (formerly `agy-statusline`) pairing a macOS Notch HUD, an `AGY Desktop Status` right-pane tab, and a fast Zig CLI `statusLine` for live `tok/s`, context curves, prompt cache hit rate, and quota reset timers. `macOS HUD + Sidecar + CLI statusLine`
- **[ag-vario](https://github.com/Staaaying/ag-vario)** — Zero-dependency, read-only macOS HUD for Antigravity 2.0 Desktop showing per-pane composer cards (session tokens, 5-category context breakdown, subagents across 2/3/4+ split panes) alongside titlebar `5h`/`7d` quota rings and a 30-day usage heatmap, with verified backup and lossless restore. `macOS` `Desktop HUD`
- **[Qufu Antigravity Monitor](https://github.com/QufuLabs/qufu-antigravity-monitor)** — Zero-token, zero-telemetry local model quota monitor for Antigravity 2.0 Desktop: tracks Gemini and Claude/GPT 5-hour and weekly limits with live 1-second reset countdowns via `agy -p "/usage"`, pairing a cross-platform `aux_pane` + `global` MCP App with an optional borderless Windows always-on-top mini bar synced to the host theme. `MCP App + Windows HUD`
- **[AGY Usage (`qiudai0627`)](https://github.com/qiudai0627/agy-usage)** — Zero-dependency, 100% local real-time quota and token usage monitor with a macOS notch-safe floating pill (`Swift`), Windows taskbar mini widget, CLI `statusLine`, and 11-language web dashboard (`Light · Airy · Dark` themes, independent Gemini & Claude/GPT 5h/7d reset timers, and privacy-safe share cards). `CLI statusLine + Desktop HUD`
- **[usage (`aqua5230`)](https://github.com/aqua5230/usage)** — Local-first macOS menu bar & Windows system tray app pinning Antigravity, Claude Code, Codex, and Grok CLI 5-hour/weekly quotas, burn rates, and HTML cost reports to your screen across 16 themes. `macOS / Windows Tray`
- **[ContextRadar](https://github.com/eatingDream-antigravity-plugins/ContextRadar)** — Native Rust MCP App for Antigravity context telemetry, 3-way cold-cache attribution, prefix-safe slice distillation, and gated `/compact` & `target:new` session relay handoffs. `Rust MCP App`
- **[Antigravity Context Viewer](https://github.com/elviscjn-cjn/antigravity-context-viewer)** — Multilingual context & usage dashboard for Google Antigravity 2.x monitoring real-time context windows, model quotas, generation speed, and Desktop/CLI token spend. `Sidecar`
- **[AGY Capsule](https://github.com/Lumidarin/agy-capsule)** — Displays live context usage, model quotas, token breakdowns, and generation metrics directly inside the Antigravity composer. `Composer HUD`
- **[Antigravity Context Window Monitor](https://github.com/AGI-is-going-to-arrive/Antigravity-Context-Window-Monitor)** — Real-time monitor for conversation context composition, dual context watermarks (`Compaction` + `200k` tier), and Orchestrator/Executor role pricing attribution. `Telemetry`
- **[Antigravity Usage & Speed Monitor](https://github.com/yuhuan-dev/antigravity-usage-monitor)** — Zero-dependency local usage, generation speed (`TPS`), `TTFT`, context window, quota, and subagent analytics monitor across Antigravity 2.0, IDE, and CLI. `Sidecar + CLI`
- **[Antigravity Context Mode](https://github.com/Domush/antigravity-plugin-context-mode)** — Local-first context protection plugin that cuts context bloat by 90%+ by preventing verbose terminal logs and multi-megabyte files from flooding conversation history. `Context Guard`
- **[AGY Context Dashboard](https://github.com/wycocoyu/agy-context-dashboard)** — Real-time context window, token usage, cache hit rate, and quota dashboard for Antigravity. `Sidecar`
- **[Antigravity Desktop Context](https://github.com/dimitr-io/antigravity-desktop-context)** — Live `/context` side panel inspector for the Antigravity 2.0 desktop app. `Aux Pane Sidecar`
- **[Antigravity Dashboard](https://github.com/ShZbz/antigravity-dashboard)** — Real-time token telemetry, quota tracker, and Rust-accelerated usage ledger across Antigravity Desktop, IDE, and CLI. `Rust + Sidecar`
- **[AGY Context (`ahmetdotsh`)](https://github.com/ahmetdotsh/agy-context)** — Native sidecar plugin to inspect live context window usage, prompt cache efficiency, and per-turn token breakdowns. `Aux Pane Sidecar`
- **[AGY Usage (`ahmetdotsh`)](https://github.com/ahmetdotsh/agy-usage)** — Native sidecar plugin for token usage analytics, API-equivalent cost estimation, and prompt cache savings. `Aux Pane Sidecar`
- **[AGY Lens (`xukp20`)](https://github.com/xukp20/agy-lens)** — Local-first Desktop telemetry sidecar featuring a prompt cache observatory, long-context cost analytics, and a daily activity heatmap. `Aux Pane Sidecar`
- **[Antigravity Status Monitor](https://github.com/rimenine/antigravity-status-monitor)** — Real-time Sidecar tracking agent phases, Lifecycle Hooks, and upstream reachability to distinguish active work from silent hangs. `Sidecar + Hooks`
- **[Antigravity Context Card](https://github.com/Shawn1565/antigravity-context-card)** — Zero-invasion, Claude Desktop-style MCP App sidebar, pure-stdlib `agy` CLI `statusLine`, and **personalized one-click Suggested Replies** (learns your style locally in SQLite; 1 primary + 2 alternatives via Desktop `Send` or pane-isolated `tmux` `Alt+y`, with zero-key `agy` subscription / BYOK / Ollama) alongside real 512K auto-compact headroom (`512K · 1M native`), `Messages` / `Thinking` / `Tool I/O` breakdown, and prompt cache %. `MCP App + Hooks + CLI statusLine`

### Antigravity IDE & VS Code Quota Panels

- **[Antigravity Cockpit (`vscode-antigravity-cockpit`)](https://github.com/jlcodes99/vscode-antigravity-cockpit)** — Antigravity IDE / VS Code extension for monitoring Google Antigravity AI quotas with a Webview dashboard, QuickPick switcher, and quota grouping. `IDE Extension`
- **[Antigravity Panel](https://github.com/n2ns/antigravity-panel)** — Real-time sidebar quota monitor and conversation cache manager for Antigravity IDE tracking Gemini, Claude, and GPT 5-hour/weekly limits with consumption trends and runway predictions. `IDE Extension`

### CLI Statuslines (`agy`)

- **[AGY Powerline](https://github.com/wassim-azi/agy-powerline)** — Zero-dependency `agy` CLI statusline with Gemini & Claude quota pacing, context progress bars, Git widgets, 22 themes, and interactive TUI and [browser](https://agy-powerline.com/configure/) configurators. `CLI statusLine`
- **[Antigravity CLI Statusline (`AndyAWD`)](https://github.com/AndyAWD/antigravity-cli-statusline)** — Cross-platform statusline skill and bar for `agy` CLI surfacing API quotas, token usage, Git branch status, and system resources with multilingual support. `CLI statusLine + Skill`
- **[Antigravity CLI Statusline (`weby-homelab`)](https://github.com/weby-homelab/antigravity-cli-statusline)** — Responsive, high-density terminal `statusLine` plugin for Antigravity CLI (`agy`). `CLI statusLine`
- **[Statusline HUD (`linbo0518`)](https://github.com/linbo0518/antigravity-hud)** — Adaptive multi-line terminal `statusLine` and interactive `/hud` configuration plugin for `agy` CLI built in pure Bash + `jq`. `CLI statusLine + Skill`
- **[AGY HUD (`franksde`)](https://github.com/franksde/agy-hud)** — Lightweight Antigravity CLI status plugin surfacing context window consumption, quota status, active model, and agent state. `CLI statusLine`

---

## Performance, Memory, Workflow & Swarm Orchestration

*Plugins that accelerate turn latency, persist cross-session memory, manage conversation history, enforce spec-driven reviews, or orchestrate multi-agent engineering loops.*

### Latency, Cache, Memory & Session Hygiene

- **[AGY Fast](https://github.com/INK-Q/agy-fast)** — Non-invasive MCP accelerator plugin for Antigravity (CLI/Desktop/IDE) designed to reduce redundant LLM turns, token consumption, and upload payloads while preserving native diffs. `MCP + Rules`
- **[AGY Dart](https://github.com/zou172866/Antigravity-agy-dart)** — Zero-dependency all-in-one plugin uniting automatic KV-cache warming, local SQLite FTS5 context-quota protection, crashed-session rescue, batched latency acceleration, and a live Sidecar dashboard. `Sidecar + MCP + Hooks`
- **[AGY Fast IO](https://github.com/oil-oil/agy-fast-io)** — Lightweight local rule plugin that trims unnecessary agent round-trips and redundant confirmation pauses. `Rules`
- **[agy-memory](https://github.com/maxLWS/agy-memory)** — Local, zero-dependency cross-conversation memory plugin for Antigravity (CLI/Desktop/IDE): injects a read-only `SessionStart` snapshot, searches transcripts (with `transcript_full.jsonl` hydration), artifacts, and Swarm boards, traces verified file edits (`file_history`) and command failures (`error_history`), stores editable Markdown notes with revision CAS, and optionally reads local Codex/Claude sessions. `MCP + Hooks + Rules + CLI`
- **[Antigravity Conversation Renamer MCP](https://github.com/falconchen/antigravity-conversation-renamer-mcp)** — Lightweight Node.js (`node:sqlite`) Stdio MCP server paired with a `/rename` Skill and optional topic-drift Rule: dynamically renames active or historical conversation titles cleanly on disk across `.pbtxt` annotations, SQLite FTS5 indexes, and Protobuf caches without Accessibility permissions or client restarts. `MCP + Skill + Rules`
- **[Anti-Power](https://github.com/mikessslxxx/anti-power)** — Local session management utility to browse, inspect, and clean up conversation histories across Antigravity Desktop App and Antigravity CLI (`agy`). `CLI / Session Utility`

### Spec-Driven Workflows, Swarm & Cloud Assistants

- **[Conductor (`gemini-cli-extensions`)](https://github.com/gemini-cli-extensions/conductor)** — Spec-Driven Development plugin (`Apache-2.0`) for Antigravity and Claude Code that guides agents to specify requirements, plan architecture, and implement features systematically. `Skills + Workflow`
- **[Superpowers for Antigravity](https://github.com/roundpilot/superpowers-antigravity)** — Native MIT-licensed workflow plugin for Antigravity 2.0 App, IDE, and `agy` CLI providing structured brainstorming, implementation planning, test-driven development (TDD), and subagent-driven execution skills. `Skills + Subagents + Hooks`
- **[Mission Control for Antigravity](https://github.com/todd866/antigravity-mission-control)** — Live pictorial Mission Control cockpit (MCP App), turn-aware AI briefings, cross-Mac relay (`agy-status` / `agy-relay`), and adaptive Flash/Carbon/Neon AI Commander for coordinating Antigravity agents. `MCP App + CLI`
- **[oh-my-antigravity (`OmA`)](https://github.com/Joonghyun-Lee-Frieren/oh-my-antigravity)** — Context-engineering multi-agent team workflow pack for Antigravity CLI (`agy`). `Skills + Subagents`
- **[LitGravity](https://github.com/wjgoarxiv/litgravity)** — Lightweight `agy` CLI workflow plugin (formerly `antigravity-swarm`): add `lit` to a prompt to trigger a planned, tested, reviewed execution cycle with automatic next-session handoff notes. `Workflow + Rules`
- **[AGYStack](https://github.com/jtaroreh/agystack)** — Closed-loop engineering workflow and multi-agent swarm orchestration plugin for Google Antigravity. `Swarm + Skills`
- **[agy-hq](https://github.com/zjshen14/agy-hq)** — Lightweight proactive Personal Agent OS (`Apache-2.0`) turning an always-on Mac or Linux workstation running Google Antigravity into a scheduled, context-aware assistant. `Go + Skills + Automation`
- **[SRE Extension (`gemini-cli-extensions`)](https://github.com/gemini-cli-extensions/sre)** — Official `Apache-2.0` Site Reliability Engineering extension providing production incident investigation, telemetry triage, and cloud diagnostics workflows for `agy` CLI and Claude Code. `Skills + Cloud SRE`
- **[Google Ads API Developer Assistant](https://github.com/googleads/google-ads-api-developer-assistant)** — Official Google Ads open-source assistant (`Apache-2.0`) for querying docs, generating GAQL queries, and executing Google Ads API workflows via natural language. `Official Assistant`
- **[AGY GCP Companion](https://github.com/ericsk/agy-gcp-companion)** — Inspect Google Cloud projects, billing accounts, budget thresholds, and BigQuery month-to-date spend inside Antigravity. `GCP + MCP`

---

## Browser, Computer Use & Creative Automation

*Plugins extending Antigravity across browser workflows, native OS GUI automation, GPU video/UI synthesis, and robotics.*

- **[GDM Robotics Plugin](https://github.com/google-deepmind/robotics-antigravity-plugin)** — Official Google DeepMind Robotics skills for 3D perception, collision-free motion planning, visual servoing, MuJoCo simulation, and sim2real robot bring-up. `Official` `Skills + Sidecar`
- **[Open Robotics Plugin](https://github.com/eust-w/open-robotics-plugin)** — Cross-agent `Apache-2.0` adaptation of DeepMind's robotics suite bringing MuJoCo simulation, perception, motion planning, and sim2real bring-up skills & sidecars to Antigravity, Claude Code, Codex, and Cursor. `Skills + Sidecar`
- **[ultrafast](https://github.com/ultrafastmov/ultrafast)** — Open-source (MIT/Apache-2.0) GPU video engine with an `agy` plugin: the agent authors a video as a JSON document, inspects contact sheets and exact frames across 20 local MCP tools, catches unreadable/clipped/overlapping text, and exports MP4, ProRes, WebM, or GIF on Linux (Vulkan) and macOS (Metal). `MCP + Skill`
- **[Google Stitch Plugin](https://github.com/AndrewMason7/stitch-plugin)** — `Apache-2.0` Antigravity plugin for Google Stitch combining cloud UI/UX prototyping, 18 MCP tools, 17 design-to-code skills, and `@google/design.md` design-token synthesis. `MCP + Skills + Subagents`
- **[Antigravity Flow](https://github.com/WeZZard/antigravity-flow)** — Antigravity plugin for Google Flow creative generation powered by Antigravity's built-in browser subagent. `Browser + Skill`
- **[Computer Use AGY](https://github.com/Jayanyixing/computer-use-agy)** — Open-source (MIT) macOS Computer Use MCP server and Antigravity plugin for desktop GUI interaction. `macOS` `MCP + Skill`
- **[Antigravity Cua Driver](https://github.com/WeZZard/antigravity-cua-driver)** — Background native GUI automation plugin across macOS, Windows, and Linux powered by Cua Driver. `Cross-Platform GUI`
- **[Firecrawl Antigravity Plugin](https://github.com/firecrawl/firecrawl-antigravity-plugin)** — Official Firecrawl plugin for clean web scraping, full-site crawling, and LLM-ready Markdown extraction. `Official` `MCP + Skill`

---

## Cross-Agent Bridges, ACP & Remote Control

*Mobile companions, instant-messaging gateways, Agent Client Protocol (ACP) servers, and multi-agent bridges connecting `agy` with Claude Code, Codex, Cursor, DeepSeek Harness, Hermes, Pi, and external clients.*

### Mobile Companions & Remote Messengers

- **[Multigravity](https://github.com/GHSaiMo/antigravity-mobile)** — Open-source (MIT) native iOS (App Store), Android, and Web PWA mobile companion with a local Go gateway (`mgy`) for Antigravity IDE/CLI: real-time chat & `/swarm` Hive monitoring, Dynamic Island live steps, APNs lock-screen command approvals, 5h/7d quota widgets, 20-week token/cache auditing, and zero-knowledge E2EE (`mgy-e2ee-v1`). `iOS / Android / PWA` `Local Go Gateway`
- **[Antigravity Telegram Suite](https://github.com/emreturkmencom/antigravity-telegram-suite)** — Remote-control Telegram bot for Antigravity Standalone App and IDE to chat, switch models, and orchestrate multi-agent workflows from mobile. `Telegram Gateway`
- **[agy-remote-wecom](https://github.com/lukeinx/agy-remote-wecom)** — Control local Antigravity (`agy`) terminal sessions and background `agy acp` sessions from WeCom on your phone over an outbound WebSocket long connection (no public server), with session resume, attachments, model/mode switching, tool-approval cards, and artifact retrieval. `macOS` `Hooks + ACP`

### Cross-Agent Harnesses & ACP / MCP Bridges

- **[Codex Bridge](https://github.com/Fanch-hui/codex-bridge)** — Self-hosted `Apache-2.0` desktop app and official MCP Registry bridge connecting ChatGPT Web, OpenAI Dot, and Gemini to authorized local projects to orchestrate `agy`, Codex, Claude Code, OpenCode, and DeepSeek Harness with approvals and live session control. `MCP Bridge + Desktop App`
- **[Antigravity for Claude Code (`yuting0624`)](https://github.com/yuting0624/antigravity-for-claude-code)** — Claude Code plugin running `agy` CLI as a collaborating Gemini sub-agent with intelligent model routing across the software delivery lifecycle. `Claude Code ↔ agy`
- **[Claude Antigravity Agents (`markfulton`)](https://github.com/markfulton/claude-antigravity-agents)** — MIT-licensed Claude Code orchestration skill that delegates parallel coding, review, analysis, and deep research tasks to `agy` CLI sub-agents. `Claude Code ↔ agy`
- **[cc-suite (`xiaolai`)](https://github.com/xiaolai/cc-suite)** — Unified cross-agent synchronization plugin aligning single-source `AGENTS.md` rules, shared skills, mirrored hooks, and bidirectional task delegation across Claude Code, Codex CLI, and `agy` CLI. `Claude ↔ Codex ↔ agy`
- **[Hermes Antigravity OAuth](https://github.com/neerazz/hermes-antigravity-oauth)** — MIT-licensed integration enabling Hermes Agent to run on your Antigravity plan via the official `agy` CLI (`npx hermes-antigravity-oauth`) while preserving custom `SOUL.md` personas. `Hermes ↔ agy`
- **[DSH AGY Link](https://github.com/amlyczz/dsh-agy-link)** — Integrates Google Antigravity (`agy` CLI & `agy acp`) models into DeepSeek Harness with multi-account quota pooling, streaming thought/tool activity, and in-chat image generation. `DeepSeek Harness ↔ agy`
- **[AGY Staff](https://github.com/keli-wen/agy-staff)** — Delegate fast Gemini coding, research, and review subtasks to `agy` CLI from Claude Code, OpenAI Codex, and other coding harnesses. `Cross-Harness CLI`
- **[Pi Antigravity ACP Provider](https://github.com/zacbemis/pi-antigravity-acp-provider)** — First-class ACP provider connecting the Pi coding harness directly to Google Antigravity's official ACP server. `Pi ↔ ACP`
- **[Antigravity Codex Worker](https://github.com/lbc9168/antigravity-codex-worker)** — Antigravity Skill orchestrating local OpenAI Codex CLI (`codex exec`) as a sandboxed coding worker while Gemini/Opus acts as Architect & Reviewer. `agy → Codex Skill`
- **[Antigravity ACP](https://github.com/shubzkothekar/antigravity-acp)** — Bun-powered Agent Client Protocol (ACP) server allowing ACP-compatible editors to drive `agy` with live streaming and history replay. `ACP Server`
- **[Antigravity Plugin for Claude Code (`simplybychris`)](https://github.com/simplybychris/antigravity-plugin-cc)** — Invoke `agy` directly inside Claude Code to delegate tasks, run quick prompts, or request cross-model code reviews. `Claude Code ↔ agy`
- **[AGY Bridge](https://github.com/sshahzaiib/agy-bridge)** — MCP bridge enabling Claude Code to offload heavy tasks to `agy` with model fallback routing, session continuity, and output truncation. `MCP Bridge`
- **[AGY MCP (`Boulea7`)](https://github.com/Boulea7/agy-mcp)** — Exposes `agy` as a 10-tool MCP server with worktree-isolated execution and long-task supervision for Cursor, Codex, or any MCP client. `MCP Server`
- **[agy-mcp (`tphakala`)](https://github.com/tphakala/agy-mcp)** — Lightweight MCP server wrapping `agy` CLI with async job supervision and completion wakes for Claude Code, Cursor, Cline, and other MCP clients. `MCP Server`
- **[NotebookLM via Antigravity](https://github.com/MarcosNahuel/antigravity-plugin-cc)** — Turns local document folders into per-doc summaries, relevance indexes, cited syntheses, audio/video transcripts, and HTML research reports via `agy`. `Research Workflow`

---

## Official & Partner Marketplace Catalog

*First-party and verified partner plugins available directly inside the **Antigravity Agent Marketplace** (`Customizations → Plugins`). Reference them by their `Catalog ID`.*

### Google Ecosystem, Cloud & Science

| Plugin | Catalog ID | Highlights |
| :--- | :--- | :--- |
| **Gemini API** | `antigravity-plugins-official/plugin/gemini-api` ([Repo](https://github.com/google-gemini/gemini-skills)) | Official skills, `gemini-api` CLI, and docs MCP for Interactions API, Decisions API, Live API, Genie 4 interactive worlds, and Omni Flash. |
| **Chrome DevTools** | `antigravity-plugins-official/plugin/chrome-devtools-plugin` ([Repo](https://github.com/ChromeDevTools/chrome-devtools-mcp)) | Official Chrome DevTools & Puppeteer MCP plus skills for network/cookie debugging, heap leak profiling, a11y audits, and LCP optimization. |
| **Elephant-Goldfish Model** | `antigravity-plugins-official/plugin/egm` ([Repo](https://github.com/google/elephant-goldfish-model)) | Multi-persona review swarm pairing context-rich drafting ("Elephant") with isolated zero-prior-context critic subagents ("Goldfish"). |
| **Modern Web Guidance** | `antigravity-plugins-official/plugin/modern-web-guidance-plugin` ([Repo](https://github.com/GoogleChrome/modern-web-guidance)) | Official Google Chrome guidance keeping coding agents aligned with Baseline HTML/CSS/JS and Manifest V3 extension best practices. |
| **Google Antigravity SDK** | `antigravity-plugins-official/plugin/google-antigravity-sdk` | Official skills and patterns for building AI agents with the Antigravity Python SDK. |
| **Google Cloud Developer** | `antigravity-plugins-official/plugin/google-cloud-developer` | GCP onboarding, credential selection, `gcloud` safety checks, and Developer Knowledge MCP. |
| **Google Developer Knowledge** | `antigravity-plugins-official/plugin/google-developer-knowledge` | Grounded search across official Cloud, Gemini, Android, Firebase, Flutter, and Web docs. |
| **Firebase** | `antigravity-plugins-official/plugin/firebase` | Prototype, build, and operate modern apps with Firebase backend, Auth, and AI services. |
| **Dart & Flutter** | `antigravity-plugins-official/plugin/flutter` | Official Flutter/Dart skills, rules, custom agents, and the Dart MCP server. |
| **Android CLI** | `antigravity-plugins-official/plugin/android-cli-plugin` | Core CLI workflows and architectural guidance for Android engineering. |
| **Google Workspace Suite** | `antigravity-plugins-official/plugin/gdocs` *(+ `gsheets`, `gslides`, `gdrive`, `gcalendar`, `gmail`)* | Read, draft, format, schedule, email, and manage Google Docs, Sheets, Slides, Drive, Calendar, and Gmail. |
| **Looker** | `antigravity-plugins-official/plugin/looker` | Connect to managed Looker MCP to explore data, run saved Looks, build dashboards, and validate LookML. |
| **Data Agent Kit** | `antigravity-plugins-official/plugin/data-agent-kit-plugin` | Specialized skills for data engineers and database architects on Google Cloud. |
| **Google Maps Platform** | `antigravity-plugins-official/plugin/google_maps_platform` | Integration skills and tools for Google Maps Platform APIs. |
| **Google Health & Home** | `antigravity-plugins-official/plugin/google-health-developer` *(+ `google-home-developer`)* | Official MCP documentation and integration diagnostics for Google Health, Google Home, Matter, and OpenThread. |
| **Scientific & Robotics** | `antigravity-plugins-official/plugin/robotics` *(+ `science-overview`, `genomics`, `structural-biology`, `chemistry`)* | DeepMind Robotics (with live MuJoCo Studio 3D viewer), AlphaGenome genetics, AlphaFold structural biology, and RDKit/ChEMBL cheminformatics. |
| **Scientific Literature** | `antigravity-plugins-official/plugin/scientific-literature` | Search peer-reviewed scientific papers, clinical trials, FDA records, and historical texts. |

### Databases, Cloud & App Platforms

| Plugin | Catalog ID | Highlights |
| :--- | :--- | :--- |
| **Supabase** | `antigravity-plugins-partners/plugin/supabase` | Official Supabase MCP & skills for Postgres schema design, RLS, Auth, Storage, and Edge Functions. |
| **MongoDB Atlas** | `antigravity-plugins-partners/plugin/mongodb-atlas` | Hosted Atlas MCP server + collection management, aggregation, and query optimization skills. |
| **Neo4j** | `antigravity-plugins-partners/plugin/neo4j` | Cypher query authoring, graph data modeling, GraphRAG pipelines, and Aura administration. |
| **Databricks** | `antigravity-plugins-partners/plugin/databricks` | Lakebase, Model Serving, Lakeflow Jobs, Spark Declarative Pipelines, and Asset Bundles (DABs). |
| **Vercel** | `antigravity-plugins-partners/plugin/vercel-plugin` | Next.js, AI SDK, and cloud deployment skills paired with the official Vercel MCP server. |
| **Cloudflare** | `antigravity-plugins-partners/plugin/cloudflare` | Build and deploy on Cloudflare Workers, KV/R2/D1 storage, and AI Gateway via Cloudflare MCP. |
| **Netlify** | `antigravity-plugins-partners/plugin/netlify` | Serverless & edge functions, blobs, database, image CDN, and the Netlify MCP server. |
| **Railway** | `antigravity-plugins-partners/plugin/railway` | Deploy, configure, and troubleshoot apps, databases, and infrastructure via Railway MCP. |
| **Base44** | `antigravity-plugins-partners/plugin/base44` | Build and deploy Base44 full-stack applications with CLI project management, JS/TS SDK skills, and production diagnostics. |
| **Spacefast** | `antigravity-plugins-partners/plugin/spacefast` | Turn ideas or local artifacts into shareable websites, interactive dashboards, and published web tools from chat. |

### Observability, Security, Code Review & Testing

| Plugin | Catalog ID | Highlights |
| :--- | :--- | :--- |
| **CodeRabbit** | `antigravity-plugins-partners/plugin/coderabbit` | Governance and AI code review control layer for catching defects and enforcing engineering standards on agent-written code. |
| **Sentry** | `antigravity-plugins-partners/plugin/sentry` | Triage production exceptions, inspect stack traces, and configure alerts & releases with live context. |
| **Datadog** | `antigravity-plugins-partners/plugin/datadog` ([Repo](https://github.com/datadog-labs/antigravity-plugin)) | Query Datadog logs, metrics, traces, monitors, and dashboards through natural conversation via Datadog MCP. |
| **Grafana Cloud** | `antigravity-plugins-partners/plugin/grafana-cloud-mcp` | Query Prometheus metrics, Loki logs, Tempo traces, profiles, and incidents via hosted MCP. |
| **Arize AX** | `antigravity-plugins-partners/plugin/arize-skills` | Inspect Arize AX LLM traces, datasets, and experiments with skills for evals and prompt optimization. |
| **SonarQube** | `antigravity-plugins-partners/plugin/sonarqube` | Catch bugs, security vulnerabilities, and leaked secrets across 7,500+ rules inside the agent loop. |
| **Endor Labs Agent Kit** | `antigravity-plugins-partners/plugin/endor-labs-agent-kit` | Packaged workflows for SCA remediation, AI SAST triage, CI/CD posture, and malware response. |
| **Orca Security** | `antigravity-plugins-partners/plugin/orca-security` | Investigate cloud risk from your workspace: query Orca alerts, assets, attack paths, CVEs, and compliance posture via Orca MCP. |
| **SentinelOne Purple AI** | `antigravity-plugins-partners/plugin/sentinelone-purple-mcp` | Query SentinelOne Singularity Console security telemetry through a self-hosted, read-only Purple AI MCP server. |
| **Exabeam Agentic SOC** | `antigravity-plugins-partners/plugin/soc` | Triage Exabeam New-Scale alerts and security cases end-to-end with evidence gathering, MITRE mapping, and gated verdicts. |
| **Browserbase** | `antigravity-plugins-partners/plugin/browse` | Local and cloud headless browsers for navigation, interaction, screenshots, and data extraction. |
| **Harness** | `antigravity-plugins-partners/plugin/harness-antigravity` | Build and debug CI/CD pipelines, manage deployments, and investigate security findings. |
| **TestMu AI** | `antigravity-plugins-partners/plugin/testmu-ai` | Cloud test triage plus Kane CLI for browser/mobile automation and Rook CLI for agent testing. |
| **Leapwork Play** | `antigravity-plugins-partners/plugin/leapwork-play` | Create, execute, and debug Leapwork Play automated test flows and runlists directly from Antigravity. |
| **Auth0** | `antigravity-plugins-partners/plugin/auth0` | Add login, MFA, SSO, Organizations, RBAC, and custom domains to any application. |
| **Clerk** | `antigravity-plugins-partners/plugin/clerk` | User management, organizations, billing, webhooks, and testing skills + Clerk MCP server. |

### Design, Productivity, Search & Business

| Plugin | Catalog ID | Highlights |
| :--- | :--- | :--- |
| **Figma** | `antigravity-plugins-partners/plugin/figma` | Turn Figma designs into production code, map components with Code Connect, and edit Figma files. |
| **Canva** | `antigravity-plugins-partners/plugin/canva` | Create, resize, review, and brand-check designs through the Canva MCP server. |
| **Kling AI** | `antigravity-plugins-partners/plugin/kling-ai` | Generate and edit images with Kling Image 4.0 and produce Kling 4.0 / Flash HDR videos with reusable Elements. |
| **Mobbin** | `antigravity-plugins-partners/plugin/mobbin` | Search 600,000+ real-world mobile and web app UI flows directly from your agent. |
| **Postman** | `antigravity-plugins-partners/plugin/postman` | Official Postman skills for API discovery, design, testing, mocking, documentation, and monitoring. |
| **Linear** | `antigravity-plugins-partners/plugin/linear` ([Repo](https://github.com/linear/antigravity-plugin)) | Manage issues, cycles, specs, and engineering roadmaps in Linear. |
| **Notion** | `antigravity-plugins-partners/plugin/notion` | Search Notion workspaces, draft specs, summarize meetings, and maintain project trackers. |
| **ClickUp** | `antigravity-plugins-partners/plugin/clickup` | Manage ClickUp tasks, track time, and collaborate across workspace lists without leaving Antigravity. |
| **Any.do** | `antigravity-plugins-partners/plugin/anydo` | Manage personal tasks, workspace boards, subtasks, reminders, and connected calendar events. |
| **Atlassian Teamwork Graph** | `antigravity-plugins-partners/plugin/atlassian-twg-cli` | Agent-first CLI unifying Jira issues, Confluence pages, and Bitbucket PRs. |
| **n8n** | `antigravity-plugins-partners/plugin/n8n-skills` | Build, test, and debug n8n workflows and AI agents through your n8n instance MCP server. |
| **Zapier** | `antigravity-plugins-partners/plugin/zapier` | Trigger actions and build automations across 10,000+ apps (Slack, Gmail, LinkedIn, YouTube, etc.). |
| **Tavily** | `antigravity-plugins-partners/plugin/tavily` | Real-time web search, content extraction, crawling, and deep research via Tavily's hosted MCP. |
| **Parallel** | `antigravity-plugins-partners/plugin/parallel` | Keyless live web search and clean page content fetching via Parallel's hosted MCP server with zero account setup. |
| **Keenable** | `antigravity-plugins-partners/plugin/keenable` *(+ `keenable-select`)* | Keyless AI-first web search & Markdown reader plus multi-query structured table extraction (`Keenable SELECT`). |
| **Zoho Business Suite** | `antigravity-plugins-partners/plugin/zoho-crm-plugin` *(+ `zoho-bigin`, `zoho-projects`, `zoho-desk-antigravity`, `zohobooks-antigravity`)* | Official Zoho MCP & agent suite spanning Zoho CRM v8, Bigin pipelines, Projects, Desk ticket triage, and Books accounting. |
| **Adspirer Analytics** | `antigravity-plugins-partners/plugin/adspirer-analytics` | Read-only marketing analytics reporting spend, conversions, CPA, and ROAS across ad platforms, GA4, and Search Console. |
| **Stripe** | `antigravity-plugins-partners/plugin/stripe` | Manage products, prices, payment links, subscriptions, invoices, and Stripe docs via MCP. |
| **Docusign** | `antigravity-plugins-partners/plugin/docusign` | Build and debug Docusign authentication, template-based eSignature envelopes, and status workflows. |

---

## Skill Suites & Plugin Authoring Toolkits

*SDKs for scaffolding new Antigravity plugins/sidecars and modular `SKILL.md` collections that can be bundled into plugins.*

- **[Antigravity Sidecar Kit](https://github.com/arthurcavallari/antigravity-sidecar-kit)** — Zero-dependency SDK and CLI scaffolder for Antigravity Auxiliary Pane sidecars (Connect RPC client, host theme & Tailwind proxy, config store, and installer). `Sidecar SDK`
- **[AI Agent Skills (`simota`)](https://github.com/simota/agent-skills)** — MIT-licensed collection of 90 specialist AI agents, 49 orchestration recipes, and 11 `SKILL.md` packs across engineering, security, FinOps, design, testing, and observability for `agy` CLI, Claude Code, and Codex. `90 Agents + 11 Skill Packs`
- **[Antigravity Skills (`rmyndharis`)](https://github.com/rmyndharis/antigravity-skills)** — Large community-curated library of Agent Skills for Google Antigravity across full-stack engineering domains. `Skill Library`
- **[Sample Google Antigravity Skills (`rominirani`)](https://github.com/rominirani/antigravity-skills)** — Clean reference examples for authoring modular `SKILL.md` bundles in Antigravity. `Reference Examples`
- **[Antigravity Skills Engine](https://github.com/buiquangvu235/antigravity-skills-engine)** — Structured multi-track skill collection for autonomous software engineering workflows. `Skill Suite`
- **[Antigravity n8n Skills](https://github.com/WilkoMarketing/antigravity-n8n-skills)** — Specialized Antigravity skills for n8n workflow design, node configuration, and schema validation. `n8n Skills`
- **[Spec-Kit Antigravity Skills](https://github.com/compnew2006/Spec-Kit-Antigravity-Skills)** — Spec-Driven Development skill system covering requirements, architecture, implementation, and verification. `SDD Skills`
- **[Antigravity Skills Chronicle](https://github.com/Zaious/Antigravity-Skills-Chronicle)** — Visual dashboard extension for browsing and managing agent skills, workflows, and rules. `Skill Manager UI`

---

## Environment & Multi-Account Managers

*Cross-platform desktop/CLI/TUI utilities for managing isolated Antigravity account profiles, quota inspection, and reproducible local environments.*

- **[Cockpit Tools (`jlcodes99`)](https://github.com/jlcodes99/cockpit-tools)** — Universal AI IDE & Antigravity account manager supporting multi-account switching, live quota monitoring, auto-wake, and isolated multi-instance launches. `Desktop Manager`
- **[Antigravity Manager (`Draculabo`)](https://github.com/Draculabo/AntigravityManager)** — Desktop application for managing Google accounts across Antigravity Classic, Antigravity IDE, and `agy` CLI with live quota inspection. `Desktop Manager`
- **[agy-manager (`eligibility-antigravity-patcher`)](https://github.com/QNIX-Dev/eligibility-antigravity-patcher/blob/main/README.en.md)** ([Repo](https://github.com/QNIX-Dev/eligibility-antigravity-patcher)) — Lightweight cross-platform environment manager (`Windows` / `Linux` / `macOS`, `x64` & `arm64`) with both an interactive TUI and a zero-dependency Python CLI: supports isolated multi-account profiles (including concurrent macOS desktop profiles), live 5-hour/weekly quota monitoring, and reversible client-side eligibility patching with automatic backup & signature restore. `TUI + CLI`
- **[agy-swap](https://agy-swap.aklkbqx.com/)** ([Repo](https://github.com/aklkbqx/agy-swap)) — Cross-platform Go TUI and CLI (`macOS` / `Linux` / `Windows`) for switching Google Antigravity CLI and IDE/Desktop accounts with live per-model quota inspection, session guards against background token overwrites, and automatic local backups before writes (`0600` `vault.json` or OS keychain via `AGY_SWAP_VAULT=keychain`). `Go TUI + CLI`
- **[AGY Switch](https://github.com/anglee0323/agy-switch)** — Manage Antigravity accounts, model quotas, and local usage across macOS, Windows, and Linux through desktop and CLI interfaces. `Desktop + CLI`
- **[AGY Auth](https://github.com/fikrilal/agy-auth)** — Multi-account switcher for Google Antigravity CLI and Desktop (`agy`). `CLI`
- **[AGY CLI Manager](https://github.com/zcop/agy-cli-manager)** — Multi-account manager for Antigravity CLI featuring quota-aware failover, switching policies, and automation hooks. `CLI + Hooks`
- **[antigravity-nix](https://github.com/jacopone/antigravity-nix)** — Auto-updating, version-pinned Nix Flake and Home Manager overlay for Google Antigravity on Linux and macOS. `Nix Flake`

---

## Localization, Themes & Accessibility

*Community language packs, color themes, and RTL typography engines for Antigravity Desktop and IDE.*

- **[Antigravity 2.0 CN (`qqxpee`)](https://github.com/qqxpee/antigravity2-cn)** — Zero-dependency Simplified & Traditional Chinese localization injector (`Windows` & `macOS`) purpose-built for Antigravity 2.0's Electron architecture with one-click install and clean restore. `zh-CN / zh-TW`
- **[Antigravity Chinese Localization (`antigravity-cn-community`)](https://github.com/antigravity-cn-community/Antigravity-Chinese-Localization)** — Community one-click Simplified Chinese localization package for Google Antigravity. `zh-CN`
- **[Chuanban Theme & Font Patch (`Anarcadia`)](https://github.com/Anarcadia/chuanban-antigravity-theme-patch)** — Non-invasive runtime CDP UI beautification, warm-paper color presets, 3-tier typography (Sarasa / Anthropic), and partial Chinese localization guided by an interactive Skill. `Theme + Skill`
- **[Antigravity Codex Theme (`nkjDSLcvanv`)](https://github.com/nkjDSLcvanv/antigravity-codex-theme)** — Modular 34-component desktop enhancement plugin (zero bundle modification) injecting Codex light/dark themes, 1,900+ Chinese strings, embedded settings, and 4-state quota indicators. `Theme + zh-CN`
- **[Antigravity Chinese (`yiheng8023`)](https://github.com/yiheng8023/antigravity-chinese)** — Full-ecosystem Chinese localization suite covering Antigravity Desktop 2.0, VS Code extension, CLI, and Marketplace descriptions with signature-safe backup and restore. `zh-CN`
- **[Antigravity zh-CN (`MIMICTE`)](https://github.com/MIMICTE/Antigravity-zh-CN)** — Simplified Chinese localization patch for Antigravity Desktop. `zh-CN`
- **[Antigravity Desktop CN (`Silas-02`)](https://github.com/Silas-02/antigravity-desktop-cn)** — Cross-platform (`macOS` / `Windows` / `Linux`) Simplified Chinese localization engine with one-click install and clean restore. `zh-CN`
- **[Antigravity 2.0 zh-TW (`workkkkkkez00m`)](https://github.com/workkkkkkez00m/antigravity2.0-zh-tw)** — Traditional Chinese (`繁體中文`) localization package for Antigravity 2.0 on Windows and macOS with clean restore. `zh-TW`
- **[Antigravity Themes](https://github.com/materialwebunofficial/antigravity-themes)** — Custom UI color themes for the Antigravity Desktop app. `Themes`
- **[Antigravity Tradução PT-BR](https://github.com/Emertels/Antigravity-Traducao-PTBR)** — Portable Brazilian Portuguese localization package for Antigravity Desktop. `pt-BR`
- **[Antigravity Smart RTL (`mmnaderi`)](https://github.com/mmnaderi/antigravity-rtl)** — Smart right-to-left UI and typography patcher for Antigravity & Antigravity IDE supporting Persian, Arabic, and Hebrew without disrupting code blocks. `RTL`
- **[RZ Antigravity RTL](https://github.com/rezasalimi01/rz-antigravity-rtl)** — High-performance Persian & Arabic RTL typography engine with offline fonts and strict Monaco editor isolation. `RTL`

---

## Quick Install & Plugin Anatomy

### Installing Plugins

1. **Marketplace Plugins**: Open **Customizations → Plugins** inside Antigravity 2.0 Desktop and search by plugin name or `Catalog ID` for one-click install.
2. **Community Open-Source Plugins**: Place or symlink any folder containing a `plugin.json` inside `~/.gemini/config/plugins/<plugin-dir>/` (machine-global) or `.agents/plugins/<plugin-dir>/` (workspace-shared). Most community repositories also include an `install.sh` helper:

```bash
git clone https://github.com/<author>/<plugin-repo>.git
cd <plugin-repo>
chmod +x ./install.sh && ./install.sh
```

Toggle plugins live at any time via **Customizations → Plugins** in the Desktop UI or `agy plugin enable <dir>` / `agy plugin disable <dir>` in the CLI—skills, rules, hooks, and MCP servers take effect without restarting Antigravity, while UI Sidecars and MCP Apps with `aux_pane` / `global` entrypoints appear directly in the Auxiliary Pane **`+`** menu or left sidebar.

### Standard Plugin Directory Layout

```text
~/.gemini/config/plugins/<plugin-dir>/
├── plugin.json                 # Required manifest (name, description, logo, suggestedPrompts)
├── README.md                   # Human-facing documentation
├── assets/logo.svg             # Square SVG/PNG icon (128x128+, ~10% margin)
├── sidecars/<id>/sidecar.json  # Optional Auxiliary Pane / Sidebar Web UI sidecar service
├── mcp_config.json             # Optional MCP servers & interactive MCP Apps (ui:// resources; supports ${PLUGIN_ROOT} & ${PLUGIN_DATA})
├── skills/<skill>/SKILL.md     # Optional on-demand progressive-disclosure agent skills
├── agents/<agent>.md           # Optional specialized subagents
├── rules/AGENTS.md             # Optional always-on prompt rules while plugin is enabled
└── hooks.json                  # Optional root-level lifecycle hooks (SessionStart, PreInvocation, PostToolUse, Stop)
```

---

## Contributing

Contributions, new plugins, and category refinements are warmly welcome! Please read [CONTRIBUTING.md](./CONTRIBUTING.md), run `python3 scripts/validate.py` to verify bilingual parity, or [open a Plugin Submission issue](../../issues/new?template=submit-plugin.yml) before submitting a Pull Request.

> **Disclaimer & Security Policy**: Community utilities that modify local client bundles (such as localization patches or environment patchers) are unofficial and used at your own discretion—always back up your installation first. Repositories containing malware, credential/token harvesters, bypass exploits, or hidden telemetry will never be accepted.

## License

[![CC0](https://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](https://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, [biTQ-m](https://github.com/biTQ-m) has waived all copyright and related or neighboring rights to this work under [CC0 1.0 Universal](./LICENSE).
