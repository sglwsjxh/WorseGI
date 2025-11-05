from mss import mss
import cv2
import numpy as np
import pyautogui as pa

# 缓存模板
_template_cache = {}
_sct = mss()

def get_xy(img_path):
    # 从缓存获取模板图像
    if img_path in _template_cache:
        img_model, width, height = _template_cache[img_path]
    else:
        img_model = cv2.imread(img_path)
        if img_model is None:
            print(f"无法读取模板图像: {img_path}")
            return False
        
        height, width = img_model.shape[:2]
        img_model_gray = cv2.cvtColor(img_model, cv2.COLOR_BGR2GRAY)
        _template_cache[img_path] = (img_model_gray, width, height)
        img_model = img_model_gray

    X, Y = pa.size()
    img_now = _sct.grab({"top": 0, "left": 0, "width": X, "height": Y})
    img_now = cv2.cvtColor(np.array(img_now), cv2.COLOR_BGRA2GRAY)

    result = cv2.matchTemplate(img_now, img_model, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    if max_val < 0.85:
        print("未找到目标")
        return False
    
    avgx = int(max_loc[0] + width / 2)
    avgy = int(max_loc[1] + height / 2)

    return avgx, avgy

def auto_click(img_path):
    result = get_xy(img_path)
    if result:
        pa.click(result)
        return True
    return False
    
def auto_circle_click(img_path):
    while True:
        result = get_xy(img_path)
        if result:
            pa.click(result)
            return True