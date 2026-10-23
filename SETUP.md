# 环境与运行方式

## 先用已有环境，不重复安装

仓库旧记录：学员机Windows 10 / PowerShell 5.1，Python 3.15.0、Git 2.56、VS Code 1.142。它们是历史记录，本次远程审查没有访问学员电脑，也未重新验证这些版本。P1仅用标准语法，无第三方依赖。

本次课件在审查者Windows / Python 3.14.4上实跑；不把它冒称成学员机3.15实测。当前环境能运行就继续，无需为了开始变量练习重新装Python、Git或扩展。

## 学员当前只需三步

1. VS Code打开本仓库**文件夹**，不只打开单个脚本。
2. 打开prep01_values/notes.md，Ctrl+Shift+V可看预览。
3. 修改.py后Ctrl+S，在底部终端（Ctrl+反引号）从项目根执行：

```powershell
python prep01_values/demo.py
```

`python ...`是终端命令，赋值和print等Python代码写进.py。若终端已进入prep01_values目录，运行python demo.py即可。不要把代码块的语言标签或三条反引号也粘进代码。

## 点右上角运行时

可以使用Python扩展的运行按钮。实际解释器、命令与工作目录取决于扩展和设置；查看终端输出，不能把“按钮永远从项目根启动”当保证。F5调试不是当前前置能力；等断点有助于理解执行时再讲，不按U2编号机械开启。

相对文件路径由当前工作目录解释。新文件课会提供并解释基于脚本位置定位样本的代码。当前P1不读文件，两种启动方式相同。原U1存在已记录的相对路径问题，仅作旧稿保留，勿把它当新路线当前作业。

## 环境确实有问题时再核对

```powershell
python --version
where.exe python
python -c "import sys; print(sys.version); print(sys.executable)"
python -c "print('中文测试')"
```

记录实际输出，不将旧电脑路径当所有机器必须一致的结果。找不到python时按Python官方安装说明修复；新电脑选择当时稳定且目标库支持的版本，不能只写“3.12以上”就承诺所有未来库兼容。

中文显示异常先区分：编辑器文件编码、open的encoding、终端显示、父进程捕获输出。UTF-8模式不等于修复一切终端乱码；不要求学员无诊断就永久setx环境变量。本课只确认自己的终端能显示三行中文即可。

## 后续第三方库

到O1才按当时目标库文档核对支持的Python版本，创建项目环境，用同一解释器的-m pip安装。先验证导入和路径，再接业务；本课不预装psutil、Netmiko或requests。

## Git与同步

仓库：https://github.com/Auroragzyx/python 。新电脑clone后打开目录，读取当前进度，虚拟环境和聊天记录不会随Git自动恢复。

先用git status/git diff看清改动，再逐项git add具体文件。不使用git add -A；未知文件保留。身份和远程以实际仓库为准，不修改全局配置。提交/推送需当前有效授权；本次是改进提案PR，不能据旧笔记自动向main发布或合并。

## 目录

每课notes.md为学员入口，task.md为唯一验收标准，演示与练习分开。样本随课，产出在单元out/，隔离验证在_work/，均不提交。真实设备表和凭据不作为教学样本。
