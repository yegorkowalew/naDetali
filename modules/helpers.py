import random

def repalce_for_name(str):
    """Удалить из строки лишние символы, чтоб можно было создать файл"""
    return str.replace('<', ' ').replace('>', ' ').replace(':', ' ').replace('|', ' ').replace('\\', ' ').replace('/', ' ').replace('?', ' ').replace('*', ' ')

def mix_text(tags, names):
    """К каждому тегу добавить название модели"""
    return_text = ''
    for tag in tags.split(', '):
        for name in names.split(', '):
            return_text = f"{return_text} {tag} {name},"
    return return_text.replace(',,', ',').replace(',  ', ', ')

def get_random_sentence(self, text):
    """Получить рандомную комбинацию строк"""
    string_list = text.split('. ')
    random.shuffle(string_list)
    str = ''
    for i in string_list:
        str = str + i.replace('.', '')+'. '
    return str