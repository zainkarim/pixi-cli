from PIL import Image, ImageEnhance, ImageOps
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

def main():
    parser = argparse.ArgumentParser(description="pixi-cli")
    parser.add_argument("image_path", help="Path to the input image")
    parser.add_argument("--output_path", help="Path to save the processed image (optional if only checking size)")
    parser.add_argument("--crop", nargs=4, type=int, metavar=('left', 'top', 'right', 'bottom'), help="Crop image")
    parser.add_argument("--exposure", type=float, help="Adjust exposure")
    parser.add_argument("--saturation", type=float, help="Adjust saturation")
    parser.add_argument("--bw", action='store_true', help = "Convert to black and white")
    parser.add_argument("--invert", action='store_true', help = "Invert colors")
    parser.add_argument("--size", action='store_true', help="Get image size")
    args = parser.parse_args()

    image = load_image(args.image_path)

    if args.size:
        width, height = get_image_size(image)
        print(f"Image size: {width}x{height}")

    if args.crop or args.exposure or args.saturation or args.bw or args.invert:
        if not args.output_path:
            parser.error("--output_path is required when performing image processing operations")
        
        if args.crop:
            image = crop_image(image, *args.crop)
        if args.exposure:
            image = adjust_ev(image, args.exposure)
        if args.saturation:
            image = adjust_sat(image, args.saturation)
        if args.bw:
            image = bw(image)
        if args.invert:
            image = invert(image)

        save_image(image, args.output_path)

if __name__ == "__main__":
    main()
