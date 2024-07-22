from PIL import Image, ImageEnhance
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

def main():
    parser = argparse.ArgumentParser(description="pixi-cli")
    parser.add_argument("image_path", help="Path to the input image")
    parser.add_argument("output_path", help="Path to save the processed image")
    parser.add_argument("--crop", nargs=4, type=int, metavar=('left', 'top', 'right', 'bottom'), help="Crop image")
    parser.add_argument("--exposure", type=float, help="Adjust exposure")
    parser.add_argument("--saturation", type=float, help="Adjust saturation")
    args = parser.parse_args()

    image = load_image(args.image_path)

    if args.crop:
        image = crop_image(image, *args.crop)
    if args.exposure:
        image = adjust_ev(image, args.exposure)
    if args.saturation:
        image = adjust_sat(image, args.saturation)

    save_image(image, args.output_path)

if __name__ == "__main__":
    main()