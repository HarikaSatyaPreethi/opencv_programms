#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 01:08:14 2019

@author: preethi
"""

import cv2

def main():
    
    
    windowName = "video play back"
    cv2.namedWindow(windowName)
    filename = '/home/preethi/Documents/opencv/output/videorecord.avi'
    
    cap = cv2.VideoCapture(filename)
        
    
    
    while(cap.isOpened()):
        
        
        ret,frame=cap.read()
        print(ret)
        if ret:
            
            
            cv2.imshow(windowName, frame)
            if cv2.waitKey(133) == 27:
                
                break
        else:
            break
        
        
        
           

    cv2.destroyAllWindows()    
    
    cap.release()

if __name__ == "__main__":
    main()
