
# pixi-cli✨

pixi-cli is a command-line tool for image conversion and basic image processing tasks.

## Features

- Crop images
- Adjust exposure
- Adjust saturation
- Adjust contrast
- Adjust sharpness
- Apply box blur
- Apply Gaussian blur
- Reduce noise
- Detect edges
- Convert images to black and white
- Invert colors
- Rotate images (90, 180, 270 degrees)
- Flip images (horizontally and vertically)
- Create thumbnails
- Compress images
- Get image size
- Fetch image metadata
- Convert between image formats (e.g., jpg, png, bmp, gif, tiff, svg)

## Installation
You can either download Pixi-CLI through PyPI (recommended, requires Python to be installed on your machine) or you can download the executable (more steps, does not requires Python to be installed on your machine)

### Installing via PyPI

1. Ensure you have Python and pip installed on your machine.
2. Install pixi-cli using pip:
```sh
pip install pixi-cli
```

### Downloading the Executable

Download the executable from the latest release of `pixi` from the [Releases](https://github.com/zainkarim/pixi-cli/releases) page and run it directly. If you’re familiar with modifying your PATH, you can add the executable to your PATH to run it from any directory.

## Usage

### Basic Usage

1. Open a terminal or Command Prompt.
2. Use the command line to perform various image processing tasks.

### Examples

1. **Get Image Size:**
   ```sh
   pixi /path/to/input.jpg --size
   ```

2. **Get Image Metadata:**
   ```sh
   pixi  /path/to/input.jpg --metadata
   ```

3. **Crop Image:**
   ```sh
   pixi /path/to/input.jpg --output_path /path/to/output.jpg --crop 50 50 200 200
   ```

4. **Adjust Exposure:**
   ```sh
   pixi /path/to/input.jpg --output_path /path/to/output.jpg --exposure 1.2
   ```

5. **Apply Gaussian Blur:**
   ```sh
   pixi /path/to/input.jpg --output_path /path/to/output.jpg --gaussian_blur 2.0
   ```

6. **Convert to Black and White:**
   ```sh
   pixi /path/to/input.jpg --output_path /path/to/output.jpg --bw
   ```

7. **Rotate Image 90 Degrees:**
   ```sh
   pixi /path/to/input.jpg --output_path /path/to/output.jpg --rotate90
   ```

8. **Convert Image Format:**
   ```sh
   pixi /path/to/input.jpg --convert png
   ```

### Full Command-Line Arguments

- `image_path`: Path to the input image (required).
- `--output_path`: Path to save the processed image (required for processing operations).
- `--crop left top right bottom`: Crop the image to the specified box.
- `--exposure factor`: Adjust the exposure by the given factor.
- `--saturation factor`: Adjust the saturation by the given factor.
- `--contrast factor`: Adjust the contrast by the given factor.
- `--sharpness factor`: Adjust the sharpness by the given factor.
- `--box_blur radius`: Apply box blur with the specified radius.
- `--gaussian_blur radius`: Apply Gaussian blur with the specified radius.
- `--reduce_noise`: Reduce noise in the image.
- `--edge_detect`: Detect edges in the image
- `--bw`: Convert the image to black and white.
- `--invert`: Invert the colors of the image.
- `--thumbnail width height`: Create a thumbnail of the specified size.
- `--compression quality`: Compress the image to the specified quality (0-100).
- `--size`: Get the size of the image.
- `--metadata`: Fetch the metadata of the image.
- `--rotate90`: Rotate the image 90 degrees clockwise.
- `--rotate180`: Rotate the image 180 degrees.
- `--rotate270`: Rotate the image 270 degrees clockwise.
- `--flip_horiz`: Flip the image horizontally.
- `--flip_vert`: Flip the image vertically.
- `--convert format`: Convert the image to the specified format.

## Contributing

Contributions are welcome! Please fork the repository and submit pull requests.

## License

This project is licensed under the MIT License.
