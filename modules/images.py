import os, shutil
from .exports import make_folder
from PIL import Image, ImageFilter
from settings import logger
from progress.bar import ChargingBar

def flip_images(dir):
    """Повернуть изображение чтоб оно было горизонтальным"""
    bar = ChargingBar('Обработка:', max=len(os.listdir(dir)), suffix='%(index)d/%(max)d, %(elapsed)ds', color='green')
    for folder_file in os.listdir(dir):
        filename = os.path.join(dir, folder_file)
        with Image.open(filename) as img:
            img.load()
        if isinstance(img, Image.Image):
            if img.size[0]<img.size[1]:
                converted_img = img.transpose(Image.ROTATE_90)
                converted_img.save(filename)
        bar.next()
    bar.finish()

def move_images_in_dir(model_list):
    """Из папки модели переместить фотографии в подпапку с оригиналами фотографий"""
    for folder in model_list:
        destination_folder = os.path.join(folder['dir_path'], '_Photos_Original')
        make_folder(destination_folder)
        for folder_file in os.listdir(folder['dir_path']):
            if '.jpg' in folder_file or '.jpeg' in folder_file or '.png' in folder_file or '.webp' in folder_file:
                shutil.move(os.path.join(folder['dir_path'], folder_file), destination_folder)

def resize_images(dir, dir_destination, new_width):
    """В папке с изображениями поменять размер каждого изображения
    и переместить в папку назначения"""
    last_folder = dir_destination.split("\\")[-2]
    logger.info('Ресайз и перемещение фотографий в папке: %s', f'{last_folder}')
    make_folder(dir_destination)
    bar = ChargingBar('Обработка:', max=len(os.listdir(dir)), suffix='%(index)d/%(max)d, %(elapsed)ds', color='green')
    for folder_file in os.listdir(dir):
        filename = os.path.join(dir, folder_file)
        with Image.open(filename) as img:
            img.load()
        if isinstance(img, Image.Image):
            img = Image.open(filename)
            width, height = img.size
            new_height = int(new_width * height / width)
            img = img.resize((new_width, new_height), Image.LANCZOS)
            img = img.filter(ImageFilter.SHARPEN)
            img.save(os.path.join(dir_destination, folder_file))
        bar.next()
    bar.finish()
