import cv2
import numpy as np

# Use the FULL path to be safe
path = r'D:\OpenCV course\codes\Assiut.png'
img = cv2.imread(path) 


# Convert to float32 for math (0.0 to 1.0)
img_f = img.astype(np.float32) / 255.0 

# Do your 'size control' math (Brighten by 50%)
bright_img = img_f + 0.5 

# 3. USE NP.CLIP to stay in bounds [cite: 249, 360, 395]
result_f = np.clip(bright_img, 0.0, 1.0) 

# 4. CONVERT BACK to uint8 for display [cite: 254, 360]
final_img = (result_f * 255).astype(np.uint8) 

cv2.imshow('Safe Pipeline Result', final_img)
cv2.waitKey(0)
cv2.destroyAllWindows()