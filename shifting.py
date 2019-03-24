#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 21:12:34 2019

@author: preethi
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np

def main():
    path = "/home/preethi/Documents/opencv/misc/"
    
    imgpath1 =  path + "4.2.01.tiff"
    
   
    
    
    
    img1 = cv2.imread(imgpath1, 1)
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
    
    
    rows, columns, channels = img1.shape
    print(columns,rows,channels)
    
    T = np.float32([[1, 0, 150], [0, 1, 50]])
    
    print(T)
    
    
    output = cv2.warpAffine(img1, T, (columns, rows))
    
    
    plt.imshow(output)
    plt.title('Shifted Image')
    plt.show()

if __name__ == "__main__":
    main()