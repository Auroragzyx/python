# 课程参考与使用边界

2026-10-23重排。学员当前只读本仓库P1讲义；以下用于导师查证，不叠加成必读课程，不按星数或最新提交日期证明教学质量。这里只引用官方目录/API事实，具体排序是针对当前反馈的教学设计。

## 用于核对前置与API

| 来源 | 本次核对内容 | 本路线用途 |
| --- | --- | --- |
| [CS50P官方目录](https://cs50.harvard.edu/python/) | 变量、条件、循环位于File I/O前；课程面向有或无编程经验者 | 对照基础依赖，不照搬它的作业量、英文要求或全部章节 |
| [Python基础教程](https://docs.python.org/3/tutorial/introduction.html) | 数值、文本与列表的基本表达 | P1–P3教师参考，先用原创运维小例子 |
| [Python控制流](https://docs.python.org/3/tutorial/controlflow.html) | if、for、函数 | P2、遍历与函数各课就近讲解 |
| [Python数据结构](https://docs.python.org/3/tutorial/datastructures.html) | 列表和字典 | 单条记录先于多记录，不直接塞给学员list[dict]术语 |
| [csv官方说明](https://docs.python.org/3/library/csv.html) | DictReader、字段、newline、缺列/多列行为 | CSV出课时使用；普通字段通常是字符串，缺列可为None、多列可为列表 |
| [pathlib](https://docs.python.org/3/library/pathlib.html) | 文件路径及脚本相邻样本定位 | 文件课先讲路径含义，支架也要解释，不提前作为P1任务 |
| [VS Code Python设置](https://code.visualstudio.com/docs/python/settings-reference) | 运行设置可配置 | 不将按钮工作目录当固定事实 |

“官方教程先讲X”不是所有人都必须先学X的证明；实际证据是此学员尚不能独立写几行，所以先从变量开始。先缩小任务，再按表现推进。

## 外部参考的用途与负担

- [python-for-devops](https://github.com/iam-veeramalla/python-for-devops)：选题参考，不作为零基础主教材，不按Day编号推进。
- [devops-exercises](https://github.com/bregman-arie/devops-exercises)：教师按需查漏，不强制阶段末额外做3–5道陌生题。
- [ops-of-python](https://github.com/xiongjungit/ops-of-python)：旧中文材料备用，引用某段时再核对当前Python行为，不泛称全部过时或全部可用。
- [psutil官方文档](https://psutil.readthedocs.io/)：O1/O2出课时核对安装兼容性、采样时长、单位及平台差异。
- [Netmiko原作者仓库](https://github.com/ktbyers/netmiko)：仅实验设备需求明确时选学，不把真实网络设备作为阶段完成前提。
- 云API文档在厂商与只读任务明确后选用；不先索要账号。

不采用星数、体积、活跃日期排名：它们易过时，也不解释此学员能否理解。旧文档将Fabric笼统判为Windows不适用，现不作这种平台一刀切判断；只因当前项目不需要而不引入。

## 使用规则

导师给中文解释和具体输入输出，学员可查阅但不要求通读英文。同一时间一个学习入口。借用外部材料时标来源、核对许可；本次讲义和练习为原创，不复制教材整章或答案。

当前落点与每阶段边界以[ROADMAP.md](ROADMAP.md)为准；不在这里另存一个带过期编号的日程。
