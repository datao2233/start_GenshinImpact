import win32gui #要安装环境


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
