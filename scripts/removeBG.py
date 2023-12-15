import PIL
from rembg import remove

input_path = 'G:\\Meine Ablage\\Images\\Ball.png'
output_path = 'G:\\Meine Ablage\\Images\\Ball_noBG.png'

with open(input_path, 'rb') as i:
    with open(output_path, 'wb') as o:
        input = i.read()
        output = remove(input)
        o.write(output)