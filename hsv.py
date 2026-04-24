import cv2, numpy as np  
img = cv2.imread('D:\OpenCV course\codes\colors.png') 
   
# Step 1: Convert BGR → HSV  
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  
   
# Step 2: Define the color range to isolate
lower_green = np.array([35,  50,  50])  
upper_green = np.array([85, 255, 255])  
   
# Step 3: Create binary mask  
mask = cv2.inRange(hsv, lower_green, upper_green) 
   
# Step 4: Apply mask to original image  
result = cv2.bitwise_and(img, img, mask=mask) 
   
# Step 5: Visualize all three stages  
import matplotlib.pyplot as plt  
fig, (ax1,ax2,ax3) = plt.subplots(1, 3, figsize=(15,5)) 
ax1.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)); 
ax1.set_title('Original'); 
ax1.axis('off') 
 
ax2.imshow(mask,  cmap='gray');  
ax2.set_title('Mask');    
ax2.axis('off') 
ax3.imshow(cv2.cvtColor(result, cv2.COLOR_BGR2RGB)); 
ax3.set_title('Segmented'); 
ax3.axis('off') 
 
plt.tight_layout(); 
plt.savefig('segmentation.png', dpi=150, bbox_inches='tight') 
plt.show()