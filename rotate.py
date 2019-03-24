#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 21:26:32 2019

@author: preethi
"""


import cv2
import matplotlib.pyplot as plt

def main():
    path = "/home/preethi/Documents/opencv/misc/"
    
    imgpath1 =  path + "4.2.01.tiff"
    
    img1 = cv2.imread(imgpath1, 1)
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
    
    
    rows, columns, channels = img1.shape
    
    R = cv2.getRotationMatrix2D((columns/3, rows/3), 370, 1)
    
    print(R)
    
    
    output = cv2.warpAffine(img1, R, (columns, rows))
    
    
    plt.imshow(output)
    plt.title('Ratated Image')
    plt.show()

if __name__ == "__main__":
    main()