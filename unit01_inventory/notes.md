# U1 讲义 — 把 CSV 读成 list[dict]，再筛出想要的设备

## 本课解决什么问题

U0 你打印的是写死的文字。这一课的数据来自文件：`samples/devices.csv`，34 行设备清单。
你要让程序读出来、挑出其中 **13 台上海的设备**，并数出条数。

本课只有一个主要新难点：**数据形状**。一行 CSV 读进来不是一串文字，而是**一个字典**；
整个文件读进来不是字符串，而是**一个列表，里面装着 34 个字典**。

## 1. 启动命令

```powershell
cd E:\python\unit01_inventory
python list_devices.py
```

**必须先 `cd` 到单元目录**，因为脚本里写的是相对路径 `samples/devices.csv`。
这一点 U0 已经埋过伏笔，这里会真的发生：

```
$ cd E:\python
$ python unit01_inventory\demo.py
FileNotFoundError: [Errno 2] No such file or directory: 'samples/devices.csv'
退出码: 1
```

文件没丢，是"当前目录"变了。相对路径永远相对于**你运行命令时所在的目录**。

## 2. 程序入口

```python
import csv
```

写在文件最上面。它把 Python 自带的 `csv` 模块拿进来——`csv` 不是第三方库，不用安装。
之后从上往下一行一行执行，没有 `main` 函数。

## 3. 准备数据：CSV 长什么样

```
hostname,ip,role,os,site,status
sw-core-01,192.0.2.11,switch,Cisco IOS,上海,online
...
```

- 第一行是**表头**：6 个列名，决定后面每个字典的键
- 后面 34 行数据，每行 6 个字段，用英文逗号分隔
- 空字段表示缺失，比如 `srv-nosite-01` 的 `site` 是空字符串
- 样本里故意混了脏数据（IP 写成 `192.0.2.300`、主机名带前后空格、多出一列、主机名重复）

**U1 不处理这些脏数据**，照原样读出来、照条件筛就行。U3 会专门处理输入校验。

## 4. 调用函数

```python
with open("samples/devices.csv", encoding="utf-8", newline="") as f:
    rows = list(csv.DictReader(f))
```

逐项说清：

| 部分 | 作用 | 返回/得到什么 |
|---|---|---|
| `open(...)` | 打开磁盘上的文件 | 文件对象 `f`（在内存里，还没读内容） |
| `encoding="utf-8"` | 按 UTF-8 解码 | 不解码或写错编码，中文站点名会乱码 |
| `newline=""` | 换行交给 csv 模块处理 | Windows 上不加这个，容易读出错位的空行 |
| `csv.DictReader(f)` | 把每行变成字典 | 一个"读取器"，一次给一行 |
| `list(...)` | 把读取器里的行全部取出来 | `rows`，一个列表 |

`DictReader` 会自动拿表头当键：第一行不进入数据，成为后面每行的键名。

## 5. 接收返回值：rows 到底是什么

`demo.py` 的实际输出（我跑过）：

```
rows 的类型: <class 'list'>
总行数: 34
第一行的类型: <class 'dict'>
第一行的键: ['hostname', 'ip', 'role', 'os', 'site', 'status']
第一行完整内容: {'hostname': 'sw-core-01', 'ip': '192.0.2.11', 'role': 'switch', 'os': 'Cisco IOS', 'site': '上海', 'status': 'online'}
第一行的 hostname: sw-core-01
hostname 的类型: <class 'str'>
```

逐层拆开看：

| 表达式 | 类型 | 具体值 |
|---|---|---|
| `rows` | `list` | 34 个字典的列表 |
| `rows[0]` | `dict` | `{'hostname': 'sw-core-01', ...}` |
| `rows[0]["hostname"]` | `str` | `'sw-core-01'` |
| `rows[0]["ip"]` | `str` | `'192.0.2.11'` ← **是字符串，不是数字** |
| `len(rows)` | `int` | `34` |

**这一课的坑就在这里**：CSV 里所有值读出来都是字符串。
`'192.0.2.11'` 看着像 IP，实际上是文字；`'80'` 看着像端口，实际上也是文字。
所以 `r["ip"] == 192.0.2.11` 永远不成立，必须写成 `r["ip"] == "192.0.2.11"`（带引号）。

## 6. 检查结果：for + if 筛选

```python
for r in rows:
    if r["site"] == "上海":
        print(r["hostname"], r["ip"], r["role"])
```

- `for r in rows:` 每次循环，`r` 是**一个字典**（不是一行文字）
- `r["site"]` 用键取值，得到字符串 `'上海'`
- `==` 比较字符串，**区分大小写，前后空格也算不同**
- `print(a, b, c)` 用逗号分隔，输出时自动用空格隔开

## 7. 统计条数

```python
count = 0
for r in rows:
    if r["site"] == "上海":
        count = count + 1
print("共", count, "台")
```

`count` 是 `int`，初始 0，每命中一次加 1。
输出 `共 13 台`——先打印 `共`，再打印数字，再打印 `台`，逗号会自动补空格。

## 8. 关闭资源

`with open(...) as f:` 的意义：**代码块结束时自动关闭文件**，即使中途报错也会关。

- 谁创建：`open` 创建了文件对象 `f`
- 谁关闭：`with` 负责，块结束就关
- 如果你写成 `f = open(...)` 而不关闭，文件句柄会一直占着，程序大了会出问题

## 9. 内存和磁盘

| 东西 | 在哪 |
|---|---|
| `samples/devices.csv` | 磁盘 |
| 文件对象 `f` | 内存（指向磁盘文件的句柄） |
| `rows`（34 个字典） | 内存 |
| 打印出来的文字 | 屏幕，程序结束就没了 |

本课**不写任何文件**。把结果保存下来是 U2 的事。

## 10. 常见错误对照

| 报错 | 原因 | 怎么查 |
|---|---|---|
| `FileNotFoundError` | 目录不对、文件名拼错 | 先 `pwd`/看终端提示符，再 `dir samples` |
| `KeyError: 'Site'` | 键名大小写错、拼错 | 打印 `list(rows[0].keys())` 看真实键名 |
| `TypeError: ... not supported` | 拿字符串当数字算 | 先 `type(r["ip"])` 确认是 `str` |
| 中文乱码 | `encoding` 写错或没写 | 统一用 `encoding="utf-8"` |

## 11. 本课任务

见 `task.md`。骨架已经给了读取部分，你要写循环、筛选、计数和输出。

## 12. 下一课

U2：把"筛选"封成函数，用字典统计各站点的台数，并把结果写成 `out/report.csv` 和 `out/summary.txt`。
