from PIL import ImageGrab
import threading
from utils.screenWhite import isScreenAllWhite
from utils.ysStart import programStart
from utils.musicStart import musicStart
from utils.windowTop import windowTop

ys = "D:\Genshin Impact\launcher.exe" # 原神安装路径
music = "Shed a Light (Like Instrumental Mix).mp3"

print("等待启动...")
while True:
    screenshot = ImageGrab.grab()
    if isScreenAllWhite(screenshot):  # 检测全白
        try:
            programStart(ys)  # 启动原神

            thread1 = threading.Thread(target=musicStart, args=(music, 0))  # 启动小曲的线程
            thread2 = threading.Thread(target=windowTop)  # 原神窗口置顶的线程
            thread1.start()  # 线程启动
            thread2.start()
            thread1.join()  # 线程结束
            thread2.join()

            break
        except:
            print("启动失败")
