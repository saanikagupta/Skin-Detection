# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 16:59:04 2018

@author: HP
"""

import imutils
import numpy as np
import cv2
lower = np.array([0, 48, 80], dtype = "uint8")
upper = np.array([20, 255, 255], dtype = "uint8")
camera = cv2.VideoCapture(0)
while True:
    (ret, frame) = camera.read()
    frame = imutils.resize(frame, width = 600)
    converted = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    skinMask = cv2.inRange(converted, lower, upper)
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (9,9))
    skinMask = cv2.erode(skinMask, kernel, iterations = 2)
    skinMask = cv2.dilate(skinMask, kernel, iterations = 2)
    skinMask = cv2.GaussianBlur(skinMask, (3, 3), 0)
    skin = cv2.bitwise_and(frame, frame, mask = skinMask)
    cv2.imshow("Images", np.hstack([frame, skin]))
    #cv2.imshow("Skin Mask",skinMask)
    #cv2.imshow("Kernel",kernel)
    # press 'q' to stop the loop
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
camera.release()
cv2.destroyAllWindows()