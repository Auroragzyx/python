# P1：先让一个名字保存一个值

本页是这一课的阅读入口。今天只学**变量赋值和使用值**：保存设备名、修改它，再打印；用两个整数算剩余端口。暂时不学if、for、字典、文件或CSV。

不需要先读其他课程。会运行print即可开始；不能独立写时就从下面第一行开始。预计一次学习，可分两次，无需安装库。

## 1．命令和代码放哪里

在VS Code打开仓库文件夹。打开prep01_values/demo.py看代码，修改后Ctrl+S。下面命令写在底部PowerShell**终端**，从仓库根运行：

```powershell
python prep01_values/demo.py
```

终端若已在prep01_values目录，运行python demo.py即可；演示不读文件，两种方式相同。.md是阅读文件，不交给Python执行。

## 2．先看一行赋值

下面是**Python代码，写在.py中**：

```python
hostname = "sw-lab-01"
print(hostname)
```

Python从上到下执行。第一行先得到右边字符串"sw-lab-01"，再让左边名字hostname指向它。`=`叫赋值，不是判断两边相等。第二行使用名字，显示其保存的值。

```text
sw-lab-01
```

hostname没有引号，是变量名；"hostname"带引号，是文字本身。所以print("hostname")只输出hostname这八个字母，不读取变量。

## 3．修改名字保存的值

```python
hostname = "sw-lab-01"
print("原设备:", hostname)
hostname = "sw-lab-02"
print("新设备:", hostname)
```

先保存01 → 打印01 → 重新赋值为02 → 打印02。重新赋值不会倒回去改变已经显示的第一行。print括号内的逗号分开多个值，显示时默认用一个空格分隔。

## 4．保存整数，计算剩余端口

```python
total_ports = 12
used_ports = 5
free_ports = total_ports - used_ports
print("剩余端口:", free_ports)
```

第一行保存整数12，第二行保存整数5。第三行先读取12和5，算12−5得到7，再交给free_ports。最后显示剩余端口: 7。

| 执行完哪行 | 名字 | 类型 | 当前值 |
| --- | --- | --- | --- |
| 第1行 | total_ports | int，整数 | 12 |
| 第2行 | used_ports | int，整数 | 5 |
| 第3行 | free_ports | int，整数 | 7 |

写成"12"会变成字符串，今天参加减法的数字不加引号；暂不需要input和类型转换。

## 5．运行完整演示，对照输出

demo.py只有上面已解释的行，不调用辅助文件，没有自定义函数或入口模板。完整输出：

```text
原设备: sw-lab-01
新设备: sw-lab-02
剩余端口: 7
```

先预测再运行。把演示中used_ports从5改成8，保存后运行，最后一行应为4。演示可以实验，不算作业通过；无需恢复也能开始作业，两个脚本独立。

所有变量只在本次进程的内存里，print显示在终端，没有写报告、连接设备或打开数据文件。结束后变量不会自动落盘，保存的是你编辑的.py代码。

## 6．自己做一个很接近的任务

打开同目录[task.md](task.md)，只做变量练习。可以查本页；卡住时贴输出，说哪一行、原本预期什么，不用先懂全部术语。

- NameError：名字没定义或拼错；used_port和used_ports不是同一名字。
- SyntaxError：先检查英文引号和括号成对。
- 输出没变：Ctrl+S，确认运行的是practice.py还是demo.py。

错误先认现象，本课不同时学try/except。本题通过后才准备P2条件。
