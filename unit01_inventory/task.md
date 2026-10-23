# U1 任务卡 — 从设备清单中筛出上海的设备

> 目标：把 CSV 读成 `list[dict]`，用 `for` + `if` 筛出指定站点，并统计条数。
> 本单元只有一个主要新难点：**数据形状（一行 = 一个 dict）**。

## 一、输入

`samples/devices.csv`（UTF-8，34 行数据 + 1 行表头，6 列）

```
hostname,ip,role,os,site,status
sw-core-01,192.0.2.11,switch,Cisco IOS,上海,online
...
```

样本里故意混了脏数据，**本单元不处理**，照原样读、照条件筛：

| 行 | 情况 |
|---|---|
| `srv-bad-01` | IP 写成 `192.0.2.300`（不合法） |
| `srv-nosite-01` | `site` 为空 |
| ` sw-space-01 ` | 主机名前后带空格 |
| `sw-extra-01` | 多出一列（备用设备） |
| `sw-core-01` | 出现两次（IP 不同） |

## 二、输出格式

每台设备一行，三个字段用空格分隔：

```
sw-core-01 192.0.2.11 switch
```

最后一行是合计：

```
共 13 台
```

## 三、你要写的文件

`unit01_inventory/list_devices.py`（骨架已提供，含 3 个 TODO）

读取部分已经写好，**不要改**；你只补 TODO 1–3。

## 四、预期输出（13 行设备 + 1 行合计）

```
sw-core-01 192.0.2.11 switch
sw-acc-01 192.0.2.12 switch
sw-acc-02 192.0.2.13 switch
rt-edge-01 192.0.2.1 router
srv-web-01 192.0.2.21 server
srv-db-01 192.0.2.22 server
ap-floor3-01 192.0.2.31 ap
srv-db-02 192.0.2.23 server
sw-acc-03 192.0.2.18 switch
srv-web-02 192.0.2.24 server
rt-edge-03 192.0.2.4 router
sw-core-01 192.0.2.10 switch
srv-bad-01 192.0.2.300 server
共 13 台
```

## 五、通过标准（唯一门槛）

- [ ] 在 `unit01_inventory` 目录下执行 `python list_devices.py`，**退出码 0**
- [ ] 设备行**恰好 13 行**，内容与上面预期输出一致，**顺序相同**
- [ ] 最后一行为 `共 13 台`
- [ ] 13 行是从 CSV 里循环出来的，**不是写死 13 个 `print`**（我会读代码）
- [ ] 使用 `csv.DictReader` 读取，并且 `rows` 是 `list`（不能手工 `split(",")`）
- [ ] `samples/devices.csv` 未被修改（sha256 不变）
- [ ] 能口头说清：`for` 循环里的 `r` 是什么类型、`r["site"]` 是什么类型

## 六、提交清单（只是交付形式，不构成门槛）

1. 终端运行输出（选中复制）
2. `list_devices.py`（我直接读文件，不用贴）
3. 对上一条口头问题的回答（写在回复里即可）

## 七、提示

- 相对路径：必须先 `cd E:\python\unit01_inventory`，从项目根直接跑会 `FileNotFoundError`
- 样本文件的起始 sha256：`42CD9880962ACCEB0DB94ADF2DF27681633531E8CFDDAD65F44CCDD46F6F975C`（可用 `Get-FileHash samples\devices.csv -Algorithm SHA256` 自查是否被改过）
- `sw-core-01` 出现两次，两台都要打印，不要"去重"
- 想确认类型，可以在循环里临时加一行 `print(type(r))` 看输出，看完删掉

## 八、额外挑战（单列，不计入通过标准）

- 同时按 `site` 和 `role` 筛选（比如上海的 switch）
- 用 `str.ljust()` 让输出列对齐
- 统计每个站点各有多少台（U2 会正式讲字典计数，这里可以先试）
