#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 20:05:46 2019

@author: preethi
"""

import cv2
import matplotlib.pyplot as plt


def main():
    
    path = "/home/preethi/Documents/opencv/misc/5.1.11.tiff"

    img = cv2.imread(path, 0)
#    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    
    L1 = cv2.Canny(img, 50, 300, L2gradient=False)
    
    L2 = cv2.Canny(img, 100, 150, L2gradient=True)

    
    titles = ['Original Image', 'L1 Norm', 'L2 Norm']

    outputs = [img, L1, L2]
    
    
    for i in range(3):
        plt.subplot(1, 3, i+1)
        plt.imshow(outputs[i], cmap='gray')
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])
    plt.show()

if __name__ == "__main__":
    main()
