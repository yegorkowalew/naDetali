import os
from PIL import Image

def flip_images(dir):
    """Повернуть изображение чтоб оно было горизонтальным"""
    for folder_file in os.listdir(dir):
        if '.jpg' in folder_file or '.jpeg' in folder_file or '.png' in folder_file or '.webp' in folder_file:
            filename = os.path.join(dir, folder_file)
            with Image.open(filename) as img:
                img.load()
            if isinstance(img, Image.Image):
                if img.size[0]<img.size[1]:
                    converted_img = img.transpose(Image.ROTATE_90) 
                    converted_img.save(filename)

# ddir = "c:\\work\\naDetali\\test\\Fujitsu Siemens\\Fujitsu Siemens Esprimo Mobile V5535\\Оптический привод DVD-RW Fujitsu Siemens Esprimo Mobile V5535 SATA\\_Photos_Original"
# flip_images(ddir)