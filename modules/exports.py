"""Copyright (c) 2023 Yegor Kowalew <kowalew.backup@gmail.com>"""

import os
import shutil
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

def files_generate(model_list, files_type):
    """Создает файлы експорта"""
    progress_bar = ChargingBar(
        'Обработка:',
        max=len(model_list),
        suffix='%(index)d/%(max)d, %(elapsed)ds',
        color='green'
    )
    if files_type == 'simple':
        template_name_perfect = 'simple_tamplate_perfect.txt'
        template_name_good = 'simple_tamplate_good.txt'
        template_name_fail = 'simple_tamplate_fail.txt'
    else:
        template_name_perfect = 'text_simple_tamplate_perfect.txt'
        template_name_good = 'text_simple_tamplate_good.txt'
        template_name_fail = 'text_simple_tamplate_fail.txt'

    for this_model in model_list:
        make_folder(this_model['dir_path'])

        data_list = {
            'model': this_model,
        }
        file_path_perfect = os.path.join(
            this_model['dir_path'],
            f"1. Отличный - {files_type} - {repalce_for_name(this_model['name'])}.txt"
            )
        file_path_good = os.path.join(
            this_model['dir_path'],
            f"2. Нормальный - {files_type} - {repalce_for_name(this_model['name'])}.txt"
            )
        file_path_fail = os.path.join(
            this_model['dir_path'],
            f"3. Плохой - {files_type} - {repalce_for_name(this_model['name'])}.txt"
            )

        to_html(data_list, template_dir, template_name_perfect, file_path_perfect)
        to_html(data_list, template_dir, template_name_good, file_path_good)
        to_html(data_list, template_dir, template_name_fail, file_path_fail)
        progress_bar.next()
    progress_bar.finish()

def files_remove(model_list):
    progress_bar = ChargingBar(
        'Обработка:',
        max=len(model_list),
        suffix='%(index)d/%(max)d, %(elapsed)ds',
        color='green'
    )
    for folder in model_list:
        flag = True
        for folder_file in os.listdir(folder['dir_path']):
            if '.jpg' in folder_file or '.jpeg' in folder_file or '.png' in folder_file or '.webp' in folder_file:
                flag = False
                break
        if flag:
            logger.info("Удаляю папку %s", folder['dir_path'])
            shutil.rmtree(folder['dir_path'])
        progress_bar.next()
    progress_bar.finish()

def get_html_text(lang, state, data_list):
    templ_dir = 'templates'
    file_loader = FileSystemLoader(templ_dir)
    env = Environment(loader=file_loader)
    if lang == 'rus':
        if state == 'perfect':
            htmltemplate = env.get_template("html_template_ru.html")
            data_list['state'] = 'perfect'
            html_template_string = htmltemplate.render(data_list)
            return html_template_string
        elif state == 'good':
            htmltemplate = env.get_template("html_template_ru.html")
            data_list['state'] = 'good'
            html_template_string = htmltemplate.render(data_list)
            return html_template_string
        elif state == 'fail':
            htmltemplate = env.get_template("html_template_ru.html")
            data_list['state'] = 'fail'
            html_template_string = htmltemplate.render(data_list)
            return html_template_string
    if lang == 'ukr':
        if state == 'perfect':
            htmltemplate = env.get_template("html_template_ua.html")
            data_list['state'] = 'perfect'
            html_template_string = htmltemplate.render(data_list)
            return html_template_string
        elif state == 'good':
            htmltemplate = env.get_template("html_template_ua.html")
            data_list['state'] = 'good'
            html_template_string = htmltemplate.render(data_list)
            return html_template_string
        elif state == 'fail':
            htmltemplate = env.get_template("html_template_ua.html")
            data_list['state'] = 'fail'
            html_template_string = htmltemplate.render(data_list)
            return html_template_string
    return None
