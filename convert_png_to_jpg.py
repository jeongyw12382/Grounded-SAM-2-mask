import os
import argparse
from PIL import Image

def convert_png_to_jpg(input_dir, output_dir):
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Loop through all files in the input directory
    for filename in os.listdir(input_dir):
        if filename.endswith(".png"):
            # Full path for the input PNG image
            png_image_path = os.path.join(input_dir, filename)
            
            # Check if the filename starts with 'rgba_' and remove that part
            if filename.startswith("rgba_"):
                base_name = filename.replace("rgba_", "").replace(".png", "")  # Remove rgba_ and .png
                jpg_filename = f"{base_name}.jpg"  # New filename in JPG format
            else:
                base_name = os.path.splitext(filename)[0]  # Remove extension if not in rgba_ format
                jpg_filename = f"{base_name}.jpg"

            # Full path for the output JPG image
            jpg_image_path = os.path.join(output_dir, jpg_filename)

            # Open the PNG image
            img = Image.open(png_image_path)

            # Convert to RGB mode (because PNG can have transparency/alpha channel)
            img = img.convert('RGB')

            # Save the image as JPG
            img.save(jpg_image_path, "JPEG")
            print(f"Converted {filename} to {jpg_filename}")


if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Convert PNG images to JPG format.")
    parser.add_argument("--input_dir", help="Directory containing PNG images.")
    parser.add_argument("--output_dir", help="Directory to save JPG images.")
    
    args = parser.parse_args()

    # Convert images
    convert_png_to_jpg(args.input_dir, args.output_dir)
