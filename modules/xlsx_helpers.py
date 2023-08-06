
from settings import logger
from setup_portal import portal_names
import pandas as pd
from setup_columns import db_columns

def get_portal_link(s):
    """Вместо текстового значения возвращает ссылку на портал"""
    for portal_item in portal_names:
        if portal_item['portal'] == s:
            return portal_item['portal_link']
    logger.warning("Не найдена ссылка для портала: %s", s)
    return None

def get_export_db(in_df):
    """Генерирует датафрейм для сохранения в файл експорта
    db_columns: имена столбцов датафрейма
    in_df: исходный датафрейм с данными
    """
    ex_df = pd.DataFrame(None, columns=db_columns)
    ex_df['Название_позиции'] = in_df['name']
    ex_df['Название_позиции_укр'] = in_df['name_ua']
    ex_df['Поисковые_запросы'] = in_df['keywords']
    ex_df['Поисковые_запросы_укр'] = in_df['keywords_ua']
    ex_df['Тип_товара'] = 'r'
    ex_df['Валюта'] = 'UAH'
    ex_df['Единица_измерения'] = 'шт.'
    ex_df['Наличие'] = '!'
    ex_df['Количество'] = '1'
    ex_df['Производитель'] = in_df['vendor']
    ex_df['Личные_заметки'] = "Y"
    ex_df['Цена_от'] = "-"
    ex_df['Где_находится_товар'] = "Полтава"
    ex_df['Адрес_подраздела'] = in_df['portal']
    # ex_df['Название_Характеристики'] = "Класс качества"
    # ex_df['Значение_Характеристики'] = "Original"

    # изменения в столбцах таблицы
    ex_df['Адрес_подраздела'] = ex_df['Адрес_подраздела'].apply(get_portal_link)
    return ex_df
