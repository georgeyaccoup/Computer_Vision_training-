import cv2
import numpy as np 

colored_photo = cv2.imread("D:\OpenCV course\codes\colors.png",1)  # colored photo attribute "1 -> cv2.IMREAD_COLOR"
cv2.imshow("colored photo",colored_photo)

gray_photo=cv2.imread("D:\OpenCV course\codes\colors.png",0 ) # gray photo scale attribute "0 -> cv2.IMREAD_GRAYSCALE"
cv2.imshow("gray photo",gray_photo)

unchanged_photo =cv2.imread("D:\OpenCV course\codes\colors.png", -1) # unchanged photo scale attribute "0 -> cv2.IMREAD_UNCHANGED"
cv2.imshow("unchanged photo",unchanged_photo)

ANYCOLOR_photo =cv2.imread("D:\OpenCV course\codes\colors.png", 4) # ANYCOLOR  photo scale attribute "0 -> cv2.IMREAD_ANYCOLOR"
cv2.imshow("ANYCOLOR photo",ANYCOLOR_photo)


cv2.waitKey(0)
cv2.destroyAllWindows()
