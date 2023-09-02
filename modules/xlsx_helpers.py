import os
from datetime import datetime
from random import random
import pandas as pd
from modules.exports import make_folder
from settings import logger
from settings import XLSX_DIR_NAME
from setup_portal import portal_names
from setup_columns import db_columns

def get_portal_link(s):
    """Вместо текстового значения возвращает ссылку на портал"""
    for portal_item in portal_names:
        if portal_item['portal'] == s:
            return portal_item['portal_link']
    logger.warning("Не найдена ссылка для портала: %s", s)
    return None

def get_description(path):
    """Получить цифру качества из пути к каталогу детали"""
    if os.path.exists(path):
        return os.listdir(path)[0].split('.')[0]
    return None

def get_html_description_rus(row):
    """Получить цифру качества из пути к каталогу детали"""
    if row['Описание'] == '1':
        return row['html_description_perfect']
    elif row['Описание'] == '2':
        return row['html_description_good']
    elif row['Описание'] == '3':
        return row['html_description_fail']
    return row['Описание']

def get_html_description_ukr(row):
    """Получить цифру качества из пути к каталогу детали"""
    if row['Описание_укр'] == '1':
        return row['html_description_perfect_ua']
    elif row['Описание_укр'] == '2':
        return row['html_description_good_ua']
    elif row['Описание_укр'] == '3':
        return row['html_description_fail_ua']
    return row['Описание_укр']

def get_time_rand_string(e):
    """Генерация уникального ключа из даты и рандомного числа"""
    this_datetime = datetime.now()
    str_date_time = f'{this_datetime.strftime("%d%m%Y%H%M%S.%f")}.{str(random())}'
    return str_date_time

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
    ex_df['Описание'] = in_df['dir_path']
    ex_df['Описание_укр'] = in_df['dir_path']
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
    ex_df['html_description_perfect'] = in_df['html_description_perfect']
    ex_df['html_description_good'] = in_df['html_description_good']
    ex_df['html_description_fail'] = in_df['html_description_fail']
    ex_df['html_description_perfect_ua'] = in_df['html_description_perfect_ua']
    ex_df['html_description_good_ua'] = in_df['html_description_good_ua']
    ex_df['html_description_fail_ua'] = in_df['html_description_fail_ua']
    # генерация поля Уникальный_идентификатор
    ex_df['Идентификатор_товара'] = ex_df['Идентификатор_товара'].apply(get_time_rand_string)
    # изменения в столбцах таблицы
    ex_df['Адрес_подраздела'] = ex_df['Адрес_подраздела'].apply(get_portal_link)
    # Генерация описания
    ex_df['Описание'] = ex_df['Описание'].apply(get_description)
    ex_df['Описание_укр'] = ex_df['Описание_укр'].apply(get_description)
    ex_df['Описание'] = ex_df.apply(get_html_description_rus, axis=1)
    ex_df['Описание_укр'] = ex_df.apply(get_html_description_ukr, axis=1)
    ex_df.drop(columns=['html_description_perfect', 'html_description_good',
    'html_description_fail', 'html_description_perfect_ua',
    'html_description_good_ua', 'html_description_fail_ua'], axis=1, inplace=True)
    return ex_df

def export_xlsx(model_obj):
    """Експорт в xlsx"""
    model_list = model_obj.get_names_list()
    data_list = []
    for item in model_list:
        if os.path.exists(item['dir_path']):
            data_list.append(item)

    in_df = pd.DataFrame.from_dict(data_list)
    export_path = os.path.join(
            model_obj.model_dir,
            XLSX_DIR_NAME)

    make_folder(export_path)

    ex_df = get_export_db(in_df)
    this_datetime = datetime.now()
    vendor_repl = model_obj.vendor.replace(' ', '_')
    model_repl = model_obj.model.replace(' ', '_')
    file_name_date = this_datetime.strftime('%d_%m_%Y_%H_%M')
    ex_df.to_excel(
        os.path.join(export_path,
        f"{vendor_repl}_{model_repl}_{file_name_date}.xlsx"),
        index= False,
        sheet_name= "Export Products Sheet")
