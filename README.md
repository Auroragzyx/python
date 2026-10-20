# Python 运维自动化学习库

运维自动化方向的 Python 学习项目。所有教案、作业、样本和代码按单元归档，换电脑后可直接继续。

仓库：<https://github.com/Auroragzyx/python>（公开仓库，样本数据全部为模拟数据）

## 怎么读（新电脑 / 新对话）

按顺序看：

1. `TEACHING.md` — 教学约定（怎么教、怎么验收、帮助怎么记录）
2. `ROADMAP.md` — 阶段路线，当前阶段拆到单元
3. `LEARNING_PROGRESS.md` — 最新进度、帮助情况、待复测项
4. `SETUP.md` — 环境重建与运行方式
5. `unitXX_*/notes.md` — 该单元讲义正文
6. `unitXX_*/task.md` — 该单元作业与通过标准

## 目录结构

```
python/
├── TEACHING.md            教学约定
├── ROADMAP.md             阶段路线
├── LEARNING_PROGRESS.md   进度与帮助记录
├── SETUP.md               环境与重建步骤
└── unit00_env/            单元 0：环境与第一个脚本
    ├── notes.md           讲义
    ├── task.md            任务卡
    └── *.py               学员代码
```

每个单元目录固定四类内容：`notes.md`（讲义）、`task.md`（作业）、代码、样本数据；运行产出统一放 `out/`，不入库。

## 当前进度

- 阶段 1：本机只读小工具（设备清单筛选与巡检报表）
- 当前单元：U0 环境（进行中）

## 环境

Windows 10 + Python 3.12 以上 + Git。详见 `SETUP.md`。

## 约定

- 不提交真实资产清单、真实 IP 段、凭据、Token、日志和虚拟环境
- 样本数据全部为虚构数据
- 提交与推送由学员本人授权后执行
