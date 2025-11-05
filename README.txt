这是一个开源的更差的原神辅助程序
基于python的mss屏幕实时监控和pyautogui的键鼠模拟
可以完成自动传送，自动拾取等操作
需要安装python的第三方扩展库：
pyautogui, mss, pydirectinput, keyboard, opencv-python

复制此行代码并在powershell中粘贴：
pip install -U pyautogui mss pydirectinput keyboard opencv-python
尽量创建一个额外的python虚拟环境：
python -m venv venv
./venv/Scripts/Activate.ps1

由于原神应用的优先级较高，会屏蔽很大程度的模拟键鼠操作，所以运行时需要以管理员权限运行
