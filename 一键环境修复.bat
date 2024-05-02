@echo off

python -m pip install -i https://pypi.tuna.tsinghua.edu.cn/simple --upgrade pip
REM 更新pip(镜像源)

pip install pillow -i https://pypi.tuna.tsinghua.edu.cn/simple

pip install numpy -i https://pypi.tuna.tsinghua.edu.cn/simple

pip install pypiwin32 -i https://pypi.tuna.tsinghua.edu.cn/simple

pip install pygame -i https://pypi.tuna.tsinghua.edu.cn/simple

pip install psutil -i https://pypi.tuna.tsinghua.edu.cn/simple
REM 用于检测是否已经启动

REM 不直接设置镜像源以防影响其他的pip指令