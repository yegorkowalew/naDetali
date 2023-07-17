import os, sys, shutil
import random
import argparse
from settings import logger
from settings import model, description, flaw, dir_path
from settings import template_dir
from setup_names import detail_names
from jinja2 import Environment, FileSystemLoader, select_autoescape


def repalce_for_name(str):
    return str.replace('<', ' ').replace('>', ' ').replace(':', ' ').replace('|', ' ').replace('\\', ' ').replace('/', ' ').replace('?', ' ').replace('*', ' ')

def toHtml(data_list, template_dir, template_name, html_file):
    file_loader = FileSystemLoader(template_dir)
    env = Environment(loader=file_loader)
    htmltemplate = env.get_template(template_name)
    htmltemplate.stream(
        data_list
        ).dump(html_file)
    logger.info('Сгенерирован текст.')
    return htmltemplate.render(
        data_list
        )

def make_folder(path):
    try:
        os.makedirs(path)
    except FileExistsError as error:
        logger.warning(error)

class ModelObj:
    def __init__(self, model, names_dict):
        self.vendor = model['vendor']
        self.model = model['model']
        self.keywords_string = model['keywords_string']
        self.state = model['state']
        self.names_dict = names_dict

    def get_random_sentence(self, text):
        # Получить рандомную комбинацию строк
        string_list = text.split('. ')
        random.shuffle(string_list)
        str = ''
        for i in string_list:
            str = str + i.replace('.', '')+'. '
        return str

    def get_names_list(self):
        # Получить список деталей
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
                'description_perfect': description['perfect'],
                'description_good': description['good'],
                'description_fail': description['fail'],
                "description_perfect_ua": description['perfect_ua'],
                "description_good_ua": description['good_ua'],
                "description_fail_ua": description['fail_ua'],
                "flaw_perfect": flaw['perfect'],
                "flaw_good": flaw['good'],
                "flaw_fail": flaw['fail'],
                "flaw_perfect_ua": flaw['perfect_ua'],
                "flaw_good_ua": flaw['good_ua'],
                "flaw_fail_ua": flaw['fail_ua'],
                'keywords':'русские теги',
                'keywords_ua':'украинские теги',
                'portal': item['portal'],
                'dir_path': os.path.join(os.path.dirname(dir_path), self.vendor, self.model, repalce_for_name(item['name'])),
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
            if '.jpg' in folder_file or '.jpeg' in folder_file or '.png' in folder_file:
                flag = False
                break
        if flag:
            logger.info("Удаляю папку %s", folder['dir_path'])
            shutil.rmtree(folder['dir_path'])
    return True

def make_files():
    """Make Files: создаем папки и файлы с описаниями объявлений"""
    logger.info('Начало')

    model_obj = ModelObj(model, detail_names)
    model_list = model_obj.get_names_list()
    make_folder(os.path.join(os.path.dirname(dir_path), model['vendor'], model['model'], '_All Photos'))
    
    for this_model in model_list:
        make_folder(this_model['dir_path'])
    
        data_list = {
            'model': this_model,
        }
        template_name_perfect = 'simple_tamplate_perfect.txt'
        template_name_good = 'simple_tamplate_good.txt'
        template_name_fail = 'simple_tamplate_fail.txt'
        
        file_path_perfect = os.path.join(os.path.dirname(this_model['dir_path']), repalce_for_name(this_model['name']), '1. Отличный - %s%s' % (repalce_for_name(this_model['name']), '.txt'))
        file_path_good = os.path.join(os.path.dirname(this_model['dir_path']), repalce_for_name(this_model['name']), '2. Нормальный - %s%s' % (repalce_for_name(this_model['name']), '.txt'))
        file_path_fail = os.path.join(os.path.dirname(this_model['dir_path']), repalce_for_name(this_model['name']), '3. Плохой - %s%s' % (repalce_for_name(this_model['name']), '.txt'))
    
        toHtml(data_list, template_dir, template_name_perfect, file_path_perfect)
        toHtml(data_list, template_dir, template_name_good, file_path_good)
        toHtml(data_list, template_dir, template_name_fail, file_path_fail)
    return True

def main():
    """Набор параметров для разветвления программы"""
    parser = argparse.ArgumentParser(
        description='Script for creating ads on the prom.ua',
        epilog='Created by Yegor Kowalew. Version 2.0 will be even better!'
        )
    parser.add_argument('-mf', action='store_true',
                        help='Make Files for model')
    parser.add_argument('-df', action='store_true',
                        help='Dlete Files. Delete empty folders and files')

    args = parser.parse_args()
    if args.mf:
        make_files()
    elif args.df:
        delete_folders()
    else:
        parser.print_help(sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    # Запуск основного тела программы
    main()
