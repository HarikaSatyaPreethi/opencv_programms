#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 21:40:47 2019

@author: preethi
"""

import cv2
import time

def main():
    path = "/home/preethi/Documents/opencv/misc/"
    
    imgpath1 =  path + "4.2.01.tiff"
    
   
    img1 = cv2.imread(imgpath1, 1)
  
    
    rows, columns, channels = img1.shape
    
    angle = 360
    
    while True:
        
        if angle == 0:
            angle = 360
        
        R = cv2.getRotationMatrix2D((columns/2, rows/2), angle, 0.2)
        
        print(R)
    
        output = cv2.warpAffine(img1, R, (columns, rows))
    
    
        cv2.imshow('Rotated Image', output)
        angle = angle - 1
        time.sleep(0.01)
        
        if cv2.waitKey(1) == 27:
            break
        
    cv2.destroyWindow('Rotated Image')

if __name__ == "__main__":
    main()
