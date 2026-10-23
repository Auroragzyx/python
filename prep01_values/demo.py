# P1独立演示：逐行执行，没有文件读取或辅助模块。
hostname = "sw-lab-01"
print("原设备:", hostname)

hostname = "sw-lab-02"
print("新设备:", hostname)

total_ports = 12
used_ports = 5
free_ports = total_ports - used_ports
print("剩余端口:", free_ports)
