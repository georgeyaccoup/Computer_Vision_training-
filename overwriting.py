import cv2
import numpy as np 

img1 = cv2.imread("D:\OpenCV course\codes\colors.png",1) 
img2 = cv2.imread("D:\OpenCV course\codes\Assiut.png",1) 

# Ensure same size  
img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0])) 
   
# 70% img1, 30% img2  
blend = cv2.addWeighted(img1, 0.7, img2, 0.3, 0) 
   
# Fade animation: 0.0 → 1.0 alpha  
for alpha in [0.0, 0.25, 0.5, 0.75, 1.0]: 
    frame = cv2.addWeighted(img1, alpha, img2, alpha, 0)  
cv2.imshow('Fade', frame)  

cv2.waitKey(0)
cv2.destroyAllWindows()
