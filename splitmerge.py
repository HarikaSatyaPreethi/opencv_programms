#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 20:20:51 2019

@author: preethi
"""

import cv2
import matplotlib.pyplot as plt

def main():
     
    path = "/home/preethi/Documents/opencv/misc/"
    
    imgpath1 =  path + "4.2.01.tiff"
    
    
    
    
    img = cv2.imread(imgpath1, 1)
    
    img1 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    R, G, B = cv2.split(img1)
    
    titles = ['Original Image', 'Red', 'Green', 'Blue']
    plt.title(titles[0])
    plt.xticks([])
    plt.yticks([])
    images = [cv2.merge((R,G,B)), R,G,B]

    
    plt.subplot(2, 2, 1)
    plt.imshow(images[0])
    
    plt.subplot(2, 2, 2)
    plt.imshow(images[1], cmap='Reds')
    plt.title(titles[1])
    plt.xticks([])
    plt.yticks([])
    
    plt.subplot(2, 2, 3)
    plt.imshow(images[2], cmap='Greens')
    plt.title(titles[2])
    plt.xticks([])
    plt.yticks([])
    
    plt.subplot(2, 2, 4)
    plt.imshow(images[3], cmap='Blues')
    plt.title(titles[3])
    plt.xticks([])
    plt.yticks([])

    plt.show()  
 
if __name__ == "__main__":
    main()
