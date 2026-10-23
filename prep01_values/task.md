# P1任务：给值取名字，再使用它

发布：2026-10-23，仅用于这次新练习，不追溯U0/U1。讲义见[notes.md](notes.md)，允许查阅，不要求闭卷。

## 写哪里、做什么

只完成prep01_values/practice.py三个TODO，不改旧作业。脚本从上到下执行，不要求def、main、input、循环、字典或文件。

1. 定义device_name，保存字符串"sw-test-01"，打印一次。
2. 对同一个device_name重新赋值"sw-test-02"，再打印。
3. 定义整数capacity=16、occupied=6，用这两个变量相减，把结果保存在remaining，再打印remaining。

先Ctrl+S，在项目根的**终端**运行：

```powershell
python prep01_values/practice.py
```

也可进入prep01_values后运行python practice.py。预期正好三行：

```text
sw-test-01
sw-test-02
10
```

骨架只有注释，退出0但没输出是未实现，不能记通过。

## 通过标准（唯一门槛）

- 正常结束，实际输出与上面三行一致。
- 两次打印使用同一个device_name变量，中间重新赋值；不能用两个写死字符串的print替代。
- remaining通过capacity与occupied相减得到；不能直接remaining=10或print(10)替代计算。

不额外要求口头题、装软件、写函数或改变旧样本。教师读保存的代码，在副本验证。

## 交付方式（不是额外门槛）

保存代码，贴终端输出即可；直接从文件读代码。没输出也可以说明卡在哪个TODO，不补造结果。之后的迁移练习单独出题记录，不撤销本题原标准的完成。

本题通过后再生成P2教案与任务。
