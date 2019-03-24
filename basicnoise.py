#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 18:13:11 2019

@author: preethi
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np
import random

def main():
    
    path = "/home/preethi/Documents/opencv/misc/4.2.07.tiff"

    img = cv2.imread(path, 1)
    img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    rows,coloumns,channels=img.shape
    p=0.05
    output=np.array(img.shape,np.uint8)
    for i in range(rows):
        for j in range(coloumns):
            r=random.random()
            if r < p/2:
                output[i][j]=[0,0,0]
            elif r<p:
                output[i][j]=[255,255,255]
            else:
                output[i][j]=img[i][j]
    

  
    plt.imshow(img)
    plt.title('Image with Salt and Pepper Noise')
    plt.show()

if __name__ == "__main__":
    main()