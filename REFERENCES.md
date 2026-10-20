# REFERENCES.md — 外部资料清单与使用规则

核验时间：2026-10-20（数据来自 GitHub API，不是凭印象）

## 一、五个仓库的判断

| 仓库 | 事实 | 用途 | 用在哪 | 风险与处理 |
|---|---|---|---|---|
| [python-for-devops](https://github.com/iam-veeramalla/python-for-devops) | 4.9k star，MIT，17 个 Day，最后提交 2024-08 | **选题参考**：看"运维场景该练什么"，不看它的教学顺序 | 阶段 1（Day 11 字典项目、Day 12 文件操作）、阶段 4（Day 14 GitHub/JIRA 集成，只借 API 思路） | 用 Ubuntu/`apt` 讲解，Windows 上换成等价操作；环境变量、API 引入过早，按本课程重排；示例依赖外部账号，不照抄 |
| [devops-exercises](https://github.com/bregman-arie/devops-exercises) | 84.9k star，7.8MB，2025-12 更新，含中文 README | **查漏与自测**：阶段结束时挑几题检验，不按它学 | 每个阶段末各挑 3–5 题（Python 基础、网络、监控） | 跨度极大（Linux/K8s/云/安全），整库学完等于换专业；答案质量不一，必须自己跑一遍 |
| [ops-of-python](https://github.com/xiongjungit/ops-of-python) | 0 star，2018-04 最后提交，CC-BY-SA，基于《简明Python教程》 | **中文概念补充**：某个概念我讲完还想换个说法时读一节 | 阶段 1 的变量/控制流/函数/文件章节 | 停更 8 年：可能混有 Python 2 写法、过时的 pip 命令、已改名的库；**代码一律实跑验证**，报错按 Python 3.15 改，不照抄 |
| [psutil](https://github.com/giampaolo/psutil) | 11.3k star，BSD-3，2026-10 仍活跃 | **阶段 2 的项目库**：本机 CPU/内存/磁盘/网络/进程 | 阶段 2（U5–U7） | Windows 与 Linux 的部分指标语义不同；官方文档是英文，由我提炼要点，不要求你通读 |
| [Netmiko](https://github.com/ktbyers/netmiko) | 4.3k star，MIT，2026-10 活跃 | **阶段 3 末的设备只读**：连交换机/路由器读命令 | 阶段 3（U10），且只在你确实管网络设备时进入 | 需要真实设备或模拟器；Windows 上依赖 `cryptography`，安装可能受 Python 3.15 新版本影响；只读优先，配置下发单独评估 |

## 二、使用规则（重要）

1. **同一时间只跟一个入口**。当前阶段需要的外部阅读，我会在教案里写明"看哪个仓库的哪一节、看多久"，其余不看。同时跟两套课程是零基础阶段最常见的失控方式。
2. **英文材料由我提炼**。给你 3–5 条要点 + 需要看的章节，不要求通读原文；你查生词可以用翻译工具，但不把"读完英文文档"当作业。
3. **旧代码必须实跑**。2018 年的示例、书上的代码、博客里的代码，一律先跑；跑不通就按当前版本改，改不动就丢掉。
4. **外部练习不计入通过标准**，除非我在任务卡里明确指定。它们只用来查漏。
5. **不复制粘贴外部代码**。看懂逻辑后自己写；确实要借用，注明来源并解释每一行在做什么。

## 三、被排除的常见内容及原因

| 内容 | 原因 |
|---|---|
| Fabric | Linux SSH 批量执行框架，Windows 环境不适用；等价能力用 paramiko / Netmiko |
| Docker / K8s 教程 | 你的环境不涉及，且对零基础是额外负担；需要时再学 |
| Web 框架（Flask/Django）、ORM | 与"运维小工具"目标不匹配，除非明确要做平台界面 |
| LeetCode / 算法刷题 | 不解决你的实际问题，ROI 低 |
| 面试题合集 | 不占技术课时 |

## 四、每个阶段的指定入口

| 阶段 | 指定入口 | 说明 |
|---|---|---|
| 1 | 本仓库 `unitXX/notes.md` + python-for-devops 的 Day 11/12 目录（只看题目，不看代码） | 其余不看 |
| 2 | psutil 官方文档的 CPU / Memory / Disk 三节（我给要点） | 英文原文可只扫标题 |
| 3 | Netmiko 官方 `README` 的 Quick Start 一节 | 需要设备时再看 |
| 4 | 目标云厂商的 API 文档"列举资源"章节 | 只读接口 |
| 5 | Python 官方文档 `argparse` / `logging` / `unittest` 的教程页 | 我给中文摘要 |
