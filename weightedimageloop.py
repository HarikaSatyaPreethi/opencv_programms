#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 19:55:55 2019

@author: preethi
"""

import cv2
import numpy as np
import time
#import matplotlib.pyplot as plt

def main():
    path = "/home/preethi/Documents/opencv/misc/"
    
    imgpath1 =  path + "4.2.01.tiff"
    imgpath2 =  path + "4.2.07.tiff"
     
    
    
    
    
    img1 = cv2.imread(imgpath1, 1)
    img2 = cv2.imread(imgpath2, 1)
    
#    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
#    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
    
    for i in np.linspace(0, 1, 200):
        alpha = i
        beta = 1 - alpha
        output = cv2.addWeighted(img1, alpha, img2, beta, 0)
        cv2.imshow('Transition', output)
        time.sleep(0.02)
        if cv2.waitKey(1) == 27:
            break
        
    cv2.destroyAllWindows()
 
if __name__ == "__main__":
    main()