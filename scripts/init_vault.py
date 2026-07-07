#!/usr/bin/env python3
"""Initialize an Obsidian personal vault skeleton.

This script is intentionally conservative:
- no network access
- no third-party dependencies
- no overwrites unless --force is passed
"""

from __future__ import annotations

import argparse
from pathlib import Path
from textwrap import dedent


DIRS = [
    "00-首页与导航",
    "10-个人档案/决策记录",
    "20-学习与项目/学习目标",
    "20-学习与项目/项目",
    "20-学习与项目/问题清单",
    "20-学习与项目/练习测验",
    "20-学习与项目/阶段复盘",
    "20-学习与项目/行动实验",
    "30-数据记录/身体/身体指标",
    "30-数据记录/身体/训练",
    "30-数据记录/身体/饮食",
    "30-数据记录/身体/睡眠与恢复",
    "30-数据记录/情绪/心情记录",
    "30-数据记录/情绪/精力与压力",
    "30-数据记录/情绪/触发因素与应对",
    "30-数据记录/时间与项目/时间投入",
    "30-数据记录/时间与项目/项目进展",
    "30-数据记录/时间与项目/阶段复盘",
    "30-数据记录/财务/收入与支出",
    "30-数据记录/财务/资产与负债",
    "30-数据记录/财务/预算与财务目标",
    "40-知识库/收件箱",
    "40-知识库/概念",
    "40-知识库/问题",
    "40-知识库/资料",
    "40-知识库/方法",
    "40-知识库/索引",
    "90-系统/模板",
    "90-系统/变更日志",
]


FILES = {
    "00-首页与导航/README.md": """# 00-首页与导航

这里是 Vault 的总入口。首页用于查看当前状态、快速记录、正在推进、近期复盘和系统说明。
""",
    "00-首页与导航/首页.md": """# 首页

## 当前状态

- [[当前状态总览]]

## 快速记录

- [[快速记录入口]]

## 正在推进

- 当前目标：[[../10-个人档案/当前目标|当前目标]]
- 学习与项目：[[../20-学习与项目/README|学习与项目]]

## 近期复盘

- [[近期复盘索引]]

## 系统说明

- [[../90-系统/助手使用说明|助手使用说明]]
- [[../90-系统/字段说明|字段说明]]
- [[../90-系统/命名规则|命名规则]]
""",
    "00-首页与导航/快速记录入口.md": """# 快速记录入口

可以记录：

- 身体：训练、身体指标、饮食、睡眠与恢复。
- 情绪：心情、精力压力、触发因素与应对。
- 时间与项目：时间投入、项目进展、阶段复盘。
- 财务：收入支出、资产负债、预算目标。

原则：追加型记录可以直接写；更新个人档案前需要预览。
""",
    "00-首页与导航/当前状态总览.md": """# 当前状态总览

## 个人档案

- [[../10-个人档案/当前目标|当前目标]]
- [[../10-个人档案/能力地图|能力地图]]
- [[../10-个人档案/健康与身体状态|健康与身体状态]]
- [[../10-个人档案/财务状态|财务状态]]

## 学习与项目

- 

## 最近观察

- 
""",
    "00-首页与导航/近期复盘索引.md": """# 近期复盘索引

## 周复盘

- 

## 月复盘

- 

## 阶段复盘

- 
""",
    "10-个人档案/README.md": """# 10-个人档案

这里保存动态自我模型和事实档案。规范档案记录当前状态，改写前需要展示差异。
""",
    "10-个人档案/基本信息.md": """---
type: profile
domain: profile
status: active
tags: [个人档案]
related: []
---

# 基本信息

## 基本情况

- 

## 长期背景

- 
""",
    "10-个人档案/当前目标.md": """---
type: profile
domain: profile
status: active
tags: [个人档案, 目标]
related: []
---

# 当前目标

## 当前主要目标

- 

## 阶段计划

- 

## 证据来源

- 

## 变更记录

- 
""",
    "10-个人档案/能力地图.md": """---
type: profile
domain: profile
status: active
tags: [个人档案, 能力]
related: []
---

# 能力地图

## 能力领域

| 能力 | 当前水平 | 证据 |
| --- | --- | --- |
|  |  |  |

## 待提升能力

- 
""",
    "10-个人档案/兴趣偏好与价值观.md": """---
type: profile
domain: profile
status: active
tags: [个人档案, 偏好, 价值观]
related: []
---

# 兴趣偏好与价值观

## 兴趣

- 

## 偏好

- 

## 价值观

- 

## 证据来源

- 
""",
    "10-个人档案/健康与身体状态.md": """---
type: profile
domain: body
status: active
tags: [个人档案, 身体]
related: []
---

# 健康与身体状态

## 当前摘要

- 

## 身体目标

- 

## 相关记录

- [[../30-数据记录/身体/README|身体数据]]

## 注意

这里不保存完整时间序列。原始记录放在 `30-数据记录/身体/`。
""",
    "10-个人档案/财务状态.md": """---
type: profile
domain: finance
status: active
tags: [个人档案, 财务]
related: []
---

# 财务状态

## 当前摘要

- 

## 财务目标

- 

## 相关记录

- [[../30-数据记录/财务/README|财务数据]]

## 注意

这里不提供投资建议。原始记录放在 `30-数据记录/财务/`。
""",
    "10-个人档案/外部反馈.md": """---
type: profile
domain: profile
status: active
tags: [个人档案, 外部反馈]
related: []
---

# 外部反馈

只记录与你成长、表达、项目、能力有关的重要反馈，避免记录他人过度隐私。

| 日期 | 来源 | 反馈 | 关联项目/能力 |
| --- | --- | --- | --- |
|  |  |  |  |
""",
    "20-学习与项目/README.md": """# 20-学习与项目

这里保存学习目标、实践项目、问题清单、练习测验、阶段复盘和行动实验。

学习闭环：目标 → 实践 → 问题 → 知识沉淀 → 练习测验 → 阶段复盘 → 调整计划。
""",
    "30-数据记录/README.md": """# 30-数据记录

数据记录分为身体、情绪、时间与项目、财务四大类。原始记录追加优先，复盘必须列出来源。
""",
    "30-数据记录/身体/README.md": """# 身体

包括身体指标、训练、饮食、睡眠与恢复。
""",
    "30-数据记录/情绪/README.md": """# 情绪

包括心情记录、精力与压力、触发因素与应对。这里只做观察，不做心理诊断。
""",
    "30-数据记录/时间与项目/README.md": """# 时间与项目

包括时间投入、项目进展、阶段复盘。
""",
    "30-数据记录/财务/README.md": """# 财务

包括收入与支出、资产与负债、预算与财务目标。这里只做记录和复盘，不做投资建议。
""",
    "40-知识库/README.md": """# 40-知识库

这里保存概念、问题、资料、方法和索引。收件箱内容整理时，补元数据和双链可直接执行；移动、合并、删除需要确认。
""",
    "90-系统/README.md": """# 90-系统

这里保存模板、字段说明、助手使用说明、命名规则和变更日志。
""",
    "90-系统/字段说明.md": """# 字段说明

```yaml
type: record | profile | review | knowledge | decision | experiment
domain: body | mood | time_project | finance | learning | knowledge | profile | mixed
date: YYYY-MM-DD
status: draft | active | archived | reviewed
tags: []
source:
related: []
```

Properties 用于筛选，正文承载完整语义。
""",
    "90-系统/助手使用说明.md": """# 助手使用说明

## 能做什么

- 追加身体、情绪、时间项目、财务记录。
- 更新个人档案前生成差异预览。
- 建立学习闭环。
- 整理知识库收件箱。
- 生成复盘、状态诊断、决策草稿和行动实验。

## 需要确认的操作

- 覆盖、删除、合并。
- 移动、重命名大量文件。
- 更新规范档案。
- 敏感档案的推断性改写。

## 安全边界

- 不读取或输出 `.env`、API Key、Token。
- 不主动联网。
- 不自动推送远程仓库。
- 不做医学诊断或投资建议。
""",
    "90-系统/命名规则.md": """# 命名规则

- 事件记录：`YYYY-MM-DD-主题.md`
- 周复盘：`YYYY-Wxx-周复盘.md`
- 月复盘：`YYYY-MM-月复盘.md`
- 规范档案：固定中文名，例如 `当前目标.md`
- 知识笔记：优先用问题或概念命名。
""",
}


TEMPLATES = {
    "训练记录.md": """---
type: record
domain: body
date:
status: active
tags: [身体, 训练]
related: []
---

# 训练记录

## 内容

| 项目 | 组数/次数/重量 | 备注 |
| --- | --- | --- |
|  |  |  |

## 状态

- 睡眠：
- 精力：
- 情绪：
- 疲劳：

## 观察

- 
""",
    "身体指标.md": """---
type: record
domain: body
date:
status: active
tags: [身体, 指标]
related: []
---

# 身体指标

| 指标 | 数值 | 备注 |
| --- | --- | --- |
| 体重 |  |  |
| 体脂 |  |  |
| 围度 |  |  |

## 观察

- 
""",
    "饮食记录.md": """---
type: record
domain: body
date:
status: active
tags: [身体, 饮食]
related: []
---

# 饮食记录

| 餐次 | 内容 | 备注 |
| --- | --- | --- |
| 早餐 |  |  |
| 午餐 |  |  |
| 晚餐 |  |  |
| 加餐 |  |  |

## 观察

- 
""",
    "睡眠恢复.md": """---
type: record
domain: body
date:
status: active
tags: [身体, 睡眠, 恢复]
related: []
---

# 睡眠与恢复

## 睡眠

- 时长：
- 质量：
- 入睡/醒来：

## 恢复

- 疲劳：
- 酸痛：
- 精力：

## 观察

- 
""",
    "心情记录.md": """---
type: record
domain: mood
date:
status: active
tags: [情绪]
related: []
---

# 心情记录

## 当前状态

- 心情：
- 精力：
- 压力：

## 触发因素

- 

## 应对方式

- 
""",
    "精力压力.md": """---
type: record
domain: mood
date:
status: active
tags: [情绪, 精力, 压力]
related: []
---

# 精力与压力

## 当前评分

- 精力：
- 压力：
- 专注：

## 可能来源

- 

## 应对

- 
""",
    "触发与应对.md": """---
type: record
domain: mood
date:
status: active
tags: [情绪, 触发因素, 应对]
related: []
---

# 触发因素与应对

## 事件

- 

## 触发因素

- 

## 反应

- 

## 有效应对

- 
""",
    "时间投入.md": """---
type: record
domain: time_project
date:
status: active
tags: [时间, 项目]
related: []
---

# 时间投入

| 项目/活动 | 时长 | 质量 | 备注 |
| --- | --- | --- | --- |
|  |  |  |  |

## 观察

- 
""",
    "项目进展.md": """---
type: record
domain: time_project
date:
status: active
tags: [项目, 进展]
related: []
---

# 项目进展

## 项目

- 

## 本次进展

- 

## 阻碍

- 

## 下一步

- 
""",
    "收支记录.md": """---
type: record
domain: finance
date:
status: active
tags: [财务]
related: []
---

# 收支记录

| 类型 | 金额 | 分类 | 备注 |
| --- | --- | --- | --- |
|  |  |  |  |
""",
    "资产负债快照.md": """---
type: record
domain: finance
date:
status: active
tags: [财务, 资产负债]
related: []
---

# 资产负债快照

## 资产

| 项目 | 金额 | 备注 |
| --- | --- | --- |
|  |  |  |

## 负债

| 项目 | 金额 | 备注 |
| --- | --- | --- |
|  |  |  |

## 观察

- 
""",
    "预算目标.md": """---
type: profile
domain: finance
date:
status: active
tags: [财务, 预算, 目标]
related: []
---

# 预算与财务目标

## 目标

- 

## 预算

| 分类 | 预算 | 实际 | 备注 |
| --- | --- | --- | --- |
|  |  |  |  |

## 复查日期

- 
""",
    "学习目标.md": """---
type: project
domain: learning
date:
status: active
tags: [学习]
related: []
---

# 学习目标

## 目标

- 

## 成功标准

- 

## 实践项目

- 

## 问题清单

- 

## 练习测验

- 

## 复盘节奏

- 
""",
    "学习问题.md": """---
type: knowledge
domain: learning
date:
status: active
tags: [学习, 问题]
related: []
---

# 学习问题

## 问题

- 

## 当前理解

- 

## 尝试过的方法

- 

## 下一步验证

- 
""",
    "练习测验.md": """---
type: review
domain: learning
date:
status: draft
tags: [学习, 练习, 测验]
related: []
---

# 练习测验

## 目标能力

- 

## 题目/练习

1. 
2. 
3. 

## 结果

- 

## 需要补的知识

- 
""",
    "阶段复盘.md": """---
type: review
domain: learning
date:
status: draft
tags: [复盘, 阶段]
related: []
---

# 阶段复盘

## 阶段目标

- 

## 完成情况

- 

## 证据

- 

## 问题与调整

- 
""",
    "决策记录.md": """---
type: decision
domain: profile
date:
status: active
tags: [决策]
related: []
---

# 决策记录

## 决策问题

- 

## 选项

- A：
- B：

## 已有证据

- 

## 利弊与风险

- 

## 最小验证行动

- 

## 复查日期

- 
""",
    "状态诊断.md": """---
type: review
domain: mixed
date:
status: draft
tags: [状态诊断]
related: []
---

# 状态诊断

## 观察问题

- 

## 读取来源

- 身体：
- 情绪：
- 时间与项目：
- 当前目标：

## 可能关联

| 观察 | 证据 | 可信度 |
| --- | --- | --- |
|  |  |  |

## 待观察变量

- 
""",
    "周复盘-模式发现.md": """---
type: review
domain: mixed
date:
status: draft
tags: [复盘, 模式发现]
related: []
---

# 周复盘：模式发现

## 本周事实

- 

## 重复出现的问题

- 

## 状态好的共同条件

- 

## 可能关联

| 观察 | 证据 | 可信度 |
| --- | --- | --- |
|  |  |  |

## 下周观察变量

- 
""",
    "复盘转行动.md": """---
type: experiment
domain: mixed
date:
status: active
tags: [复盘, 行动实验]
related: []
---

# 复盘转行动

## 来源复盘

- 

## 三个以内最小行动

1. 
2. 
3. 

## 验证方式

- 
""",
    "概念笔记.md": """---
type: knowledge
domain: knowledge
status: active
tags: [概念]
source:
related: []
---

# 概念

## 问题

- 

## 当前理解

- 

## 证据/来源

- 

## 适用边界

- 
""",
    "问题笔记.md": """---
type: knowledge
domain: knowledge
status: active
tags: [问题]
source:
related: []
---

# 问题笔记

## 问题

- 

## 背景

- 

## 当前答案

- 

## 证据/来源

- 

## 后续

- 
""",
    "资料卡片.md": """---
type: knowledge
domain: knowledge
status: active
tags: [资料]
source:
related: []
---

# 资料卡片

## 来源

- 

## 摘要

- 

## 可复用内容

- 

## 关联问题/项目

- 
""",
    "方法卡片.md": """---
type: knowledge
domain: knowledge
status: active
tags: [方法]
source:
related: []
---

# 方法卡片

## 适用场景

- 

## 步骤

1. 
2. 
3. 

## 注意事项

- 

## 相关实践

- 
""",
}


def normalize(text: str) -> str:
    return dedent(text).strip() + "\n"


def write_file(path: Path, content: str, *, dry_run: bool, force: bool) -> str:
    if path.exists() and not force:
        return f"skip existing file: {path}"
    if dry_run:
        action = "overwrite" if path.exists() else "create"
        return f"{action} file: {path}"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(normalize(content), encoding="utf-8")
    return f"wrote file: {path}"


def init_vault(vault: Path, *, dry_run: bool, force: bool) -> list[str]:
    actions: list[str] = []

    for item in DIRS:
        path = vault / item
        if dry_run:
            actions.append(f"ensure dir: {path}")
        else:
            path.mkdir(parents=True, exist_ok=True)
            actions.append(f"ensured dir: {path}")

    for rel_path, content in FILES.items():
        actions.append(write_file(vault / rel_path, content, dry_run=dry_run, force=force))

    for name, content in TEMPLATES.items():
        actions.append(write_file(vault / "90-系统" / "模板" / name, content, dry_run=dry_run, force=force))

    return actions


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Initialize an Obsidian personal vault skeleton.")
    parser.add_argument("--vault", required=True, help="Path to the Obsidian vault directory.")
    parser.add_argument("--dry-run", action="store_true", help="Print planned actions without writing files.")
    parser.add_argument("--force", action="store_true", help="Overwrite existing files.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    vault = Path(args.vault).expanduser().resolve()
    actions = init_vault(vault, dry_run=args.dry_run, force=args.force)
    for action in actions:
        print(action)


if __name__ == "__main__":
    main()
