This is an open-source WorseGI auxiliary program.

It is based on Python's mss for real-time screen monitoring and pyautogui for mouse and keyboard simulation.

It can perform operations such as automatic teleportation and automatic picking up.

The following third-party Python extension libraries need to be installed:
pyautogui, mss, pydirectinput, keyboard, opencv-python

Copy the following line of code and paste it in PowerShell:
pip install -r requirements

Try to create an additional Python virtual environment:
python -m venv venv
./venv/Scripts/Activate.ps1

Before running, please copy your Genshin Impact game executable to the app_path.txt file.

Run code: 
python main.py

Since Genshin Impact has a high application priority, it will block a large extent of simulated mouse and keyboard operations. Therefore, it needs to be run with administrator privileges.

-----------------------------------------------------------------------------------------

这是一个开源的更差的原神辅助程序

基于python的mss屏幕实时监控和pyautogui的键鼠模拟

可以完成自动传送，自动拾取等操作

需要安装python的第三方扩展库：
pyautogui, mss, pydirectinput, keyboard, opencv-python

复制此行代码并在powershell中粘贴：
pip install -r requirements

尽量创建一个额外的python虚拟环境：
python -m venv venv
./venv/Scripts/Activate.ps1

在运行之前，请将你的原神游戏本体复制到app_path.txt中

运行代码：
python main.py

由于原神应用的优先级较高，会屏蔽很大程度的模拟键鼠操作，所以运行时需要以管理员权限运行
