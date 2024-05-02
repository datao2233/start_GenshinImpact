import numpy as np
import ctypes
from PIL import ImageGrab
import win32gui
import pygame
import time
import os
from tkinter import messagebox # 弹窗
import psutil # 检测是否已经启动

# VSCode 对 pywin32 给出虚假警告，忽略
# 对路径使用`r`以防止以外的 SyntaxWarning
# 本地测试 pass

os.chdir(os.path.dirname(os.path.abspath(__file__)))  # 避免意外的位置

# -----------相关变量设置---------------
ys = r"D:\Genshin Impact\Genshin Impact Game\YuanShen.exe" # 原神安装路径
music = r"startmusic.mp3" # 启动音乐
program_name = "YuanShen.exe" # 不用动，除非你启动的是启动器而非游戏本体
# -------------------------------------


def isScreenAllWhite(image):  # 判断屏幕全白
    # 将截图转换为numpy数组，以便分析每个像素的颜色
    pixel_data = np.array(image)
    # 计算所有白色像素的数量，检查每个像素是否为白色
    white_pixel_count = np.sum(np.all(pixel_data == [255, 255, 255], axis=-1))
    total_pixels = pixel_data.shape[0] * pixel_data.shape[1]  # 计算总像素数量
    white_ratio = white_pixel_count / total_pixels  # 计算白色像素的比例
    return white_ratio > 0.8     # 在这里设置灵敏度，默认为白色占80%时启动原神 <---------------- 在这里修改灵敏度

def programStart(program):  # 启动指定路径的程序
    try:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", program, None, None, 1)
    except:
        messagebox.showerror("没安原神？","改罚！")
        #time.sleep(3)
        #os.system("shutdown -s -t 30") 高危指令，千万别取消注释
        #os.system("shutdown -a") 
        

def windowTop():  # 置顶原神窗口
    window_title = "原神"

    while True:
        try:
            hwnd = win32gui.FindWindow(None, window_title)
            if hwnd:
                win32gui.SetForegroundWindow(hwnd)
                print("启动成功！")
                break
        except:
            ...

def musicStart(audio_file, start_position):
    pygame.init()

    pygame.mixer.init()
    pygame.mixer.music.load(audio_file)
    pygame.mixer.music.play(start=start_position)
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    pygame.quit()

def is_program_running(program_name):# 检测是否已经启动
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] == program_name:
            return True
    return False

if os.access(ys, os.F_OK):
    os.system("cls")# 清除来自pygame的消息
    print("程序加载完成，等待原神启动...")
    while True:
        screenshot = ImageGrab.grab()
        if isScreenAllWhite(screenshot):  # 检测全白
            if not is_program_running(program_name):
                try:
                    programStart(ys)  # 启动原神
                    print("原神？启动！")
                    musicStart(music, 0)  # 启动小曲
                    windowTop
                    break
                except:
                    messagebox.showerror("一定是玩原神玩的！", "启动失败")
            else:
                print("启动太多了，要装不下了~")
        time.sleep(0) # <--- 如果cpu消耗太大，可以在这里修改检测间隔(单位秒，可以改为0.3，效果较佳)
else:
    messagebox.showerror("没装原神？","该罚！")
    #time.sleep(3)
    #os.system("shutdown -s -t 30") 高危指令，千万别取消注释
    #os.system("shutdown -a") 
