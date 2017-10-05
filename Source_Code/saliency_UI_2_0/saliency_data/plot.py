#!/usr/bin/python
# -*- coding: utf-8 -*-
from PIL import Image
from numpy import *
from scipy.ndimage import filters
from pylab import *
import os
for i in range(1,9):
	seq = str(i)

	figure()
	im1 = array(Image.open(seq+'_ori.jpg'))

	subplot(1,3,1)
	imshow(im1)
	axis('off')

	im2 = array(Image.open(seq+'.jpg'))

	subplot(1,3,2)
	imshow(im2)
	axis('off')

	im3 = array(Image.open(seq+'res1.jpg'))

	subplot(1,3,3)
	imshow(im3)
	axis('off')
	#savefig('foo.png', bbox_inches='tight')
	savefig('present/'+seq+'_final.png', bbox_inches='tight')
	# show()
