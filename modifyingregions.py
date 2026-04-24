import cv2
import numpy as np 
img = cv2.imread('D:\OpenCV course\codes\Assiut.png') 
   
H, W = img.shape[:2]  
   
# Crop a region  returns a VIEW (not a copy)  

roi = img[100:300, 50:250] 
print(roi.shape)
   
# Fill a region with a solid color  
img[100:300, 50:250] = [0, 255, 0]  
   
# Draw a horizontal white line  
img[H//2, :] = [255, 255, 255] 
   
# Draw a vertical white line  
img[:, W//2] = [255, 255, 255] 
   
cv2.imshow("image", img)

# Save  format determined by extension  
success = cv2.imwrite('output.jpg', img)

cv2.waitKey(0)
cv2.destroyAllWindows()