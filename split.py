import cv2
import numpy as np

img = cv2.imread('D:\OpenCV course\codes\colors.png') 

B,G,R = cv2.split(img)

cv2.imshow('how our image is created : ',B,R,G)

cv2.imshow('full image', img)

cv2.waitKey(0) 
cv2.destroyAllWindows()

