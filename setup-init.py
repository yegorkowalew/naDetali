# Название детали
detail_name = "HP DescTest Pro NAH-7350"

# Теги детали
detail_tag_string = "HP DescTest Pro, HP, DescJetTest Pro, HP DescJetTest Pro NAH-7350, NAH-7350"

# Дополнительные теги рус
detail_tag_string_rus = "ноутбук, запчасть, деталь"

# Дополнительные теги укр
detail_tag_string_ukr = "ноутбук, запчастина, деталь"

# деталь аналоги
detail_analog_tag_string = "NAH-7350h, NAH-7350a, NAH-7355u"

# Состояние ноутбука, принимает три состояния: 
# "Б/У" - бывший в употреблении 
# "Новый" - новый
# "Н" - состояние не указывается
detail_state = "Б/У"

def get_global_tag_string_rus(detail_name, detail_tag_string, detail_tag_string_rus, detail_analog_tag_string):
    tag_string = ""
    for tag in detail_tag_string.split(', ') + detail_tag_string_rus.split(', ') + detail_analog_tag_string.split(', '):
        tag_string += tag + ', '
    tag_string += detail_name
    return tag_string

def get_detail_state_rus(detail_state):
    if detail_state == "Б/У":
        return "Б/У"
    if detail_state == "Новый":
        return "Новый"
    if detail_state == "Н":
        return ""
    return ""

def get_detail_state_ukr(detail_state):
    if detail_state == "Б/У":
        return "Б/В"
    if detail_state == "Новый":
        return "Новий"
    if detail_state == "Н":
        return ""
    return ""

print(get_global_tag_string_rus(detail_name, detail_tag_string, detail_tag_string_rus, detail_analog_tag_string))
print(get_detail_state_rus(detail_state))
print(get_detail_state_ukr(detail_state))