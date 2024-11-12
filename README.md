# Color Palette Generator

This project is a **Streamlit** web application that generates a color palette based on the dominant colors in an uploaded image. Using **KMeans clustering** to identify key colors, this app is ideal for designers, artists, and anyone who wants to extract color themes from images.

## Features

- **Upload an Image**: Supports JPG, JPEG, and PNG formats.
- **Extract Dominant Colors**: Uses KMeans clustering to identify the top 5 dominant colors.
- **Generate a Color Palette**: Displays a palette image with the extracted colors.

## How It Works

1. **Image Upload**: The user uploads an image through the Streamlit interface.
2. **Image Processing**: The image is loaded and reshaped to a 2D array.
3. **KMeans Clustering**: The app performs KMeans clustering to find the most dominant colors.
4. **Color Palette Creation**: A color palette image is generated and displayed, with each dominant color represented as a swatch.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/color-palette-generator.git
   cd color-palette-generator
   ```

2. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

## Dependencies

- `streamlit`: For building the web application.
- `numpy`: For data manipulation.
- `scikit-learn`: For KMeans clustering.
- `Pillow`: For image creation and manipulation.
- `matplotlib`: For image processing.

## Usage

1. Launch the app with `streamlit run app.py`.
2. Upload an image through the app interface.
3. The app will display the uploaded image and the generated color palette based on dominant colors.

## Code Explanation

- `create_color_palette(dominant_colors)`: Generates an image of the color palette based on the dominant colors extracted.
- `main()`: The main function that loads the Streamlit interface, processes the image, performs clustering, and displays the palette.


## Future Improvements

- Add functionality to allow users to select the number of colors.
- Provide options for different clustering algorithms.
- Allow download of the generated color palette.

## License

This project is open-source and available under the MIT License.
