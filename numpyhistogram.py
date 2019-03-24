#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 10:46:17 2019

@author: preethi
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np

def main():
    
    path = "/home/preethi/Documents/opencv/misc/4.2.07.tiff"
    img = cv2.imread(path, 0)

    plt.subplot(1, 2, 1)
    plt.imshow(img, cmap='gray')
    plt.title('Image')
    plt.xticks([])
    plt.yticks([])
    
    plt.subplot(1, 2, 2)
    hist, bins = np.histogram(img.ravel(), 256, [0,255])
    plt.xlim([0, 255])
    plt.ylim([0, 3000])
    plt.plot(hist)
    plt.title('Histogram')
    plt.show()

if __name__ == "__main__":
    main()