# U1 演示：CSV 读进来之后，数据长什么样
# 在 unit01_inventory 目录下运行：python demo.py

import csv

with open("samples/devices.csv", encoding="utf-8", newline="") as f:
    rows = list(csv.DictReader(f))

print("rows 的类型:", type(rows))
print("总行数:", len(rows))
print("第一行的类型:", type(rows[0]))
print("第一行的键:", list(rows[0].keys()))
print("第一行完整内容:", rows[0])
print("第一行的 hostname:", rows[0]["hostname"])
print("hostname 的类型:", type(rows[0]["hostname"]))
print("总行数减一:", len(rows) - 1, "（这是巧合，不是通用规律）")
