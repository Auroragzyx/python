# Python 运维自动化学习库

运维自动化方向的 Python 学习项目。教案、作业、样本、代码按单元归档，换电脑后可直接继续。

仓库：<https://github.com/Auroragzyx/python>（公开仓库，样本数据全部为虚构数据）

## 怎么读（新电脑 / 新对话）

按顺序看：

1. `TEACHING.md` — 教学约定（怎么教、怎么验收、帮助怎么记录）
2. `ROADMAP.md` — 学习计划：阶段、单元、产出、验收、时间估算
3. `LEARNING_PROGRESS.md` — 最新进度、帮助情况、待复测项
4. `SETUP.md` — 环境重建与运行方式
5. `REFERENCES.md` — 外部资料清单与使用规则
6. `unitXX_*/notes.md` — 该单元讲义正文
7. `unitXX_*/task.md` — 该单元作业与通过标准

在 OpenCode 里打开本仓库时，项目级 skill `python-mentor` 会自动加载，上面这个阅读顺序不用每次手动交代。

## 计划概况

| 阶段 | 目标 | 核心产出 |
|---|---|---|
| 1（进行中） | 语言核心 + 文件数据处理 | 设备清单筛选与巡检报表 |
| 2 | 第三方库 + 本机巡检 | psutil 巡检脚本 + 每日报告 |
| 3 | 网络探测 + 设备只读 | 批量端口检查器 / Netmiko |
| 4 | HTTP / API / 云（只读） | API 数据报表 |
| 5 | 工程化 | 可交付的命令行工具 |
| 6（可选） | 平台化 | 定时采集 + 存储 + 界面 |

详见 `ROADMAP.md`。当前单元：**U0 环境**（Python、VS Code、Git 已就绪，待交 `hello.py`）。

## 目录结构

```
python/
├── TEACHING.md            教学约定
├── ROADMAP.md             学习计划（阶段/单元/验收）
├── LEARNING_PROGRESS.md   进度与帮助记录
├── SETUP.md               环境与重建步骤
├── REFERENCES.md          外部资料清单与使用规则
├── .vscode/               编辑器配置（UTF-8、终端、Python）
├── .opencode/skills/python-mentor/SKILL.md   项目级教学 skill（自动加载）
└── unit00_env/            单元 0：环境与第一个脚本
    ├── notes.md           讲义
    ├── task.md            任务卡
    └── demo.py            演示脚本
```

每个单元目录固定两类文档：`notes.md`（讲义）、`task.md`（作业）；代码直接在目录内，样本数据同样；运行产出放 `out/`，不入库。

## 环境

Windows 10 + Python 3.15 + Git 2.56 + VS Code 1.142。详见 `SETUP.md`。

## 约定

- 不提交真实资产清单、真实 IP 段、凭据、Token、日志和虚拟环境
- 样本数据全部虚构（如 `192.0.2.x` 这类文档保留段）
- 提交与推送由学员授权后执行
