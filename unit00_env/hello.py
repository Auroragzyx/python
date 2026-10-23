

print ("桌面运维 - 张三")
print ("桌面运维 -> Python")
print (2+3*4)  #14
# 因为：乘法先算
# 报错文件名：hello.py
# 报错行号：line 4
# 运算要包含到括号里，
# 报错一般都是从下往上看
# 看红色上箭头指的地方~~~~~~~~~~~~~^~，一般就是有问题的地方
# 红色箭头下面是报错内容，一般英语直接翻译就能很快懂
# TypeError: unsupported operand type(s) for *: 'NoneType' and 'int'
# 有时候得拆开翻译
#"e:\python\unit00_env\hello.py", line 4,
# 这一行是告诉你报错在代码文件的位置，和文件内的第几行 line 是行的意思

# ===== 三个故障实验记录（2026-10-23，Python 3.15.0 / Windows）=====
# 实验1 目录不对：在 E:\python 下执行 python hello.py
#   退出码：2
#   输出：无
#   报错：can't open file 'E:\python\hello.py': [Errno 2] No such file or directory
#   结论：文件没坏，是"当前目录"不对；python 把相对路径拼在当前目录后面
#
# 实验2 删掉第 5 行右括号
#   退出码：1
#   输出：无，前面三行一行都没打印
#   报错：SyntaxError: '(' was never closed（File "...hello.py", line 5）
#   结论：语法错误在"读文件"阶段就报，整个文件一行都不执行
#
# 实验3 第 3 行下面插入 print(hostname)
#   退出码：1
#   输出：只有"桌面运维 - 张三"，后面两行没打印
#   报错：NameError: name 'hostname' is not defined（line 4）
#   结论：执行到出错那行才停，前面的输出已经生效 —— 部分执行
#
# 排查顺序：先确认"文件找得到吗"，再看"语法通得过吗"，最后才是"运行时数据对不对"

