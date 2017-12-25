# -*- coding: utf-8 -*-

from PIL import Image
from pylab import *
from numpy import *

im = array(Image.open('images/empire.jpg').convert('L'))
print int(im.min()), int(im.max())
imshow(im)
show()

im2 = 255 - im  # 对虚线进行反相处理
print int(im2.min()), int(im2.max())
imshow(im2)
show()

im3 = (100.0 / 255) * im + 100  # 将图像像素值变换到 100...200 区间
print int(im3.min()), int(im3.max())
imshow(im3)
show()

im4 = 255.0 * (im / 255.0)**2  # 对图像像素值求平方后得到的图像
print int(im4.min()), int(im4.max())
imshow(im4)
show()
