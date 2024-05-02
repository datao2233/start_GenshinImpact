# Start_GenshinImpact
本说明适用于 `1.3-index.py` 。

## 如何修改程序的灵敏度？

在程序代码第29行中可以修改，默认0.8，既白色区域超过整个屏幕的80%时，将会执行原始启动，可以自行修改。<br>
这行代码长这样：<br>
```python
    return white_ratio > 0.8     # 在这里设置灵敏度，默认为白色占80%时启动原神 <---------------- 在这里修改灵敏度
```

## 程序运行时CPU占用太高了怎么办？

在程序执行中，默认不会进行限制，如果程序运行后，CPU实在吃不消，在第74行中进行修改，其中的数字`0`可以修改为`0.5`，即为每`0.5`秒检测一次，可根据需要修改。<br>
这行代码长这样:<br>
```python
        time.sleep(0) # <-------------------------------- 在这里修改检测间隔(单位秒)
```

## 为什么执行过程中会报错？

第一次使用请先安装运行环境，下载后双击打开`一键环境修复.bat`。如果不是环境报错，可私信告诉我:<br>
[作者b站账号](https://space.bilibili.com/475148096) 或 [鸭鸭_カモ(贡献者)](https://space.bilibili.com/2054654702)<br>
也可以直接[提交 Issues](https://github.com/datao2233/start_GenshinImpact/issues)<br>

## 在哪里修改原神的启动路径？

在程序代码中的以下部分可以修改:<br>
```python
# -----------相关变量设置---------------
ys = r"D:\path\to\Genshin Impact\Genshin Impact Game\YuanShen.exe" # 原神安装路径
music = r"Shed a Light (Like Instrumental Mix).mp3" # 启动音乐
# -------------------------------------
```
