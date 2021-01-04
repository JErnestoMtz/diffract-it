import numpy as np
import math as m
import matplotlib.pyplot as plt
from PIL import Image, ImageTk
import cv2
import re

def preprocess(image, imgwidth, imggeight): # imput arbitrary image, return a square croped b&w image, size (imgwidth, imggeight)
	w, h = image.size
	if w == h:
			x1, y1, x2, y2 = 0, 0, w, h
	elif w > h:
		x1, y1, x2, y2 = int((w-h)/2), 0, (int((w-h)/2)+h), h
	elif h > w:
		x1, y1, x2, y2 = 0,  int((h-w)/2), w, (int((h-w)/2)+w)

	preimage = image.crop((x1, y1, x2, y2)).convert('L').resize((imgwidth, imggeight))
	return preimage


def img_to_numpynorm(image,n): #imput a squere image, output a inverted normalized numpy array size (n,n)
	im_scale = image.resize((n,n))
	im_mat1 = np.array(im_scale)
	im_mat2 = cv2.bitwise_not(im_mat1)
	print(im_mat2.max())
	f = im_mat2/255
	return f