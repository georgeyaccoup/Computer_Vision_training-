import cv2
import numpy as np 

img = cv2.imread("D:\OpenCV course\codes\colors.png",1)  
mask = np.zeros(img.shape[:2], dtype=np.uint8)
cv2.rectangle(mask, (50, 50), (200, 200), 255, -1) 
cv2.circle(mask, (300, 150), 80, 255, 1) 
cv2.imshow("mask", mask) 
result_and = cv2.bitwise_and(img, img, mask=mask)
cv2.imshow("result_and", result_and) 
# NOT  invert the mask  
inv_mask = cv2.bitwise_not(mask) 
background = cv2.bitwise_and(img, img, mask=inv_mask) 
   
# OR  combine two masks  
mask1 = np.zeros(img.shape[:2], dtype=np.uint8)  
mask2 = np.zeros(img.shape[:2], dtype=np.uint8)  
cv2.rectangle(mask1, (50, 50),  (200, 200), 255, -1)
cv2.rectangle(mask2, (150, 150),(300, 300), 255, -1) 
combined = cv2.bitwise_or(mask1, mask2) 
   
# XOR  only non-overlapping parts  
diff = cv2.bitwise_xor(mask1, mask2) 

cv2.waitKey(0)
cv2.destroyAllWindows()
