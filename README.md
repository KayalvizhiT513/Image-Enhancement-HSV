# Image Enhancement using HSV Color Space

This Streamlit app allows users to enhance images by targeting specific color channels (Red, Green, or Blue) using the HSV color space. Users can upload an image, select a color channel, and adjust the luminance and saturation factors to enhance the image. The app provides side-by-side comparisons of the original and enhanced images, and users can download the enhanced image.

## Features

- **Color Channel Selection**: Choose between Red, Green, or Blue channels to target for enhancement.
- **Adjustable Luminance and Saturation**: Modify the luminance and saturation of the selected color channel.
- **Side-by-Side Comparison**: View the original and enhanced images side by side.
- **Download Enhanced Image**: Save the enhanced image to your local machine.

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/image-enhancement-hsv.git
    cd image-enhancement-hsv
    ```

2. **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Streamlit app:**
    ```bash
    streamlit run app.py
    ```

## Usage

1. **Upload an Image**: Use the file uploader in the sidebar to upload an image in JPG or PNG format.
2. **Select Color Channel**: Choose the color channel (Red, Green, or Blue) you want to enhance.
3. **Adjust Luminance and Saturation**: Use the sliders to adjust the luminance and saturation values for the selected color channel.
4. **View and Compare**: The original and enhanced images are displayed side by side for easy comparison.
5. **Download the Enhanced Image**: Click the "Download Enhanced Image" button to save the enhanced image.

## Dependencies

- Python 3.x
- Streamlit
- OpenCV
- NumPy
- Pillow
