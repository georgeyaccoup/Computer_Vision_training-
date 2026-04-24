import cv2
import numpy as np 
img = cv2.imread('D:\OpenCV course\codes\Assiut.png') 
   
# Set one pixel to pure red (BGR order!)  
img[100, 200] = [0, 0, 255] 
   
# Set to white  
img[100, 200] = [255, 255, 255] 
   
# Set to black  
img[100, 200] = [0, 0, 0] 
   
# Modify only the Red channel  
img[100, 200, 2] = 255 
img[100, 200, 0] = 0 

cv2.imshow("Image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()