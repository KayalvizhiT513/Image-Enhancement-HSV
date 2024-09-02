import streamlit as st
from PIL import Image
import numpy as np
import cv2

# Streamlit app title
st.title("Image Enhancement using HSV Color Space")

# Upload image
uploaded_file = st.sidebar.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Load the image
    image = Image.open(uploaded_file)

    # Convert the image to a NumPy array
    image_array = np.array(image)

    # Sidebar options for color channel and factors
    color_channel = st.sidebar.selectbox("Choose Color Channel", ["Red", "Green", "Blue"], index=1)
    luminance_factor = st.sidebar.slider("Luminance Factor", 0.0, 2.0, 0.45)
    saturation_factor = st.sidebar.slider("Saturation Factor", 0.0, 255.0, 255.0)

    # Mapping the selected color channel to the respective index
    channel_indices = {"Red": 0, "Green": 1, "Blue": 2}
    selected_channel_index = channel_indices[color_channel]

    # Convert the RGB image to HSV color space using OpenCV
    hsv_image = cv2.cvtColor(image_array, cv2.COLOR_RGB2HSV)

    # Identify where the selected color component is dominating in the original RGB image
    color_dominant = (
        (image_array[:, :, selected_channel_index] > image_array[:, :, (selected_channel_index + 1) % 3]) & 
        (image_array[:, :, selected_channel_index] > image_array[:, :, (selected_channel_index + 2) % 3])
    )

    # Increase the saturation and luminance in the HSV image for those color-dominant pixels
    hsv_image[:, :, 1][color_dominant] = np.clip(hsv_image[:, :, 1][color_dominant] + saturation_factor, 0, 255)
    hsv_image[:, :, 2][color_dominant] = np.clip(hsv_image[:, :, 2][color_dominant] * luminance_factor, 0, 255)

    # Convert the HSV image back to RGB color space
    enhanced_image_array = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2RGB)

    # Convert the array back to a PIL image
    enhanced_image = Image.fromarray(enhanced_image_array.astype('uint8'))

    # Display the original and enhanced images side by side
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Original Image")
        st.image(image, use_column_width=True)

    with col2:
        st.subheader("Enhanced Image")
        st.image(enhanced_image, use_column_width=True)
        
    # Option to download the enhanced image
    enhanced_image.save("enhanced_image.png")
    with open("enhanced_image.png", "rb") as file:
        btn = st.download_button(
            label="Download Enhanced Image",
            data=file,
            file_name="enhanced_image.png",
            mime="image/png"
        )
