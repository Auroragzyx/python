# U1 分步练习（先做这个，`notes.md` 暂时不用读全）

觉得讲义看着头大，就只做下面 3 步。每步只有几行代码，跑完看输出即可，不用先理解全部概念。

准备：在 VS Code 终端里（`` Ctrl+` ``）

```powershell
cd E:\python\unit01_inventory
```

---

## 第 1 步：字典是什么

```powershell
python step1_dict.py
```

实际输出：

```
{'hostname': 'sw-core-01', 'ip': '192.0.2.11'}
sw-core-01
2
```

看三件事：

- 大括号 `{ }` 里面是"**名字: 值**"，用逗号隔开
- `device["hostname"]` 是"按名字取一个值"
- `len(device)` 是"里面有几对名字和值"

一句话：**字典 = 几个名字，各自对应一个值。**

---

## 第 2 步：文件读进来是什么样

```powershell
python step2_one_row.py
```

实际输出：

```
一共读了几行: 34
第一行是什么: {'hostname': 'sw-core-01', 'ip': '192.0.2.11', 'role': 'switch', 'os': 'Cisco IOS', 'site': '上海', 'status': 'online'}
```

一句话：**34 行数据就是 34 个字典。** 每个字典的"名字"来自 CSV 第一行（`hostname`、`ip`、`role`…），"值"来自每一行数据。

这就是本课唯一要记住的事。

---

## 第 3 步：把每一行都打印出来

```powershell
python step3_loop.py
```

输出 34 行，每行一个主机名：

```
sw-core-01
sw-acc-01
sw-acc-02
rt-edge-01
srv-web-01
...
```

一句话：`for r in rows` 里，**每一次的 `r` 就是第 2 步看到的那个字典**。

---

## 第 4 步：该你写了

打开 `list_devices.py`，把三步合成一个脚本，再加上条件：

1. 在 `for r in rows:` 里面写 `if r["site"] == "上海":`
2. 成立时打印 `r["hostname"] r["ip"] r["role"]`
3. 另外计数，最后打印 `共 13 台`

**先只写 `if` 和 `print`，跑通 13 行以后，再加计数。** 一次只加一件事。

---

## 输出不对时先查这几条

| 现象 | 先查什么 |
|---|---|
| 没有任何输出 | `if` 的缩进要比 `for` 多 4 个空格；`print` 要在 `if` 里面 |
| 报 `KeyError` | 键名拼错或大小写错，`site` 不是 `Site` |
| 结果里出现北京/深圳 | 比较的是 `r["site"]`，别写成 `r["os"]` |
| `FileNotFoundError` | 终端没 `cd` 到 `unit01_inventory` |
| 只打印了 1 台 | `print` 写在了 `for` 外面，没缩进 |
