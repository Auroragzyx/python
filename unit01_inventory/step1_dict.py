# 第 1 步：字典长什么样
# 这一步不读文件，也不涉及 csv，只看"一个字典"是什么
# 运行：python step1_dict.py

device = {"hostname": "sw-core-01", "ip": "192.0.2.11"}

print(device)                # 整个字典：一对大括号，里面是"名字: 值"
print(device["hostname"])    # 用名字取值，得到 sw-core-01
print(len(device))           # 里面有几个"名字: 值"
