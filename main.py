import os, sys, shutil
import argparse
from settings import logger
from settings import model, description, flaw, dir_path, all_photos_dir_name
from settings import template_dir
from settings import IMG_ORIGINAL_NAME, IMG_RESIZED_NAME, IMG_MAX_WIDTH
from setup_names import detail_names
from modules.helpers import repalce_for_name, mix_text, get_models_from_dir
from modules.exports import to_html, make_folder
from modules.xlsx_helpers import get_export_db
from modules.images import move_images_in_dir, resize_images, flip_images
from progress.bar import ChargingBar

class ModelObj:
    def __init__(self, model, names_dict):
        self.vendor = model['vendor']
        self.model = model['model']
        self.keywords_string = model['keywords_string']
        self.state = model['state']
        self.names_dict = names_dict

        # Dirs
        # папка всех фотографий:
        self.all_photos_dir = os.path.join(
            dir_path,
            self.vendor,
            f"{self.vendor} {self.model}",
            all_photos_dir_name
        )

    def get_names_list(self):
        """Получить список деталей"""
        global_list = []
        for item in self.names_dict:
            item_dict = {
                'vendor': self.vendor,
                'model': self.model,
                'model_name': f"{self.vendor} {self.model}",
                'name': item['name'],
                'name_ua': item['name_ua'],
                'description_small': item['description_small'],
                'description_small_ua': item['description_small_ua'],
                'description_perfect': f"{description['perfect']} {item['description_perfect']}",
                'description_good': f"{description['good']} {item['description_good']}",
                'description_fail': f"{description['fail']} {item['description_fail']}",
                "description_perfect_ua": f"{description['perfect_ua']} {item['description_perfect_ua']}",
                "description_good_ua": f"{description['good_ua']} {item['description_good_ua']}",
                "description_fail_ua": f"{description['fail_ua']} {item['description_fail_ua']}",
                "flaw_perfect": f"{item['flaw_perfect']} {flaw['perfect']}",
                "flaw_good": f"{item['flaw_good']} {flaw['good']}",
                "flaw_fail": f"{item['flaw_fail']} {flaw['fail']}",
                "flaw_perfect_ua": f"{item['flaw_perfect_ua']} {flaw['perfect_ua']}",
                "flaw_good_ua": f"{item['flaw_good_ua']} {flaw['good_ua']}",
                "flaw_fail_ua": f"{item['flaw_fail_ua']} {flaw['fail_ua']}",
                'keywords': mix_text(item['keywords'], model['keywords_string']),
                'keywords_ua':mix_text(item['keywords_ua'], model['keywords_string']),
                'portal': item['portal'],
                'dir_path': os.path.join(
                    os.path.dirname(dir_path),
                    self.vendor,
                    f"{self.vendor} {self.model}",
                    repalce_for_name(item['name'])),
            }
            global_list.append(item_dict)
        return global_list

def delete_folders():
    """Delete Folders: Удаляем пустые папки с ненужными файлами описаний"""
    model_obj = ModelObj(model, detail_names)
    model_list = model_obj.get_names_list()
    for folder in model_list:
        flag = True
        for folder_file in os.listdir(folder['dir_path']):
            if '.jpg' in folder_file or '.jpeg' in folder_file or '.png' in folder_file or '.webp' in folder_file:
                flag = False
                break
        if flag:
            logger.info("Удаляю папку %s", folder['dir_path'])
            shutil.rmtree(folder['dir_path'])
    return True

def make_images():
    data_list = get_models_from_dir(ModelObj(model, detail_names))
    move_images_in_dir(data_list)
    for folder in data_list:
        in_dir = os.path.join(folder['dir_path'], IMG_ORIGINAL_NAME)
        out_dir = os.path.join(folder['dir_path'], IMG_RESIZED_NAME)
        resize_images(in_dir, out_dir, IMG_MAX_WIDTH)

def rotate_images():
    """Перевернуть вертикальные изображения в папке _All_Photos"""
    logger.info('Перевернуть вертикальные изображения в папке _All_Photos')
    model_obj = ModelObj(model, detail_names)
    flip_images(model_obj.all_photos_dir)

def make_files():
    """Make Files: создаем папки и файлы с описаниями объявлений"""
    logger.info('Создать папки и файлы с описаниями объявлений')

    model_obj = ModelObj(model, detail_names)
    model_list = model_obj.get_names_list()
    make_folder( 
        # ! Поменять на all_photos_dir
        os.path.join(
            os.path.dirname(dir_path),
            model['vendor'],
            f"{model['vendor']} {model['model']}",
            '_All Photos')
            )
    bar = ChargingBar('Обработка:', max=len(model_list), suffix='%(index)d/%(max)d, %(elapsed)ds')
    for this_model in model_list:
        make_folder(this_model['dir_path'])
    
        data_list = {
            'model': this_model,
        }
        template_name_perfect = 'simple_tamplate_perfect.txt'
        template_name_good = 'simple_tamplate_good.txt'
        template_name_fail = 'simple_tamplate_fail.txt'

        file_path_perfect = os.path.join(
            this_model['dir_path'],
            f"1. Отличный - {repalce_for_name(this_model['name'])}.txt"
            )
        file_path_good = os.path.join(
            this_model['dir_path'],
            f"2. Нормальный - {repalce_for_name(this_model['name'])}.txt"
            )
        file_path_fail = os.path.join(
            this_model['dir_path'],
            f"3. Плохой - {repalce_for_name(this_model['name'])}.txt"
            )
        
        to_html(data_list, template_dir, template_name_perfect, file_path_perfect)
        to_html(data_list, template_dir, template_name_good, file_path_good)
        to_html(data_list, template_dir, template_name_fail, file_path_fail)
        bar.next()
    bar.finish()
    return True

def make_small_files():
    """Make Files: создаем папки и файлы с описаниями объявлений"""
    logger.info('Начало')

    model_obj = ModelObj(model, detail_names)
    model_list = model_obj.get_names_list()
    make_folder(
        # ! Поменять на all_photos_dir
        os.path.join(
            os.path.dirname(dir_path),
            model['vendor'],
            model['model'],
            '_All Photos')
            )

    for this_model in model_list:
        data_list = {
            'model': this_model,
        }

        make_folder(this_model['dir_path'])
        template_name_perfect = 'text_simple_tamplate_perfect.txt'
        template_name_good = 'text_simple_tamplate_good.txt'
        template_name_fail = 'text_simple_tamplate_fail.txt'

        file_path_perfect = os.path.join(
            this_model['dir_path'],
            f"1. Отличный - {repalce_for_name(this_model['name'])}.txt"
            )
        file_path_good = os.path.join(
            this_model['dir_path'],
            f"2. Нормальный - {repalce_for_name(this_model['name'])}.txt"
            )
        file_path_fail = os.path.join(
            this_model['dir_path'],
            f"2. Плохой - {repalce_for_name(this_model['name'])}.txt"
            )
        
        to_html(data_list, template_dir, template_name_perfect, file_path_perfect)
        to_html(data_list, template_dir, template_name_good, file_path_good)
        to_html(data_list, template_dir, template_name_fail, file_path_fail)
    return True

def export_xlsx():
    """Експорт в xlsx"""
    import pandas as pd
    model_obj = ModelObj(model, detail_names)
    model_list = model_obj.get_names_list()
    data_list = []
    for item in model_list:
        if os.path.exists(item['dir_path']):
            data_list.append(item)

    in_df = pd.DataFrame.from_dict(data_list)
    export_path = os.path.join(
            os.path.dirname(dir_path),
            model['vendor'],
            model['model'],
            '_Export')

    make_folder(export_path)

    ex_df = get_export_db(in_df)
    ex_df.to_excel(
        os.path.join(export_path,
        f"{model['vendor']} {model['model']} export.xlsx"),
        index= False,
        sheet_name= "Export Products Sheet")

def main():
    """Набор параметров для разветвления программы"""
    parser = argparse.ArgumentParser(
        description='Script for creating ads on the prom.ua',
        epilog='Created by Yegor Kowalew. Version 2.0 will be even better!'
        )
    parser.add_argument('-mf', action='store_true',
                        help='Make Files for model')
    parser.add_argument('-tf', action='store_true',
                        help='Make small text Files for model')
    parser.add_argument('-df', action='store_true',
                        help='Dlete Files. Delete empty folders and files')
    parser.add_argument('-mi', action='store_true',
                        help='Make image files')
    parser.add_argument('-ri', action='store_true',
                        help='Rotate image files')
    parser.add_argument('-ex', action='store_true',
                        help='Make export file')

    args = parser.parse_args()
    if args.mf:
        make_files()
    elif args.tf:
        make_small_files()
    elif args.df:
        delete_folders()
    elif args.mi:
        make_images()
    elif args.ri:
        rotate_images()
    elif args.ex:
        export_xlsx()
    else:
        parser.print_help(sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    """Запуск основного тела программы"""
    main()
