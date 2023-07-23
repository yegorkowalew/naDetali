
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
