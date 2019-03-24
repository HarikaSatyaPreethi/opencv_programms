#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 19:19:37 2019

@author: preethi
"""

import cv2
import matplotlib.pyplot as plt

def main():
    
    path = "/home/preethi/Documents/opencv/misc/"
    
    imgpath1 =  path + "4.2.01.tiff"
    imgpath2 =  path + "4.2.07.tiff"
    
    img1 = cv2.imread(imgpath1, 1)
    img2 = cv2.imread(imgpath2, 1)
    
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
    
   
    
    plt.subplot(1, 2, 1)
    plt.imshow(img1)
    plt.title('Liquid Drop')
    plt.xticks([])
    plt.yticks([])

    plt.subplot(1, 2, 2)
    plt.imshow(img2)
    plt.title('fruits')
    plt.xticks([])
    plt.yticks([])
    
    plt.show()  
 
if __name__ == "__main__":
    main()
