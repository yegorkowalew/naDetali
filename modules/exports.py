import os

from jinja2 import Environment, FileSystemLoader
from settings import logger

def to_html(data_list, template_dir, template_name, html_file):
    """Генерация текста"""
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
    """Cоздать папку"""
    try:
        os.makedirs(path)
    except FileExistsError as error:
        logger.warning(error)
