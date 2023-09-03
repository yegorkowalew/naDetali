"""Copyright (c) 2023 Yegor Kowalew <kowalew.backup@gmail.com>"""

import os
import sys
import argparse
from settings import logger
from settings import model, description, flaw, dir_path, all_photos_dir_name
from settings import IMG_ORIGINAL_NAME, IMG_RESIZED_NAME, IMG_MAX_WIDTH
from setup_names import detail_names
from modules.helpers import repalce_for_name, mix_text, get_models_from_dir
from modules.exports import make_folder, files_generate, files_remove, get_html_text
from modules.xlsx_helpers import export_xlsx
from modules.images import move_images_in_dir, resize_images, flip_images


class ModelObj:
    """Основной класс деталей модели ноутбука"""
    def __init__(self, model_cfg, names_dict):
        self.vendor = model_cfg['vendor']
        self.model = model_cfg['model']
        self.keywords_string = model_cfg['keywords_string']
        self.state = model_cfg['state']
        self.names_dict = names_dict

        # Dirs
        # папка модели ноутбука
        self.model_dir = os.path.join(
            dir_path,
            self.vendor,
            f"{self.vendor} {self.model}",
        )
        # папка всех фотографий:
        self.all_photos_dir = os.path.join(
            self.model_dir,
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
                'dir_path': os.path.join(self.model_dir, repalce_for_name(item['name'])),

                "Название_Характеристики_1":item.get("Название_Характеристики_1"),
                "Название_Характеристики_2":item.get("Название_Характеристики_2"),
                "Название_Характеристики_3":item.get("Название_Характеристики_3"),
                "Название_Характеристики_4":item.get("Название_Характеристики_4"),
                "Название_Характеристики_5":item.get("Название_Характеристики_5"),
                "Название_Характеристики_6":item.get("Название_Характеристики_6"),
                "Название_Характеристики_7":item.get("Название_Характеристики_7"),
                "Название_Характеристики_8":item.get("Название_Характеристики_8"),
                "Название_Характеристики_9":item.get("Название_Характеристики_9"),
                "Название_Характеристики_10":item.get("Название_Характеристики_10"),
                "Значение_Характеристики_1":item.get("Значение_Характеристики_1"),
                "Значение_Характеристики_2":item.get("Значение_Характеристики_2"),
                "Значение_Характеристики_3":item.get("Значение_Характеристики_3"),
                "Значение_Характеристики_4":item.get("Значение_Характеристики_4"),
                "Значение_Характеристики_5":item.get("Значение_Характеристики_5"),
                "Значение_Характеристики_6":item.get("Значение_Характеристики_6"),
                "Значение_Характеристики_7":item.get("Значение_Характеристики_7"),
                "Значение_Характеристики_8":item.get("Значение_Характеристики_8"),
                "Значение_Характеристики_9":item.get("Значение_Характеристики_9"),
                "Значение_Характеристики_10":item.get("Значение_Характеристики_10"),

                'default_price':item.get("default_price"),

            }
            # хтмл текст для ексель таблиц
            data_list = item_dict
            item_dict["html_description_perfect"] = get_html_text('rus', 'perfect', data_list)
            item_dict["html_description_good"] = get_html_text('rus', 'good', data_list)
            item_dict["html_description_fail"] = get_html_text('rus', 'fail', data_list)
            item_dict["html_description_perfect_ua"] = get_html_text('ukr', 'perfect', data_list)
            item_dict["html_description_good_ua"] = get_html_text('ukr', 'good', data_list)
            item_dict["html_description_fail_ua"] = get_html_text('ukr', 'fail', data_list)
            global_list.append(item_dict)
        return global_list

    def create_files(self, file_type):
        """Создает файлы и папки"""
        names_list = self.get_names_list()
        make_folder(self.all_photos_dir)
        files_generate(names_list, file_type)

    def remove_files(self):
        """Удаляет пустые файлы и папки"""
        names_list = self.get_names_list()
        files_remove(names_list)

    def rotate_images(self):
        """Повернуть вертикальные изображения в папке на 90 градусов"""
        flip_images(self.all_photos_dir)

    def create_images(self):
        """Создать папки для изображений и переместить их туда"""
        data_list = get_models_from_dir(self)
        move_images_in_dir(data_list)
        for folder in data_list:
            in_dir = os.path.join(folder['dir_path'], IMG_ORIGINAL_NAME)
            out_dir = os.path.join(folder['dir_path'], IMG_RESIZED_NAME)
            resize_images(in_dir, out_dir, IMG_MAX_WIDTH)

    def create_xlsx_file(self):
        """Создать xlsx-файл для импорта"""
        export_xlsx(self)

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
                        help='Delete Files. Delete empty folders and files')
    parser.add_argument('-mi', action='store_true',
                        help='Make image files')
    parser.add_argument('-ri', action='store_true',
                        help='Rotate image files')
    parser.add_argument('-ex', action='store_true',
                        help='Make export file')

    args = parser.parse_args()

    model_obj = ModelObj(model, detail_names)
    if args.mf:
        logger.info('Создать папки и файлы с описаниями объявлений')
        model_obj.create_files('simple')
    elif args.tf:
        logger.info('Создать папки и файлы с описаниями объявлений')
        model_obj.create_files('text')
    elif args.df:
        logger.info('Удалить пустые папки с ненужными файлами описаний')
        model_obj.remove_files()
    elif args.mi:
        logger.info('Создать папки для изображений и переместить их туда')
        model_obj.create_images()
    elif args.ri:
        logger.info('Перевернуть вертикальные изображения в папке _All_Photos')
        model_obj.rotate_images()
    elif args.ex:
        logger.info('Создать xlsx-файл для импорта')
        model_obj.create_xlsx_file()
    else:
        parser.print_help(sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
