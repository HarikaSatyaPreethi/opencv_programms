#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 00:45:36 2019

@author: preethi
"""

import cv2
import numpy as np
img=np.zeros((512,512,3),np.uint8)
cv2.line(img,(0,99),(99,0),(255,0,0),5)
cv2.rectangle(img,(0,44),(44,0),(0,0,255),-1)
cv2.circle(img,(77,77),10,(0,255,0),-1)
cv2.ellipse(img,(120,120),(5,60),0,0,360,(127,127,127),-1)
points=np.array([[10,20],[30,40],[40,50],[60,70],[80,90]],np.int32)
points=points.reshape((-1,1,2))
cv2.polylines(img,[points],True,(0,255,0))
cv2.putText(img,"preethi",(100,100),cv2.FONT_HERSHEY_SIMPLEX,2,(255,255,0))
cv2.namedWindow("lena",cv2.WINDOW_AUTOSIZE)
cv2.imshow("lena", img)
cv2.waitKey(0)
cv2.destroyAllWindows()


