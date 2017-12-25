# -*- coding: utf-8 -*-

from PIL import Image
from pylab import *
from numpy import *
from scipy.ndimage import filters


def make_contour(im):
    figure()
    gray()
    contour(im, origin='image')
    axis('equal')
    axis('off')


def gaussian_filter(im, sigma):
    filtered_im = filters.gaussian_filter(im, sigma)
    make_contour(filtered_im)
    

im = array(Image.open('images/empire.jpg').convert('L'))
make_contour(im)
title('original')

im2 = gaussian_filter(im, 2)
title('gaussian filter with sigma=2')

im5 = gaussian_filter(im, 5)
title('gaussian filter with sigma=5')

im10 = gaussian_filter(im, 10)
title('gaussian filter with sigma=10')

show()
