# SETUP.md — 环境与运行方式

## 本机实测（2026-10-20）
- 系统：Windows 10（build 19041），默认 shell 为 Windows PowerShell 5.1
- 工作目录：`E:\python`（学习项目根目录），剩余空间约 378 GB
- 网络：可访问 `python.org`（HTTP 200）
- 以下命令**均不在 PATH**：`python`、`py`、`python3`、`pip`、`conda`、`winget`
- `git` 已于 2026-10-20 安装（见下方 Git 一节），不在旧终端里生效，需新开窗口
- 未发现常见 Python 安装目录（`%LOCALAPPDATA%\Programs\Python`、`C:\Python*`、Anaconda/Miniconda）
- 已知问题：控制台代码页非 UTF-8，Python 中文输出会乱码

## U0：安装 Python（进行中）
1. 打开 <https://www.python.org/downloads/windows/>，选最新 **Stable Releases** 的
   `Windows installer (64-bit)`，版本 ≥ 3.12（不要选 pre-release）
2. 运行安装包，**勾选 `Add python.exe to PATH`**，点 `Install Now`，默认路径即可
3. 关掉所有已打开的 PowerShell 窗口（PATH 只对新建进程生效）
4. 新开 PowerShell 执行：`setx PYTHONUTF8 1`，再关掉并重开一次窗口（解决中文乱码）

## 验证命令与预期结果
```powershell
python --version                # Python 3.1x.x
where.exe python                # ...\Python3xx\python.exe
python -c "print('中文测试')"    # 中文测试（不乱码）
python -c "import sys; print(sys.version); print(sys.executable)"
```

## Git 与仓库同步（2026-10-20 完成）
- 版本：`git version 2.56.0.windows.2`，安装在 `C:\Program Files\Git`，已写入**系统 PATH**
- 认证：Git Credential Manager 2.9.1，首次 `git push` 会弹浏览器登录 GitHub，凭据存 Windows 凭据管理器，不落项目文件
- 仓库：<https://github.com/Auroragzyx/python>（公开），分支 `main`
- 提交身份：`Auroragzyx <345183435+Auroragzyx@users.noreply.github.com>`（GitHub noreply 地址，不暴露真实邮箱）
- 日常同步：
  ```powershell
  cd E:\python
  git status          # 看哪些文件变了
  git add -A
  git commit -m "u01: 讲义与任务卡"
  git push
  ```

## 目录约定
- 每单元一个目录：`unit00_env\`、`unit01_inventory\` …
- 样本数据、辅助代码放在单元目录内，代码用**相对路径**引用，不写绝对路径
- 运行产出放各单元 `out\` 下，不提交、不复用为下一单元的输入
- 默认不 import 旧作业代码

## 重建步骤（换电脑照做）
1. 安装 Python 3.12+ 并勾选 PATH（同上）
2. `setx PYTHONUTF8 1`，重开终端
3. 跑上面四条验证命令，版本号记到本文件
4. 进入单元目录，`python <脚本名>.py` 运行

（Python 实际版本号待 U0 通过后补记）
