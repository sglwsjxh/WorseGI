import auto_click
import subprocess
from time import sleep
import pyautogui as pa
from pygetwindow import getWindowsWithTitle
import os

# 预加载模板路径，避免重复拼接字符串
TEMPLATES = {
    'login': r".\models\原神登录界面.png",
    'teleport': r".\models\传送按键.png", 
    'interact': r".\models\交互按键F.png",
    'dialog': r".\models\对话按键.png",
    'exit': r".\models\退出至桌面.png"
}

def check_game_running():
    try:
        output = subprocess.check_output(['tasklist'], shell=True).decode('gbk', errors='ignore')
        return "yuanshen.exe" in output.lower()
    except:
        return False

def launch_game():
    print("启动原神...")
    subprocess.Popen(r"D:\games\miHoYo Launcher\games\Genshin Impact Game\YuanShen.exe")
    sleep(10)  # 增加等待时间确保完全启动
    
    # 等待登录界面，最多等待30秒
    for _ in range(30):
        if auto_click.auto_click(TEMPLATES['login']):
            break
        sleep(1)
    
    # 移动到屏幕中心
    X, Y = pa.size()
    pa.moveTo(X / 2, Y / 2)
    sleep(8)

def main_loop():
    counter = 0
    while True:
        # 每10次循环清空一次控制台，减少IO操作
        if counter % 10 == 0:
            os.system('cls')
            print(f"运行中... 循环次数: {counter}")
        
        # 自动传送 - 每次循环都检查
        auto_click.auto_click(TEMPLATES['teleport'])
        
        # 自动拾取 - 每2次循环检查一次，减少图像处理频率
        if counter % 2 == 0:
            if (auto_click.get_xy(TEMPLATES['interact']) and not auto_click.get_xy(TEMPLATES['dialog'])):
                pa.press('f')
        
        # 自动退出
        if auto_click.auto_click(TEMPLATES['exit']):
            os.system('cls')
            print("检测到退出按钮，程序结束")
            break
        
        counter += 1
        sleep(0.15)  # 稍微增加延迟减少CPU使用

if __name__ == "__main__":
    # 进入原神
    if not check_game_running():
        launch_game()
    else:
        windows = getWindowsWithTitle("原神")
        if windows:
            windows[0].activate()
            sleep(2)
    
    # 运行主循环
    main_loop()