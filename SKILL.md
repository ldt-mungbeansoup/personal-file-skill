---
name: personal-file
description: "Use this to manage an Obsidian-based personal file system: personal profile, learning loops, body/mood/time-project/finance records, knowledge organization, reviews, state diagnosis, and decision support."
---

# personal-file

Obsidian 个人知识库、个人档案、学习闭环与生活数据助手。

## 何时使用

当用户希望在 Obsidian 中整理个人知识库、建立个人档案、记录身体/情绪/时间项目/财务数据、辅助学习、复盘、状态诊断或决策辅助时，使用本 Skill。

典型请求：

- “帮我初始化一个 Obsidian 个人知识库。”
- “记录今天训练：深蹲 5x5，睡眠一般。”
- “更新我的当前目标。”
- “帮我建立一个学习项目。”
- “整理收件箱，重复笔记先给我预览。”
- “复盘这周，看看训练、情绪和项目推进有什么关系。”
- “帮我做一个决策记录。”
- “把复盘压缩成下周三个行动。”

## 核心原则

1. 本地 Markdown 是唯一事实源。
2. 用户必须能手动阅读、维护和接管 Vault。
3. 原始记录追加优先；规范档案谨慎改写。
4. 低风险直接执行，中风险先预览，高风险单独确认。
5. 不读取、不输出 `.env`、API Key、Token。
6. 不主动联网，不自动推送远程仓库。
7. 健康、财务、心理相关内容只做记录、复盘和观察，不做高风险专业结论。
8. 不认识的人工字段默认保留，不擅自清理。

## 必读参考

执行任务前，根据任务类型读取：

- 初始化或解释 Vault 结构：`references/vault-structure.md`
- 判断用户意图和风险：`references/intent-routing.md`
- 创建或修改模板：`references/templates.md`

## 默认工作流

1. 识别用户意图：记录、更新档案、学习闭环、知识整理、复盘、状态诊断、决策辅助、复盘转行动。
2. 限定读取范围：只读完成任务所需的目录和索引。
3. 说明将新增、修改、移动或删除哪些文件。
4. 按风险分级处理：
   - 低风险：追加记录、补标签、补双链、生成草稿，可直接执行。
   - 中风险：移动、重命名、批量分类、更新项目状态，先预览。
   - 高风险：删除、合并、覆盖、敏感推断性改写，单独确认并建议 Git 检查点。
5. 写入后校验：
   - 路径是否正确。
   - Properties 和正文是否一致。
   - 双链是否合理。
   - 是否保留用户人工字段。
   - 是否避免泄露敏感值。
6. 最后说明验证方式。

## 初始化 Vault

可以使用脚本生成首批目录、首页、核心档案、模板和系统说明：

```bash
python3 scripts/init_vault.py --vault /path/to/ObsidianVault --dry-run
python3 scripts/init_vault.py --vault /path/to/ObsidianVault
```

脚本默认不覆盖已有文件。只有用户明确允许时才使用 `--force`。

## 模块顺序

实施与扩展优先级：

1. B：个人档案。
2. D：学习辅助。
3. C：数据记录与分析。
4. A：知识库整理。

## 输出风格

给方案时先说明优劣势和权衡，再给建议。  
写文件前说明会改哪些文件。  
写文件后说明验证方式。  
保持改动最小，不碰无关文件。
