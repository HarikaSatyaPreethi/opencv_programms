#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 21:00:50 2019

@author: preethi
"""


import cv2

def main():
    path = "/home/preethi/Documents/opencv/misc/"
    
    imgpath1 =  path + "4.2.01.tiff"
    
   
    
    
    img1 = cv2.imread(imgpath1, 1)

    
    output = cv2.resize( img1, None, fx=1, fy=1, interpolation=cv2.INTER_LINEAR )
   
    
    cv2.imshow('Output', output)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
 
if __name__ == "__main__":
    main()