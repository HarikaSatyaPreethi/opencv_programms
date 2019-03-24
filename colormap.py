#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 02:45:35 2019

@author: preethi
"""
import cv2
import matplotlib.pyplot as plt
imgpath="/home/preethi/Documents/opencv/standard_test_images/lena_color_512.tif"

img = cv2.imread(imgpath,0)
plt.imshow(img,cmap="nipy_spectral_r")
plt.title("color")
plt.xticks([])
plt.yticks([])
plt.show()
plt.imshow(img,cmap="gray")
plt.title("grey color")
plt.xticks([])
plt.yticks([])
plt.show()



cv2.waitKey(0)
cv2.destroyAllWindows()

