# U1 作业：筛出 site 为"上海"的设备
# 运行：cd E:\python\unit01_inventory 然后 python list_devices.py
# 读取部分已写好，不用改；只补 TODO 1-3

import csv

CSV_PATH = "samples/devices.csv"
SITE = "上海"

with open(CSV_PATH, encoding="utf-8", newline="") as f:
    rows = list(csv.DictReader(f))

# 想确认读到了多少行，可以临时加一行：print(len(rows))，看完删掉

# TODO 1：遍历 rows，每一行 r 是一个字典

# TODO 2：判断 r["site"] 是否等于 SITE，成立时打印 hostname、ip、role

# TODO 3：统计命中的条数，最后打印 "共 N 台"
