import cv2
import numpy as np 


colored_photo = cv2.imread("D:\OpenCV course\codes\colors.png",1)  # colored photo attribute "1 -> cv2.IMREAD_COLOR"
cv2.imshow("colored photo",colored_photo)

gray_photo=cv2.cvtColor(colored_photo, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray photo",gray_photo)

print(gray_photo.shape) 
print(gray_photo.ndim) 
cv2.waitKey(0)
cv2.destroyAllWindows()
