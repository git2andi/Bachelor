import argparse
from PIL import Image

def split_image(image_path):
    # Open the image
    with Image.open(image_path) as img:
        width, height = img.size

        # Ensure the image has the correct dimensions
        if width != 4096 or height != 1024:
            raise ValueError("Image dimensions must be 4096x1024")

        # Split the image into four parts
        parts = []
        for i in range(4):
            left = i * 1024
            right = left + 1024
            part = img.crop((left, 0, right, height))
            parts.append(part)

        # Save each part
        for i, part in enumerate(parts, start=1):
            # Construct the new file name
            new_file_name = f"{image_path.rsplit('.', 1)[0]}_part{i}.png"
            part.save(new_file_name)
            print(f"Saved: {new_file_name}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Split an image into four parts.')
    parser.add_argument('--image', type=str, required=True, help='Path to the image file')
    
    args = parser.parse_args()
    split_image(args.image)
