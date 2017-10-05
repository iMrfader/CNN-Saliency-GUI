import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from pylab import *
import os
import sys
weight = 0.4
for n in range(1,11):
	seq = str(n)
	img_ori = np.array(Image.open('/Users/konglingkun/Desktop/fk/'+seq+'_ori.jpg'))
	img_add = np.array(Image.open('/Users/konglingkun/Desktop/fk/t_'+seq+'.jpg'))
	x,y,z = img_ori.shape
	a,b,c = img_add.shape

	img_res = img_ori
	for i in range(a):
		for j in range(b):
			for t in range(3):
				img_res[a-i-1][b-j-1][t] = img_ori[a-i-1][b-j-1][t] * (img_add[a-i-1][b-j-1][t] / 255.0)
	
	img_res2 = img_ori
	for i in range(a):
		for j in range(b):
			for t in range(3):
				img_res2[a-i-1][b-j-1][t] = weight*img_ori[a-i-1][b-j-1][t] + (1-weight)*img_add[a-i-1][b-j-1][t]

	plt.imsave('/Users/konglingkun/Desktop/fk/res/'+seq+'_mul.jpg',img_res)
	plt.imsave('/Users/konglingkun/Desktop/fk/res/'+seq+'_add.jpg',img_res2)