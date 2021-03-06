#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 20:49:43 2019

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
    
    img3 = cv2.bitwise_not(img1)
    img4 = cv2.bitwise_and(img1, img2)
    img5 = cv2.bitwise_or(img1, img2)
    img6 = cv2.bitwise_xor(img1, img2)
    
    titles = ['Image 1', 'Image 2','Image NOT', 'AND', 'OR', 'XOR']
    images = [img1, img2, img3, img4, img5, img6]
    
    for i in range(6):
        plt.subplot(3, 2, i+1)
        plt.imshow(images[i])
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])

    plt.show()  
 
if __name__ == "__main__":
    main()