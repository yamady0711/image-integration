# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 15:09:43 2019

@author: yamad
"""
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2

src1 = cv2.imread('imgs/IMG_1380.jpg')
src2 = cv2.imread('imgs/IMG_1387.jpg')

src2 = cv2.resize(src2, src1.shape[1::-1])

dst = cv2.addWeighted(src1, 0.5, src2, 0.5, 0)

cv2.imwrite('imgs/opencv_add_weighted.jpg', dst)
