#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 21:47:25 2019

@author: preethi
"""
import cv2
imgpath="/home/preethi/Documents/opencv/standard_test_images/lena_color_512.tif"

img = cv2.imread(imgpath,1)
outpath="/home/preethi/Documents/opencv/output/lena_color_512.jpg"
cv2.namedWindow("lena",cv2.WINDOW_AUTOSIZE)
cv2.imwrite(outpath,img)
cv2.imshow("lena", img)
cv2.waitKey(0)
cv2.destroyAllWindows()


