# -*- coding: utf-8 -*-

from datetime import date
import os
import logging
import configparser  # импортируем библиотеку


# Сегодняшняя дата
TODAY = date.today()

# Путь к папке скрипта, корневая директория скрипта
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Путь к log-файлу
LOG_FILE = os.path.join(BASE_DIR, 'logs', '%s%s%s' % ('log - ', TODAY.strftime('%d.%m.%Y'), '.txt'))

# Путь к папке c конфигурационными файлами
config = configparser.ConfigParser()

# model.ini
config.read(os.path.join(BASE_DIR, 'model.ini'), encoding="utf-8")  # читаем конфиг
brand_name = config["Model"]["brand"]
model_name = config["Model"]["name"]
model_tag_string = config["Model"]["tag_string"]
model_tag_string_rus = config["Model"]["tag_string_rus"]
model_tag_string_ukr = config["Model"]["tag_string_ukr"]
model_state = config["Model"]["state"]
dir_path = config["Path"]["directory"]

# description.ini
config.read(os.path.join(BASE_DIR, 'description.ini'), encoding="utf-8")  # читаем конфиг
description_perfect_rus = config["Description"]["perfect_rus"]
description_perfect_ukr = config["Description"]["perfect_ukr"]
description_good_rus = config["Description"]["good_rus"]
description_good_ukr = config["Description"]["good_ukr"]
description_fail_rus = config["Description"]["fail_rus"]
description_fail_ukr = config["Description"]["fail_ukr"]

flaw_perfect_rus = config["Flaw"]["perfect_rus"]
flaw_perfect_ukr = config["Flaw"]["perfect_ukr"]
flaw_good_rus = config["Flaw"]["good_rus"]
flaw_good_ukr = config["Flaw"]["good_ukr"]
flaw_fail_rus = config["Flaw"]["fail_rus"]
flaw_fail_ukr = config["Flaw"]["fail_ukr"]

template_dir = os.path.join(BASE_DIR, 'templates')

logger = logging.getLogger('naDetali')
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler(LOG_FILE)
fh.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('[%(asctime)s] [LINE:%(lineno)d] %(levelname)-8s %(message)s',"%Y-%m-%d %H:%M:%S")
formatter_console = logging.Formatter('[%(asctime)s] %(levelname)-8s %(message)s',"%Y-%m-%d %H:%M:%S")
ch.setFormatter(formatter_console)
fh.setFormatter(formatter)
logger.addHandler(ch)
logger.addHandler(fh)