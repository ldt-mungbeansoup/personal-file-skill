# personal-file Skill 实施与自检

## 本次实现内容

本次实现新增一个可安装 Skill 包，并附带正式设计文档与初始化脚本。Skill 名称为 `personal-file`，已同步安装到本机 Codex Skills 目录：

```text
/Users/lvdoutang/.codex/skills/personal-file/
```

新增文件：

```text
docs/personal-file-skill-design.md
docs/personal-file-skill-implementation.md

codex-skills/personal-file/SKILL.md
codex-skills/personal-file/references/vault-structure.md
codex-skills/personal-file/references/intent-routing.md
codex-skills/personal-file/references/templates.md
codex-skills/personal-file/scripts/init_vault.py
```

## 使用方法

### 1. 在 Codex 中使用 Skill

把 `codex-skills/personal-file/` 安装或复制到 Codex Skills 目录后，即可用类似方式调用：

```text
$personal-file 帮我初始化一个 Obsidian 个人知识库
$personal-file 记录今天训练：深蹲 5x5 100kg，睡眠一般
$personal-file 整理收件箱，重复笔记先给我合并预览
$personal-file 复盘这周，重点看训练、情绪和项目推进的关系
```

### 2. 初始化 Vault 骨架

在 Skill 包目录下运行：

```bash
python3 scripts/init_vault.py --vault /path/to/your/ObsidianVault
```

预览将创建哪些文件：

```bash
python3 scripts/init_vault.py --vault /path/to/your/ObsidianVault --dry-run
```

默认不会覆盖已有文件。若确实要覆盖模板文件，可以加：

```bash
python3 scripts/init_vault.py --vault /path/to/your/ObsidianVault --force
```

## 实施阶段

### B：个人档案

已覆盖：

- 基本信息。
- 当前目标。
- 能力地图。
- 兴趣偏好与价值观。
- 健康与身体状态。
- 财务状态。
- 外部反馈。
- 决策记录目录。

### D：学习辅助

已覆盖：

- 学习目标模板。
- 学习问题模板。
- 练习测验模板。
- 项目进展模板。
- 阶段复盘模板。
- 行动实验目录。

### C：数据记录与分析

已覆盖：

- 身体：身体指标、训练、饮食、睡眠恢复。
- 情绪：心情记录、精力压力、触发与应对。
- 时间与项目：时间投入、项目进展、阶段复盘。
- 财务：收支记录、资产负债快照、预算目标。
- 状态诊断。
- 周复盘-模式发现。
- 复盘转行动。

### A：知识库整理

已覆盖：

- 概念笔记。
- 问题笔记。
- 资料卡片。
- 方法卡片。
- 收件箱整理规则。
- 移动、合并、删除确认策略。

## 自检结果

### 结构完整性

- [x] 顶层目录覆盖 `00-首页与导航`、`10-个人档案`、`20-学习与项目`、`30-数据记录`、`40-知识库`、`90-系统`。
- [x] 数据记录按身体、情绪、时间与项目、财务四大类细分。
- [x] 新增决策辅助、外部反馈、行动实验、状态诊断、复盘转行动。

### 安全性

- [x] Skill 明确禁止读取和输出 `.env`、API Key、Token。
- [x] 初始化脚本不联网、不依赖第三方包。
- [x] 初始化脚本默认不覆盖已有文件。
- [x] 合并、删除、覆盖、敏感档案改写要求确认。

### 人工可读性

- [x] 首页、快速记录入口、当前状态总览、近期复盘索引已设计。
- [x] 每个一级目录设计 README。
- [x] 模板正文使用中文说明，不只依赖 Properties。
- [x] 系统目录包含字段说明和助手使用说明。

### 可实施性

- [x] Skill 包有 `SKILL.md` 主入口。
- [x] 参考文档拆分为目录结构、意图路由、模板说明。
- [x] 初始化脚本可生成最小可用 Vault 骨架。
- [x] 设计文档可作为后续扩展依据。

## 后续建议

1. 找一个空目录运行 `init_vault.py --dry-run`。
2. 确认预期后运行正式初始化。
3. 用 Obsidian 打开该目录。
4. 先从 B 阶段填写个人档案，再进入 D/C/A。
5. 本机已安装 Skill；若以后在其他机器使用，把 `codex-skills/personal-file/` 复制到 `~/.codex/skills/personal-file/`。
