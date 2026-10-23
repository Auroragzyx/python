# 第 2 步：读文件，只看第一行
# 运行：python step2_one_row.py
# 只观察输出，不要改

import csv

with open("samples/devices.csv", encoding="utf-8", newline="") as f:
    rows = list(csv.DictReader(f))

print("一共读了几行:", len(rows))
print("第一行是什么:", rows[0])
