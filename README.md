# 🖼️ Computer Vision Training — OpenCV with Python

A structured, hands-on collection of Python scripts for learning **Computer Vision** from scratch using **OpenCV**, **NumPy**, **Matplotlib**, and **Pillow**. Each script focuses on a specific concept, building progressively from environment setup to advanced image manipulation.

---

## 📦 Requirements

Install all dependencies before running any script:

```bash
pip install opencv-python numpy matplotlib Pillow openpyxl
```

> **Python version:** 3.8 or higher recommended.

---

## 📁 Repository Structure

```
Computer_Vision_training-/
│
├── 🔧 Setup & Basics
│   ├── instulation_verificatoin.py
│   ├── np_test.py
│   └── first_CV.py
│
├── 🖼️ Image Data & Pixel Access
│   ├── img_data.py
│   ├── access_pixel.py
│   └── image_operations.py
│
├── 🎨 Color Spaces
│   ├── gray_scal.py
│   ├── creat_gray_scale.py
│   ├── hsv.py
│   ├── LAB.py
│   ├── scales.py
│   ├── split.py
│   └── split_lib.py
│
├── ✏️ Drawing & Shapes
│   ├── drawing_lines.py
│   ├── all_shapes_drawing.py
│   └── drawing_task_solution.py
│
├── 🔄 Transformations
│   ├── resize.py
│   ├── rotation.py
│   ├── sizeControl.py
│   ├── modifyingregions.py
│   └── overwriting.py
│
├── ⚙️ Bitwise Operations
│   └── bitwiseOperation.py
│
├── 📐 Distance Metrics
│   ├── L_1.py
│   └── L2_code.py
│
├── 📊 Visualization
│   └── matplotlib_intro.py
│
├── 🖱️ Interactive
│   └── interactive_app.py
│
├── 🗂️ Misc / Utility
│   ├── pexcel_modify.py
│   └── testing.py
│
└── 🖼️ Image Assets
    ├── Assiut.png
    ├── assiut_gray.jpeg
    ├── colors.png
    ├── elephant.jpg
    ├── hero-270-park.jpg
    └── photo.jfif
```

---

## 📄 File Descriptions

---

### 🔧 Setup & Basics

---

#### `instulation_verificatoin.py`
**Purpose:** Verifies that all required Computer Vision libraries are properly installed and working.

**What it does:**
- Prints the installed versions of Python, OpenCV, and NumPy to the console.
- Creates a simple green 200×200 pixel image using NumPy from scratch.
- Displays the test image using three different methods: OpenCV (`cv2.imshow`), Matplotlib (`plt.imshow`), and Pillow (`Image.show`).
- Prints a ✅ success message if all libraries are functioning correctly.

**Key concepts:** Library version checking, NumPy image creation, multi-library display comparison.

**Libraries used:** `cv2`, `numpy`, `PIL`, `matplotlib`, `sys`

---

#### `np_test.py`
**Purpose:** Introduces NumPy array operations in the context of image data.

**What it does:**
- Exercises basic NumPy array creation, slicing, indexing, and data type handling.
- Demonstrates how images are represented as multi-dimensional NumPy arrays.
- Serves as a mathematical foundation exercise before working with real images.

**Key concepts:** NumPy array fundamentals, dtype, array shape, multi-dimensional indexing.

**Libraries used:** `numpy`

---

#### `first_CV.py`
**Purpose:** The very first hands-on OpenCV script — loads a real image and reads pixel values directly.

**What it does:**
- Loads `Assiut.png` from disk using `cv2.imread()`.
- Accesses the pixel at position `[100, 200]` and prints its full BGR array value.
- Unpacks the pixel into individual Blue, Green, and Red channels using tuple assignment.
- Accesses a single channel value using a third index (`img[100, 200, 0]`).
- Displays the image in an OpenCV window and prints the data type of the pixel array.

**Key concepts:** Reading images, pixel indexing (`img[row, col]`), BGR channel order, NumPy array data types.

**Sample output:**
```
total [B G R], b=..., g=..., r=..., index_3 ...
Data structure type: <class 'numpy.ndarray'>
```

**Libraries used:** `cv2`, `numpy`

---

### 🖼️ Image Data & Pixel Access

---

#### `img_data.py`
**Purpose:** Explores the metadata and structure of a loaded image.

**What it does:**
- Loads `Assiut.png` and prints all key structural properties of the image array.
- Reports `img.shape` (Height × Width × Channels), `img.ndim` (number of dimensions), `img.dtype` (data type, e.g., `uint8`), and `img.size` (total number of pixel values).
- Unpacks shape into individual `H`, `W`, and `C` variables for clarity.
- Demonstrates advanced NumPy slicing to extract a single channel slice of the image.

**Key concepts:** Image shape, channels, dtype, size, NumPy array properties.

**Sample output:**
```
image shape:  (H, W, 3)
image channels:  3
array type: uint8
```

**Libraries used:** `cv2`, `numpy`

---

#### `access_pixel.py`
**Purpose:** Demonstrates how to access and extract individual pixel color values from specific image coordinates.

**What it does:**
- Loads `Assiut.png` and prints the image size and shape.
- Uses NumPy slice notation (`img.shape[::2]`) to extract Height and Width without the channel dimension.
- Accesses the bottom-right pixel of the image using `img[H-1, W-1]`.
- Separates and prints the individual Blue, Green, and Red channel values of that pixel using channel indexing (`img[H-1, W-1, 0]`, etc.).

**Key concepts:** Pixel coordinate access, channel separation, NumPy step slicing.

**Sample output:**
```
top left pixel =  [B G R]
B=... G=... R=...
```

**Libraries used:** `cv2`, `numpy`

---

#### `image_operations.py`
**Purpose:** Demonstrates Region of Interest (ROI) extraction — the technique of isolating and working with specific sub-regions of an image.

**What it does:**
- Loads `colors.png` and prints its dimensions.
- Extracts a 150×150 ROI from the top-left corner using array slicing: `img[0:150, 0:150]`.
- Extracts the entire top-left quadrant of the image using dynamic coordinates.
- Extracts a center-region ROI by calculating the image center and slicing symmetrically.
- Uses `.copy()` to create an independent copy of an ROI, then fills it with solid green `[0, 255, 0]` — demonstrating that `.copy()` prevents changes from affecting the original image.

**Key concepts:** ROI cropping, in-place modification, `.copy()` vs view slicing, region-based editing.

**Libraries used:** `cv2`, `numpy`

---

### 🎨 Color Spaces

---

#### `gray_scal.py`
**Purpose:** Introduces grayscale conversion using OpenCV's built-in color transformation function.

**What it does:**
- Loads `colors.png` in color mode (`cv2.IMREAD_COLOR`).
- Converts the color BGR image to grayscale using `cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)`.
- Displays both the original color image and the resulting grayscale image side-by-side.
- Prints the shape and number of dimensions of the grayscale image to illustrate that it's a 2D array (no channel dimension), unlike the 3D BGR array.

**Key concepts:** `cv2.cvtColor`, BGR to Grayscale, 2D vs 3D image arrays, `cv2.COLOR_BGR2GRAY`.

**Libraries used:** `cv2`, `numpy`

---

#### `creat_gray_scale.py`
**Purpose:** Implements the grayscale conversion formula **manually** from scratch using pixel-by-pixel iteration — no OpenCV conversion functions used.

**What it does:**
- Loads `Assiut.png` and creates a blank 2D NumPy array of the same height and width.
- Iterates over every pixel using nested `for` loops.
- Applies the standard luminosity formula to compute the grayscale value:
  > `gray = 0.299×R + 0.587×G + 0.114×B`
- Assigns the computed value to each pixel of the grayscale array.
- Saves the result as `assiut_gray.jpeg` with JPEG quality set to 50 using `cv2.imwrite`.

**Key concepts:** Manual grayscale formula, pixel-level iteration, `np.zeros()`, `cv2.imwrite()`, JPEG quality parameter.

> ⚠️ Note: This approach is very slow for large images — it's written for learning purposes. Use `cv2.cvtColor()` in production.

**Libraries used:** `cv2`, `numpy`

---

#### `hsv.py`
**Purpose:** Demonstrates color-based image segmentation using the HSV (Hue, Saturation, Value) color space.

**What it does:**
- Loads `colors.png` and converts it from BGR to HSV using `cv2.cvtColor(img, cv2.COLOR_BGR2HSV)`.
- Defines a hue range for green: `lower_green = [35, 50, 50]`, `upper_green = [85, 255, 255]`.
- Creates a binary mask using `cv2.inRange()` — pixels within the green range become white (255), all others become black (0).
- Applies the mask to the original image using `cv2.bitwise_and()` to isolate only the green regions.
- Visualizes all three stages (Original → Mask → Segmented result) in a 1×3 Matplotlib subplot.
- Saves the final visualization as `segmentation.png`.

**Key concepts:** HSV color space, `cv2.inRange()`, binary masking, color segmentation, `cv2.bitwise_and()`.

**Libraries used:** `cv2`, `numpy`, `matplotlib`

---

#### `LAB.py`
**Purpose:** Introduces the LAB color space and demonstrates CLAHE (Contrast Limited Adaptive Histogram Equalization) for local contrast enhancement.

**What it does:**
- Loads `colors.png` and converts it to both LAB and HSV color spaces for comparison.
- Displays the original BGR, LAB, and HSV versions of the image.
- Splits the LAB image into its three channels: `L` (lightness), `A` (green-red axis), `B` (blue-yellow axis).
- Applies CLAHE to the `L` (lightness) channel only, using `clipLimit=2.0` and a tile grid of 8×8.
- Merges the enhanced `L` channel back with the original `A` and `B` channels.
- Converts the enhanced LAB image back to BGR and displays the improved result.

**Key concepts:** LAB color space, `cv2.split()`, `cv2.merge()`, CLAHE, contrast enhancement without affecting colors.

**Libraries used:** `cv2`, `numpy`

---

#### `scales.py`
**Purpose:** Explores additional color space conversions and color scale comparisons.

**Key concepts:** Color space transformations, visual comparison of color representations.

**Libraries used:** `cv2`, `numpy`

---

#### `split.py`
**Purpose:** Demonstrates manual channel splitting of a BGR image using NumPy array slicing.

**What it does:**
- Splits a color image into its individual B, G, R channels using index slicing (`img[:, :, 0]`, etc.).
- Displays each channel separately to visualize how individual color components look as grayscale images.

**Key concepts:** Channel splitting via NumPy indexing, visual understanding of RGB channels.

**Libraries used:** `cv2`, `numpy`

---

#### `split_lib.py`
**Purpose:** Demonstrates channel splitting using OpenCV's built-in `cv2.split()` function — the library-native equivalent of the manual approach in `split.py`.

**What it does:**
- Uses `cv2.split(img)` to unpack the image into B, G, R channel arrays in one call.
- Optionally recombines channels using `cv2.merge()`.
- Compares results with the manual slicing approach.

**Key concepts:** `cv2.split()`, `cv2.merge()`, channel manipulation.

**Libraries used:** `cv2`, `numpy`

---

### ✏️ Drawing & Shapes

---

#### `drawing_lines.py`
**Purpose:** Draws geometric shapes manually using pixel-level math — **without** using any OpenCV drawing functions.

**What it does:**
- Creates a blank 200×200 grayscale image using `np.zeros()`.
- Draws the **main diagonal** by iterating `i` from 0 to 199 and setting `img[i, i] = 255`.
- Draws the **anti-diagonal** using `img[199 - i, i] = 255`.
- Draws a **circle** from scratch using the circle equation `x² + y² = r²`. For each x, computes both positive and negative y offsets using `math.sqrt()` and places white pixels at the resulting coordinates.
- Displays the result showing two crossing diagonals and a mathematically perfect circle.

**Key concepts:** Pixel-level drawing, mathematical geometry, diagonal lines, circle equation, `math.sqrt()`.

**Libraries used:** `cv2`, `numpy`, `math`

---

#### `all_shapes_drawing.py`
**Purpose:** A comprehensive reference script that demonstrates **all major OpenCV drawing functions** in a single canvas.

**What it does:**
Draws the following 10 shape types on a 1000×1000 black canvas, each with commented syntax:

| # | Shape | OpenCV Function |
|---|-------|----------------|
| 1 | Line | `cv2.line()` |
| 2 | Rectangle (outline) | `cv2.rectangle()` with `thickness=2` |
| 3 | Filled Rectangle | `cv2.rectangle()` with `thickness=-1` |
| 4 | Circle (outline) | `cv2.circle()` with `thickness=2` |
| 5 | Filled Circle | `cv2.circle()` with `thickness=-1` |
| 6 | Ellipse | `cv2.ellipse()` |
| 7 | Triangle (outline) | `cv2.polylines()` with `isClosed=True` |
| 8 | Filled Triangle | `cv2.fillPoly()` |
| 9 | Arrowed Line | `cv2.arrowedLine()` |
| 10 | Text | `cv2.putText()` with `FONT_HERSHEY_SIMPLEX` |

**Key concepts:** All OpenCV drawing primitives, `np.array` point arrays, filled vs outlined shapes, text rendering.

**Libraries used:** `cv2`, `numpy`

---

#### `drawing_task_solution.py`
**Purpose:** A practical drawing exercise / challenge solution that combines multiple shapes to produce a composite image.

**What it does:**
- Applies multiple drawing functions learned in `all_shapes_drawing.py` to create a specific composite scene or pattern as a training task.

**Key concepts:** Applied drawing, combining multiple shapes, coordinate planning.

**Libraries used:** `cv2`, `numpy`

---

### 🔄 Transformations

---

#### `resize.py`
**Purpose:** Covers all common image resizing strategies using `cv2.resize()`.

**What it does:**
- Loads `colors.png` and demonstrates three resizing approaches:
  1. **Exact dimensions:** Resizes directly to 320×240 regardless of aspect ratio.
  2. **Scale factor:** Creates half-size (`W//2, H//2`) and double-size (`W*2, H*2`) versions.
  3. **Fixed width with aspect-ratio preservation:** Sets target width to 400px, computes the proportional height using `scale = new_w / W`, and resizes accordingly.
- Displays the aspect-ratio-preserved resized image.

**Key concepts:** `cv2.resize()`, aspect ratio, scaling factors, width-based resizing.

**Libraries used:** `cv2`, `numpy`

---

#### `rotation.py`
**Purpose:** Comprehensive coverage of all image rotation and flipping operations in OpenCV.

**What it does:**
- **Flipping:**
  - `cv2.flip(img, 0)` — vertical flip
  - `cv2.flip(img, 1)` — horizontal flip
  - `cv2.flip(img, -1)` — both axes flip
- **Arbitrary angle rotation:**
  - Computes a rotation matrix using `cv2.getRotationMatrix2D(center, angle=45, scale=1.0)`.
  - Applies the rotation using `cv2.warpAffine()`.
- **Fixed-angle rotation shortcuts:**
  - `cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)`
  - `cv2.rotate(img, cv2.ROTATE_180)`
  - `cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)`
- **Canvas expansion:** Recalculates the output canvas size using trigonometry to prevent corner clipping when rotating to arbitrary angles.

**Key concepts:** `cv2.flip()`, `cv2.getRotationMatrix2D()`, `cv2.warpAffine()`, rotation matrix, canvas expansion.

**Libraries used:** `cv2`, `numpy`

---

#### `sizeControl.py`
**Purpose:** Explores dynamic image size control techniques and dimension-aware operations.

**Key concepts:** Dynamic dimension calculation, conditional resizing, output size management.

**Libraries used:** `cv2`, `numpy`

---

#### `modifyingregions.py`
**Purpose:** Demonstrates how to modify specific rectangular regions (ROIs) of an image in-place.

**What it does:**
- Extracts an ROI from an image using array slicing.
- Modifies the pixel values within that region directly (without creating a copy), which updates the original image.
- Demonstrates the difference between modifying a view (in-place) vs a `.copy()`.

**Key concepts:** In-place region modification, view vs copy behavior in NumPy, ROI editing.

**Libraries used:** `cv2`, `numpy`

---

#### `overwriting.py`
**Purpose:** Demonstrates overwriting a region of one image with content from another image or a solid color.

**What it does:**
- Copies a region from one location and pastes it into another position.
- Overwrites image regions with solid color blocks.
- Demonstrates composite image editing by pasting sub-images.

**Key concepts:** Region copy-paste, in-place overwriting, compositing.

**Libraries used:** `cv2`, `numpy`

---

### ⚙️ Bitwise Operations

---

#### `bitwiseOperation.py`
**Purpose:** Demonstrates all four bitwise operations (AND, OR, NOT, XOR) applied to image masks — a foundational technique used in masking and compositing.

**What it does:**
- Loads `colors.png` and creates a blank mask of the same H×W.
- Draws a filled white rectangle and a circle outline onto the mask.
- **AND:** Applies `cv2.bitwise_and(img, img, mask=mask)` to keep only the unmasked regions of the image.
- **NOT:** Inverts the mask with `cv2.bitwise_not(mask)`, then ANDs to get the background (everything outside the shapes).
- **OR:** Creates two overlapping rectangle masks (`mask1`, `mask2`) and combines them with `cv2.bitwise_or()` to merge both regions.
- **XOR:** Uses `cv2.bitwise_xor(mask1, mask2)` to isolate only the non-overlapping parts of the two masks.

**Key concepts:** Binary masks, `cv2.bitwise_and/or/not/xor`, mask inversion, region isolation, compositing.

**Libraries used:** `cv2`, `numpy`

---

### 📐 Distance Metrics

---

#### `L_1.py`
**Purpose:** Explores image channel analysis and data type conversions across multiple images (a structured lab exercise).

**What it does:**
- Loads `elephant.jpg` three times (representing three analysis sessions).
- For each load, prints: shape, data type, total pixel count, and the center pixel value in BGR.
- Converts the image from `uint8` to `float32` using `.astype(np.float32)` and back, printing center pixel values at each stage to observe precision changes.
- Manually splits the image into B, G, R channels using NumPy index slicing.
- Displays each channel separately as a grayscale image.

**Key concepts:** Data type conversion (`uint8` ↔ `float32`), channel extraction via slicing, pixel value analysis, center pixel access.

> 📌 The name "L_1" refers to Lecture 1 of the training course — it's a comprehensive practical lab, not a distance metric implementation.

**Libraries used:** `cv2`, `numpy`

---

#### `L2_code.py`
**Purpose:** Continues the lecture series with more advanced image analysis and manipulation exercises.

**Key concepts:** Building on L_1 concepts, additional channel operations, image comparison techniques.

**Libraries used:** `cv2`, `numpy`

---

### 📊 Visualization

---

#### `matplotlib_intro.py`
**Purpose:** Introduces Matplotlib as a visualization tool for displaying images and data from OpenCV, with focus on correct color handling.

**What it does:**
- Loads images using OpenCV (BGR format) and displays them correctly in Matplotlib by converting with `cv2.cvtColor(img, cv2.COLOR_BGR2RGB)` before passing to `plt.imshow()`.
- Demonstrates subplot layouts for displaying multiple images side-by-side.
- Uses `plt.axis('off')` for clean display and `plt.title()` for labeling.
- Compares how the same image looks with and without the BGR→RGB conversion.

**Key concepts:** BGR vs RGB display, `plt.imshow()`, `plt.subplots()`, figure layout, axis removal.

> ⚠️ OpenCV loads images as BGR, but Matplotlib expects RGB — always convert before displaying, or colors will appear inverted.

**Libraries used:** `cv2`, `matplotlib`

---

### 🖱️ Interactive

---

#### `interactive_app.py`
**Purpose:** Builds an interactive OpenCV application using trackbars (sliders) for real-time parameter control.

**What it does:**
- Creates a named window with one or more trackbars using `cv2.createTrackbar()`.
- Reads trackbar positions in a live loop using `cv2.getTrackbarPos()`.
- Applies the trackbar values to dynamically adjust image properties (e.g., brightness, color channel values, or threshold levels) in real time.
- Updates the displayed image on every loop iteration.

**Key concepts:** `cv2.createTrackbar()`, `cv2.getTrackbarPos()`, real-time parameter adjustment, interactive UI in OpenCV.

**Libraries used:** `cv2`, `numpy`

---

### 🗂️ Misc / Utility

---

#### `pexcel_modify.py`
**Purpose:** Demonstrates using Python to read from or write to Excel files using `openpyxl` — useful for logging image processing results or managing datasets.

**What it does:**
- Opens or creates an Excel workbook.
- Reads or writes cell values programmatically.
- Saves the modified workbook back to disk.

**Key concepts:** `openpyxl` basics, spreadsheet automation, data logging for CV pipelines.

**Libraries used:** `openpyxl`

---

#### `testing.py`
**Purpose:** A scratch/experimentation file used for quick code testing and debugging during the learning process.

**What it does:**
- Contains temporary or exploratory code snippets for testing new functions or debugging errors.
- May contain commented-out experiments and print statements.

> 📌 This file is not part of the structured curriculum — it's a personal scratchpad.

---

## 🖼️ Image Assets

| File | Description |
|------|-------------|
| `Assiut.png` | Primary training image — a photo of Assiut, Egypt. Used in most early scripts. |
| `assiut_gray.jpeg` | Grayscale version of `Assiut.png`, generated by `creat_gray_scale.py`. |
| `colors.png` | A synthetic color test image with distinct color regions. Used for color space and drawing exercises. |
| `elephant.jpg` | A real-world photo of an elephant. Used for channel analysis in `L_1.py`. |
| `hero-270-park.jpg` | Additional real-world photo used for transformation and region exercises. |
| `photo.jfif` | Supplementary image asset in JFIF format (a variant of JPEG). |

---

## 📚 Learning Path (Recommended Order)

Follow this sequence for the best learning progression:

```
1. instulation_verificatoin.py  → Verify your environment
2. np_test.py                   → NumPy fundamentals
3. first_CV.py                  → First image + pixel access
4. img_data.py                  → Image structure & metadata
5. access_pixel.py              → Pixel coordinates & channels
6. image_operations.py          → ROI cropping & editing
7. gray_scal.py                 → Grayscale via OpenCV
8. creat_gray_scale.py          → Grayscale from scratch
9. split.py / split_lib.py      → Channel splitting
10. hsv.py                      → HSV & color segmentation
11. LAB.py                      → LAB space & CLAHE
12. drawing_lines.py            → Manual geometry drawing
13. all_shapes_drawing.py       → All OpenCV drawing functions
14. bitwiseOperation.py         → Masking & bitwise ops
15. resize.py                   → Image resizing
16. rotation.py                 → Rotation & flipping
17. modifyingregions.py         → Region modification
18. L_1.py / L2_code.py         → Comprehensive lab exercises
19. matplotlib_intro.py         → Visualization with Matplotlib
20. interactive_app.py          → Interactive trackbar app
```

---

## 🗒️ Notes

- All scripts use **hardcoded local paths** (e.g., `D:\OpenCV course\codes\...`). Update these paths to match your local directory before running.
- OpenCV loads images in **BGR** order (not RGB). Always convert to RGB when using Matplotlib for display.
- Scripts prefixed with `L_` (e.g., `L_1.py`, `L2_code.py`) correspond to lecture exercises in the training course.

---

## 👤 Author

**George Yaccoup**
GitHub: [@georgeyaccoup](https://github.com/georgeyaccoup)
