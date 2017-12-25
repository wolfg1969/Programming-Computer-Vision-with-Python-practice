# -*- coding: utf-8 -*-

from PIL import Image
from pylab import *

# 读取图像到数组中
im = array(Image.open('images/empire.jpg'))

# 绘制图像
imshow(im)

# 一些点
x = [100, 100, 400, 400]
y = [200, 500, 200, 500]

# 使用红色星状标记绘制点
plot(x, y, 'r*')
# plot(x, y, 'go-')  # 带有圆圈标记的绿线
# plot(x, y, 'w+--')  # 带有加号标记的白色虚线
# plot(x, y, 'ks:')  # 带有正方形标记的黑色点线

# 绘制连接前两个点的线
plot(x[:2], y[:2])

# 添加标题，显示绘制的图像
title('Plotting: "empire.jpg"')

# 关闭座标轴
# axis('off')

show()
