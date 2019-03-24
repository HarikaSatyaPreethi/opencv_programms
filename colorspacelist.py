#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 03:34:21 2019

@author: preethi
"""

import cv2

def main():
    j = 0
    for filename in dir(cv2):
        if filename.startswith('COLOR_'):
            print(filename)
            j =  j +1

    print('There are ' + str((j+1)) + ' color conversion flags in OpenCV.')
 
if __name__ == "__main__":
    main()
