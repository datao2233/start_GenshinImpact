import ctypes  # 控制面板\系统和安全\安全和维护  更改用户账户控制设置


def programStart(program):  # 启动指定路径的程序
    try:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", program, None, None, 1)
    except:
        print("启动失败，请检查文件路径是否错误！！！")
