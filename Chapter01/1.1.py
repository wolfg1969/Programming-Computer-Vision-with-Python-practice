#!/bin/env python

from PIL import Image

pil_im = Image.open('images/empire.jpg')

pil_im.show()

pil_im_gray = pil_im.copy().convert('L')

pil_im_gray.show()

pil_im_copy = pil_im.copy()
box = (100, 100, 400, 400)
region = pil_im_copy.crop(box)

region = region.transpose(Image.ROTATE_180)
pil_im_copy.paste(region, box)

pil_im_copy.show()

out = pil_im.resize((128, 128))
out.show()

out = pil_im.rotate(45)
out.show()

pil_im.thumbnail((128, 128))
pil_im.show()
