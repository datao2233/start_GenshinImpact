import numpy as np
import ctypes
from PIL import ImageGrab
import threading
import win32gui
import pygame
import time

def isScreenAllWhite(image):  # 判断屏幕全白
    # 将截图转换为numpy数组，以便分析每个像素的颜色
    pixel_data = np.array(image)
    # 计算所有白色像素的数量，检查每个像素是否为白色
    white_pixel_count = np.sum(np.all(pixel_data == [255, 255, 255], axis=-1))
    total_pixels = pixel_data.shape[0] * pixel_data.shape[1]  # 计算总像素数量
    white_ratio = white_pixel_count / total_pixels  # 计算白色像素的比例
    return white_ratio > 0.9     # 如果白色占比超过90%，则判断为成功



def programStart(program):  # 启动指定路径的程序
    try:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", program, None, None, 1)
    except:
        print("启动失败，请检查文件路径是否错误！！！")



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



def musicStart(audio_file, start_position):  # 播放音频
    pygame.init()

    pygame.mixer.init()
    pygame.mixer.music.load(audio_file)
    pygame.mixer.music.play(start=start_position)
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    pygame.quit()



ys = "D:\Genshin Impact\launcher.exe" # 原神安装路径
music = "Shed a Light (Like Instrumental Mix).mp3"

print("加载完成，等待原神启动...")
while True:
    screenshot = ImageGrab.grab()
    if isScreenAllWhite(screenshot):  # 检测全白
        try:
            print("原神？启动！")
            programStart(ys)  # 启动原神
            musicStart(music, 0)  # 启动小曲的线程
            windowTop  # 原神窗口置顶的线程
            break
        except:
            print("启动失败")
    time.sleep(0.5)