# Import libraries
import cv2
import numpy as np

# -------- IMAGE 1 --------
img = cv2.imread("D:\OpenCV course\codes\elephant.jpg")

print("\n--- Image 1 ---")
print("Shape:", img.shape)
print("Data type:", img.dtype)
print("Total pixels:", img.size)

h, w = img.shape[:2]

print("Center pixel (BGR):", img[h//2, w//2])

img_float = img.astype(np.float32)
print("Center pixel (float32):", img_float[h//2, w//2])

img_uint8 = img_float.astype(np.uint8)

# Split channels using slicing
B = img[:, :, 0]
G = img[:, :, 1]
R = img[:, :, 2]

# Show channels
cv2.imshow("Image1 - Blue", B)
cv2.imshow("Image1 - Green", G)
cv2.imshow("Image1 - Red", R)

cv2.waitKey(0)
cv2.destroyAllWindows()


# -------- IMAGE 2 --------
img = cv2.imread("D:\OpenCV course\codes\elephant.jpg")

print("\n--- Image 2 ---")
print("Shape:", img.shape)
print("Data type:", img.dtype)
print("Total pixels:", img.size)

h, w = img.shape[:2]

print("Center pixel (BGR):", img[h//2, w//2])

img_float = img.astype(np.float32)
print("Center pixel (float32):", img_float[h//2, w//2])

img_uint8 = img_float.astype(np.uint8)

B = img[:, :, 0]
G = img[:, :, 1]
R = img[:, :, 2]

cv2.imshow("Image2 - Blue", B)
cv2.imshow("Image2 - Green", G)
cv2.imshow("Image2 - Red", R)

cv2.waitKey(0)
cv2.destroyAllWindows()


# -------- IMAGE 3 --------
img = cv2.imread("D:\OpenCV course\codes\elephant.jpg")

print("\n--- Image 3 ---")
print("Shape:", img.shape)
print("Data type:", img.dtype)
print("Total pixels:", img.size)

h, w = img.shape[:2]

print("Center pixel (BGR):", img[h//2, w//2])

img_float = img.astype(np.float32)
print("Center pixel (float32):", img_float[h//2, w//2])

img_uint8 = img_float.astype(np.uint8)

B = img[:, :, 0]
G = img[:, :, 1]
R = img[:, :, 2]

cv2.imshow("Image3 - Blue", B)
cv2.imshow("Image3 - Green", G)
cv2.imshow("Image3 - Red", R)

cv2.waitKey(0)
cv2.destroyAllWindows()