import numpy as np


def isScreenAllWhite(image):  # 判断屏幕全白

    # 将截图转换为numpy数组，以便分析每个像素的颜色
    pixel_data = np.array(image)

    # 计算所有白色像素的数量，检查每个像素是否为白色
    white_pixel_count = np.sum(np.all(pixel_data == [255, 255, 255], axis=-1))

    total_pixels = pixel_data.shape[0] * pixel_data.shape[1]  # 计算总像素数量
    white_ratio = white_pixel_count / total_pixels  # 计算白色像素的比例

    # 如果白色像素的比例超过90%，则判断为屏幕全白
    return white_ratio > 0.9
