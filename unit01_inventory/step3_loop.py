# 第 3 步：把每一行的主机名打出来（先不筛选）
# 运行：python step3_loop.py
# 应该出现 34 行，每行一个主机名

import csv

with open("samples/devices.csv", encoding="utf-8", newline="") as f:
    rows = list(csv.DictReader(f))

for r in rows:
    print(r["hostname"])
