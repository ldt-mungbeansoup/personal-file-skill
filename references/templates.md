# 模板体系

## 统一 Properties

建议字段：

```yaml
---
type:
domain:
date:
status:
tags:
source:
related:
---
```

说明：

- `type`：record、profile、review、knowledge、decision、experiment。
- `domain`：body、mood、time_project、finance、learning、knowledge、profile。
- `date`：记录日期。
- `status`：draft、active、archived、reviewed。
- `tags`：Obsidian 标签。
- `source`：来源文件或输入。
- `related`：相关双链。

正文必须保留人类可读说明，不能只依赖 Properties。

## 记录模板

### 训练记录

```markdown
---
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
```

### 心情记录

```markdown
---
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

## 备注

- 
```

### 时间投入

```markdown
---
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
```

### 收支记录

```markdown
---
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

## 观察

- 
```

## 档案模板

### 当前目标

```markdown
---
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
```

### 决策记录

```markdown
---
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
```

## 学习模板

### 学习目标

```markdown
---
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
```

## 复盘模板

### 周复盘-模式发现

```markdown
---
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
```

### 复盘转行动

```markdown
---
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
```

## 知识模板

### 概念笔记

```markdown
---
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

## 相关链接

- 
```
