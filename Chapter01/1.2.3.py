# -*- coding: utf-8 -*-

from PIL import Image
from pylab import *

im = array(Image.open('images/empire.jpg'))

imshow(im)

print 'Please click 3 points'

x = ginput(3)

print 'You clicked:', x

show()