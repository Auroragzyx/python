# SETUP.md — 环境与运行方式

## 本机现状（2026-10-20 实测）
| 组件 | 状态 |
|---|---|
| 系统 | Windows 10（build 19041），默认 shell：Windows PowerShell 5.1 |
| 项目目录 | `E:\python`，剩余约 378 GB |
| Python | **3.15.0**，`C:\Users\Administrator\AppData\Local\Programs\Python\Python315\python.exe`（用户 PATH，`python` 命令可用） |
| Git | **2.56.0**，`C:\Program Files\Git`（系统 PATH） |
| VS Code | **1.142.0**，`E:\VSCode\Microsoft VS Code`（`code` 命令可用） |
| 扩展 | ms-python.python / pylance / debugpy / 中文语言包 |
| 未安装 | conda、winget、WSL |

- 编码：Python 3.15 默认启用 UTF-8 模式（PEP 686），**不需要**再设 `PYTHONUTF8`；项目统一 UTF-8 + LF（`.vscode/settings.json` 已配）
- 网络：可访问 python.org 与 github.com

## VS Code 怎么用（本课程固定姿势）

1. **打开项目**：终端执行 `code E:\python`，或 文件 → 打开文件夹 → `E:\python`（必须打开这个根目录，不要只打开某个文件，否则相对路径和 Git 都不对）
2. **界面中文**：中文语言包已装，首次启动会问是否切换，选"Change Language and Restart"
3. **终端**：按 `` Ctrl+` `` 打开，默认 PowerShell，工作目录就是项目根
4. **选解释器**：`Ctrl+Shift+P` → `Python: Select Interpreter` → 选 `Python 3.15.0`
5. **运行脚本**：在终端手敲（不要点右上角三角，也不要按 F5）
   ```powershell
   cd unit00_env
   python hello.py
   ```
   F5 是调试器，等 U2 之后再学。现在点它会把"命令 → 解释器 → 输出"这条链路藏起来，正好跳过本课要学的东西。
6. **看改动**：左侧"源代码管理"图标能看到哪些文件变了；提交和推送仍在终端敲 `git` 命令

## 验证命令与预期结果
```powershell
python --version                # Python 3.15.0
where.exe python                # ...\Python315\python.exe
python -c "print('中文测试')"    # 中文测试（不乱码）
python -c "import sys; print(sys.version); print(sys.executable)"
```

## Git 与仓库同步
- 版本：`git version 2.56.0.windows.2`，安装在 `C:\Program Files\Git`，已写入**系统 PATH**
- 认证：Git Credential Manager 2.9.1，首次 `git push` 弹浏览器登录 GitHub，凭据存 Windows 凭据管理器，不落项目文件
- 仓库：<https://github.com/Auroragzyx/python>（**公开**），分支 `main`
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
- 每单元固定：`notes.md`（讲义）、`task.md`（任务卡）、代码、样本数据
- 样本数据、辅助代码放在单元目录内，代码用**相对路径**引用，不写绝对路径
- 运行产出放各单元 `out\` 下（已被 `.gitignore` 排除），不复用为下一单元的输入
- 默认不 import 旧作业代码

## 换电脑重建步骤
1. 安装 Python 3.12 以上，安装时勾选 `Add python.exe to PATH`
2. 安装 Git for Windows（默认选项即可，自带凭据管理器）
3. 安装 VS Code，并装四个扩展：
   ```powershell
   code --install-extension ms-python.python
   code --install-extension ms-python.vscode-pylance
   code --install-extension ms-python.debugpy
   code --install-extension ms-ceintl.vscode-language-pack-zh-hans
   ```
4. `git clone https://github.com/Auroragzyx/python.git`
5. `code python` 打开，跑上面四条验证命令，版本号记回本文件
6. 进入单元目录，`python <脚本名>.py` 运行
