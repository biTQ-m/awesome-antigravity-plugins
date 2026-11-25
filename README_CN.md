<div align="center">

<img src="assets/banner.svg" width="100%" alt="Awesome Antigravity Plugins Banner" />

<br />

[![Awesome](https://awesome.re/badge-flat2.svg)](https://awesome.re)
[![Plugins Curated](https://img.shields.io/badge/已收录-70%2B%20精选插件-6366f1.svg)](#目录导航)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-10b981.svg)](./CONTRIBUTING.md)
[![License: CC0-1.0](https://img.shields.io/badge/License-CC0%201.0-f59e0b.svg)](./LICENSE)

[English](./README.md) · **简体中文**

*精选收录面向 **Google Antigravity（`agy` CLI & Antigravity 2.0 Desktop / IDE）** 的开源插件、右侧辅助面板（Aux Pane UI Sidecar）、桌面悬浮窗（HUD）、终端状态栏、MCP 扩展包、Skill 技能集与官方应用市场插件。*

</div>

---

> [!NOTE]
> **什么是 Antigravity Plugin？**
> 在 Google Antigravity 中，**插件（`plugin.json`）** 是可一键安装、启用与停用的命名空间扩展包，内部可自由组合 **UI Sidecar 侧边栏面板**（`sidecars/`）、**Skills 技能**（`skills/<name>/SKILL.md`）、**MCP 服务**（`mcp_config.json`）、**生命周期钩子**（`hooks.json`）、**常驻提示词规则**（`rules/AGENTS.md`）以及 **子代理**（`agents/`）。

## 目录导航

- [桌面端 UI 面板、辅助栏与悬浮窗 (HUD)](#桌面端-ui-面板辅助栏与悬浮窗-hud)
- [遥测监控、上下文窗口与 CLI 状态栏](#遥测监控上下文窗口与-cli-状态栏)
- [性能加速、工程流与多智能体编排](#性能加速工程流与多智能体编排)
- [浏览器自动化、Computer Use 与创意工作流](#浏览器自动化computer-use-与创意工作流)
- [跨智能体桥接与 ACP 协议生态](#跨智能体桥接与-acp-协议生态)
- [官方与合作伙伴 Marketplace 精选目录](#官方与合作伙伴-marketplace-精选目录)
  - [Google 官方生态与云服务](#google-官方生态与云服务)
  - [数据库、云平台与部署](#数据库云平台与部署)
  - [可观测性、安全扫描、测试与认证](#可观测性安全扫描测试与认证)
  - [设计协作、项目管理与商业支付](#设计协作项目管理与商业支付)
- [Skill 技能合集与插件开发脚手架](#skill-技能合集与插件开发脚手架)
- [环境配置与多账号管理工具](#环境配置与多账号管理工具)
- [界面汉化、主题美化与无障碍排版](#界面汉化主题美化与无障碍排版)
- [快速安装指南与标准插件结构](#快速安装指南与标准插件结构)
- [贡献与收录规范](#贡献与收录规范)

---

## 桌面端 UI 面板、辅助栏与悬浮窗 (HUD)

*专为 Antigravity 2.0 桌面端打造的原生 `UI Sidecar`（`SIDECAR_UI_ENTRYPOINT_AUX_PANE`）辅助面板、macOS 灵动胶囊悬浮窗与交互增强工作台。*

- **[AGY Floating HUD](https://github.com/biTQ-m/agy-floating-hud)** — 专为 Antigravity 2.0 Desktop (macOS) 打造的全屏置顶**灵动胶囊进度悬浮窗（`NSPanel`）**：通过只读 SQLite WAL + Lifecycle Hooks 毫秒级感知多会话实时进度、工具动作与 `task.md` 清单完成度，支持悬停展开多任务卡片、`<5ms` 点击直达对应会话标签页及完成发光/提示音提醒。`macOS` `Swift + Sidecar + Hooks`
- **[Postman Studio (`agy-postman`)](https://github.com/biTQ-m/agy-postman)** — Antigravity 右侧辅助栏原生可视化 **HTTP / REST / SSE 接口调试工作台**：零第三方 npm 依赖，内置零 CORS 本地 Node 代理、DNS/TCP/TLS/TTFB 耗时瀑布图、`transcript.jsonl` 对话流接口/cURL 自动嗅探、Postman Collection v2.1 导入导出、迷你并发压测与 AI Skill 双向互通。`Aux Pane Sidecar + Skill`
- **[Voice Reader (`agy-voice-reader`)](https://github.com/biTQ-m/agy-voice-reader)** — Antigravity 2.0 极速发音与**沉浸式双语词汇工作台（macOS）**：选中文本连按两下 `⌥` 或深按触摸板（Force Click）即刻朗读，内置 ~120ms 真人词典热通道 + 微软 Edge 高清神经人声流式混读；启用插件即通过 `rules/AGENTS.md` 自动注入目标词汇量与中英混排提示词闭环，并在侧边栏自动提炼重点词汇卡片与双语例句。`macOS` `Aux Pane Sidecar + Rules + Skill`
- **[AGY Powertools](https://github.com/WhiteBr1ck/agy-powertools)** — Antigravity 2.0 原生界面增强套件：支持类 Codex 紧凑排版与阶段汇报、上下文与缓存监控、会话分支及本地用量面板。
- **[Antigravity Sidecar Studio](https://github.com/burnerous/antigravity-sidecar-studio)** — 三合一侧边栏增强插件：集成工作区文件树、Word / Excel / PPT / PDF 离线高保真预览与编辑、划词引用联动 AI 及只读对话轨迹查看器。
- **[Antigravity Doc Preview](https://github.com/Cl-Ask47/antigravity-doc-preview)** — 在 Antigravity 侧边栏与内联聊天中直接预览 PDF、Word、PowerPoint 和 Excel 文档。
- **[Antigravity Pulse](https://github.com/yangyu2004/antigravity-pulse)** — 提供 Claude 风格内联步骤卡片、生命周期卡死监测与实时 Token 吞吐量仪表盘。
- **[Antigravity Inline Editor](https://github.com/mustafaakben/antigravity-inline-editor)** — 为 Antigravity 桌面端提供带自动保存、查找替换、批注与引用功能的内联编辑标签页。

---

## 遥测监控、上下文窗口与 CLI 状态栏

*100% 本地优先的观测插件与终端状态栏，用于实时追踪生成速度（`tok/s`）、上下文窗口预算、Prompt 缓存命中率与模型额度消耗。*

- **[AGY Statusline & Desktop Status](https://github.com/2fa0/agy-statusline)** — 零外部依赖、纯本地只读的状态监控套件：同时包含基于 Zig 构建的极速 CLI `statusLine` 与桌面端右侧常驻面板 `AGY Desktop Status`，实时展示平均输出速度（`tok/s`）及趋势图、轮次/会话耗时、上下文占用与 Prompt 缓存命中率。
- **[AGY Capsule](https://github.com/Lumidarin/agy-capsule)** — 直接在 Antigravity 输入框（Composer）内嵌展示上下文占用、模型配额、Token 细分与生成速率指标。
- **[Antigravity Context Mode](https://github.com/Domush/antigravity-plugin-context-mode)** — 本地优先的上下文窗口保护插件，拦截超长终端输出、构建日志与大文件刷屏，可削减 90%+ 无效上下文膨胀。
- **[AGY Context Dashboard](https://github.com/wycocoyu/agy-context-dashboard)** — 实时展示 Antigravity 上下文窗口、Token 消耗、缓存命中率与额度状态的仪表盘插件。
- **[AGY Powerline](https://github.com/wassim-azi/agy-powerline)** — 零依赖 `agy` CLI 状态栏，支持 Gemini 与 Claude 额度节奏提示、上下文进度条、Git 状态组件、22 套主题及终端与[浏览器](https://agy-powerline.com/configure/)可视化配置器。
- **[AGY HUD](https://github.com/franksde/agy-hud)** — 轻量级 Antigravity CLI 状态插件，集中展示上下文用量、配额比例、当前模型信息与 Agent 运行态。
- **[Antigravity Desktop Context](https://github.com/dimitr-io/antigravity-desktop-context)** — 面向 Antigravity 2.0 桌面端的实时 `/context` 侧边栏透视面板。
- **[Antigravity Dashboard](https://github.com/ShZbz/antigravity-dashboard)** — 支持 Desktop、IDE 与 CLI 的实时 Token 遥测与 Rust 加速本地用量账本。
- **[AGY Context](https://github.com/ahmetdotsh/agy-context)** — 原生 Sidecar 插件，用于查看实时上下文窗口构成、Prompt 缓存效率与单轮 Token 明细。
- **[AGY Usage](https://github.com/ahmetdotsh/agy-usage)** — 原生 Sidecar 插件，统计历史 Token 用量、API 等价成本估算与缓存节省金额。
- **[AGY Lens](https://github.com/xukp20/agy-lens)** — 本地只读桌面端遥测 Sidecar，内置 Prompt 缓存观测台、长上下文成本分析与日历热力图。
- **[Antigravity Status Monitor](https://github.com/rimenine/antigravity-status-monitor)** — 实时追踪 Agent 执行阶段、Lifecycle Hooks 与上游连通性的 Sidecar，快速区分正常思考与静默卡顿。
- **[ag-vario](https://github.com/Staaaying/ag-vario)** — 面向 macOS Antigravity 2.0 桌面端的零依赖、纯只读观测 HUD：支持在 2/3/4 分屏各窗格输入栏独立展示会话 Token、5 类上下文构成与子代理状态，顶栏提供 `5h`/`7d` 额度圆环与 30 天用量热力图，自带原版备份与一键无损还原。`macOS` `Desktop HUD`

---

## 性能加速、工程流与多智能体编排

*减少冗余轮次、管理会话工程流、自动化代码审查与多 Agent 闭环协作插件。*

- **[AGY Fast](https://github.com/INK-Q/agy-fast)** — 非侵入式 MCP 加速插件（支持 CLI / Desktop / IDE），在不破坏原生 UI 与 Diff 视图的前提下减少冗余工具轮次与 Token 开销。
- **[agy-memory](https://github.com/maxLWS/agy-memory)** — 零依赖本地跨对话记忆插件（支持 CLI / Desktop / IDE，与 `AGY Fast` 互补共存）：启动注入只读开场快照，支持中英文全文检索（自动回填 `transcript_full.jsonl` 长回复）、Swarm 倒序装包、文件写读与命令报错回溯（`file_history` / `error_history`）、带修订校验的可编辑 Markdown 笔记以及按需只读查本机 Codex / Claude 会话。`MCP + Hooks + Rules + CLI`
- **[AGY Dart](https://github.com/zou172866/agy-dart)** — 将批量工具加速、本地 SQLite FTS5 上下文窗口保护与实时 Sidecar 仪表盘融为一体的综合增强插件。
- **[AGY Fast IO](https://github.com/oil-oil/agy-fast-io)** — 让 Antigravity 少走冗余回合、减少非必要等待的轻量本地规则插件。
- **[Antigravity Conversation Renamer MCP](https://github.com/falconchen/antigravity-conversation-renamer-mcp)** — 基于 Node.js 内置 `node:sqlite` 的轻量级本地 Stdio MCP 服务（配套 `/rename` 斜杠命令 Skill 与话题偏离自动更新 Rule）：免辅助功能权限、无需重启客户端，在 `.pbtxt` 注解、SQLite 主表与 FTS5 索引及 Protobuf 缓存间原子无损同步重命名当前或历史会话标题。`MCP + Skill + Rules`
- **[AGYStack](https://github.com/jtaroreh/agystack)** — 面向 Google Antigravity 的闭环软件工程工作流与多智能体（Swarm）编排插件。
- **[Mission Control for Antigravity](https://github.com/todd866/antigravity-mission-control)** — 图形化 Antigravity 多会话控制中心（MCP App）：支持单轮 AI 摘要简报、跨 Mac 会话协同（`agy-status` / `agy-relay`）与 Flash / Carbon / Neon 自适应 AI Commander。`MCP App + CLI`
- **[Multigravity](https://github.com/GHSaiMo/antigravity-mobile)** — 面向 Google Antigravity IDE/CLI 的开源（MIT）原生 iOS（App Store 已上架）、Android 与 Web PWA 移动伴侣，通过本地 Go 网关（`mgy`）直连本机官方实例：支持实时对话与 `/swarm` 蜂巢监控、灵动岛实时步骤、APNs 锁屏一键审批、5h/7d 额度小组件、20 周 Token/缓存审计与零知识端到端加密（`mgy-e2ee-v1`）。`iOS / Android / PWA` `Local Go Gateway`
- **[CodeRabbit Antigravity Plugin](https://github.com/coderabbitai/antigravity-plugin)** — CodeRabbit 官方出品的原生插件，提供自动化 AI 代码审查与带安全护栏的 PR 自动修复工作流。
- **[AGY GCP Companion](https://github.com/ericsk/agy-gcp-companion)** — 在 Antigravity 内直接查看 GCP 项目、账单账户、预算水位与 BigQuery 当月支出。

---

## 浏览器自动化、Computer Use 与创意工作流

*打通内置浏览器子代理、桌面操作系统 GUI 操控、网页抓取与具身智能机器人的扩展插件。*

- **[GDM Robotics Plugin](https://github.com/google-deepmind/robotics-antigravity-plugin)** — Google DeepMind 官方开源机器人插件，涵盖 3D 感知、无碰撞运动规划、视觉伺服、MuJoCo 仿真与真机部署（Sim2Real）。
- **[Antigravity Flow](https://github.com/WeZZard/antigravity-flow)** — 基于 Antigravity 内置浏览器驱动 Google Flow 视频与创意生成工作流的插件。
- **[Computer Use AGY](https://github.com/Jayanyixing/computer-use-agy)** — 基于 MIT 协议开源的 macOS Computer Use MCP 服务与 Antigravity 桌面操控插件。
- **[Antigravity Cua Driver](https://github.com/WeZZard/antigravity-cua-driver)** — 基于 Cua Driver 的跨平台（macOS / Windows / Linux）后台原生 GUI 自动化插件。
- **[Firecrawl Antigravity Plugin](https://github.com/firecrawl/firecrawl-antigravity-plugin)** — Firecrawl 官方插件，为 Agent 提供高质量网页抓取、整站爬取与结构化 Markdown 提取能力。

---

## 跨智能体桥接与 ACP 协议生态

*基于 Agent Client Protocol (ACP) 与 MCP 的跨工具桥接器，支持在 Claude Code、Codex、Cursor 等客户端与 `agy` 之间协同派单。*

- **[AGY Staff](https://github.com/keli-wen/agy-staff)** — 在 Claude Code、OpenAI Codex 等工具中将 `agy` CLI 作为高速子代理调用，分担代码检索、长上下文阅读与交叉代码审查。
- **[Antigravity ACP](https://github.com/shubzkothekar/antigravity-acp)** — 基于 Bun 构建的 Agent Client Protocol (ACP) 服务端，让兼容 ACP 协议的编辑器直连驱动 `agy` 并支持流式输出与历史回放。
- **[Antigravity Plugin for Claude Code (`simplybychris`)](https://github.com/simplybychris/antigravity-plugin-cc)** — 在 Claude Code 内直接调用 `agy` 委派开发任务、执行快速问答或进行跨模型 Code Review。
- **[AGY Bridge](https://github.com/sshahzaiib/agy-bridge)** — 专为跨 Agent 协同设计的 MCP 桥接服务，支持模型回退路由、会话延续与长输出截断。
- **[AGY MCP](https://github.com/Boulea7/agy-mcp)** — 将 `agy` 封装为含 10 个强类型工具、支持 Git Worktree 隔离执行的标准 MCP 后端，可供任意 MCP 客户端接入。
- **[NotebookLM via Antigravity](https://github.com/MarcosNahuel/antigravity-plugin-cc)** — 借助 `agy` 实现本地版 NotebookLM：支持文件夹级文档摘要、相关性索引、带引用的综合问答、音视频转写与 HTML 研究报告导出。
- **[agy-remote-wecom](https://github.com/lukeinx/agy-remote-wecom)** — 在手机企业微信里通过长连接（无需公网服务器）远程遥控本机 Antigravity (`agy`) 终端会话与后台 `agy acp` 会话：支持切换/恢复历史会话、收发文字图片与文件、切换模型与权限模式、工具调用卡片审批与产物回传（macOS，含 `agy` 生命周期 Hook 插件）。

---

## 官方与合作伙伴 Marketplace 精选目录

*以下插件均已上架 **Antigravity 内置插件市场（Agent Marketplace）**，可在桌面端 `Customizations → Plugins` 搜索名称或通过 `Catalog ID` 一键安装。*

### Google 官方生态与云服务

| 插件名称 | Catalog ID | 核心能力 |
| :--- | :--- | :--- |
| **Google Antigravity SDK** | `antigravity-plugins-official/plugin/google-antigravity-sdk` | 使用官方 Google Antigravity Python SDK 构建自定义智能体的开发指南与技能包。 |
| **Google Cloud Developer** | `antigravity-plugins-official/plugin/google-cloud-developer` | GCP 项目初始化、凭据配置、`gcloud` 高危命令安全校验，并内置官方文档 MCP。 |
| **Google Developer Knowledge** | `antigravity-plugins-official/plugin/google-developer-knowledge` | 跨 Google Cloud、Gemini、Android、Firebase、Flutter 与 Web 官方文档的实时检索。 |
| **Firebase** | `antigravity-plugins-official/plugin/firebase` | 覆盖 Firebase 后端服务、认证、数据库与 AI 基础设施的原型构建与运维支持。 |
| **Dart & Flutter** | `antigravity-plugins-official/plugin/flutter` | Flutter / Dart 官方插件，打包专属 Skills、Rules、Custom Agents 与 Dart MCP Server。 |
| **Android CLI** | `antigravity-plugins-official/plugin/android-cli-plugin` | Android 应用开发核心命令行工具链与工程实践技能。 |
| **Google Workspace 套件** | `antigravity-plugins-official/plugin/gdocs` *(及 `gsheets`, `gslides`, `gdrive`, `gcalendar`)* | 官方打通 Google Docs、Sheets、Slides、Drive 与 Calendar 的读写、排版与日程协作。 |
| **Data Agent Kit** | `antigravity-plugins-official/plugin/data-agent-kit-plugin` | 面向 Google Cloud 数据工程师与数据库架构师的专业数仓/管道构建技能集。 |
| **Google Maps Platform** | `antigravity-plugins-official/plugin/google_maps_platform` | Google Maps Platform 地图与地理编码 API 集成工具与最佳实践。 |
| **科研与具身智能套件** | `antigravity-plugins-official/plugin/robotics` *(及 `genomics`, `structural-biology`)* | DeepMind 机器人研发、AlphaGenome 基因变异分析与 AlphaFold 蛋白质结构探索。 |

### 数据库、云平台与部署

| 插件名称 | Catalog ID | 核心能力 |
| :--- | :--- | :--- |
| **Supabase** | `antigravity-plugins-partners/plugin/supabase` | 官方 Supabase MCP 与技能集：涵盖 Postgres 表结构设计、RLS 权限、Auth、Storage 与边缘函数。 |
| **MongoDB Atlas** | `antigravity-plugins-partners/plugin/mongodb-atlas` | 连接托管版 Atlas MCP Server，支持集合探索、聚合管道编写与慢查询调优。 |
| **Neo4j** | `antigravity-plugins-partners/plugin/neo4j` | Cypher 查询编写、图数据建模、GraphRAG 流水线搭建及 Aura 实例运维。 |
| **Databricks** | `antigravity-plugins-partners/plugin/databricks` | 覆盖 Databricks CLI、Lakebase、Model Serving、Lakeflow 与 Spark 声明式管道。 |
| **Vercel** | `antigravity-plugins-partners/plugin/vercel-plugin` | Next.js 与 AI SDK 开发指南，配套官方 Vercel MCP 实现一键部署与日志排查。 |
| **Cloudflare** | `antigravity-plugins-partners/plugin/cloudflare` | 通过统一 Cloudflare MCP 开发与管理 Workers、KV/R2/D1 存储及 AI Gateway。 |
| **Netlify** | `antigravity-plugins-partners/plugin/netlify` | 支持 Serverless/Edge Functions、Blobs、数据库、图像 CDN 与 Netlify MCP 服务。 |
| **Railway** | `antigravity-plugins-partners/plugin/railway` | 在 Antigravity 内完成应用与数据库的部署、环境变量配置、监控及故障排查。 |

### 可观测性、安全扫描、测试与认证

| 插件名称 | Catalog ID | 核心能力 |
| :--- | :--- | :--- |
| **Sentry** | `antigravity-plugins-partners/plugin/sentry` | 拉取线上真实异常堆栈与 Release 上下文，辅助定位生产环境 Bug 并配置告警。 |
| **Grafana Cloud** | `antigravity-plugins-partners/plugin/grafana-cloud-mcp` | 通过托管 MCP 查询指标（Metrics）、日志（Logs）、链路（Traces）、性能剖析与告警事件。 |
| **SonarQube** | `antigravity-plugins-partners/plugin/sonarqube` | 在 AI 编码闭环内执行 7,500+ 条代码质量、安全漏洞与密钥泄露静态检测规则。 |
| **Browserbase** | `antigravity-plugins-partners/plugin/browse` | 为智能体提供本地及云端真实无头浏览器，支持自动交互、截图与网页结构化提取。 |
| **Harness** | `antigravity-plugins-partners/plugin/harness-antigravity` | 构建与调试 CI/CD 流水线、管理发布部署并排查安全扫描结果。 |
| **TestMu AI** | `antigravity-plugins-partners/plugin/testmu-ai` | 云端自动化测试排障，集成浏览器/移动端测试工具 Kane CLI 与智能体测试工具 Rook CLI。 |
| **Auth0** | `antigravity-plugins-partners/plugin/auth0` | 快速为任意应用接入登录认证、多因素认证（MFA）、企业 SSO、RBAC 权限与自定义域名。 |
| **Clerk** | `antigravity-plugins-partners/plugin/clerk` | 提供用户管理、多租户组织、计费订阅、Webhook 调试技能及官方 Clerk MCP 服务。 |

### 设计协作、项目管理与商业支付

| 插件名称 | Catalog ID | 核心能力 |
| :--- | :--- | :--- |
| **Figma** | `antigravity-plugins-partners/plugin/figma` | 将 Figma 设计稿转化为生产级代码、通过 Code Connect 映射组件库并读写 Figma 文件。 |
| **Canva** | `antigravity-plugins-partners/plugin/canva` | 通过 Canva MCP 自动生成海报/配图、批量调整尺寸并执行品牌视觉规范校验。 |
| **Mobbin** | `antigravity-plugins-partners/plugin/mobbin` | 让智能体直接检索 600,000+ 真实商业级移动端与 Web 产品界面截图作为设计参考。 |
| **Linear** | `antigravity-plugins-partners/plugin/linear`（[源码](https://github.com/linear/antigravity-plugin)） | 在编码上下文中直接查询、创建和流转 Linear Issue、迭代周期与技术方案。 |
| **Notion** | `antigravity-plugins-partners/plugin/notion` | 连接 Notion 工作区，支持检索知识库、撰写需求文档（PRD）、整理会议纪要与项目看板。 |
| **Atlassian Teamwork Graph** | `antigravity-plugins-partners/plugin/atlassian-twg-cli` | 专为编码智能体设计的统一命令行接口，贯通 Jira 任务、Confluence 文档与 Bitbucket PR。 |
| **Stripe** | `antigravity-plugins-partners/plugin/stripe` | 通过官方 Stripe MCP 管理商品定价、支付链接、订阅账单、退款并检索最新支付文档。 |

---

## Skill 技能合集与插件开发脚手架

*用于快速开发 Antigravity 新插件 / Sidecar 的开发工具包，以及可封装进插件的高质量 `SKILL.md` 技能仓库。*

- **[Antigravity Sidecar Kit](https://github.com/arthurcavallari/antigravity-sidecar-kit)** — 零依赖的 Antigravity 右侧辅助面板（Aux Pane Sidecar）SDK 与命令行脚手架，内置 Connect RPC 客户端、宿主主题与 Tailwind 同步代理及安装器。
- **[Antigravity Skills (`rmyndharis`)](https://github.com/rmyndharis/antigravity-skills)** — 高人气社区精选 Google Antigravity 技能库，覆盖前后端架构、测试、安全与运维场景。
- **[Sample Google Antigravity Skills (`rominirani`)](https://github.com/rominirani/antigravity-skills)** — 结构清晰的官方风格 `SKILL.md` 示例集合，适合作为编写自定义技能的入门模板。
- **[Antigravity Skills Engine](https://github.com/buiquangvu235/antigravity-skills-engine)** — 按专业工程赛道组织的工业级智能体技能库。
- **[Antigravity n8n Skills](https://github.com/WilkoMarketing/antigravity-n8n-skills)** — 专为 n8n 自动化工作流编排、节点参数配置与校验打造的 Antigravity 技能集。
- **[Spec-Kit Antigravity Skills](https://github.com/compnew2006/Spec-Kit-Antigravity-Skills)** — 面向规范驱动开发（Spec-Driven Development）的全流程软件工程技能体系。
- **[Antigravity Skills Chronicle](https://github.com/Zaious/Antigravity-Skills-Chronicle)** — 用于可视化浏览、启用与管理本地 Agent Skills、Workflows 和 Rules 的面板扩展。

---

## 环境配置与多账号管理工具

*面向 Antigravity CLI、Manager 与 Desktop/IDE 的跨平台多账号环境隔离、实时配额巡检与客户端环境管理工具。*

- **[agy-manager (`eligibility-antigravity-patcher`)](https://github.com/QNIX-Dev/eligibility-antigravity-patcher/blob/main/README.en.md)**（[源码仓库](https://github.com/QNIX-Dev/eligibility-antigravity-patcher)）— 跨平台轻量级 Antigravity 环境管理器（支持 `Windows` / `Linux` / `macOS`，兼容 `x64` 与 `arm64`），同时提供交互式 TUI 面板与零依赖 Python 标准库 CLI：支持多账号隔离配置切换、实时模型配额监控（5 小时与周维度窗口）以及带自动备份/签名还原的客户端地区可用性（Eligibility）补丁管理。
- **[AGY Switch](https://github.com/anglee0323/agy-switch)** — 跨平台（macOS / Windows / Linux）Antigravity 多账号切换、模型额度追踪与本地用量管理工具，同时提供桌面端与 CLI 界面。
- **[AGY Auth](https://github.com/fikrilal/agy-auth)** — 面向 Google Antigravity CLI 与桌面端的轻量级多账号快速切换工具。
- **[AGY CLI Manager](https://github.com/zcop/agy-cli-manager)** — 支持配额感知自动切换策略与自动化脚本接口的 Antigravity CLI 多账号管理器。
- **[agy-swap](https://agy-swap.aklkbqx.com/)**（[源码仓库](https://github.com/aklkbqx/agy-swap)）— 跨平台 Go 语言 TUI 与 CLI 工具（支持 `macOS` / `Linux` / `Windows`），用于在 Antigravity CLI 与 Desktop/IDE 间切换多账号并查看各模型实时剩余配额，内置防止后台令牌刷新覆盖当前会话的会话保护与写入前自动本地备份机制。凭证仅保存在本地（`0600` 权限的 `vault.json` 或通过 `AGY_SWAP_VAULT=keychain` 存入系统钥匙串），无使用遥测，仅含可选的每日版本检查缓存。`TUI + CLI`

---

## 界面汉化、主题美化与无障碍排版

*面向 Antigravity 桌面端的社区多语言包、自定义配色主题与排版增强工具。*

- **[Antigravity zh-CN (`MIMICTE`)](https://github.com/MIMICTE/Antigravity-zh-CN)** — 高星开源的 Google Antigravity 桌面端简体中文汉化补丁。
- **[Antigravity Desktop CN (`Silas-02`)](https://github.com/Silas-02/antigravity-desktop-cn)** — 支持 macOS / Windows / Linux 全平台一键安装、动态翻译与无损还原的桌面版汉化引擎。
- **[Antigravity Themes](https://github.com/materialwebunofficial/antigravity-themes)** — 面向 Antigravity Desktop 的第三方精选深浅色主题合集。
- **[Antigravity Tradução PT-BR](https://github.com/Emertels/Antigravity-Traducao-PTBR)** — 巴西葡萄牙语桌面端本地化语言包。
- **[RZ Antigravity RTL](https://github.com/rezasalimi01/rz-antigravity-rtl)** — 高性能从右向左（波斯语 / 阿拉伯语）排版引擎，严格隔离 Monaco 代码编辑器区域。

---

## 快速安装指南与标准插件结构

### 安装开源社区插件

绝大多数社区开源插件均在仓库根目录提供了 `install.sh` 一键脚本（默认软链接或拷贝至 `~/.gemini/config/plugins/<插件目录>`）：

```bash
git clone https://github.com/<作者>/<插件仓库>.git
cd <插件仓库>
chmod +x ./install.sh && ./install.sh
```

安装完成后，可在 Antigravity 桌面端 **Customizations → Plugins** 页面实时查看、启用或停用插件（Skills、Rules 与 MCP 即开即用；含 UI Sidecar 的插件可在右上角辅助面板栏点击 **`+`** 打开对应面板）。

### 标准插件目录解剖

```text
~/.gemini/config/plugins/<plugin-name>/
├── plugin.json                 # 必填清单（name, description, logo, suggestedPrompts 等）
├── README.md                   # 面向用户的说明文档
├── assets/logo.svg             # 方形图标资源（建议 128x128+，预留约 10% 边距）
├── sidecars/<id>/sidecar.json  # 可选：右侧辅助栏 Web UI Sidecar 服务声明
├── skills/<skill>/SKILL.md     # 可选：按需激活的智能体专业技能
├── agents/<agent>.md           # 可选：专属子代理（Subagent）定义
├── rules/AGENTS.md             # 可选：随插件启停自动生效的常驻提示词规则
├── hooks.json                  # 可选：PreInvocation / PostToolUse / Stop 生命周期钩子
└── mcp_config.json             # 可选：随插件生命周期托管的 MCP Server 配置
```

---

## 贡献与收录规范

非常欢迎提交你开发的 Antigravity 插件、UI Sidecar、MCP 扩展或修正现有分类！提交前请阅读 [CONTRIBUTING.md](./CONTRIBUTING.md)，或直接通过 [提交插件 Issue 模板](../../issues/new?template=submit-plugin.yml) 推荐项目。

> **免责与安全收录说明**：涉及本地客户端包体修改的社区工具（如界面汉化补丁、客户端环境补丁等）均为非官方项目，请结合自身环境审慎评估并做好原文件备份。任何包含恶意代码、窃取凭据/Token 或暗藏隐私上报的项目均不予收录。

## 开源协议

[![CC0](https://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](https://creativecommons.org/publicdomain/zero/1.0/)

在法律允许的最大范围内，[biTQ-m](https://github.com/biTQ-m) 基于 [CC0 1.0 通用公共领域奉献协议](./LICENSE) 放弃本精选列表的著作权及相关邻接权，欢迎自由传播与共建。
