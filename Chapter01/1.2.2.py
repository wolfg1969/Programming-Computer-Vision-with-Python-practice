# -*- coding: utf-8 -*-

from PIL import Image
from pylab import *

im = array(Image.open('images/empire.jpg').convert('L'))

# 新建一个图像
figure()

# 不使用颜色信息
gray()

# 在原点的左上角显示轮廓图像
contour(im, origin='image')

axis('equal')
axis('off')

figure()

# 直方图
hist(im.flatten(), 128)

show()
