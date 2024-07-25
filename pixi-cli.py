from PIL import Image, ImageEnhance, ImageOps, ImageFilter, ExifTags
import argparse

# Load image
def load_image(image_path):
    return Image.open(image_path)

# Save new image
def save_image(image, output_path):
    image.save(output_path)

# === IMAGE PROCESSING ===
# Crop image
def crop_image(image, left, top, right, bottom):
    return image.crop((left, top, right, bottom))

# Adjust exposure
def adjust_ev(image, factor):
    enhancer = ImageEnhance.Brightness(image)
    return enhancer.enhance(factor)

# Adjust saturation
def adjust_sat(image, factor):
    enhancer = ImageEnhance.Color(image)
    return enhancer.enhance(factor)

# Adjust contrast
def adjust_contrast(image, factor):
    enhancer = ImageEnhance.Contrast(image)
    return enhancer.enhance(factor)

# Adjust sharpness
def adjust_sharpness(image, factor):
    enhancer = ImageEnhance.Sharpness(image)
    return enhancer.enhance(factor)

# Blur image: box blur
def box_blur(image, radius):
    blurred_image = image.filter(ImageFilter.BoxBlur(radius))
    return blurred_image

# Blur image: Gaussian blue
def gaussian_blur(image, radius):
    blurred_image = image.filter(ImageFilter.GaussianBlur(radius))
    return blurred_image

# Convert to BW
def bw(image):
    black_and_white = image.convert("L")
    return black_and_white

# Invert colors
def invert(image):
    inverted = ImageOps.invert(image)
    return inverted

# === TOOLS ===
# Get image size
def get_image_size(image):
    return image.size

# Extract image metadata
# Get image metadata
def get_metadata(image):
    metadata = image._getexif()
    if metadata is not None:
        exif_data = {}
        relevant_tags = {
            271: "Make",
            272: "Model",
            305: "Software",
            306: "DateTime",
            33432: "Copyright",
            315: "Artist",
            37386: "FocalLength",
            33434: "ExposureTime",
            33437: "FNumber",
            34855: "ISOSpeedRatings",
            42036: "LensModel"
        }

        for tag, value in metadata.items():
            if tag in relevant_tags:
                tag_name = relevant_tags[tag]
                exif_data[tag_name] = value
        
        return exif_data
    else:
        return {}


# Rotate image 90 degrees
def rotate_90(image):
    rotated_image = image.transpose(Image.ROTATE_90)
    return rotated_image

# Rotate image 180 degrees
def rotate_180(image):
    rotated_image = image.transpose(Image.ROTATE_180)
    return rotated_image

# Rotate image 180 degrees
def rotate_270(image):
    rotated_image = image.transpose(Image.ROTATE_270)
    return rotated_image

# Flip image horizontally
def flip_horiz(image):
    flip_image = image.transpose(Image.FLIP_LEFT_RIGHT)
    return flip_image

# Flip image vertically
def flip_vert(image):
    flip_image = image.transpose(Image.FLIP_TOP_BOTTOM)
    return flip_image

def main():
    parser = argparse.ArgumentParser(description="pixi-cli")
    parser.add_argument("image_path", help="Path to the input image")
    parser.add_argument("--output_path", help="Path to save the processed image (optional if only checking size or fetching metadata)")
    parser.add_argument("--crop", nargs=4, type=int, metavar=('left', 'top', 'right', 'bottom'), help="Crop image")
    parser.add_argument("--exposure", type=float, help="Adjust exposure")
    parser.add_argument("--saturation", type=float, help="Adjust saturation")
    parser.add_argument("--contrast", type = float, help = "Adjust contrast")
    parser.add_argument("--sharpness", type = float, help = "Adjust sharpness")
    parser.add_argument("--box_blur", type = float, help = "Blur image (box blur)")
    parser.add_argument("--gaussian_blur", type = float, help = "Blur image (Gaussian blur)")
    parser.add_argument("--bw", action='store_true', help = "Convert to black and white")
    parser.add_argument("--invert", action='store_true', help = "Invert colors")
    parser.add_argument("--size", action='store_true', help="Get image size")
    parser.add_argument("--metadata", action='store_true', help="Get image metadata")
    parser.add_argument("--rotate90", action='store_true', help="Rotate image 90 degrees")
    parser.add_argument("--rotate180", action='store_true', help="Rotate image 180 degrees")
    parser.add_argument("--rotate270", action='store_true', help="Rotate image 270 degrees")
    parser.add_argument("--flip_horiz", action='store_true', help="Flip image horizontally")
    parser.add_argument("--flip_vert", action='store_true', help="Flip image vertically")
    args = parser.parse_args()

    image = load_image(args.image_path)

    if args.size:
        width, height = get_image_size(image)
        print(f"Image size: {width}x{height}")

    if args.metadata:
        metadata = get_metadata(image)
        for key, value in metadata.items():
            print(f"{key}: {value}")

    if args.crop or args.exposure or args.saturation or args.contrast or args.sharpness or args.box_blur or args.gaussian_blur or args.bw or args.invert or args.rotate90 or args.rotate180 or args.rotate270 or args.flip_horiz or args.flip_vert:
        if not args.output_path:
            parser.error("--output_path is required when performing image processing operations")
        
        if args.crop:
            image = crop_image(image, *args.crop)
        if args.exposure:
            image = adjust_ev(image, args.exposure)
        if args.saturation:
            image = adjust_sat(image, args.saturation)
        if args.contrast:
            image = adjust_contrast(image, args.contrast)
        if args.sharpness:
            image = adjust_sharpness(image, args.sharpness)
        if args.box_blur:
            image = box_blur(image, args.box_blur)
        if args.gaussian_blur:
            image = gaussian_blur(image, args.gaussian_blur)
        if args.bw:
            image = bw(image)
        if args.invert:
            image = invert(image)
        if args.rotate90:
            image = rotate_90(image)
        if args.rotate180:
            image = rotate_180(image)
        if args.rotate270:
            image = rotate_270(image)
        if args.flip_horiz:
            image = flip_horiz(image)
        if args.flip_vert:
            image = flip_vert(image)

        save_image(image, args.output_path)

if __name__ == "__main__":
    main()
