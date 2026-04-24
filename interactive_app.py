# streamlit run "d:/OpenCV course/codes/interactive_app.py"
import streamlit as st
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Set page layout to wide to give more room for images alongside the sidebar
st.set_page_config(layout="wide")

st.title("📸 CV Zero to Hero: Image Lab")

# ==========================================
# 1. NEW: Input Selection (Upload vs Create)
# ==========================================
input_mode = st.radio("How would you like to start?", ["Upload a Photo", "Create an Image from Scratch"], horizontal=True)

img = None # Variable to hold our working image

if input_mode == "Upload a Photo":
    uploaded_file = st.file_uploader("Upload a photo to begin", type=['jpg', 'jpeg', 'png'])
    if uploaded_file is not None:
        # Convert uploaded file to OpenCV BGR format
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        img = cv2.imdecode(file_bytes, 1)

else:
    st.subheader("🛠️ Image Creator")
    
    # Dimensions
    c1, c2 = st.columns(2)
    with c1:
        new_h = st.number_input("Image Height (px)", 10, 1000, 300)
    with c2:
        new_w = st.number_input("Image Width (px)", 10, 1000, 500)
    
    # Color Space Type
    color_type = st.selectbox("Choose Color Space", ["Grayscale", "BGR", "HSV", "LAB"])
    
    # Dynamic Inputs based on space
    val_code = ""
    creation_code = ""
    
    if color_type == "Grayscale":
        gray_val = st.slider("Gray Intensity (0-255)", 0, 255, 128)
        # Create 1-channel image and convert to BGR for compatibility
        raw_img = np.full((new_h, new_w), gray_val, dtype=np.uint8)
        img = cv2.cvtColor(raw_img, cv2.COLOR_GRAY2BGR)
        
        val_code = f"intensity = {gray_val}"
        creation_code = f"img_gray = np.full(({new_h}, {new_w}), intensity, dtype=np.uint8)\nimg = cv2.cvtColor(img_gray, cv2.COLOR_GRAY2BGR)"
        
    elif color_type == "BGR":
        b_val = st.slider("Blue", 0, 255, 200)
        g_val = st.slider("Green", 0, 255, 100)
        r_val = st.slider("Red", 0, 255, 50)
        img = np.zeros((new_h, new_w, 3), dtype=np.uint8)
        img[:] = [b_val, g_val, r_val]
        
        val_code = f"color = [{b_val}, {g_val}, {r_val}]"
        creation_code = f"img = np.zeros(({new_h}, {new_w}, 3), dtype=np.uint8)\nimg[:] = color"
        
    elif color_type == "HSV":
        h_val = st.slider("Hue (0-179)", 0, 179, 90)
        s_val = st.slider("Saturation (0-255)", 0, 255, 200)
        v_val = st.slider("Value (0-255)", 0, 255, 200)
        hsv_img = np.zeros((new_h, new_w, 3), dtype=np.uint8)
        hsv_img[:] = [h_val, s_val, v_val]
        img = cv2.cvtColor(hsv_img, cv2.COLOR_HSV2BGR)
        
        val_code = f"hsv_color = [{h_val}, {s_val}, {v_val}]"
        creation_code = f"hsv_img = np.zeros(({new_h}, {new_w}, 3), dtype=np.uint8)\nhsv_img[:] = hsv_color\nimg = cv2.cvtColor(hsv_img, cv2.COLOR_HSV2BGR)"

    elif color_type == "LAB":
        l_val = st.slider("L (Lightness)", 0, 255, 150)
        a_val = st.slider("A (Green-Red)", 0, 255, 128)
        b_lab_val = st.slider("B (Blue-Yellow)", 0, 255, 128)
        lab_img = np.zeros((new_h, new_w, 3), dtype=np.uint8)
        lab_img[:] = [l_val, a_val, b_lab_val]
        img = cv2.cvtColor(lab_img, cv2.COLOR_LAB2BGR)
        
        val_code = f"lab_color = [{l_val}, {a_val}, {b_lab_val}]"
        creation_code = f"lab_img = np.zeros(({new_h}, {new_w}, 3), dtype=np.uint8)\nlab_img[:] = lab_color\nimg = cv2.cvtColor(lab_img, cv2.COLOR_LAB2BGR)"

    # --- TWO BOXES (Code and Photo) ---
    st.markdown("### Creation Results")
    res_col1, res_col2 = st.columns(2)
    
    with res_col1:
        st.write("**The Code:**")
        st.code(f"""import numpy as np
import cv2

{val_code}
{creation_code}""")

    with res_col2:
        st.write("**The Created Photo:**")
        st.image(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), caption=f"Solid {color_type} Canvas")

# ==========================================
# REST OF THE APP (ONLY RUNS IF IMG EXISTS)
# ==========================================
if img is not None:
    # Extract properties for student understanding
    h, w, c = img.shape
    st.divider()
    st.write(f"**Current Image Dimensions:** {w}x{h} | **Channels:** {c} | **Dtype:** {img.dtype}")

    st.sidebar.title("Navigation")
    menu_options = [
        "📍 Coordinate Finder", 
        "🎛️ Channel Mixer", 
        "🖊️ Pixel Editor", 
        "📐 Slicing & Shapes",
        "⚫ BGR vs Gray",
        "🌈 HSV Segmentation",
        "🧑 LAB & YCrCb",
        "✂️ Cropping & Resizing",
        "🔄 Rotation & Blending",
        "🧩 Bitwise Operations"
    ]
    selected_tab = st.sidebar.radio("Select a module to explore:", menu_options)

    # --- TAB 1: COORDINATE EXPLORATION ---
    if selected_tab == "📍 Coordinate Finder":
        st.header("Understanding the Grid")
        st.info("Note: Row increases downward (y), Column increases rightward (x).")
        
        col_input = st.number_input("Enter Column (x)", 0, w-1, w//2)
        row_input = st.number_input("Enter Row (y)", 0, h-1, h//2)
        
        # Create a copy for visualization so we don't ruin the original 
        viz_img = img.copy()
        
        # Draw the target lines using NumPy slicing
        viz_img[row_input, :] = [255, 255, 255] 
        viz_img[:, col_input] = [255, 255, 255] 
        
        st.code(f"""# Extracting the BGR values at specific coordinates:
b, g, r = img[{row_input}, {col_input}]
print("BGR Value:", b, g, r)  # Output: {img[row_input, col_input]}""")
        
        # Display with BGR to RGB conversion for correct colors 
        st.image(cv2.cvtColor(viz_img, cv2.COLOR_BGR2RGB), caption=f"Intersection at ({col_input}, {row_input})")

    # --- TAB 2: CHANNEL VISUALIZATION ---
    elif selected_tab == "🎛️ Channel Mixer":
        st.header("Channel Concentration")
        # Split channels using indexing
        b_ch = img[:, :, 0]
        g_ch = img[:, :, 1]
        r_ch = img[:, :, 2]
        
        st.write("Modify the intensity of specific channels (0.0 to 2.0x)")
        b_mult = st.slider("Blue Intensity", 0.0, 2.0, 1.0)
        g_mult = st.slider("Green Intensity", 0.0, 2.0, 1.0)
        r_mult = st.slider("Red Intensity", 0.0, 2.0, 1.0)
        
        st.code(f"""# Split channels using array slicing
b_ch, g_ch, r_ch = img[:, :, 0], img[:, :, 1], img[:, :, 2]

# Apply multipliers using the "Safe Pipeline" (float32 -> clip -> uint8)
new_b = np.clip(b_ch.astype(np.float32) * {b_mult}, 0, 255).astype(np.uint8)
new_g = np.clip(g_ch.astype(np.float32) * {g_mult}, 0, 255).astype(np.uint8)
new_r = np.clip(r_ch.astype(np.float32) * {r_mult}, 0, 255).astype(np.uint8)

# Merge back
merged = cv2.merge([new_b, new_g, new_r])""")

        # Apply multipliers
        new_b = np.clip(b_ch.astype(np.float32) * b_mult, 0, 255).astype(np.uint8)
        new_g = np.clip(g_ch.astype(np.float32) * g_mult, 0, 255).astype(np.uint8)
        new_r = np.clip(r_ch.astype(np.float32) * r_mult, 0, 255).astype(np.uint8)
        
        # Merge back
        merged = cv2.merge([new_b, new_g, new_r])
        
        # Buttons to see individual channels as grayscale
        c1, c2, c3 = st.columns(3)
        if c1.button("Show Blue Channel"): st.image(new_b, caption="Blue (Grayscale View)", clamp=True)
        if c2.button("Show Green Channel"): st.image(new_g, caption="Green (Grayscale View)", clamp=True)
        if c3.button("Show Red Channel"): st.image(new_r, caption="Red (Grayscale View)", clamp=True)
        
        st.image(cv2.cvtColor(merged, cv2.COLOR_BGR2RGB), caption="Modified Channel Mix")

    # --- TAB 3: PIXEL MANIPULATION ---
    elif selected_tab == "🖊️ Pixel Editor":
        st.header("Manual Pixel Control")
        st.write("Select a pixel and force it to a specific color.")
        
        edit_col = st.number_input("Pixel X", 0, w-1, w//2, key="edit_x")
        edit_row = st.number_input("Pixel Y", 0, h-1, h//2, key="edit_y")
        
        new_b_val = st.slider("Set Blue", 0, 255, int(img[edit_row, edit_col, 0]))
        new_g_val = st.slider("Set Green", 0, 255, int(img[edit_row, edit_col, 1]))
        new_r_val = st.slider("Set Red", 0, 255, int(img[edit_row, edit_col, 2]))
        
        st.code(f"""# Directly modifying the pixel array
# Remember: OpenCV uses BGR order!
img[{edit_row}, {edit_col}] = [{new_b_val}, {new_g_val}, {new_r_val}]""")
        
        # Modify the array directly
        img[edit_row, edit_col] = [new_b_val, new_g_val, new_r_val]
        
        st.success(f"Pixel at {edit_col, edit_row} updated to {[new_b_val, new_g_val, new_r_val]}")
        st.image(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), caption="Live Edited Image (Zoom in to see the pixel!)")

    # --- TAB 4: SLICING & Shapes ---
    elif selected_tab == "📐 Slicing & Shapes":
        st.header("NumPy Slicing & Region Control")
        st.markdown("This tab demonstrates **Region of Interest (ROI)** manipulation and **Coordinate Grids**.")
        
        # Use a copy to avoid modifying the base image permanently for other tabs
        shape_img = img.copy()

        # --- Section A: Rectangular ROI ---
        st.subheader("1. Rectangular Slice (ROI)")
        y_range = st.slider("Select Row Range (y1 to y2)", 0, h, (h//4, 3*h//4))
        x_range = st.slider("Select Column Range (x1 to x2)", 0, w, (w//4, 3*w//4))
        
        # Allow user to fill the rectangle with color
        rect_color = st.color_picker("Pick a fill color for the rectangle", "#00FF00")
        r_hex = int(rect_color[1:3], 16)
        g_hex = int(rect_color[3:5], 16)
        b_hex = int(rect_color[5:7], 16)
        
        if st.button("Apply Rectangular Fill"):
            shape_img[y_range[0]:y_range[1], x_range[0]:x_range[1]] = [b_hex, g_hex, r_hex]
            st.code(f"# Slicing a region and broadcasting a color array to it:\nimg[{y_range[0]}:{y_range[1]}, {x_range[0]}:{x_range[1]}] = [{b_hex}, {g_hex}, {r_hex}]")

        # --- Section B: The Circle (Task 2 Method) ---
        st.subheader("2. NumPy Grid Circle")
        st.info("Uses (x-cx)^2 + (y-cy)^2 <= r^2 with `np.ogrid`.")
        
        circle_x = st.slider("Circle Center X", 0, w, w//2)
        circle_y = st.slider("Circle Center Y", 0, h, h//2)
        circle_r = st.slider("Radius", 1, min(h, w)//2, min(h, w)//10)
        
        # Implementation from Lecture 2
        y_grid, x_grid = np.ogrid[:h, :w]
        mask = (x_grid - circle_x)**2 + (y_grid - circle_y)**2 <= circle_r**2
        
        if st.checkbox("Draw White Circle"):
            shape_img[mask] = [255, 255, 255]
            st.code(f"""# Creating an open grid based on image dimensions
y, x = np.ogrid[:{h}, :{w}]

# Mathematical equation for a circle: (x - cx)^2 + (y - cy)^2 <= r^2
mask = (x - {circle_x})**2 + (y - {circle_y})**2 <= {circle_r}**2

# Apply a white color where the mask is True
img[mask] = [255, 255, 255]""")

        # Display the result
        st.image(cv2.cvtColor(shape_img, cv2.COLOR_BGR2RGB), caption="Slicing & Shapes Visualization")

        # --- Section C: View vs Copy Explanation ---
        with st.expander("🎓 View vs. Copy: The Critical Difference"):
            st.write("""
            * **VIEW:** Slicing (`roi = img[y1:y2, x1:x2]`) returns a view. Modifying `roi` **will change** the original image.
            * **COPY:** Using `.copy()` creates an independent array. Modifying the copy **will not** affect the original.
            """)

    # --- TAB 5: BGR vs GRAY ---
    elif selected_tab == "⚫ BGR vs Gray":
        st.header("BGR vs Grayscale")
        st.write("Grayscale removes color and retains luminance. It does not average the channels equally; it uses a perceptual weight: `0.299*R + 0.587*G + 0.114*B` because human eyes are most sensitive to green.")
        
        st.code("""# Convert BGR color space to Grayscale using OpenCV
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)""")

        # Convert to Grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        col1, col2 = st.columns(2)
        with col1:
            st.image(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), caption="Original BGR (3D Array)")
        with col2:
            st.image(gray, caption="Grayscale (2D Matrix)")
            
        st.subheader("Compare a 2x2 Pixel Region (4 Values)")
        st.write("Select a starting coordinate to extract a 2x2 grid and see the exact array values:")
        
        sample_x = st.slider("Select X (Column)", 0, w-2, w//2, key="gray_x")
        sample_y = st.slider("Select Y (Row)", 0, h-2, h//2, key="gray_y")
        
        # Extract 2x2 slices
        bgr_slice = img[sample_y:sample_y+2, sample_x:sample_x+2]
        gray_slice = gray[sample_y:sample_y+2, sample_x:sample_x+2]
        
        st.write("**BGR Array (4 pixels, 3 channels each):**")
        st.code(f"bgr_slice = img[{sample_y}:{sample_y+2}, {sample_x}:{sample_x+2}]\nprint(bgr_slice)\n\n{bgr_slice}")
        st.write("**Grayscale Array (4 pixels, 1 channel each):**")
        st.code(f"gray_slice = gray[{sample_y}:{sample_y+2}, {sample_x}:{sample_x+2}]\nprint(gray_slice)\n\n{gray_slice}")

    # --- TAB 6: HSV SEGMENTATION ---
    elif selected_tab == "🌈 HSV Segmentation":
        st.header("HSV Color Segmentation")
        st.write("HSV separates Hue (color), Saturation (vividness), and Value (brightness). It is the best space for isolating objects by color regardless of lighting.")
        
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        H, S, V = cv2.split(hsv)
        
        with st.expander("Show Split HSV Arrays"):
            st.write(f"**Hue Array (0-179):**\n{H[:2, :2]}...")
            st.write(f"**Saturation Array (0-255):**\n{S[:2, :2]}...")
            st.write(f"**Value Array (0-255):**\n{V[:2, :2]}...")
            
        st.subheader("Find & Isolate a Color")
        st.write("Adjust the sliders to isolate your object. Remember OpenCV Hue goes from 0-179.")
        
        col1, col2 = st.columns(2)
        with col1:
            h_min = st.slider("H min", 0, 179, 35)
            s_min = st.slider("S min", 0, 255, 50)
            v_min = st.slider("V min", 0, 255, 50)
        with col2:
            h_max = st.slider("H max", 0, 179, 85)
            s_max = st.slider("S max", 0, 255, 255)
            v_max = st.slider("V max", 0, 255, 255)
            
        lower_bound = np.array([h_min, s_min, v_min])
        upper_bound = np.array([h_max, s_max, v_max])
        
        st.code(f"""# 1. Convert to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# 2. Define upper and lower bounds (Hue, Saturation, Value)
lower_bound = np.array([{h_min}, {s_min}, {v_min}])
upper_bound = np.array([{h_max}, {s_max}, {v_max}])

# 3. Create a binary mask using cv2.inRange
mask = cv2.inRange(hsv, lower_bound, upper_bound)

# 4. Extract the object using bitwise AND
result = cv2.bitwise_and(img, img, mask=mask)""")

        # Create mask and apply it
        mask = cv2.inRange(hsv, lower_bound, upper_bound)
        result = cv2.bitwise_and(img, img, mask=mask)
        
        # Find contours to locate the object and circle it
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        circled_result = result.copy()
        locations = []
        
        if contours:
            # Find the largest contour
            largest_contour = max(contours, key=cv2.contourArea)
            if cv2.contourArea(largest_contour) > 50: # Filter small noise
                (x, y), radius = cv2.minEnclosingCircle(largest_contour)
                center = (int(x), int(y))
                radius = int(radius)
                cv2.circle(circled_result, center, radius, (0, 0, 255), 3)
                locations.append(f"X: {center[0]}, Y: {center[1]} (Radius: {radius}px)")
        
        c1, c2, c3 = st.columns(3)
        with c1:
            st.image(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), caption="Original")
        with c2:
            st.image(mask, caption="Binary Mask")
        with c3:
            st.image(cv2.cvtColor(circled_result, cv2.COLOR_BGR2RGB), caption="Segmented Result")
            
        if locations:
            st.success(f"Object found at location: {locations[0]}")
        else:
            st.warning("No object found matching this color range. Try adjusting the sliders.")

    # --- TAB 7: LAB & YCrCb ---
    elif selected_tab == "🧑 LAB & YCrCb":
        st.header("LAB & YCrCb Specialized Spaces")
        
        st.subheader("1. LAB Space & CLAHE")
        st.write("LAB separates Lightness (L) from color (A/B). We can apply CLAHE (Contrast Limited Adaptive Histogram Equalization) purely to the L channel to improve contrast without distorting colors.")
        
        lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
        L, A, B = cv2.split(lab)
        
        clip_limit = st.slider("CLAHE Clip Limit", 1.0, 10.0, 2.0, 0.5)
        
        st.code(f"""# Convert to LAB and split channels
lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
L, A, B = cv2.split(lab)

# Create CLAHE object and apply to Lightness channel ONLY
clahe = cv2.createCLAHE(clipLimit={clip_limit}, tileGridSize=(8,8))
L_enhanced = clahe.apply(L)

# Merge back and return to BGR
lab_enhanced = cv2.merge([L_enhanced, A, B])
enhanced_bgr = cv2.cvtColor(lab_enhanced, cv2.COLOR_LAB2BGR)""")
        
        clahe = cv2.createCLAHE(clipLimit=clip_limit, tileGridSize=(8,8))
        L_enhanced = clahe.apply(L)
        lab_enhanced = cv2.merge([L_enhanced, A, B])
        enhanced_bgr = cv2.cvtColor(lab_enhanced, cv2.COLOR_LAB2BGR)
        
        col1, col2 = st.columns(2)
        with col1:
            st.image(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), caption="Original BGR")
        with col2:
            st.image(cv2.cvtColor(enhanced_bgr, cv2.COLOR_BGR2RGB), caption=f"LAB L-Channel CLAHE (Clip={clip_limit})")

        st.markdown("---")
        
        st.subheader("2. YCrCb Space for Skin Detection")
        st.write("YCrCb clusters human skin tones tightly into a small region of the Cr and Cb planes. Empirical starting ranges are Cr: 133-173, Cb: 77-127.")
        
        ycrcb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
        
        c1, c2 = st.columns(2)
        with c1:
            cr_min = st.slider("Cr min", 0, 255, 133)
            cr_max = st.slider("Cr max", 0, 255, 173)
        with c2:
            cb_min = st.slider("Cb min", 0, 255, 77)
            cb_max = st.slider("Cb max", 0, 255, 127)
            
        lower_skin = np.array([0, cr_min, cb_min], dtype=np.uint8)
        upper_skin = np.array([255, cr_max, cb_max], dtype=np.uint8)
        
        st.code(f"""# Convert to YCrCb (Luma, Red Chroma, Blue Chroma)
ycrcb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)

# Define skin tone boundaries
lower_skin = np.array([0, {cr_min}, {cb_min}], dtype=np.uint8)
upper_skin = np.array([255, {cr_max}, {cb_max}], dtype=np.uint8)

# Mask and isolate skin pixels
skin_mask = cv2.inRange(ycrcb, lower_skin, upper_skin)
skin_only = cv2.bitwise_and(img, img, mask=skin_mask)""")
        
        skin_mask = cv2.inRange(ycrcb, lower_skin, upper_skin)
        skin_only = cv2.bitwise_and(img, img, mask=skin_mask)
        
        col3, col4 = st.columns(2)
        with col3:
            st.image(skin_mask, caption="Skin Mask")
        with col4:
            st.image(cv2.cvtColor(skin_only, cv2.COLOR_BGR2RGB), caption="Detected Skin Pixels")
            
        skin_px_count = cv2.countNonZero(skin_mask)
        total_px = img.shape[0] * img.shape[1]
        st.info(f"**Skin Coverage:** {100 * skin_px_count / total_px:.1f}% of image pixels.")

    # --- TAB 8: CROPPING & RESIZING ---
    elif selected_tab == "✂️ Cropping & Resizing":
        st.header("Geometric Transformations: Cropping & Resizing")
        
        # Section A: Cropping
        st.subheader("1. Cropping (NumPy Slicing)")
        st.write("In OpenCV, cropping is simply achieved by slicing the NumPy array `img[y_start:y_end, x_start:x_end]`. Use the sliders to select the region you want to keep.")
        
        c1, c2 = st.columns(2)
        with c1:
            # Slider for Row (Y) Range
            crop_y = st.slider("Select Y (Row) Range", 0, h, (int(h*0.1), int(h*0.9)))
        with c2:
            # Slider for Column (X) Range
            crop_x = st.slider("Select X (Column) Range", 0, w, (int(w*0.1), int(w*0.9)))
            
        if crop_y[0] < crop_y[1] and crop_x[0] < crop_x[1]:
            cropped_img = img[crop_y[0]:crop_y[1], crop_x[0]:crop_x[1]]
            crop_h, crop_w = cropped_img.shape[:2]
            
            st.code(f"# Slicing out a specific section of the image array\ncropped = img[{crop_y[0]}:{crop_y[1]}, {crop_x[0]}:{crop_x[1]}]")
            st.image(cv2.cvtColor(cropped_img, cv2.COLOR_BGR2RGB), caption=f"Cropped Image | Dimensions: {crop_w}x{crop_h} pixels")
        else:
            st.warning("Invalid range! Make sure the minimum value is less than the maximum value.")

        st.markdown("---")

        # Section B: Resizing & Interpolation
        st.subheader("2. Resizing & Interpolation (`cv2.resize`)")
        st.write("Resizing changes the actual number of pixels in the image. The mathematical algorithm used to create new pixels is called Interpolation.")
        
        scale_method = st.radio("Choose how to resize:", ["By Percentage (%)", "By Exact Pixels"])
        
        if scale_method == "By Percentage (%)":
            scale_pct = st.slider("Scale %", 10, 300, 50, 10)
            new_w = int(w * scale_pct / 100)
            new_h = int(h * scale_pct / 100)
        else:
            c3, c4 = st.columns(2)
            with c3:
                new_w = st.number_input("Target Width (px)", 10, w*3, w//2)
            with c4:
                new_h = st.number_input("Target Height (px)", 10, h*3, h//2)
                
        st.info(f"The image will be resized from **{w}x{h}** to **{new_w}x{new_h}**.")
        
        # New Interpolation selection section
        st.write("### Interpolation Methods")
        
        # Dictionary storing flag, description, and properties for the student
        interp_options = {
            "cv2.INTER_NEAREST": {
                "flag": cv2.INTER_NEAREST, 
                "name": "Nearest neighbor",
                "usage": "Mask / label resizing",
                "quality": "Fast, pixelated. Preserves exact values."
            },
            "cv2.INTER_LINEAR": {
                "flag": cv2.INTER_LINEAR, 
                "name": "Bilinear (default)",
                "usage": "General upscaling",
                "quality": "Fast, slightly blurry. Good balance."
            },
            "cv2.INTER_CUBIC": {
                "flag": cv2.INTER_CUBIC, 
                "name": "Bicubic",
                "usage": "High-quality upscaling",
                "quality": "Slower, sharpest edges."
            },
            "cv2.INTER_AREA": {
                "flag": cv2.INTER_AREA, 
                "name": "Pixel area relation",
                "usage": "Downscaling",
                "quality": "Best for shrink. Avoids aliasing/moiré."
            },
            "cv2.INTER_LANCZOS4": {
                "flag": cv2.INTER_LANCZOS4, 
                "name": "Lanczos",
                "usage": "Maximum-quality upscaling",
                "quality": "Slowest, best quality. Great for image editing."
            }
        }
        
        # Default index 1 is cv2.INTER_LINEAR (the general default)
        selected_interp = st.selectbox("Select Interpolation Algorithm:", list(interp_options.keys()), index=1)
        interp_data = interp_options[selected_interp]
        
        # Displaying the properties dynamically
        st.markdown(f"""
        * **Full Name:** {interp_data['name']}
        * **When to use:** {interp_data['usage']}
        * **Speed/Quality:** {interp_data['quality']}
        """)
        
        st.code(f"""# Resize the image using OpenCV with selected interpolation
resized_img = cv2.resize(img, ({new_w}, {new_h}), interpolation={selected_interp})""")
        
        if st.button("Apply Resize & Preview"):
            # Execute resize using the selected algorithm
            resized_img = cv2.resize(img, (new_w, new_h), interpolation=interp_data['flag'])
            
            st.image(cv2.cvtColor(resized_img, cv2.COLOR_BGR2RGB), caption=f"Resized Image | {new_w}x{new_h} px | {selected_interp}")

    # --- TAB 9: ROTATION & BLENDING ---
    elif selected_tab == "🔄 Rotation & Blending":
        st.header("Basic Operations: Rotation, Flipping & Blending")
        
        st.subheader("1. Flipping & 90° Rotations")
        st.write("OpenCV provides optimized functions for standard 90-degree rotations and axis flipping.")
        
        transform_type = st.radio("Select Transformation:", ["None", "Flip Horizontal (1)", "Flip Vertical (0)", "Flip Both (-1)", "Rotate 90° Clockwise", "Rotate 90° Counter-Clockwise", "Rotate 180°"])
            
        transformed_img = img.copy()
        
        if transform_type == "Flip Horizontal (1)":
            transformed_img = cv2.flip(img, 1)
            st.code("transformed_img = cv2.flip(img, 1)  # 1 means horizontal flip")
        elif transform_type == "Flip Vertical (0)":
            transformed_img = cv2.flip(img, 0)
            st.code("transformed_img = cv2.flip(img, 0)  # 0 means vertical flip")
        elif transform_type == "Flip Both (-1)":
            transformed_img = cv2.flip(img, -1)
            st.code("transformed_img = cv2.flip(img, -1) # -1 means flip on both axes")
        elif transform_type == "Rotate 90° Clockwise":
            transformed_img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
            st.code("transformed_img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)")
        elif transform_type == "Rotate 90° Counter-Clockwise":
            transformed_img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
            st.code("transformed_img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)")
        elif transform_type == "Rotate 180°":
            transformed_img = cv2.rotate(img, cv2.ROTATE_180)
            st.code("transformed_img = cv2.rotate(img, cv2.ROTATE_180)")
        else:
            st.code("# No transformation applied")
            
        st.image(cv2.cvtColor(transformed_img, cv2.COLOR_BGR2RGB), caption=transform_type)
        
        st.markdown("---")
        
        st.subheader("2. Arbitrary Angle Rotation")
        st.write("For arbitrary angles, you must calculate a 2D rotation matrix and warp the image using `cv2.warpAffine`.")
        
        col_rot1, col_rot2 = st.columns(2)
        with col_rot1:
            angle = st.slider("Rotation Angle (Degrees)", -180, 180, 45)
        with col_rot2:
            scale = st.slider("Scale", 0.1, 3.0, 1.0, 0.1)
            
        st.code(f"""# 1. Get the rotation matrix around the center of the image
center = ({w//2}, {h//2})
M = cv2.getRotationMatrix2D(center, angle={angle}, scale={scale})

# 2. Apply the affine transformation
rotated_img = cv2.warpAffine(img, M, ({w}, {h}))""")

        M = cv2.getRotationMatrix2D((w//2, h//2), angle, scale)
        rotated_img = cv2.warpAffine(img, M, (w, h))
        
        st.image(cv2.cvtColor(rotated_img, cv2.COLOR_BGR2RGB), caption=f"Rotated by {angle}°, Scaled by {scale}x")
        
        st.markdown("---")
        
        st.subheader("3. Image Blending (`cv2.addWeighted`)")
        st.write("Blending combines two images using the mathematical formula: `dst = (alpha * img1) + (beta * img2) + gamma`.")
        
        uploaded_file2 = st.file_uploader("Upload Image 2 for blending", type=['jpg', 'jpeg', 'png'])
        
        if uploaded_file2 is not None:
            file_bytes2 = np.asarray(bytearray(uploaded_file2.read()), dtype=np.uint8)
            img2 = cv2.imdecode(file_bytes2, 1)
            
            # cv2.addWeighted requires images to be identical in dimensions and channels
            img2_resized = cv2.resize(img2, (w, h))
            st.info(f"Image 2 was automatically resized to {w}x{h} to match Image 1's dimensions.")
            
            c_blend1, c_blend2, c_blend3 = st.columns(3)
            with c_blend1:
                alpha = st.slider("Alpha (Weight of Img 1)", 0.0, 1.0, 0.5, 0.05)
            with c_blend2:
                beta = st.slider("Beta (Weight of Img 2)", 0.0, 1.0, 0.5, 0.05)
            with c_blend3:
                gamma = st.slider("Gamma (Scalar added to all pixels)", 0, 100, 0)
                
            st.code(f"""# Images must be the exact same size to blend them!
img2_resized = cv2.resize(img2, ({w}, {h}))

# Apply cv2.addWeighted(src1, alpha, src2, beta, gamma)
blended = cv2.addWeighted(img, {alpha:.2f}, img2_resized, {beta:.2f}, {gamma})""")
            
            blended_img = cv2.addWeighted(img, alpha, img2_resized, beta, gamma)
            
            b1, b2, b3 = st.columns(3)
            with b1:
                st.image(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), caption="Image 1")
            with b2:
                st.image(cv2.cvtColor(img2_resized, cv2.COLOR_BGR2RGB), caption="Image 2 (Resized)")
            with b3:
                st.image(cv2.cvtColor(blended_img, cv2.COLOR_BGR2RGB), caption="Blended Result")
        else:
            st.warning("Upload a second image above to unlock the Blending controls!")

    # --- TAB 10: BITWISE OPERATIONS (NEW) ---
    elif selected_tab == "🧩 Bitwise Operations":
        st.header("Logic with Pixels: Bitwise Operations")
        
        st.subheader("1. Create a Mask")
        st.write("Draw shapes on a black canvas to create a mask. White areas (255) represent 'True', black areas (0) represent 'False'.")
        
        # Create a black 3-channel image of the same size
        mask = np.zeros_like(img)
        
        col_m1, col_m2 = st.columns(2)
        with col_m1:
            st.write("**Draw a Circle**")
            cx = st.slider("Circle Center X", 0, w, w//2, key="bw_cx")
            cy = st.slider("Circle Center Y", 0, h, h//2, key="bw_cy")
            cr = st.slider("Circle Radius", 10, min(w, h), int(min(w,h)*0.2), key="bw_cr")
            
            # Draw the circle on the mask (White and Filled)
            cv2.circle(mask, (cx, cy), cr, (255, 255, 255), -1) 
            
        with col_m2:
            st.write("**Draw a Line**")
            x1 = st.slider("Line Start X", 0, w, int(w*0.1), key="bw_x1")
            y1 = st.slider("Line Start Y", 0, h, int(h*0.1), key="bw_y1")
            x2 = st.slider("Line End X", 0, w, int(w*0.9), key="bw_x2")
            y2 = st.slider("Line End Y", 0, h, int(h*0.9), key="bw_y2")
            thickness = st.slider("Line Thickness", 1, 100, 20, key="bw_th")
            
            # Draw the line on the mask (White)
            cv2.line(mask, (x1, y1), (x2, y2), (255, 255, 255), thickness)
            
        st.image(cv2.cvtColor(mask, cv2.COLOR_BGR2RGB), caption="Generated Mask (White = True, Black = False)")
        
        st.markdown("---")
        
        st.subheader("2. Apply Bitwise Operation")
        st.write("Choose a logical operation to combine your generated mask with the uploaded image.")
        
        operation = st.radio("Choose Operation:", ["AND", "OR", "XOR", "NOT (Invert Image)", "NOT (Invert Mask)"], horizontal=True)
        
        if operation == "AND":
            result = cv2.bitwise_and(img, mask)
            code_str = "result = cv2.bitwise_and(img, mask)"
        elif operation == "OR":
            result = cv2.bitwise_or(img, mask)
            code_str = "result = cv2.bitwise_or(img, mask)"
        elif operation == "XOR":
            result = cv2.bitwise_xor(img, mask)
            code_str = "result = cv2.bitwise_xor(img, mask)"
        elif operation == "NOT (Invert Image)":
            result = cv2.bitwise_not(img)
            code_str = "result = cv2.bitwise_not(img)"
        elif operation == "NOT (Invert Mask)":
            result = cv2.bitwise_not(mask)
            code_str = "result = cv2.bitwise_not(mask)"
            
        st.code(f"""# 1. Create a blank black canvas of the same size
mask = np.zeros_like(img)

# 2. Draw white shapes to define the "True" regions
cv2.circle(mask, ({cx}, {cy}), {cr}, (255, 255, 255), -1)
cv2.line(mask, ({x1}, {y1}), ({x2}, {y2}), (255, 255, 255), {thickness})

# 3. Apply the Bitwise Operation
{code_str}""")

        st.image(cv2.cvtColor(result, cv2.COLOR_BGR2RGB), caption=f"Result of Bitwise {operation}")
else:
    st.info("Waiting for image input... Choose to upload or create one above! 🚀")