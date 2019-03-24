#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 00:45:36 2019

@author: preethi
"""
import cv2
import numpy as np
img=np.zeros((512,512,3),np.uint8)
cv2.namedWindow("events")
#mouse call back events
def drawcircle(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x,y),40,(0,255,0),-1)
    if event==cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img,(x,y),40,(0,0,255),-1)
      
        
    
cv2.setMouseCallback("events",drawcircle)
def main():
 
    events=[i for i in dir(cv2) if 'EVENT' in i]
    print(events)
    while(True):
        cv2.imshow("events",img)
        if cv2.waitKey(20)==27:
            break
       
    
    cv2.destroyAllWindows() 
if __name__=="__main__":
    main()
     
              
        
    
        
   
