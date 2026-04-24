import cv2, numpy as np

img = cv2.imread('D:\OpenCV course\codes\colors.png')
lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

cv2.imshow("BGR", img)
cv2.imshow("LAB",lab)
cv2.imshow("hsv",hsv)
L, A, B = cv2.split(lab) 
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8)) 
L_enhanced = clahe.apply(L)
lab_enhanced = cv2.merge([L_enhanced, A, B]) 
result = cv2.cvtColor(lab_enhanced, cv2.COLOR_LAB2BGR) 

cv2.imshow("result", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
