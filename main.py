import os
import random
from settings import (logger, brand_name, model_name, model_tag_string, 
                      model_tag_string_rus, model_tag_string_ukr, model_state,
                      dir_path, description_perfect_rus, description_perfect_ukr, 
                      description_good_rus, description_good_ukr, description_fail_rus, 
                      description_fail_ukr, flaw_perfect_rus, flaw_perfect_ukr, flaw_good_rus, 
                      flaw_good_ukr, flaw_fail_rus, flaw_fail_ukr)
from settings import template_dir
from setup_names import detail_names
from jinja2 import Environment, FileSystemLoader, select_autoescape

def repalce_for_name(str):
    return str.replace('<', ' ').replace('>', ' ').replace(':', ' ').replace('|', ' ').replace('\\', ' ').replace('/', ' ').replace('?', ' ').replace('*', ' ')
    # print(str)
    # return str


def toHtml(data_list, template_dir, template_name, html_file):
    file_loader = FileSystemLoader(template_dir)
    env = Environment(loader=file_loader)
    htmltemplate = env.get_template(template_name)
    htmltemplate.stream(
        data_list
        ).dump(html_file)
    # logger.info('Письмо: записан html-файл: %s' % (html_file))
    return htmltemplate.render(
        data_list
        )
    logger.info('Сгенерирован текст.')

def make_folder(path):
    try:
        os.makedirs(path)
    except FileExistsError as error:
        logger.warning(error)

class ModelObj:
    def __init__(self, brand, name, model_tag_string, model_tag_string_rus, 
               model_tag_string_ukr, detail_names):
        self.brand = brand
        self.name = name
        self.tag_string = model_tag_string
        self.tag_string_rus = model_tag_string_rus
        self.tag_string_ukr = model_tag_string_ukr
        self.state = model_state
        self.names_dict = detail_names
    
    def get_random_sentence(self, text):
        string_list = text.split('. ')
        random.shuffle(string_list)
        str = ''
        for i in string_list:
            str = str + i.replace('.', '')+'. '
        return str

    def get_names_list(self):
        global_list = []
        for item in self.names_dict:
            item_dict = {
                'model_name':self.name,
                'name_rus': item['name_rus'],
                'name_ukr': item['name_ukr'],
                'tags_rus': '%s, %s, %s, %s' % (self.brand, item['tags_rus'], self.tag_string, self.tag_string_rus),
                'tags_ukr': '%s, %s, %s, %s' % (self.brand, item['tags_ukr'], self.tag_string, self.tag_string_ukr),
                'category': item['category'],
                'dir_path': os.path.join(os.path.dirname(dir_path), self.brand, self.name, repalce_for_name(item['name_rus'])),
                'description_perfect_rus': '%s %s' % (self.get_random_sentence(description_perfect_rus), item['description_rus']),
                'description_good_rus': '%s %s' % (self.get_random_sentence(description_good_rus), item['description_rus']),
                'description_fail_rus': '%s %s' % (self.get_random_sentence(description_fail_rus), item['description_rus']),
                'description_perfect_ukr': '%s %s' % (self.get_random_sentence(description_perfect_ukr), item['description_ukr']),
                'description_good_ukr': '%s %s' % (self.get_random_sentence(description_good_ukr), item['description_ukr']),
                'description_fail_ukr': '%s %s' % (self.get_random_sentence(description_fail_ukr), item['description_ukr']),
                'flaw_perfect_rus': '%s %s' % (self.get_random_sentence(flaw_perfect_rus), item['flaw_rus']),
                'flaw_good_rus': '%s %s' % (self.get_random_sentence(flaw_good_rus), item['flaw_rus']),
                'flaw_fail_rus': '%s %s' % (self.get_random_sentence(flaw_fail_rus), item['flaw_rus']),
                'flaw_perfect_ukr': '%s %s' % (self.get_random_sentence(flaw_perfect_ukr), item['flaw_ukr']),
                'flaw_good_ukr': '%s %s' % (self.get_random_sentence(flaw_good_ukr), item['flaw_ukr']),
                'flaw_fail_ukr': '%s %s' % (self.get_random_sentence(flaw_fail_ukr), item['flaw_ukr']),
            }
            # print(item_dict['dir_path'])
            global_list.append(item_dict)
        return global_list



if __name__ == "__main__":
    logger.info('Начало')

    model = ModelObj(brand_name, model_name, model_tag_string, 
                     model_tag_string_rus, model_tag_string_ukr, detail_names)
    model_list = model.get_names_list()
    make_folder(os.path.join(os.path.dirname(dir_path), brand_name, model_name, '_All Photos'))
    
    for this_model in model_list:
        make_folder(this_model['dir_path'])
    
        data_list = {
            'model': this_model,
        }
        template_name_perfect = 'simple_tamplate_perfect.txt'
        template_name_good = 'simple_tamplate_good.txt'
        template_name_fail = 'simple_tamplate_fail.txt'
        # print()
        file_path_perfect = os.path.join(os.path.dirname(this_model['dir_path']), repalce_for_name(this_model['name_rus']), '1. Отличный - %s%s' % (repalce_for_name(this_model['name_rus']), '.txt'))
        file_path_good = os.path.join(os.path.dirname(this_model['dir_path']), repalce_for_name(this_model['name_rus']), '2. Нормальный - %s%s' % (repalce_for_name(this_model['name_rus']), '.txt'))
        file_path_fail = os.path.join(os.path.dirname(this_model['dir_path']), repalce_for_name(this_model['name_rus']), '3. Плохой - %s%s' % (repalce_for_name(this_model['name_rus']), '.txt'))
    
        toHtml(data_list, template_dir, template_name_perfect, file_path_perfect)
        toHtml(data_list, template_dir, template_name_good, file_path_good)
        toHtml(data_list, template_dir, template_name_fail, file_path_fail)
