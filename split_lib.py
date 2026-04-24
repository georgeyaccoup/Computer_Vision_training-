import cv2
import numpy as np
import matplotlib.pyplot as plt

# 1. Load the image using a raw string (r'') to avoid backslash errors
img = cv2.imread(r'D:\OpenCV course\codes\colors.png') 

if img is None:
    print("Error: Could not load Assiut.png. Check the path!")
else:
    # 2. Split the channels (3D Array -> three 2D Matrices)
    B, G, R = cv2.split(img) # 

    # 3. Convert BGR to RGB for Matplotlib display
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # [cite: 351, 387]

    # 4. Create the 1x4 grid
    fig, axes = plt.subplots(1, 4, figsize=(15, 5)) # 

    # Show each channel as a grayscale matrix
    axes[0].imshow(B, cmap='gray')
    axes[0].set_title('Blue Channel')

    axes[1].imshow(G, cmap='gray')
    axes[1].set_title('Green Channel')

    axes[2].imshow(R, cmap='gray')
    axes[2].set_title('Red Channel')

    # Show the final "Sum" (the full color 3D array)
    axes[3].imshow(img_rgb)
    axes[3].set_title('Full Image (RGB)')

    # 5. The function that caused the error—now clean!
    plt.tight_layout() # This fixes the spacing between images 
    plt.show() # Render the window