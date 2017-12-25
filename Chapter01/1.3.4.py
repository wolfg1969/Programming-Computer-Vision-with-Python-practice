# -*- coding: utf-8 -*-

from PIL import Image
from pylab import *
from numpy import *

import os, sys
sys.path.append('.')
import imtools

im = array(Image.open('images/empire.jpg').convert('L'))

im2 = imtools.histeq(im)
