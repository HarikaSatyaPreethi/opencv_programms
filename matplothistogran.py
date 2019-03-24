#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 22:39:48 2019

@author: preethi
"""

import cv2
import matplotlib.pyplot as plt

def main():
    path = "/home/preethi/Documents/opencv/misc/5.1.11.tiff"
    img = cv2.imread(path, 0)
      
    plt.subplot(1, 2, 1)
    plt.imshow(img, cmap='gray')
    plt.title('Image')
    plt.xticks([])
    plt.yticks([])
    
    plt.subplot(1, 2, 2)
    plt.hist(img.ravel(), 256, [0, 255])
    plt.title('Histogram')
    plt.xlim(xmin=0, xmax=256)
    plt.show()

if __name__ == "__main__":
    main()
