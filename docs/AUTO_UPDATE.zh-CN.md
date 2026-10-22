# 每日自动维护：启用与审阅

本流程每天检索与人类视频驱动机器人学习相关的论文，仅在 `Learning Paradigms` 下新增四个类别的条目：

1. Agent+Human Data+Robot
2. World Action Model (WAM)
3. Vision-Language-Action Model (VLA)
4. In-Context & Video-Conditioned Learning (ICL & VCL)

不修改旧的 Information Transfer Taxonomy、数据集表格或其他章节，也不删除、改写已有论文。新增类别的 human data 在本仓库内指人类视频/视觉演示；纯文本、纯动捕或纯触觉数据不自动纳入。类别允许重叠。

## 你需要手动完成的步骤

### 1. 提交并推送当前 auto-update 分支

在仓库根目录运行，先检查暂存内容：

```bash
git switch auto-update
git add README.md .gitignore .github/workflows/auto-update.yml config/auto-update.json scripts/auto_update.py tests/test_auto_update.py data/auto-update/state.json docs/AUTO_UPDATE.zh-CN.md
git diff --cached --stat
git commit -m "feat: automate Learning Paradigms maintenance"
git push -u origin auto-update
```

如果你已经提交过这批文件，直接推送即可。不要将密钥写入文件或提交到 Git。

### 2. 将基础设施 PR 合入默认分支（通常为 main）

在 GitHub 创建 `auto-update → main` 的 PR，审阅并合并本次新增的工作流、脚本、配置、测试、状态文件、说明，以及 README 的新分类标题。

GitHub 的 `schedule` 只使用默认分支上的工作流，所以仅推送 `auto-update` 还不能启用每日运行。这个初次合并完成后，工作流每次都会切换到 `auto-update`，合并默认分支的新变化，再将论文更新推送到 `auto-update`，不会直接推送到 `main`。

建议保留 `auto-update` 分支。即使合并 PR 后删除了它，下次运行也会从默认分支重建；未合并的更新和队列状态只有保留分支才能保留。使用正常 merge commit 最便于这个长期分支持续合并。

### 3. 配置模型 API

打开仓库 **Settings → Secrets and variables → Actions**。

在 **Secrets** 新建：

| 名称 | 内容 |
| --- | --- |
| `LLM_API_KEY` | 模型服务商的 API Key |

在 **Variables** 新建：

| 名称 | 内容 |
| --- | --- |
| `LLM_BASE_URL` | 支持 Chat Completions 格式的 API 基础地址，包含服务商要求的版本路径，例如 `https://你的服务商域名/v1`；支持明确配置的 HTTP 地址和自定义端口；不要写到 `/chat/completions` |
| `LLM_MODEL` | 账号有权限调用的模型 ID；填写服务商给出的实际名称 |
| `LLM_JSON_MODE` | 可选；服务商支持 `response_format: {"type":"json_object"}` 时设为 `true`，否则留空或 `false` |

脚本请求 `${LLM_BASE_URL}/chat/completions`，使用 Bearer API Key、`messages` 和 `max_tokens` 参数。服务商必须兼容这些字段。模型需要可靠的论文阅读、分类和 JSON 输出能力，建议至少 64k token 上下文窗口。正文最多输入 60,000 字符，具体 token 数依语言和公式而变化。

模型接口地址由仓库维护者明确配置，可以使用 HTTP 和自定义端口；从论文中提取的外部链接仍单独校验。HTTP 会明文传输 API 密钥和请求内容，服务商提供 HTTPS 时应优先使用 HTTPS。

只有这个 Secret 是必需的凭据。推送和创建 PR 使用 GitHub 自带的 `GITHUB_TOKEN`，通常不需要额外 PAT。Actions 运行额度和模型 API 费用遵循各自服务商的计费规则。

### 4. 允许工作流写入分支和创建 PR

打开 **Settings → Actions → General → Workflow permissions**：

- 允许 **Read and write permissions**。
- 勾选 **Allow GitHub Actions to create and approve pull requests**。本工作流只创建/更新 PR，不会自动批准或合并。
- 确保仓库启用了 Actions，组织策略允许上述权限和 GitHub 官方 Actions。
- 分支规则需要允许机器人推送 `auto-update`；`main` 可以继续保持保护。

如果组织禁止 Actions 创建 PR，运行会在 PR 步骤报错；分支可能已成功推送，你仍可手动创建 PR，或由管理员放开权限。

### 5. 先预览，再正式运行

进入 **Actions → Maintain Learning Paradigms → Run workflow**：

1. 使用默认分支运行，保留 `dry_run = true`。预览也会调用模型，产生正常 API 用量，但不推送分支或创建 PR。
2. `lookback_days` 留空使用默认配置；需要补收时可填 `30`，最多回溯配置中的 `max_catchup_days`（默认 90）。
3. 查看运行的 **Summary** 和 `auto-update-report-…` artifact，核对论文、分类理由和引文。
4. 再运行一次，取消 `dry_run`，检查 `auto-update` 分支和自动创建的 PR。

每天计划在北京时间 **08:00** 运行（UTC 00:00），GitHub 可能排队延迟。之后无需电脑保持开机。只有默认分支中已合入的工作流会按时运行；修改执行时间也需要将工作流变更合入默认分支。

公开仓库长时间无活动时，GitHub 可能暂停定时工作流，可到 Actions 页面重新启用。失败可在 Actions 运行记录中查看；需要通知时在 GitHub 个人通知设置中启用 Actions 失败通知。

## 每次运行的实际流程

1. arXiv 按关键词和首次提交日期检索，默认覆盖最近 7 天；如果中间漏跑，从上次成功检索日期前一天补查，最多 90 天。
2. 补充最近 3 天的 Hugging Face Daily Papers；这些论文仍回到 arXiv 获取正式元数据，并以人类视觉数据和机器人相关词做初筛，避免无关热门论文挤占队列。该辅助来源失败会记录警告，核心 arXiv 查询失败则不提交。
3. 将候选与 `data/auto-update/state.json` 对照去重。每轮最多检查 12 篇，未处理候选留在分支队列，优先处理先入队的论文。
4. 获取 arXiv HTML 正文；失败时下载 PDF 并用 `pdftotext` 提取。全文无法获取的论文不凭摘要自动收录。
5. 模型根据四类定义判断相关性，返回分类理由、置信度、人类数据使用证据、机器人学习证据及分类证据。程序要求引文确实出现在输入正文/元数据中，置信度默认至少 0.85。该数值是模型自评，不是经过校准的正确率；最终仍通过 PR 审阅。
6. Code/Page 只能来自论文正文、链接或作者评论中出现的 HTTPS 地址，且须有归属于该论文的引文；再检查链接可访问。缺失或验证失败保留 `[Code]` / `[Page]`。只有确认 GitHub 仓库包含源代码文件才加 🌟；有物理机器人实验原文依据才加 🤖。
7. 使用 arXiv 标题和首次提交年月，按现有格式插入对应分类和年份。同一分类不重复添加 arXiv ID/同名论文；允许在多个分类出现。已有条目原样保留。
8. 只提交 README 和候选状态到 `auto-update`。有 README 差异时创建或更新一个待审阅 PR；只有队列/排除记录变化时不新建 PR。不会自动合并。

正式运行的状态文件保留判断、分类、原文引文、来源地址和模型/规则指纹，便于检查，也避免对没有变化的论文反复调用模型。修改分类规则、模型或模型接口设置后会重新排队判断；不回删 README 已有内容。单篇全文或模型输出解析失败最多尝试三次，之后进入 `review`。如果本轮所有模型检查都失败，任务返回失败状态、生成包含具体错误的报告，并跳过 README 和状态写入及推送。

PR 正文与 Actions Summary 展示**最近一次运行**，PR 的 Files changed 则显示尚未合并的累计更新。历史逐篇证据保存在状态文件；运行报告 artifact 保留 30 天。

## 可以调整的配置

编辑 `config/auto-update.json`：

| 字段 | 默认值 / 用途 |
| --- | --- |
| `lookback_days` | 7；每日重叠检索窗口 |
| `max_catchup_days` | 90；漏跑或手动补查的最大天数 |
| `max_candidates_per_run` | 12；每次最多检查几篇，主要控制模型用量 |
| `max_results_per_query` | 300；每个 arXiv 查询的结果上限；超限会报错，避免默默漏掉结果 |
| `max_source_chars` | 60000；每篇正文的字符上限，不是 token 上限 |
| `min_confidence` | 0.85；模型自评低于此值转待核查 |
| `huggingface_daily_days` | 3；设为 0 可以关闭该辅助来源 |
| `queries` | arXiv 查询表达式；覆盖 human video、egocentric、human demonstrations 等 |
| `seed_arxiv_ids` | 手动补充待检查 ID，如 `["2602.04600"]`；可超出近期窗口 |
| `excluded_arxiv_ids` | 人工永久排除的 ID，不会自动插入；已有 README 条目需要你另行删除 |
| `scope`、`categories.*.criteria` | 纳入标准与四类定义；不要改变类别 ID/标题，渲染器会拒绝未知分类 |

配置修改建议通过 PR 合入默认分支，下一次会同步到 `auto-update`。仅在 `auto-update` 上的修改也会用于该分支执行，但不会改变默认分支的定时触发设置。

待核查文章可在报告和 `state.json` 中找到。人工确认后可以按现有模板直接添加。若要让程序重新尝试某篇论文，从状态文件删除该 ID 对应记录，并把 ID 放入 `seed_arxiv_ids`；确认要拒绝的论文加入 `excluded_arxiv_ids`。这些改动也应提交。

## 覆盖范围与限制

- 首版自动发现的是 arXiv 论文，辅以 Hugging Face 日报；不会自动阅读微信公众号或发现所有机构博客。没有 arXiv 的 Dyna、Skild 等官方技术博客仍需人工维护。
- arXiv 检索按首次提交日期，不能保证发现旧论文刚发布的代码、新版本或新会议录用信息。手动 seed 可以重新获取其元数据，但已有 README 行不会自动改写。
- 这是新增流程，不自动修订历史标题、移动分类或删除条目。错误分类应通过 PR 修正，必要时排除对应 ID。
- 主题召回依赖关键词，不承诺穷尽论文。过多低相关候选占用额度时可收紧查询或提高每轮处理数量。
- 本地验证和离线测试不能代替实际服务商联调。HTTP 401/403 通常检查密钥和模型权限；404 检查基础地址和模型名；429 检查额度；上下文超限可降低 `max_source_chars`。
- 报告中 `Model check failed` 后会显示具体错误，例如 `finish_reason=length` 表示模型输出达到长度上限，`Missing decision or reason` 表示返回 JSON 缺少必需字段。所有检查失败时 Actions 会显示失败，不会再只更新状态文件却显示成功。
- `auto-update` 与默认分支冲突时任务停止，不做强制覆盖。你可以本地 `git fetch origin`、`git switch auto-update`、合并 `origin/main`，解决冲突后提交推送，再手动重跑。若默认分支不是 main，请替换该名字。
- 如果机器人推送与人工推送发生竞争，普通 push 会失败而不会覆盖对方；同步分支后重新运行。

## 本地测试和检索预览

无需模型密钥的离线测试：

```bash
python3 -m unittest discover -s tests -v
```

只检索，不调用模型、不修改 README/状态：

```bash
python3 scripts/auto_update.py --discover-only --lookback-days 7
```

本地完整预览需要 Python 3.11+、上述三个 `LLM_*` 环境变量和网络访问；PDF 回退需要 `pdftotext`（macOS 可安装 poppler）。报告文件默认写在根目录并已加入 `.gitignore`。

```bash
python3 scripts/auto_update.py --dry-run
```

不要把 API Key 粘贴进 README、配置、PR 或聊天记录。建议使用本地密钥管理器设置环境变量。
