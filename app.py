import streamlit as st
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
from PIL import Image, ImageDraw

def create_color_palette(dominant_colors, palette_size=(300, 50)):
    # Create an image to display the colors
    palette = Image.new("RGB", palette_size)
    draw = ImageDraw.Draw(palette)

    # Calculate the width of each color swatch
    swatch_width = palette_size[0] // len(dominant_colors)

    # Draw each color as a rectangle on the palette
    for i, color in enumerate(dominant_colors):
        draw.rectangle([i * swatch_width, 0, (i + 1) * swatch_width, palette_size[1]], fill=tuple(color))

    return palette

def main():
    st.title("Color Palette Generator")

    # Upload image through Streamlit
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Display the uploaded image
        image = mpimg.imread(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        # Reshape the image
        X = image.reshape(-1, 3)

        # Perform KMeans clustering
        kmeans = KMeans(n_clusters=5)
        kmeans.fit(X)

        # Generate and display color palette
        st.subheader("Generated Color Palette:")
        color_palette = create_color_palette(kmeans.cluster_centers_.astype(int))
        st.image(color_palette, use_column_width=True, caption="Color Palette")
        
if __name__ == "__main__":
    main()

