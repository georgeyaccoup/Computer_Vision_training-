import cv2
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import sys

print("Python version:", sys.version)
print("OpenCV version:", cv2.__version__)
print("NumPy version:", np.__version__)

# Create a simple image using numpy
img = np.zeros((200, 200, 3), dtype=np.uint8)
img[:] = (0, 255, 0)  # green image

# Show using OpenCV
cv2.imshow("Test Image (OpenCV)", img)
cv2.waitKey(2000)
cv2.destroyAllWindows()

# Show using matplotlib
plt.imshow(img)
plt.title("Matplotlib Display Test")
plt.axis('off')
plt.show()

# Pillow test
pil_img = Image.fromarray(img)
pil_img.show()

print("✅ All libraries are working correctly!")