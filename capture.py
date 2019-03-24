#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 23:51:21 2019

@author: preethi
"""

import cv2
import matplotlib.pyplot as plt


def main():
    cap = cv2.VideoCapture(0)
    
    if cap.isOpened():
        ret, frame = cap.read()
        print(ret)
        print(frame)
    else:
        ret = False
    img1 = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    outpath="/home/preethi/Documents/opencv/output/2.jpg"
    cv2.imwrite(outpath,img1)
 
    
    plt.imshow(img1)
    plt.title('Color Image RGB')
    plt.xticks([])
    plt.yticks([])
    plt.show()
    

    cap.release()
   

if __name__ == "__main__":
    main()

