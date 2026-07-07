# personal-file

`personal-file` 是一个用于 Obsidian 的个人系统 Skill。它帮助你把知识、学习、个人档案、身体数据、情绪状态、时间与项目、财务记录、复盘和决策整理到一个本地 Markdown Vault 里。

它的目标不是把 Obsidian 变成 AI 黑箱，而是建立一个你自己也能打开、阅读、维护和接管的个人档案系统。

## 它能做什么

`personal-file` 主要支持这些能力：

- 建立 Obsidian Vault 骨架。
- 维护个人档案：当前目标、能力地图、兴趣偏好、健康状态、财务状态、外部反馈、决策记录。
- 建立学习闭环：学习目标、实践项目、问题清单、练习测验、阶段复盘、行动实验。
- 记录数据：身体、情绪、时间与项目、财务。
- 整理知识库：收件箱、概念笔记、问题笔记、资料卡片、方法卡片。
- 做复盘：周复盘、月复盘、阶段复盘、模式发现。
- 做状态诊断：观察睡眠、训练、情绪、时间投入、项目压力之间的可能关联。
- 做决策辅助：整理目标、证据、利弊、风险和最小验证行动。
- 把复盘转成 1-3 个可执行行动。

## 适合什么时候用

你可以在这些场景里调用它：

```text
$personal-file 帮我初始化一个 Obsidian 个人知识库
$personal-file 记录今天训练：深蹲 5x5 100kg，睡眠一般
$personal-file 我想 4 周学会 TypeScript，帮我建立学习项目
$personal-file 记录学习问题：我分不清 interface 和 type
$personal-file 复盘这周，看看训练、情绪和项目推进有什么关系
$personal-file 整理收件箱，重复笔记先给我合并预览
$personal-file 帮我做一个决策记录：是否暂停 A 项目
$personal-file 把这次复盘压缩成下周三个行动
```

## Vault 结构

初始化后建议的 Obsidian Vault 顶层结构：

```text
00-首页与导航
10-个人档案
20-学习与项目
30-数据记录
40-知识库
90-系统
```

其中 `30-数据记录` 分为四大类：

```text
30-数据记录
├── 身体
│   ├── 身体指标
│   ├── 训练
│   ├── 饮食
│   └── 睡眠与恢复
├── 情绪
│   ├── 心情记录
│   ├── 精力与压力
│   └── 触发因素与应对
├── 时间与项目
│   ├── 时间投入
│   ├── 项目进展
│   └── 阶段复盘
└── 财务
    ├── 收入与支出
    ├── 资产与负债
    └── 预算与财务目标
```

## 初始化 Vault

可以使用内置脚本初始化一个空的 Obsidian Vault 骨架。

先 dry-run 预览：

```bash
python3 scripts/init_vault.py --vault /path/to/ObsidianVault --dry-run
```

确认后正式创建：

```bash
python3 scripts/init_vault.py --vault /path/to/ObsidianVault
```

脚本默认不会覆盖已有文件。只有在你明确需要覆盖模板或系统文件时，才使用：

```bash
python3 scripts/init_vault.py --vault /path/to/ObsidianVault --force
```

## 工作原则

`personal-file` 遵循这些原则：

- 本地 Markdown 是唯一事实源。
- 原始记录追加优先。
- 规范档案谨慎改写。
- 低风险操作可直接执行。
- 中风险操作先预览。
- 高风险操作单独确认。
- 不主动联网。
- 不自动推送远程仓库。
- 不读取或输出 `.env`、API Key、Token。
- 健康、心理、财务相关内容只做记录和观察，不做医学诊断或投资建议。
- 不认识的人工字段默认保留，不擅自清理。

## 风险分级

低风险，通常可直接执行：

- 新增记录。
- 补 Properties。
- 补标签。
- 补双链。
- 生成草稿和派生视图。

中风险，需要先预览：

- 移动文件。
- 重命名文件。
- 批量调整分类。
- 更新项目状态。

高风险，必须单独确认：

- 删除文件。
- 合并文件。
- 覆盖既有内容。
- 修改大量历史记录。
- 涉及健康、财务等敏感档案的推断性改写。

## 学习闭环

学习辅助是这个 Skill 的核心能力之一。它不是只生成学习计划，而是把学习变成闭环：

```text
学习目标 → 实践项目 → 学习问题 → 知识沉淀 → 练习测验 → 阶段复盘 → 下一步行动
```

例如：

```text
$personal-file 我想 4 周学 TypeScript，目标是能改自己的项目代码
```

它会帮助创建：

- 学习目标。
- 实践项目。
- 问题清单。
- 练习测验。
- 阶段复盘。
- 相关知识笔记。

完成阶段学习后，还可以把成果整理到 `10-个人档案/能力地图.md`，作为能力证据。

## 关键文件

Skill 包内主要文件：

```text
SKILL.md
README.md
references/vault-structure.md
references/intent-routing.md
references/templates.md
scripts/init_vault.py
```

说明：

- `SKILL.md`：Skill 的主入口和行为规则。
- `README.md`：使用说明。
- `references/vault-structure.md`：Vault 结构规范。
- `references/intent-routing.md`：意图路由与风险规则。
- `references/templates.md`：模板体系说明。
- `scripts/init_vault.py`：Vault 初始化脚本。

## 验证安装

确认文件存在：

```bash
ls ~/.codex/skills/personal-file
```

测试初始化脚本：

```bash
python3 ~/.codex/skills/personal-file/scripts/init_vault.py --vault /tmp/personal-file-test --dry-run
```

如果刚安装后 `$personal-file` 不能立刻调用，可能是当前 Codex 线程还没有刷新技能索引。新开线程或重启 Codex 后再试。

