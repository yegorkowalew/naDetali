"""Copyright (c) 2023 Yegor Kowalew <kowalew.backup@gmail.com>"""

import os
from jinja2 import Environment, FileSystemLoader
from progress.bar import ChargingBar
from settings import logger, template_dir
from modules.helpers import repalce_for_name

def to_html(data_list, templ_dir, templ_name, html_file):
    """Генерация текста"""
    file_loader = FileSystemLoader(templ_dir)
    env = Environment(loader=file_loader)
    htmltemplate = env.get_template(templ_name)
    htmltemplate.stream(
        data_list
        ).dump(html_file)
    logger.info('Сгенерирован текст.')
    return htmltemplate.render(
        data_list
        )

def make_folder(path):
    """Cоздать папку"""
    try:
        os.makedirs(path)
    except FileExistsError as error:
        logger.warning(error)

def files_generate(model_list):
    """Создает файлы експорта"""
    progress_bar = ChargingBar('Обработка:', max=len(model_list), suffix='%(index)d/%(max)d, %(elapsed)ds', color='green')
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
        progress_bar.next()
    progress_bar.finish()
