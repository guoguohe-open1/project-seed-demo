# AI Project Seed

一套面向 Codex 与其他 Coding Agent 的轻量项目启动模板。目标不是让每个项目先写完大量文档，而是把**稳定的工程规则固化一次**，再根据项目类型和风险按需启用。

## 设计原则

1. **先有一个可验证的纵向闭环，再逐步抽象。** 不在没有真实用例前设计庞大的通用框架。
2. **文档分工明确。** `AGENTS.md` 管工作规则；`PRODUCT.md` 管目标与范围；`ARCHITECTURE.md` 管系统边界；`CONTRACTS.md` 管接口和不变量；ADR 记录重要决策；变更 Spec 管单次工作。
3. **风险决定流程重量。** 小修复走轻流程；跨模块功能、公共契约变化、数据迁移和高风险副作用走完整流程。
4. **测试证据优先于口头声明。** 必须区分已运行、未运行、失败和被阻塞的检查。
5. **种子不替代判断。** 模板是起点，不是必须填满的文档清单。

## 5 分钟启动

需要 Python 3.10+，无第三方依赖。

```bash
python scripts/bootstrap.py --target ../my-agent-project --name "My Agent Project" --description "项目的一句话说明" --profile agent-evaluation
cd ../my-agent-project
```

可选 Profile：

- `generic`：通用项目
- `agent-evaluation`：Agent 评测与仿真
- `agent-application`：面向业务的 Agent 应用
- `rag-system`：RAG / 知识增强系统

脚本只会在目标目录不存在或为空时写入文件；不会覆盖已有项目文件。

## 新项目启动流程

1. 运行 `bootstrap.py` 生成最小文档骨架。
2. 只填写 `docs/PROJECT_BRIEF.md` 中的已知信息；未知内容标为 `TBD`，不要为了完整而臆造。
3. 让 Codex 做一次**只读发现与规划**，对需求、现有文件、风险和未知项进行归纳；暂不写业务代码。
4. 人工确认目标、非目标、首个纵向切片和验收条件。
5. 先实现一条端到端闭环；根据真实代码与测试更新架构文档。
6. 之后每个中等以上任务使用一个变更 Spec；重大架构变化必须有选项比较和 ADR。

## 常用命令

```bash
python scripts/bootstrap.py --target ../my-project --name "My Project" --profile generic
python -m unittest discover -s tests -v
python scripts/bootstrap.py --help
```

## 何时需要完整流程？

| 改动 | 建议流程 |
|---|---|
| 文案、注释、局部小修复 | 明确范围 + 针对性验证 |
| 单模块功能 | Feature Spec + 测试 + Diff 审查 |
| 跨模块功能 / 公共接口变化 | 影响分析 + 契约测试 + 完整回归 |
| 架构替换 / 数据迁移 / 外部副作用 | 方案比较 + ADR + 回滚计划 + 明确批准 |
| 技术路线不确定 | Time-boxed Spike，先实验后决定 |

## GitHub Template Repository

将本仓库推送到 GitHub 后，可以在仓库 Settings 中启用 **Template repository**。之后可通过 “Use this template” 创建新仓库。也可以克隆本仓库后运行 `bootstrap.py`，生成一个干净的项目骨架。

## 版本策略

- `v0.x`：模板格式允许快速演进；使用者应按需挑选更新，不建议盲目覆盖项目文档。
- 更新种子时先比较 Diff；只迁移通用规则和明确需要的模板变化。
- 项目的业务事实、架构决策和运行数据归具体项目所有，不反向写回种子。

## 目录导航

- `AGENTS.md`：维护本种子仓库本身时使用的规则。
- `templates/`：复制到新项目的基础文件。
- `profiles/`：项目类型专项规则。
- `scripts/bootstrap.py`：生成项目骨架。
- `tests/`：验证脚手架行为。
