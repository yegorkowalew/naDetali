import os, random
from settings import logger
from progress.spinner import MoonSpinner

def repalce_for_name(str):
    """Удалить из строки лишние символы, чтоб можно было создать файл"""
    return str.replace('<', ' ').replace('>', ' ').replace(':', ' ').replace('|', ' ').replace('\\', ' ').replace('/', ' ').replace('?', ' ').replace('*', ' ')

def mix_text(tags, names):
    """К каждому тегу добавить название модели"""
    return_text = ''
    spinner = MoonSpinner('Генерирую теги ')
    for tag in tags.split(', '):
        for name in names.split(', '):
            if len(f"{return_text} {tag} {name},") > 1024:
                logger.info('Сокращен текст keywords для: %s', tags)
                return return_text.replace(',,', ',').replace(',  ', ', ')
            else:
                return_text = f"{return_text} {tag} {name},"
            spinner.next()
    return return_text.replace(',,', ',').replace(',  ', ', ')

def get_random_sentence(self, text):
    """Получить рандомную комбинацию строк"""
    string_list = text.split('. ')
    random.shuffle(string_list)
    str = ''
    for i in string_list:
        str = str + i.replace('.', '')+'. '
    return str

def get_models_from_dir(model_obj):
    """Возвращает список объектов модели, которые есть в папке проекта"""
    model_list = model_obj.get_names_list()
    data_list = []
    for item in model_list:
        if os.path.exists(item['dir_path']):
            data_list.append(item)
    logger.info('Деталей в папке: %s', len(data_list))
    return data_list
