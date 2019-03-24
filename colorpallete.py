#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 00:45:36 2019

@author: preethi
"""
import cv2
import numpy as np
def emptyfunction():
    pass
def main():
    img=np.zeros((512,512,3),np.uint8)
    cv2.namedWindow("color palete",cv2.WINDOW_AUTOSIZE)
    cv2.createTrackbar("B","color palete",0,255,emptyfunction)
    cv2.createTrackbar("G","color palete",0,255,emptyfunction)
    cv2.createTrackbar("R","color palete",0,255,emptyfunction)
    while(True):
        
        
        cv2.imshow("color palete",img)
        if cv2.waitKey(1)==27:
            
            
            
            break
        blue=cv2.getTrackbarPos("B","color palete")
        green=cv2.getTrackbarPos("G","color palete")
        red=cv2.getTrackbarPos("R","color palete")
        img[:]=[blue,green,red]
        print(blue,green,red)
    
    cv2.destroyAllWindows() 
if __name__=="__main__":
    main()
     
              
        
    
        
   
    



   






