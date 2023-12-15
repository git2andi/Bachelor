from PIL import Image

def resize_image(input_path, output_path):
    # Open the image file
    with Image.open(input_path) as img:
        # Calculate the new width maintaining the aspect ratio
        aspect_ratio = img.size[0] / img.size[1]
        new_width = int(1024 * aspect_ratio)

        # Resize the image
        img = img.resize((new_width, 1024), Image.Resampling.LANCZOS)

        # Save the resized image
        img.save(output_path)

input_image = 'C:\\Users\\Andi\\Desktop\\Bachelor\\etc\\a high quality rendering of a playmobil firefighter\\fantasia3d_Magic3DInput\\fantasia_playmobil_result.png'
output_image = 'C:\\Users\\Andi\\Desktop\\Bachelor\\etc\\a high quality rendering of a playmobil firefighter\\fantasia3d_Magic3DInput\\fantasia_playmobil_result_resize.png'
resize_image(input_image, output_image)
