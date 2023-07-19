from settings import model
vendor = model['vendor']
model = model['model']
state = "Б/У"
state_ua = "Б/В"
model_name = f"{vendor} {model}"

detail_names = [
    {
        "name": 'Петли (левая, правая) %s' % (model_name),
        "name_ua": 'Петлі (ліва, права) %s' % (model_name),

        "description_small": f"Петли (левая, правая) к ноутбуку {model_name}, оригинальные, {state}",
        "description_small_ua": f"Петлі (ліва, права) до ноутбуку, {model_name}, оригінальні, {state_ua}",

        "keywords": "петли, петля левая, петля правая, петля, петли матрицы, петли экрана, экран, матрица, крепление, часть корпуса",
        "keywords_ua": "петлі, петля ліва, петля права, петля, петлі матриці, петлі екрану, екран, матрица, кріплення, частина корпусу",
        "portal": "Части корпуса ноутбука",
        
        "description_perfect": "Петли почищены, сгибаются-разгибаются как новые. Левая и правая петля продаются вместе.",
        "description_good": "Петли почищены, сгибаются-разгибаются нормально. Левая и правая петля продаются вместе.",
        "description_fail": "Петли почищены, сгибаются-разгибаются нормально. Левая и правая петля продаются вместе.",

        "description_perfect_ua": "Петлі почищені, згинаються-розгинаються як нові. Ліва та права петля продаються разом.",
        "description_good_ua": "Петлі почищені, згинаються-розгинаються нормально. Ліва та права петля продаються разом.",
        "description_fail_ua": "Петлі почищені, згинаються-розгинаються нормально. Ліва та права петля продаються разом.",

        "flaw_perfect": "",
        "flaw_good": "",
        "flaw_fail": "",

        "flaw_perfect_ua": "",
        "flaw_good_ua": "",
        "flaw_fail_ua": "",
    },
    {
        "name": 'Петля левая (петли) %s' % (model_name),
        "name_ua": 'Петля ліва (петлі) %s' % (model_name),

        "description_small": f"Петля левая к ноутбуку {model_name}, оригинальная, {state}",
        "description_small_ua": f"Петля ліва до ноутбуку, {model_name}, оригінальна, {state_ua}",

        "keywords": "петли, петля левая, петля, петли матрицы, петли экрана, экран, матрица, крепление, часть корпуса",
        "keywords_ua": "петлі, петля ліва, петля, петлі матриці, петлі екрану, екран, матрица, кріплення, частина корпусу",
        "portal": "Части корпуса ноутбука",
        
        "description_perfect": "Петля почищена, сгибается-разгибается как новая. <b>Внимание! Продается только левая петля.</b>",
        "description_good": "Петля почищена, сгибается-разгибается нормально. <b>Внимание! Продается только левая петля.</b>",
        "description_fail": "Петля почищена, сгибается-разгибается нормально. <b>Внимание! Продается только левая петля.</b>",

        "description_perfect_ua": "Петля почищена, згинається-розгинається як нова. <b>Увага! Продається тільки ліва петля.</b>",
        "description_good_ua": "Петля почищена, згинається-розгинається нормально. <b>Увага! Продається тільки ліва петля.</b>",
        "description_fail_ua": "Петля почищена, згинається-розгинається нормально. <b>Увага! Продається тільки ліва петля.</b>",

        "flaw_perfect": "",
        "flaw_good": "",
        "flaw_fail": "",

        "flaw_perfect_ua": "",
        "flaw_good_ua": "",
        "flaw_fail_ua": "",
    },
    {
        "name": 'Петля правая (петли) %s' % (model_name),
        "name_ua": 'Петля права (петлі) %s' % (model_name),

        "description_small": f"Петля правая к ноутбуку {model_name}, оригинальная, {state}",
        "description_small_ua": f"Петля права до ноутбуку, {model_name}, оригінальна, {state_ua}",

        "keywords": "петли, петля правая, петля, петли матрицы, петли экрана, экран, матрица, крепление, часть корпуса",
        "keywords_ua": "петлі, петля права, петля, петлі матриці, петлі екрану, екран, матрица, кріплення, частина корпусу",
        "portal": "Части корпуса ноутбука",
        
        "description_perfect": "Петля почищена, сгибается-разгибается как новая. <b>Внимание! Продается только правая петля.</b>",
        "description_good": "Петля почищена, сгибается-разгибается нормально. <b>Внимание! Продается только правая петля.</b>",
        "description_fail": "Петля почищена, сгибается-разгибается нормально. <b>Внимание! Продается только правая петля.</b>",

        "description_perfect_ua": "Петля почищена, згинається-розгинається як нова. <b>Увага! Продається тільки права петля.</b>",
        "description_good_ua": "Петля почищена, згинається-розгинається нормально. <b>Увага! Продається тільки права петля.</b>",
        "description_fail_ua": "Петля почищена, згинається-розгинається нормально. <b>Увага! Продається тільки права петля.</b>",

        "flaw_perfect": "",
        "flaw_good": "",
        "flaw_fail": "",

        "flaw_perfect_ua": "",
        "flaw_good_ua": "",
        "flaw_fail_ua": "",
    },
    {
        "name": 'Нижняя часть корпуса %s (низ, дно, поддон, корыто)' % (model_name),
        "name_ua": 'Нижня частина корпуса %s (низ, дно, піддон, корито)' % (model_name),

        "description_small": f"Нижняя часть корпуса к ноутбуку {model_name}, оригинальная, {state}",
        "description_small_ua": f"Нижня частина корпусу до ноутбука {model_name}, оригинальна, {state_ua}",

        "keywords": "нижняя крышка базы, нижняя часть корпуса, дно, днище, нижняя крышка базы, корито, нижний корпус, низ, поддон",
        "keywords_ua": "нижня кришка бази, нижня частина корпуса, дно, днище, нижняя крышка базы, корито, нижній корпус, низ, піддон",
        "portal": "Части корпуса ноутбука",
        
        "description_perfect": "Дно корпуса вымыто и почищено.",
        "description_good": "Дно корпуса вымыто и почищено.",
        "description_fail": "Дно корпуса вымыто и почищено.",

        "description_perfect_ua": "Дно корпуса вимито та почищено.",
        "description_good_ua": "Дно корпуса вимито та почищено.",
        "description_fail_ua": "Дно корпуса вимито та почищено.",

        "flaw_perfect": "",
        "flaw_good": "",
        "flaw_fail": "",

        "flaw_perfect_ua": "",
        "flaw_good_ua": "",
        "flaw_fail_ua": "",
    },
    {
        "name": 'Крышка матрицы %s (крышка экрана, дисплея)' % (model_name),
        "name_ua": 'Кришка матриці %s (крышка екрану, дисплею)' % (model_name),

        "description_small": f"Крышка матрицы к ноутбуку {model_name}, оригинальная, {state}",
        "description_small_ua": f"Кришка матриці до ноутбуку {model_name}, оригінальна, {state_ua}",

        "keywords": "кришка матрицы, крышка экрана, корпус экрана, корпус, корпус ноутбука, задняя крышка экрана",
        "keywords_ua": "кришка матриці, кришка екрану, корпус екрану, корпус, корпус ноутбука, корпус ноутбуку, задня кришка екрану",
        "portal": "Части корпуса ноутбука",
        
        "description_perfect": "Крышка матрицы вымыта и почищена.",
        "description_good": "Крышка матрицы вымыта и почищена.",
        "description_fail": "Крышка матрицы вымыта и почищена.",

        "description_perfect_ua": "Кришка матриці вымита та почищена.",
        "description_good_ua": "Кришка матриці вымита та почищена.",
        "description_fail_ua": "Кришка матриці вымита та почищена.",

        "flaw_perfect": "",
        "flaw_good": "",
        "flaw_fail": "",

        "flaw_perfect_ua": "",
        "flaw_good_ua": "",
        "flaw_fail_ua": "",
    },
    {
        "name": 'Рамка матрицы (дисплея) %s' % (model_name),
        "name_ua": 'Рамка матриці (дисплею) %s' % (model_name),

        "description_small": f"Рамка матрицы к ноутбуку {model_name}, оригинальная, {state}",
        "description_small_ua": f"Рамка матриці до ноутбуку {model_name}, оригінальна, {state_ua}",

        "keywords": "рамка матрицы, рамка экрана, рамка дисплея",
        "keywords_ua": "рамка матриці, рамка екрану, рамка дисплея, рамка дисплею",
        "portal": "Части корпуса ноутбука",
        
        "description_perfect": "Рамка матрицы вымыта и почищена.",
        "description_good": "Рамка матрицы вымыта и почищена.",
        "description_fail": "Рамка матрицы вымыта и почищена.",

        "description_perfect_ua": "Рамка матриці вимита та почищена.",
        "description_good_ua": "Рамка матриці вимита та почищена.",
        "description_fail_ua": "Рамка матриці вимита та почищена.",

        "flaw_perfect": "",
        "flaw_good": "",
        "flaw_fail": "",

        "flaw_perfect_ua": "",
        "flaw_good_ua": "",
        "flaw_fail_ua": "",
    },
    {
        "name": 'Панель с кнопками %s' % (model_name),
        "name_ua": 'Панель з кнопками %s' % (model_name),

        "description_small": f"Панель з кнопками к ноутбуку {model_name}, оригинальная, {state}",
        "description_small_ua": f"Панель з кнопками до ноутбуку {model_name}, оригінальна, {state_ua}",

        "keywords": "панель кнопок, верхняя панель, панель кнопки включения, панель, панель с кнопками, панель питания",
        "keywords_ua": "панель кнопок, верхня панель, панель кнопки включення, панель, панель кнопки живлення, панель з кнопками, панель живлення",
        "portal": "Части корпуса ноутбука",
        
        "description_perfect": "Панель вымыта и почищена.",
        "description_good": "Панель вымыта и почищена.",
        "description_fail": "Панель вымыта и почищена.",

        "description_perfect_ua": "Панель вимита та почищена.",
        "description_good_ua": "Панель вимита та почищена.",
        "description_fail_ua": "Панель вимита та почищена.",

        "flaw_perfect": "",
        "flaw_good": "",
        "flaw_fail": "",

        "flaw_perfect_ua": "",
        "flaw_good_ua": "",
        "flaw_fail_ua": "",
    },
    {
        "name": 'Панель кнопки включения %s (вкл/выкл)' % (model_name),
        "name_ua": 'Панель кнопки включення (живлення) %s (вкл/викл)' % (model_name),

        "description_small": f"Панель кнопки включения к ноутбуку {model_name}, оригинальная, {state}",
        "description_small_ua": f"Панель кнопки включення, кнопки живлення, до ноутбуку {model_name}, оригінальна, {state_ua}",

        "keywords": "панель кнопки включения, панель, панель с кнопками, панель питания",
        "keywords_ua": "панель кнопки включення, панель, панель кнопки живлення, панель з кнопками, панель живлення",
        "portal": "Части корпуса ноутбука",
        
        "description_perfect": "Панель вымыта и почищена.",
        "description_good": "Панель вымыта и почищена.",
        "description_fail": "Панель вымыта и почищена.",

        "description_perfect_ua": "Панель вимита та почищена.",
        "description_good_ua": "Панель вимита та почищена.",
        "description_fail_ua": "Панель вимита та почищена.",

        "flaw_perfect": "",
        "flaw_good": "",
        "flaw_fail": "",

        "flaw_perfect_ua": "",
        "flaw_good_ua": "",
        "flaw_fail_ua": "",
    },
    {
        "name": 'Заглушки (крышки) петель %s' % (model_name),
        "name_ua": 'Заглушки (крышки) петель %s' % (model_name),

        "description_small": f"Крышки на петли, заглушки петель к ноутбуку {model_name}, оригинальные, {state}",
        "description_small_ua": f"Кришки на петлі, заглушки петель до ноутбуку {model_name}, оригінальні, {state_ua}",

        "keywords": "колпачки, заглушки (крышки) петель, заглушки, заглушка, петли, петля",
        "keywords_ua": "ковпачки, заглушки (крышки) петель, заглушки, заглушка, петлі, петля",
        "portal": "Части корпуса ноутбука",
        
        "description_perfect": "Крышки петель вымыты и почищены.",
        "description_good": "Крышки петель вымыты и почищены.",
        "description_fail": "Крышки петель вымыты и почищены.",

        "description_perfect_ua": "Кришки петель вимиті та почищені.",
        "description_good_ua": "Кришки петель вимиті та почищені.",
        "description_fail_ua": "Кришки петель вимиті та почищені.",

        "flaw_perfect": "",
        "flaw_good": "",
        "flaw_fail": "",

        "flaw_perfect_ua": "",
        "flaw_good_ua": "",
        "flaw_fail_ua": "",
    },
    {
        "name": 'Накладка на петли %s' % (model_name),
        "name_ua": 'Накладка на петлі %s' % (model_name),

        "description_small": f"Накладка на петли к ноутбуку {model_name}, оригинальная, {state}",
        "description_small_ua": f"Накладка на петлі до ноутбуку {model_name}, оригінальна, {state_ua}",

        "keywords": "накладка, накладка на петли, петля, петли, колпачки, заглушки, заглушка",
        "keywords_ua": "накладка, накладка на петлі, петля, петлі, ковпачки, заглушки, заглушка",
        "portal": "Части корпуса ноутбука",
        
        "description_perfect": "Накладка петель вымыта и почищена.",
        "description_good": "Накладка петель вымыта и почищена.",
        "description_fail": "Накладка петель вымыта и почищена.",

        "description_perfect_ua": "Накладка петель вимита та почищена.",
        "description_good_ua": "Накладка петель вимита та почищена.",
        "description_fail_ua": "Накладка петель вимита та почищена.",

        "flaw_perfect": "",
        "flaw_good": "",
        "flaw_fail": "",

        "flaw_perfect_ua": "",
        "flaw_good_ua": "",
        "flaw_fail_ua": "",
    },
    {
        "name": 'Тачпад (трекпад) %s (touchpad)' % (model_name),
        "name_ua": 'Тачпад (трекпад) %s (touchpad)' % (model_name),

        "description_small": f"Тачпад или трекпад к ноутбуку {model_name}, оригинальный, {state}",
        "description_small_ua": f"Тачпад або трекпад до ноутбука {model_name}, оригінальний, {state_ua}",

        "keywords": "Плата тачпад, тачпад, touchpad, трекпад",
        "keywords_ua": "Плата тачпад, тачпад, touchpad, трекпад",
        "portal": "Части корпуса ноутбука",
        
        "description_perfect": "",
        "description_good": "",
        "description_fail": "",

        "description_perfect_ua": "",
        "description_good_ua": "",
        "description_fail_ua": "",

        "flaw_perfect": "",
        "flaw_good": "",
        "flaw_fail": "",

        "flaw_perfect_ua": "",
        "flaw_good_ua": "",
        "flaw_fail_ua": "",
    },
    {
        "name": 'Панель тачпада (трекпада) %s' % (model_name),
        "name_ua": 'Панель тачпада (трекпада) %s' % (model_name),

        "description_small": f"Панель тачпада к ноутбуку {model_name}, оригинальная, {state}",
        "description_small_ua": f"Панель тачпада до ноутбука {model_name}, оригінальна, {state_ua}",

        "keywords": "панель тачпада, тачпад, touchpad",
        "keywords_ua": "панель тачпада, тачпад, touchpad",
        "portal": "Части корпуса ноутбука",
        
        "description_perfect": "Панель вымита и почищена.",
        "description_good": "Панель вымита и почищена.",
        "description_fail": "Панель вымита и почищена.",

        "description_perfect_ua": "Панель вимита та почищена.",
        "description_good_ua": "Панель вимита та почищена.",
        "description_fail_ua": "Панель вимита та почищена.",

        "flaw_perfect": "",
        "flaw_good": "",
        "flaw_fail": "",

        "flaw_perfect_ua": "",
        "flaw_good_ua": "",
        "flaw_fail_ua": "",
    },
    {
        "name": 'Плата, шлейф, кнопки тачпада %s (touchpad)' % (model_name),
        "name_ua": 'Плата, шлейф, кнопки тачпаду %s (touchpad)' % (model_name),

        "description_small": f"Плата, шлейф и кнопки тачпада к ноутбуку {model_name}, оригинальные, {state}",
        "description_small_ua": f"Плата, шлейф, кнопки тачпада до ноутбука {model_name}, оригінальні, {state_ua}",

        "keywords": "Плата, шлейф, кнопки тачпада, (touchpad)",
        "keywords_ua": "Плата, шлейф, кнопки тачпаду, (touchpad)",
        "portal": "Части корпуса ноутбука",
        
        "description_perfect": "",
        "description_good": "",
        "description_fail": "",

        "description_perfect_ua": "",
        "description_good_ua": "",
        "description_fail_ua": "",

        "flaw_perfect": "",
        "flaw_good": "",
        "flaw_fail": "",

        "flaw_perfect_ua": "",
        "flaw_good_ua": "",
        "flaw_fail_ua": "",
    },
    {
        "name": 'Плата, кнопки тачпада %s (touchpad)' % (model_name),
        "name_ua": 'Плата, кнопки тачпаду %s (touchpad)' % (model_name),

        "description_small": f"Плата и кнопки тачпада к ноутбуку {model_name}, оригинальные, {state}",
        "description_small_ua": f"Плата та кнопки тачпада до ноутбука {model_name}, оригінальні, {state_ua}",

        "keywords": "touchpad, плата, кнопки тачпада",
        "keywords_ua": "touchpad, плата, кнопки тачпаду",
        "portal": "Адаптеры и платы расширения портов",
        
        "description_perfect": "",
        "description_good": "",
        "description_fail": "",

        "description_perfect_ua": "",
        "description_good_ua": "",
        "description_fail_ua": "",

        "flaw_perfect": "",
        "flaw_good": "",
        "flaw_fail": "",

        "flaw_perfect_ua": "",
        "flaw_good_ua": "",
        "flaw_fail_ua": "",
    },
    {
        "name": 'Сервисная крышка корпуса %s (заглушка)' % (model_name),
        "name_ua": 'Сервісна кришка корпусу %s (заглушка)' % (model_name),

        "description_small": f"Сервисная крышка корпуса к ноутбуку {model_name}, оригинальная, {state}",
        "description_small_ua": f"Сервісна кришка корпуса до нутбуку {model_name}, оригінальна, {state_ua}",

        "keywords": "сервисная крышка, крышка, заглушка, крышка корпуса",
        "keywords_ua": "сервісна кришка, кришка, заглушка, кришка корпусу",
        "portal": "Части корпуса ноутбука",
        
        "description_perfect": "Сервисная крышка вымыта и почищена.",
        "description_good": "Сервисная крышка вымыта и почищена.",
        "description_fail": "Сервисная крышка вымыта и почищена.",

        "description_perfect_ua": "Сервісна кришка вимита та почищена.",
        "description_good_ua": "Сервісна кришка вимита та почищена.",
        "description_fail_ua": "Сервісна кришка вимита та почищена.",

        "flaw_perfect": "",
        "flaw_good": "",
        "flaw_fail": "",

        "flaw_perfect_ua": "",
        "flaw_good_ua": "",
        "flaw_fail_ua": "",
    },
    {
        "name": 'Сервисная крышка HDD/SSD %s' % (model_name),
        "name_ua": 'Сервісна кришка HDD/SSD %s' % (model_name),

        "description_small": f"Сервисная крышка для HDD или SSD ноутбука {model_name}, оригинальная, {state}",
        "description_small_ua": f"Сервісна кришка для HDD або SSD ноутбуку {model_name}, оригінальна, {state_ua}",

        "keywords": "сервисная крышка, крышка, hdd, ssd, hdd/ssd, заглушка",
        "keywords_ua": "сервісна кришка, кришка, hdd, ssd, hdd/ssd, заглушка",
        "portal": "Части корпуса ноутбука",
        
        "description_perfect": "Сервисная крышка вымыта и почищена.",
        "description_good": "Сервисная крышка вымыта и почищена.",
        "description_fail": "Сервисная крышка вымыта и почищена.",

        "description_perfect_ua": "Сервісна кришка вимита та почищена.",
        "description_good_ua": "Сервісна кришка вимита та почищена.",
        "description_fail_ua": "Сервісна кришка вимита та почищена.",

        "flaw_perfect": "",
        "flaw_good": "",
        "flaw_fail": "",

        "flaw_perfect_ua": "",
        "flaw_good_ua": "",
        "flaw_fail_ua": "",
    },
    {
        "name": 'Сервисная крышка охлаждение %s' % (model_name),
        "name_ua": 'Сервісна кришка охолодження %s' % (model_name),

        "description_small": f"Сервисная крышка охлаждения к ноутбуку {model_name}, оригинальная, {state}",
        "description_small_ua": f"Сервісна кришка охолодження до ноутбука {model_name}, оригінальна, {state_ua}",

        "keywords": "сервисная крышка, крышка, охлаждение, заглушка",
        "keywords_ua": "сервісна кришка, кришка, охолодження, заглушка",
        "portal": "Части корпуса ноутбука",
        
        "description_perfect": "Сервисная крышка вымыта и почищена.",
        "description_good": "Сервисная крышка вымыта и почищена.",
        "description_fail": "Сервисная крышка вымыта и почищена.",

        "description_perfect_ua": "Сервісна кришка вимита та почищена.",
        "description_good_ua": "Сервісна кришка вимита та почищена.",
        "description_fail_ua": "Сервісна кришка вимита та почищена.",

        "flaw_perfect": "",
        "flaw_good": "",
        "flaw_fail": "",

        "flaw_perfect_ua": "",
        "flaw_good_ua": "",
        "flaw_fail_ua": "",
    },
    {
        "name": 'Клавиатура %s' % (model_name),
        "name_ua": 'Клавіатура %s' % (model_name),

        "description_small": f"Клавиатура ноутбука {model_name}, оригинальная, {state}",
        "description_small_ua": f"Клавіатура ноутбука {model_name}, оригінальна, {state_ua}",

        "keywords": "клавиатура, клава, keyboard",
        "keywords_ua": "клавіатура, клава, keyboard",
        "portal": "Клавиатурные блоки для ноутбуков",
        
        "description_perfect": "Клавиатура вымыта, почищена, протестирована специальным прибором. Все кнопки работают и не имеют хруста.",
        "description_good": "Клавиатура вымыта, почищена, протестирована специальным прибором. Все кнопки работают и не имеют хруста.",
        "description_fail": "Клавиатура вымыта, почищена, протестирована специальным прибором. Все кнопки работают и не имеют хруста.",

        "description_perfect_ua": "Клавіатура вимита, почищена, протестована спеціальним прибором. Всі кнопки працюють та не мають хрусту.",
        "description_good_ua": "Клавіатура вимита, почищена, протестована спеціальним прибором. Всі кнопки працюють та не мають хрусту.",
        "description_fail_ua": "Клавіатура вимита, почищена, протестована спеціальним прибором. Всі кнопки працюють та не мають хрусту.",

        "flaw_perfect": "",
        "flaw_good": "",
        "flaw_fail": "",

        "flaw_perfect_ua": "",
        "flaw_good_ua": "",
        "flaw_fail_ua": "",
    },
    {
        "name": 'Рамка клавиатуры %s' % (model_name),
        "name_ua": 'Рамка клавіатури %s' % (model_name),

        "description_small": f"Рамка клавиатуры {model_name}, оригинальная, {state}",
        "description_small_ua": f"Рамка клавіатури {model_name}, оригінальна, {state_ua}",

        "keywords": "рамка клавиатуры, рамка, клавиатура, клава, keyboard",
        "keywords_ua": "рамка клавіатури, рамка, клавіатура, клава, keyboard",
        "portal": "Части корпуса ноутбука",
        
        "description_perfect": "Рамка вымыта и почищена.",
        "description_good": "Рамка вымыта и почищена.",
        "description_fail": "Рамка вымыта и почищена.",

        "description_perfect_ua": "Рамка вимита та почищена.",
        "description_good_ua": "Рамка вимита та почищена.",
        "description_fail_ua": "Рамка вимита та почищена.",

        "flaw_perfect": "",
        "flaw_good": "",
        "flaw_fail": "",

        "flaw_perfect_ua": "",
        "flaw_good_ua": "",
        "flaw_fail_ua": "",
    },
    {
        "name": 'Шлейф клавиатуры %s (keyboard)' % (model_name),
        "name_ua": 'Шлейф клавіатури %s (keyboard)' % (model_name),

        "description_small": f"Шлейф клавиатуры к ноутбуку {model_name}, оригинальный, {state}",
        "description_small_ua": f"Шлейф клавіатури до ноутбука {model_name}, оригінальний, {state_ua}",

        "keywords": "шлейф клавиатуры, шлейф, клавиатура, клава, keyboard",
        "keywords_ua": "шлейф клавіатури, шлейф, клавіатура, клава, keyboard",
        "portal": "Шлейфы и разъемы для ноутбуков",
        
        "description_perfect": "",
        "description_good": "",
        "description_fail": "",

        "description_perfect_ua": "",
        "description_good_ua": "",
        "description_fail_ua": "",

        "flaw_perfect": "",
        "flaw_good": "",
        "flaw_fail": "",

        "flaw_perfect_ua": "",
        "flaw_good_ua": "",
        "flaw_fail_ua": "",
    },

    {
        "name": 'Материнская плата %s (Системная плата)' % (model_name),
        "name_ua": 'Материнська плата %s (Системна плата)' % (model_name),

        "description_small": f"Материнская плата к ноутбуку {model_name}, оригинальная, РАБОЧАЯ, {state}",
        "description_small_ua": f"Материнська плата до ноутбуку {model_name}, оригінальна, РОБОЧА, {state_ua}",

        "keywords": "материнская плата, системная плата",
        "keywords_ua": "материнська плата, системна плата",
        "portal": "Материнские платы",
        
        "description_perfect": "",
        "description_good": "",
        "description_fail": "",

        "description_perfect_ua": "",
        "description_good_ua": "",
        "description_fail_ua": "",

        "flaw_perfect": "",
        "flaw_good": "",
        "flaw_fail": "",

        "flaw_perfect_ua": "",
        "flaw_good_ua": "",
        "flaw_fail_ua": "",
    },
    {
        "name": 'Материнская плата %s (Системная плата, нр)' % (model_name),
        "name_ua": 'Материнська плата %s (Системна плата, нп)' % (model_name),

        "description_small": f"Материнская плата до ноутбука {model_name}, оригинальная, {state}",
        "description_small_ua": f"Материнська плата до ноутбука {model_name}, оригінальна, {state_ua}",

        "keywords": "материнская плата, системная плата",
        "keywords_ua": "материнська плата, системна плата",
        "portal": "Материнские платы",
        
        "description_perfect": "<b>Внимание! Материнская плата не работает!</b> На детали или под восстановление.",
        "description_good": "<b>Внимание! Материнская плата не работает!</b> На детали или под восстановление.",
        "description_fail": "<b>Внимание! Материнская плата не работает!</b> На детали или под восстановление.",

        "description_perfect_ua": "<b>Увага! Материнська плата не працює!</b> На деталі або під відновлення.",
        "description_good_ua": "<b>Увага! Материнська плата не працює!</b> На деталі або під відновлення.",
        "description_fail_ua": "<b>Увага! Материнська плата не працює!</b> На деталі або під відновлення.",

        "flaw_perfect": "",
        "flaw_good": "",
        "flaw_fail": "",

        "flaw_perfect_ua": "",
        "flaw_good_ua": "",
        "flaw_fail_ua": "",
    },
    {
        "name": 'Кулер, вентилятор %s (FAN)' % (model_name),
        "name_ua": 'Кулер, вентилятор %s (FAN)' % (model_name),

        "description_small": f"Кулер, вентилятор, снятый с ноутбука {model_name}, оригинальный, {state}",
        "description_small_ua": f"Кулер, вентилятор, знятий з ноутбука {model_name}, оригінальний, {state_ua}",

        "keywords": "кулер, вентилятор, fan",
        "keywords_ua": "кулер, вентилятор, fan",
        "portal": "Системы охлаждения для ноутбуков",
        
        "description_perfect": "Кулер почищен, вымыт, смазан специальной смазкой. Проверен, не шумит.",
        "description_good": "Кулер почищен, вымыт, смазан специальной смазкой. Проверен, не шумит.",
        "description_fail": "Кулер почищен, вымыт, смазан специальной смазкой. Проверен, не шумит.",

        "description_perfect_ua": "Кулер почищений, вимитий та змазаний спеціальною змазкою. Перевірений, не шумить.",
        "description_good_ua": "Кулер почищений, вимитий та змазаний спеціальною змазкою. Перевірений, не шумить.",
        "description_fail_ua": "Кулер почищений, вимитий та змазаний спеціальною змазкою. Перевірений, не шумить.",

        "flaw_perfect": "",
        "flaw_good": "",
        "flaw_fail": "",

        "flaw_perfect_ua": "",
        "flaw_good_ua": "",
        "flaw_fail_ua": "",
    },
    {
        "name": 'Система охлаждения, термотрубка %s DIS' % (model_name),
        "name_ua": 'Система охолодження, термотрубка %s DIS' % (model_name),

        "description_small": f"Система охлаждения, радиатор снятый с ноутбука {model_name}, оригинальный, {state}",
        "description_small_ua": f"Система охлаждения, радіатор знятий з ноутбука {model_name}, оригінальний, {state_ua}",

        "keywords": "термотрубка, термотрубки, радиатор, система охлаждения, охлаждение, термотрубка системы охлаждения",
        "keywords_ua": "термотрубка, термотрубки, радіатор, система охолодження, охолодження, термотрубка системи охолодження",
        "portal": "Кулеры и системы охлаждения",
        
        "description_perfect": "",
        "description_good": "",
        "description_fail": "",

        "description_perfect_ua": "",
        "description_good_ua": "",
        "description_fail_ua": "",

        "flaw_perfect": "",
        "flaw_good": "",
        "flaw_fail": "",

        "flaw_perfect_ua": "",
        "flaw_good_ua": "",
        "flaw_fail_ua": "",
    },
    {
        "name": 'Система охлаждения, термотрубка %s UMA' % (model_name),
        "name_ua": 'Система охолодження, термотрубка %s UMA' % (model_name),

        "description_small": f"Термотрубка, радиатор, снятый с ноутбука {model_name}, оригинальный, {state}",
        "description_small_ua": f"Термотрубка, радіатор, знятий з ноутбука {model_name}, оригінальний, {state_ua}",

        "keywords": "термотрубка, термотрубки, радиатор, система охлаждения, охлаждение, термотрубка системы охлаждения",
        "keywords_ua": "термотрубка, термотрубки, радіатор, система охолодження, охолодження, термотрубка системи охолодження",
        "portal": "Кулеры и системы охлаждения",
        
        "description_perfect": "Термотрубка проверена на теплопроводность - все в норме.",
        "description_good": "Термотрубка проверена на теплопроводность - все в норме.",
        "description_fail": "Термотрубка проверена на теплопроводность - все в норме.",

        "description_perfect_ua": "Термотрубка перевірена на теплопровідність - все в нормі.",
        "description_good_ua": "Термотрубка перевірена на теплопровідність - все в нормі.",
        "description_fail_ua": "Термотрубка перевірена на теплопровідність - все в нормі.",

        "flaw_perfect": "",
        "flaw_good": "",
        "flaw_fail": "",

        "flaw_perfect_ua": "",
        "flaw_good_ua": "",
        "flaw_fail_ua": "",
    },
    {
        "name": 'Оптический привод DVD-RW %s' % (model_name),
        "name_ua": 'Оптичний привід DVD-RW %s' % (model_name),

        "description_small": f"Оптический привод DVD-RW, снятый с ноутбука {model_name}, оригинальный, {state}",
        "description_small_ua": f"Оптичний привід DVD-RW, знятий з ноутбука {model_name}, оригінальний, {state_ua}",

        "keywords": "оптический привод, привод, dvd-rw, dvd-r",
        "keywords_ua": "оптичний привід, привід, dvd-rw, dvd-r",
        "portal": "Оптические приводы",
        
        "description_perfect": "",
        "description_good": "",
        "description_fail": "",

        "description_perfect_ua": "",
        "description_good_ua": "",
        "description_fail_ua": "",

        "flaw_perfect": "",
        "flaw_good": "",
        "flaw_fail": "",

        "flaw_perfect_ua": "",
        "flaw_good_ua": "",
        "flaw_fail_ua": "",
    },
    {
        "name": 'Оптический привод CD-RW %s' % (model_name),
        "name_ua": 'Оптичний привід CD-RW %s' % (model_name),

        "description_small": f"Оптический привод CD-RW, снятый с ноутбука {model_name}, оригинальный, {state}",
        "description_small_ua": f"Оптичний привід CD-RW, знятий з ноутбука {model_name}, оригінальний, {state_ua}",

        "keywords": "оптический привод, привод, dvd-rw, dvd-r",
        "keywords_ua": "оптичний привід, привід, dvd-rw, dvd-r",
        "portal": "Оптические приводы",
        
        "description_perfect": "",
        "description_good": "",
        "description_fail": "",

        "description_perfect_ua": "",
        "description_good_ua": "",
        "description_fail_ua": "",

        "flaw_perfect": "",
        "flaw_good": "",
        "flaw_fail": "",

        "flaw_perfect_ua": "",
        "flaw_good_ua": "",
        "flaw_fail_ua": "",
    },
    {
        "name": 'Динамики, колонки %s' % (model_name),
        "name_ua": 'Динаміки, колонки %s' % (model_name),

        "description_small": f"Динамики к ноутбука {model_name}, оригинальные, {state}",
        "description_small_ua": f"Динаміки до ноутбука {model_name}, оригінальні, {state_ua}",

        "keywords": "динамики, колонки, динамик, колонка, динамик ноутбука, колонка ноутбука, дифузор, звук, саунд, sound",
        "keywords_ua": "динаміки, колонки, динамік, колонка, динамік ноутбука, динаміки ноутбуку, колонка ноутбука, дифузор, звук, саунд, sound",
        "portal": "Звуковые запчасти для портативных пк",
        
        "description_perfect": "Динамики проверены на работоспособность - работают оба.",
        "description_good": "Динамики проверены на работоспособность - работают оба.",
        "description_fail": "Динамики проверены на работоспособность - работают оба.",

        "description_perfect_ua": "Динаміки перевірені на працездатність - працюють обидва.",
        "description_good_ua": "Динаміки перевірені на працездатність - працюють обидва.",
        "description_fail_ua": "Динаміки перевірені на працездатність - працюють обидва.",

        "flaw_perfect": "",
        "flaw_good": "",
        "flaw_fail": "",

        "flaw_perfect_ua": "",
        "flaw_good_ua": "",
        "flaw_fail_ua": "",
    },
    {
        "name": 'Сабвуфер, динамик %s' % (model_name),
        "name_ua": 'Сабвуфер, динамік %s' % (model_name),

        "description_small": f"Динамик, сабвуфер ноутбука {model_name}, оригинальный, {state}",
        "description_small_ua": f"Динамік, сабвуфер до ноутбука {model_name}, оригінальний, {state_ua}",

        "keywords": "динамики, колонки, динамик, колонка, динамик ноутбука, колонка ноутбука, дифузор, звук, саунд, sound",
        "keywords_ua": "динаміки, колонки, динамік, колонка, динамік ноутбука, динаміки ноутбуку, колонка ноутбука, дифузор, звук, саунд, sound",
        "portal": "Звуковые запчасти для портативных пк",
        
        "description_perfect": "Динамик проверен на работоспособность - работает.",
        "description_good": "Динамик проверен на работоспособность - работает.",
        "description_fail": "Динамик проверен на работоспособность - работает.",

        "description_perfect_ua": "Динамік перевірений на працездатність - працює.",
        "description_good_ua": "Динамік перевірений на працездатність - працює.",
        "description_fail_ua": "Динамік перевірений на працездатність - працює.",

        "flaw_perfect": "",
        "flaw_good": "",
        "flaw_fail": "",

        "flaw_perfect_ua": "",
        "flaw_good_ua": "",
        "flaw_fail_ua": "",
    },
    {
        "name": 'Плата USB %s (юсб)' % (model_name),
        "name_ua": 'Плата USB %s (юсб)' % (model_name),

        "description_small": f"Плата USB к ноутбуку {model_name}, оригинальный, {state}",
        "description_small_ua": f"Плата USB до ноутбука {model_name}, оригінальний, {state_ua}",

        "keywords": "плата, usb, юсб",
        "keywords_ua": "плата, usb, юсб",
        "portal": "Адаптеры и платы расширения портов",
        
        "description_perfect": "",
        "description_good": "",
        "description_fail": "",

        "description_perfect_ua": "",
        "description_good_ua": "",
        "description_fail_ua": "",

        "flaw_perfect": "",
        "flaw_good": "",
        "flaw_fail": "",

        "flaw_perfect_ua": "",
        "flaw_good_ua": "",
        "flaw_fail_ua": "",
    },
    {
        "name": 'Плата USB, audio %s (юсб, аудио)' % (model_name),
        "name_ua": 'Плата USB, audio %s (юсб, аудіо)' % (model_name),

        "description_small": f"Плата юсб, аудио к ноутбуку {model_name}, оригинальная, {state}",
        "description_small_ua": f"Плата юсб, аудіо до ноутбука {model_name}, оригінальна, {state_ua}",

        "keywords": "плата, usb, юсб, audio, аудио",
        "keywords_ua": "плата, usb, юсб, audio, аудіо",
        "portal": "Адаптеры и платы расширения портов",
        
        "description_perfect": "",
        "description_good": "",
        "description_fail": "",

        "description_perfect_ua": "",
        "description_good_ua": "",
        "description_fail_ua": "",

        "flaw_perfect": "",
        "flaw_good": "",
        "flaw_fail": "",

        "flaw_perfect_ua": "",
        "flaw_good_ua": "",
        "flaw_fail_ua": "",
    },
    {
        "name": 'Плата USB, audio, cardreader %s (юсб, аудио, кардридер)' % (model_name),
        "name_ua": 'Плата USB, audio, cardreader %s (юсб, аудіо, кардрідер)' % (model_name),

        "description_small": f"Плата юсб, аудио, кардридер к ноутбуку {model_name}, оригинальная, {state}",
        "description_small_ua": f"Плата юсб, аудіо, кардрідер до ноутбука {model_name}, оригінальна, {state_ua}",

        "keywords": "плата, плата юсб, плата аудио, юсб, аудио, кардридер, USB, audio, cardreader",
        "keywords_ua": "плата, плата юсб, плата аудіо, юсб, аудіо, кардрідер, USB, audio, cardreader",
        "portal": "Адаптеры и платы расширения портов",
        
        "description_perfect": "",
        "description_good": "",
        "description_fail": "",

        "description_perfect_ua": "",
        "description_good_ua": "",
        "description_fail_ua": "",

        "flaw_perfect": "",
        "flaw_good": "",
        "flaw_fail": "",

        "flaw_perfect_ua": "",
        "flaw_good_ua": "",
        "flaw_fail_ua": "",
    },
    {
        "name": 'Плата audio %s (аудио)' % (model_name),
        "name_ua": 'Плата audio %s (аудіо)' % (model_name),

        "description_small": f"Плата аудио к ноутбуку {model_name}, оригинальная, {state}",
        "description_small_ua": f"Плата аудіо до ноутбука {model_name}, оригінальна, {state_ua}",

        "keywords": "audio, аудио, плата аудио, плата",
        "keywords_ua": "audio, аудіо, плата аудіо, плата",
        "portal": "Адаптеры и платы расширения портов",
        
        "description_perfect": "",
        "description_good": "",
        "description_fail": "",

        "description_perfect_ua": "",
        "description_good_ua": "",
        "description_fail_ua": "",

        "flaw_perfect": "",
        "flaw_good": "",
        "flaw_fail": "",

        "flaw_perfect_ua": "",
        "flaw_good_ua": "",
        "flaw_fail_ua": "",
    },
    {
        "name": 'Плата VGA %s (видео)' % (model_name),
        "name_ua": 'Плата VGA %s (відео)' % (model_name),

        "description_small": f"Дополнительная плата расширения с видеоразъемом к ноутбуку {model_name}, оригинальная, {state}",
        "description_small_ua": f"Додаткова плата розширення з відеороз'ємом до ноутбука {model_name}, оригінальна, {state_ua}",

        "keywords": "плата, плата vga, vga, video, плата видео, плата video",
        "keywords_ua": "плата, плата vga, vga, video, плата відео, плата video",
        "portal": "Адаптеры и платы расширения портов",
        
        "description_perfect": "",
        "description_good": "",
        "description_fail": "",

        "description_perfect_ua": "",
        "description_good_ua": "",
        "description_fail_ua": "",

        "flaw_perfect": "",
        "flaw_good": "",
        "flaw_fail": "",

        "flaw_perfect_ua": "",
        "flaw_good_ua": "",
        "flaw_fail_ua": "",
    },
    {
        "name": 'Плата HDMI %s (видео)' % (model_name),
        "name_ua": 'Плата HDMI %s (відео)' % (model_name),

        "description_small": f"Дополнительная плата расширения HDMI к ноутбуку {model_name}, оригинальная, {state}",
        "description_small_ua": f"Додаткова плата розширення HDMI до ноутбука {model_name}, оригінальна, {state_ua}",

        "keywords": "плата, hdmi, видео",
        "keywords_ua": "плата, hdmi, відео",
        "portal": "Адаптеры и платы расширения портов",
        
        "description_perfect": "",
        "description_good": "",
        "description_fail": "",

        "description_perfect_ua": "",
        "description_good_ua": "",
        "description_fail_ua": "",

        "flaw_perfect": "",
        "flaw_good": "",
        "flaw_fail": "",

        "flaw_perfect_ua": "",
        "flaw_good_ua": "",
        "flaw_fail_ua": "",
    },
    {
        "name": 'Плата VGA, USB, audio, HDMI %s (видео, юсб, аудио)' % (model_name),
        "name_ua": 'Плата VGA, USB, audio, HDMI %s (відео, юсб, аудіо)' % (model_name),

        "description_small": f"Дополнительная плата расширения VGA, USB, audio, HDMI к ноутбуку {model_name}, оригинальная, {state}",
        "description_small_ua": f"Додаткова плата розширення VGA, USB, audio, HDMI до ноутбука {model_name}, оригінальна, {state_ua}",

        "keywords": "VGA, USB, audio, HDMI, видео, юсб, аудио",
        "keywords_ua": "VGA, USB, audio, HDMI, відео, юсб, аудіо",
        "portal": "Адаптеры и платы расширения портов",
        
        "description_perfect": "",
        "description_good": "",
        "description_fail": "",

        "description_perfect_ua": "",
        "description_good_ua": "",
        "description_fail_ua": "",

        "flaw_perfect": "",
        "flaw_good": "",
        "flaw_fail": "",

        "flaw_perfect_ua": "",
        "flaw_good_ua": "",
        "flaw_fail_ua": "",
    },
    {
        "name": 'Плата мультимедиа, кардридер %s (multimedia, cardreader)' % (model_name),
        "name_ua": 'Плата мультимедіа, кардрідер %s (multimedia, cardreader)' % (model_name),

        "description_small": f"Дополнительная плата расширения мультимедиа и кардридер к ноутбуку {model_name}, оригинальная, {state}",
        "description_small_ua": f"Додаткова плата розширення мультимедіа и кардрідер до ноутбука {model_name}, оригінальна, {state_ua}",

        "keywords": "мультимедиа, кардридер, multimedia, cardreader",
        "keywords_ua": "мультимедіа, кардрідер, multimedia, cardreader",
        "portal": "Адаптеры и платы расширения портов",
        
        "description_perfect": "",
        "description_good": "",
        "description_fail": "",

        "description_perfect_ua": "",
        "description_good_ua": "",
        "description_fail_ua": "",

        "flaw_perfect": "",
        "flaw_good": "",
        "flaw_fail": "",

        "flaw_perfect_ua": "",
        "flaw_good_ua": "",
        "flaw_fail_ua": "",
    },
    {
        "name": 'Смарт-кардридер %s (Smart Card Reader Board)' % (model_name),
        "name_ua": 'Смарт-кардрідер %s (Smart Card Reader Board)' % (model_name),

        "description_small": f"Дополнительная плата расширения: смарт-кардридер к ноутбуку {model_name}, оригинальная, {state}",
        "description_small_ua": f"Додаткова плата розширення: смарт-кардрідер до ноутбука {model_name}, оригінальна, {state_ua}",

        "keywords": "мультимедиа, кардридер, Smart Card Reader Board",
        "keywords_ua": "мультимедіа, кардрідер, Smart Card Reader Board",
        "portal": "Адаптеры и платы расширения портов",
        
        "description_perfect": "",
        "description_good": "",
        "description_fail": "",

        "description_perfect_ua": "",
        "description_good_ua": "",
        "description_fail_ua": "",

        "flaw_perfect": "",
        "flaw_good": "",
        "flaw_fail": "",

        "flaw_perfect_ua": "",
        "flaw_good_ua": "",
        "flaw_fail_ua": "",
    },
    {
        "name": 'Плата, шлейф мультимедийные кнопки %s (multimedia)' % (model_name),
        "name_ua": 'Плата, шлейф мультимедійні кнопки %s (multimedia)' % (model_name),

        "description_small": f"Дополнительная плата расширения мультимедийных кнопок и шлейф к ноутбуку {model_name}, оригинальная, {state}",
        "description_small_ua": f"Додаткова плата розширення мультимедійных кнопок та шлейф до ноутбука {model_name}, оригінальна, {state_ua}",

        "keywords": "плата, шлейф, мультимедиа кнопки, multimedia",
        "keywords_ua": "плата, шлейф, мультимедіа кнопки, multimedia",
        "portal": "Адаптеры и платы расширения портов",
        
        "description_perfect": "",
        "description_good": "",
        "description_fail": "",

        "description_perfect_ua": "",
        "description_good_ua": "",
        "description_fail_ua": "",

        "flaw_perfect": "",
        "flaw_good": "",
        "flaw_fail": "",

        "flaw_perfect_ua": "",
        "flaw_good_ua": "",
        "flaw_fail_ua": "",
    },
    {
        "name": 'Плата, шлейф, кнопка включения (питания) %s (вкл/выкл)' % (model_name),
        "name_ua": 'Плата, шлейф, кнопка включення (живлення) %s (вкл/викл)' % (model_name),

        "description_small": f"Дополнительная плата кнопки включения и шлейф к ноутбуку {model_name}, оригинальная, {state}",
        "description_small_ua": f"Додаткова плата кнопки включення (живлення) та шлейф до ноутбука {model_name}, оригінальна, {state_ua}",

        "keywords": "плата, шлейф, кнопка, кнопка включения, вкл, выкл, вкл/выкл",
        "keywords_ua": "плата, шлейф, кнопка, кнопка включення, кнопка живлення, вкл, викл, вкл/викл",
        "portal": "Адаптеры и платы расширения портов",
        
        "description_perfect": "",
        "description_good": "",
        "description_fail": "",

        "description_perfect_ua": "",
        "description_good_ua": "",
        "description_fail_ua": "",

        "flaw_perfect": "",
        "flaw_good": "",
        "flaw_fail": "",

        "flaw_perfect_ua": "",
        "flaw_good_ua": "",
        "flaw_fail_ua": "",
    },
    {
        "name": 'Плата индикации %s' % (model_name),
        "name_ua": 'Плата індикації %s' % (model_name),

        "description_small": f"Дополнительная плата индикации к ноутбуку {model_name}, оригинальная, {state}",
        "description_small_ua": f"Додаткова плата индикації до ноутбука {model_name}, оригінальна, {state_ua}",

        "keywords": "плата индикации, плата, индикация",
        "keywords_ua": "плата індикації, плата, індикація",
        "portal": "Адаптеры и платы расширения портов",
        
        "description_perfect": "",
        "description_good": "",
        "description_fail": "",

        "description_perfect_ua": "",
        "description_good_ua": "",
        "description_fail_ua": "",

        "flaw_perfect": "",
        "flaw_good": "",
        "flaw_fail": "",

        "flaw_perfect_ua": "",
        "flaw_good_ua": "",
        "flaw_fail_ua": "",
    },
    {
        "name": 'Корзина, крепление HDD/SSD %s (caddy)' % (model_name),
        "name_ua": 'Корзина, кріплення HDD/SSD %s (caddy)' % (model_name),

        "description_small": f"Корзина, крепление HDD или SSD к ноутбуку {model_name}, оригинальная, {state}",
        "description_small_ua": f"Корзина, кріплення HDD або SSD до ноутбука {model_name}, оригінальна, {state_ua}",

        "keywords": "корзина, крепление HDD/SSD, caddy",
        "keywords_ua": "корзина, крепление HDD/SSD, caddy",
        "portal": "Карманы для жестких дисков",
        
        "description_perfect": "",
        "description_good": "",
        "description_fail": "",

        "description_perfect_ua": "",
        "description_good_ua": "",
        "description_fail_ua": "",

        "flaw_perfect": "",
        "flaw_good": "",
        "flaw_fail": "",

        "flaw_perfect_ua": "",
        "flaw_good_ua": "",
        "flaw_fail_ua": "",
    },
    {
        "name": 'Шлейф матрицы %s' % (model_name),
        "name_ua": 'Шлейф матриці %s' % (model_name),

        "description_small": f"Шлейф матрицы к ноутбуку {model_name}, оригинальный, {state}",
        "description_small_ua": f"Шлейф матриці до ноутбука {model_name}, оригінальний, {state_ua}",

        "keywords": "шлейф матрицы, шлейф, матрица",
        "keywords_ua": "шлейф матриці, шлейф, матриця",
        "portal": "Шлейфы и разъемы для ноутбуков",
        
        "description_perfect": "",
        "description_good": "",
        "description_fail": "",

        "description_perfect_ua": "",
        "description_good_ua": "",
        "description_fail_ua": "",

        "flaw_perfect": "",
        "flaw_good": "",
        "flaw_fail": "",

        "flaw_perfect_ua": "",
        "flaw_good_ua": "",
        "flaw_fail_ua": "",
    },
    {
        "name": 'Разьем, адаптер, шлейф SATA HDD/SSD %s' % (model_name),
        "name_ua": "Роз'єм, адаптер, шлейф SATA HDD/SSD %s" % (model_name),

        "description_small": f"Разьем, адаптер, шлейф SATA HDD или SSD к ноутбуку {model_name}, оригинальный, {state}",
        "description_small_ua": f"Роз'єм, адаптер, шлейф SATA HDD або SSD до ноутбука {model_name}, оригінальний, {state_ua}",

        "keywords": "разьем, адаптер, шлейф, sata, hdd, ssd",
        "keywords_ua": "роз'єм, адаптер, шлейф, sata, hdd, ssd",
        "portal": "Шлейфы и разъемы для ноутбуков",
        
        "description_perfect": "",
        "description_good": "",
        "description_fail": "",

        "description_perfect_ua": "",
        "description_good_ua": "",
        "description_fail_ua": "",

        "flaw_perfect": "",
        "flaw_good": "",
        "flaw_fail": "",

        "flaw_perfect_ua": "",
        "flaw_good_ua": "",
        "flaw_fail_ua": "",
    },
    {
        "name": 'Разъем, гнездо, кабель питания %s' % (model_name),
        "name_ua": "Роз'єм, гніздо, кабель живлення %s" % (model_name),

        "description_small": f"Разъем питания, гнездо, и кабель подключения к ноутбуку {model_name}, оригинальный, {state}",
        "description_small_ua": f"Роз'єм живлення, гніздо та кабель підключення до ноутбука {model_name}, оригінальний, {state_ua}",

        "keywords": "разъем, гнездо, кабель питания, кабель, питание",
        "keywords_ua": "роз'єм, гніздо, кабель живлення, кабель, живлення",
        "portal": "Шлейфы и разъемы для ноутбуков",
        
        "description_perfect": "",
        "description_good": "",
        "description_fail": "",

        "description_perfect_ua": "",
        "description_good_ua": "",
        "description_fail_ua": "",

        "flaw_perfect": "",
        "flaw_good": "",
        "flaw_fail": "",

        "flaw_perfect_ua": "",
        "flaw_good_ua": "",
        "flaw_fail_ua": "",
    },
    {
        "name": 'Модуль Wi-Fi %s' % (model_name),
        "name_ua": 'Модуль Wi-Fi %s' % (model_name),

        "description_small": f"Модуль Wi-Fi к ноутбуку {model_name}, оригинальный, {state}",
        "description_small_ua": f"Модуль Wi-Fi до ноутбука {model_name}, оригінальний, {state_ua}",

        "keywords": "модуль Wi-Fi, модуль, wi-fi, wifi",
        "keywords_ua": "модуль Wi-Fi, модуль, wi-fi, wifi",
        "portal": "Адаптеры и платы расширения портов",
        
        "description_perfect": "",
        "description_good": "",
        "description_fail": "",

        "description_perfect_ua": "",
        "description_good_ua": "",
        "description_fail_ua": "",

        "flaw_perfect": "",
        "flaw_good": "",
        "flaw_fail": "",

        "flaw_perfect_ua": "",
        "flaw_good_ua": "",
        "flaw_fail_ua": "",
    },
    {
        "name": 'Модуль блютуз, bluetooth %s' % (model_name),
        "name_ua": 'Модуль блютуз, bluetooth %s' % (model_name),

        "description_small": f"Модуль блютуз к ноутбуку {model_name}, оригинальный, {state}",
        "description_small_ua": f"Модуль блютуз до ноутбука {model_name}, оригінальний, {state_ua}",

        "keywords": "модуль блютуз, bluetooth, модуль bluetooth",
        "keywords_ua": "модуль блютуз, bluetooth, модуль bluetooth",
        "portal": "Адаптеры и платы расширения портов",
        
        "description_perfect": "",
        "description_good": "",
        "description_fail": "",

        "description_perfect_ua": "",
        "description_good_ua": "",
        "description_fail_ua": "",

        "flaw_perfect": "",
        "flaw_good": "",
        "flaw_fail": "",

        "flaw_perfect_ua": "",
        "flaw_good_ua": "",
        "flaw_fail_ua": "",
    },
    {
        "name": 'ВЕБ-камера %s (WEB-camera)' % (model_name),
        "name_ua": 'ВЕБ-камера %s (WEB-camera)' % (model_name),

        "description_small": f"ВЕБ-камера к ноутбуку {model_name}, оригинальная, {state}",
        "description_small_ua": f"ВЕБ-камера до ноутбука {model_name}, оригінальна, {state_ua}",

        "keywords": "ВЕБ-камера, WEB-camera, камера, видео камера",
        "keywords_ua": "ВЕБ-камера, WEB-camera, камера, відео камера",
        "portal": "Камеры для портативных пк",
        
        "description_perfect": "",
        "description_good": "",
        "description_fail": "",

        "description_perfect_ua": "",
        "description_good_ua": "",
        "description_fail_ua": "",

        "flaw_perfect": "",
        "flaw_good": "",
        "flaw_fail": "",

        "flaw_perfect_ua": "",
        "flaw_good_ua": "",
        "flaw_fail_ua": "",
    },
    {
        "name": 'Шлейф ВЕБ-камеры %s (WEB-camera)' % (model_name),
        "name_ua": 'Шлейф ВЕБ-камери %s (WEB-camera)' % (model_name),

        "description_small": f"Шлейф подключения ВЕБ-камеры к ноутбуку {model_name}, оригинальный, {state}",
        "description_small_ua": f"Шлейф підключення ВЕБ-камери до ноутбука {model_name}, оригінальний, {state_ua}",

        "keywords": "шлейф ВЕБ-камеры, шлейф, ВЕБ-камера, WEB-camera, камера, видео камера",
        "keywords_ua": "шлейф ВЕБ-камери, шлейф, ВЕБ-камера, WEB-camera, камера, відео камера",
        "portal": "Шлейфы и разъемы для ноутбуков",
        
        "description_perfect": "",
        "description_good": "",
        "description_fail": "",

        "description_perfect_ua": "",
        "description_good_ua": "",
        "description_fail_ua": "",

        "flaw_perfect": "",
        "flaw_good": "",
        "flaw_fail": "",

        "flaw_perfect_ua": "",
        "flaw_good_ua": "",
        "flaw_fail_ua": "",
    },
    {
        "name": 'Инвертор матрицы %s' % (model_name),
        "name_ua": 'Інвертор матриці %s' % (model_name),

        "description_small": f"Инвертор матрицы к ноутбуку {model_name}, оригинальный, {state}",
        "description_small_ua": f"Інвертор матриці до ноутбука {model_name}, оригінальний, {state_ua}",

        "keywords": "инвертор матрицы, инвертор, матрица",
        "keywords_ua": "інвертор матриці, інвертор, матриця",
        "portal": "Шлейфы и разъемы для ноутбуков",
        
        "description_perfect": "",
        "description_good": "",
        "description_fail": "",

        "description_perfect_ua": "",
        "description_good_ua": "",
        "description_fail_ua": "",

        "flaw_perfect": "",
        "flaw_good": "",
        "flaw_fail": "",

        "flaw_perfect_ua": "",
        "flaw_good_ua": "",
        "flaw_fail_ua": "",
    },
    {
        "name": 'Микрофон %s' % (model_name),
        "name_ua": 'Мікрофон %s' % (model_name),

        "description_small": f"Микрофон к ноутбуку {model_name}, оригинальный, {state}",
        "description_small_ua": f"Мікрофон до ноутбука {model_name}, оригінальний, {state_ua}",

        "keywords": "микрофон, мик, mic",
        "keywords_ua": "мікрофон, мік, mic",
        "portal": "Адаптеры и платы расширения портов",
        
        "description_perfect": "",
        "description_good": "",
        "description_fail": "",

        "description_perfect_ua": "",
        "description_good_ua": "",
        "description_fail_ua": "",

        "flaw_perfect": "",
        "flaw_good": "",
        "flaw_fail": "",

        "flaw_perfect_ua": "",
        "flaw_good_ua": "",
        "flaw_fail_ua": "",
    },
    {
        "name": 'Антенна Wi-Fi %s' % (model_name),
        "name_ua": 'Антена Wi-Fi %s' % (model_name),

        "description_small": f"Антенна Wi-Fi к ноутбуку {model_name}, оригинальная, {state}",
        "description_small_ua": f"Антена Wi-Fi до ноутбука {model_name}, оригінальна, {state_ua}",

        "keywords": "антенна wi-fi, антенна wifi, антенна, антена, антена wifi, антена wi-fi, wifi, wi-fi",
        "keywords_ua": "антена wi-fi, антена wifi, антена, wi-fi, wifi",
        "portal": "Адаптеры и платы расширения портов",
        
        "description_perfect": "",
        "description_good": "",
        "description_fail": "",

        "description_perfect_ua": "",
        "description_good_ua": "",
        "description_fail_ua": "",

        "flaw_perfect": "",
        "flaw_good": "",
        "flaw_fail": "",

        "flaw_perfect_ua": "",
        "flaw_good_ua": "",
        "flaw_fail_ua": "",
    },
    {
        "name": 'Оригинальная батарея %s' % (model_name),
        "name_ua": 'Оригінальна батарея %s' % (model_name),

        "description_small": f"Оригинальная батарея к ноутбуку {model_name}, {state}",
        "description_small_ua": f"Оригінальна батарея до ноутбука {model_name}, {state_ua}",

        "keywords": "оригинальная батарея, оригинал батареи, батарея, оригинальный аккумулятор, аккумулятор",
        "keywords_ua": "оригіральна батарея, оригінал батареї, батарея, оригінальний акумулятор, акумулятор",
        "portal": "Аккумуляторы для ноутбуков",
        
        "description_perfect": "",
        "description_good": "",
        "description_fail": "",

        "description_perfect_ua": "",
        "description_good_ua": "",
        "description_fail_ua": "",

        "flaw_perfect": "",
        "flaw_good": "",
        "flaw_fail": "",

        "flaw_perfect_ua": "",
        "flaw_good_ua": "",
        "flaw_fail_ua": "",
    },
    {
        "name": 'Батарея %s' % (model_name),
        "name_ua": 'Батарея %s' % (model_name),

        "description_small": f"Батарея к ноутбуку {model_name}, {state}",
        "description_small_ua": f"Батарея до ноутбука {model_name}, {state_ua}",

        "keywords": "батарея, battery",
        "keywords_ua": "батарея, battery",
        "portal": "Аккумуляторы для ноутбуков",
        
        "description_perfect": "",
        "description_good": "",
        "description_fail": "",

        "description_perfect_ua": "",
        "description_good_ua": "",
        "description_fail_ua": "",

        "flaw_perfect": "",
        "flaw_good": "",
        "flaw_fail": "",

        "flaw_perfect_ua": "",
        "flaw_good_ua": "",
        "flaw_fail_ua": "",
    },
    {
        "name": 'Плата LED %s' % (model_name),
        "name_ua": 'Плата LED %s' % (model_name),

        "description_small": f"Плата LED к ноутбуку {model_name}, оригинальная, {state}",
        "description_small_ua": f"Плата LED до ноутбука {model_name}, оригінальна, {state_ua}",

        "keywords": "плата, плата led",
        "keywords_ua": "плата, плата led",
        "portal": "Части корпуса ноутбука",
        
        "description_perfect": "",
        "description_good": "",
        "description_fail": "",

        "description_perfect_ua": "",
        "description_good_ua": "",
        "description_fail_ua": "",

        "flaw_perfect": "",
        "flaw_good": "",
        "flaw_fail": "",

        "flaw_perfect_ua": "",
        "flaw_good_ua": "",
        "flaw_fail_ua": "",
    },
    {
        "name": 'Модем %s' % (model_name),
        "name_ua": 'Модем %s' % (model_name),

        "description_small": f"Модем к ноутбуку {model_name}, оригинальный, {state}",
        "description_small_ua": f"Модем до ноутбука {model_name}, оригінальний, {state_ua}",

        "keywords": "плата, плата led",
        "keywords_ua": "плата, плата led",
        "portal": "Адаптеры и платы расширения портов",
        
        "description_perfect": "",
        "description_good": "",
        "description_fail": "",

        "description_perfect_ua": "",
        "description_good_ua": "",
        "description_fail_ua": "",

        "flaw_perfect": "",
        "flaw_good": "",
        "flaw_fail": "",

        "flaw_perfect_ua": "",
        "flaw_good_ua": "",
        "flaw_fail_ua": "",
    },
    {
        "name": 'Матрица, экран, дисплей %s' % (model_name),
        "name_ua": 'Матриця, екран, дисплей %s' % (model_name),

        "description_small": f"Матрица к ноутбуку {model_name}, оригинальная, {state}",
        "description_small_ua": f"Матриця до ноутбука {model_name}, оригінальна, {state_ua}",

        "keywords": "матрица, экран, дисплей",
        "keywords_ua": "матриця, екран, дисплей",
        "portal": "Части корпуса ноутбука",
        
        "description_perfect": "",
        "description_good": "",
        "description_fail": "",

        "description_perfect_ua": "",
        "description_good_ua": "",
        "description_fail_ua": "",

        "flaw_perfect": "",
        "flaw_good": "",
        "flaw_fail": "",

        "flaw_perfect_ua": "",
        "flaw_good_ua": "",
        "flaw_fail_ua": "",
    },
    {
        "name": 'Разъем модема %s' % (model_name),
        "name_ua": "Роз'єм модема %s" % (model_name),

        "description_small": f"Разъем модема к ноутбуку {model_name}, оригинальная, {state}",
        "description_small_ua": f"Роз'єм модема до ноутбука {model_name}, оригінальна, {state_ua}",

        "keywords": "разъем модема, разъем, кабель модема, к модему",
        "keywords_ua": "роз'єм модема, роз'єм, кабель модема, до модему",
        "portal": "Шлейфы и разъемы для ноутбуков",
        
        "description_perfect": "",
        "description_good": "",
        "description_fail": "",

        "description_perfect_ua": "",
        "description_good_ua": "",
        "description_fail_ua": "",

        "flaw_perfect": "",
        "flaw_good": "",
        "flaw_fail": "",

        "flaw_perfect_ua": "",
        "flaw_good_ua": "",
        "flaw_fail_ua": "",
    },
    {
        "name": 'Динамик левый %s' % (model_name),
        "name_ua": 'Динамік лівий %s' % (model_name),

        "description_small": f"Динамик левый к ноутбуку {model_name}, оригинальный, {state}",
        "description_small_ua": f"Динамік лівий до ноутбука {model_name}, оригінальий, {state_ua}",

        "keywords": "динамики, колонки, динамик, колонка, динамик ноутбука, колонка ноутбука, дифузор, звук, саунд, sound",
        "keywords_ua": "динаміки, колонки, динамік, колонка, динамік ноутбука, динаміки ноутбуку, колонка ноутбука, дифузор, звук, саунд, sound",
        "portal": "Звуковые запчасти для портативных пк",
        
        "description_perfect": "Динамик проверен на работоспособность - работает.",
        "description_good": "",
        "description_fail": "",

        "description_perfect_ua": "Динамік перевірений на працездатність - працює.",
        "description_good_ua": "",
        "description_fail_ua": "",

        "flaw_perfect": "",
        "flaw_good": "",
        "flaw_fail": "",

        "flaw_perfect_ua": "",
        "flaw_good_ua": "",
        "flaw_fail_ua": "",
    },
    {
        "name": 'Динамик правый %s' % (model_name),
        "name_ua": 'Динамік правий %s' % (model_name),

        "description_small": f"Динамик правый к ноутбуку {model_name}, оригинальный, {state}",
        "description_small_ua": f"Динамік правий до ноутбука {model_name}, оригінальий, {state_ua}",

        "keywords": "динамики, колонки, динамик, колонка, динамик ноутбука, колонка ноутбука, дифузор, звук, саунд, sound",
        "keywords_ua": "динаміки, колонки, динамік, колонка, динамік ноутбука, динаміки ноутбуку, колонка ноутбука, дифузор, звук, саунд, sound",
        "portal": "Звуковые запчасти для портативных пк",
        
        "description_perfect": "Динамик проверен на работоспособность - работает.",
        "description_good": "",
        "description_fail": "",

        "description_perfect_ua": "Динамік перевірений на працездатність - працює.",
        "description_good_ua": "",
        "description_fail_ua": "",

        "flaw_perfect": "",
        "flaw_good": "",
        "flaw_fail": "",

        "flaw_perfect_ua": "",
        "flaw_good_ua": "",
        "flaw_fail_ua": "",
    },
    {
        "name": 'Накладка, на среднюю часть корпуса %s' % (model_name),
        "name_ua": 'Накладка, на середню частину корпуса %s' % (model_name),

        "description_small": f"Накладка, на среднюю часть корпуса к ноутбуку {model_name}, оригинальный, {state}",
        "description_small_ua": f"Накладка, на середню частину корпуса до ноутбука {model_name}, оригінальий, {state_ua}",

        "keywords": "накладка, накладка на среднюю часть, топкейс, средняя часть, верхняя крышка, палмрест, palmrest, верхняя крышка базы",
        "keywords_ua": "накладка, накладка на середню частину, топкейс, средня частина, верхня кришка, палмрест, palmrest, верхня кришка бази",
        "portal": "Части корпуса ноутбука",
        
        "description_perfect": "Накладка вымыта и почищена.",
        "description_good": "",
        "description_fail": "",

        "description_perfect_ua": "Накладка вимита та почищена.",
        "description_good_ua": "",
        "description_fail_ua": "",

        "flaw_perfect": "",
        "flaw_good": "",
        "flaw_fail": "",

        "flaw_perfect_ua": "",
        "flaw_good_ua": "",
        "flaw_fail_ua": "",
    },
    {
        "name": 'Топкейс, средняя часть %s (верхняя крышка)' % (model_name),
        "name_ua": 'Топкейс, середня частина %s (верхня кришка)' % (model_name),

        "description_small": f"Топкейс, средняя часть к ноутбуку {model_name}, оригинальный, {state}",
        "description_small_ua": f"Топкейс, середня частина до ноутбука {model_name}, оригінальий, {state_ua}",

        "keywords": "топкейс, средняя часть, верхняя крышка, палмрест, palmrest, верхняя крышка базы",
        "keywords_ua": "топкейс, средня частина, верхня кришка, палмрест, palmrest, верхня кришка бази",
        "portal": "Части корпуса ноутбука",
        
        "description_perfect": "Крышка вымыта и почищена.",
        "description_good": "",
        "description_fail": "",

        "description_perfect_ua": "Кришка вимита та почищена.",
        "description_good_ua": "",
        "description_fail_ua": "",

        "flaw_perfect": "",
        "flaw_good": "",
        "flaw_fail": "",

        "flaw_perfect_ua": "",
        "flaw_good_ua": "",
        "flaw_fail_ua": "",
    },
    {
        "name": 'Топкейс, средняя часть с клавиатурой %s (верхняя крышка)' % (model_name),
        "name_ua": 'Топкейс, средня частина з клавіатурою %s (верхня кришка)' % (model_name),

        "description_small": f"Топкейс, средняя часть с клавиатурой к ноутбуку {model_name}, оригинальный, {state}",
        "description_small_ua": f"Топкейс, средня частина з клавіатурою до ноутбука {model_name}, оригінальий, {state_ua}",

        "keywords": "топкейс, средняя часть, клавиатура, palmrest, верхняя крышка базы",
        "keywords_ua": "топкейс, средня частина, клавіатура, palmrest, верхня кришка бази",
        "portal": "Части корпуса ноутбука",
        
        "description_perfect": "Крышка вымыта и почищена. Клавиатура проверена специальным прибором, все кнопки работают и не хрустят.",
        "description_good": "",
        "description_fail": "",

        "description_perfect_ua": "Кришка вимита та почищена. Клавіатура перевірена спеціальним прибором, всі кнопки працюють та не хрустят.",
        "description_good_ua": "",
        "description_fail_ua": "",

        "flaw_perfect": "",
        "flaw_good": "",
        "flaw_fail": "",

        "flaw_perfect_ua": "",
        "flaw_good_ua": "",
        "flaw_fail_ua": "",
    },
    {
        "name": 'Топкейс, средняя часть с клавиатурой и тачпадом %s (верхняя крышка)' % (model_name),
        "name_ua": 'Топкейс, средня частина з клавіатурою та тачпадом %s (верхня кришка)' % (model_name),

        "description_small": f"Топкейс, средняя часть с клавиатурой и тачпадом к ноутбуку {model_name}, оригинальный, {state}",
        "description_small_ua": f"Топкейс, средня частина з клавіатурою та тачпадом до ноутбука {model_name}, оригінальий, {state_ua}",

        "keywords": "топкейс, средняя часть, клавиатура, palmrest, верхняя крышка базы, плата тачпад, тачпад, touchpad, трекпад",
        "keywords_ua": "топкейс, средня частина, клавіатура, palmrest, верхня кришка бази, плата тачпад, тачпад, touchpad, трекпад",
        "portal": "Части корпуса ноутбука",
        
        "description_perfect": "Крышка вымыта и почищена. Клавиатура проверена специальным прибором, все кнопки работают и не хрустят. Тачпад.",
        "description_good": "",
        "description_fail": "",

        "description_perfect_ua": "Кришка вимита та почищена. Клавіатура перевірена спеціальним прибором, всі кнопки працюють та не хрустят. Тачпад.",
        "description_good_ua": "",
        "description_fail_ua": "",

        "flaw_perfect": "",
        "flaw_good": "",
        "flaw_fail": "",

        "flaw_perfect_ua": "",
        "flaw_good_ua": "",
        "flaw_fail_ua": "",
    },
    {
        "name": 'Топкейс, средняя часть с тачпадом %s (верхняя крышка)' % (model_name),
        "name_ua": 'Топкейс, средня частина та тачпад %s (верхня кришка)' % (model_name),

        "description_small": f"Топкейс, средняя часть с тачпадом к ноутбуку {model_name}, оригинальный, {state}",
        "description_small_ua": f"Топкейс, средня частина та тачпад до ноутбука {model_name}, оригінальий, {state_ua}",

        "keywords": "топкейс, средняя часть, palmrest, верхняя крышка базы, плата тачпад, тачпад, touchpad, трекпад",
        "keywords_ua": "топкейс, средня частина, palmrest, верхня кришка бази, плата тачпад, тачпад, touchpad, трекпад",
        "portal": "Части корпуса ноутбука",
        
        "description_perfect": "Крышка вымыта и почищена. Тачпад.",
        "description_good": "",
        "description_fail": "",

        "description_perfect_ua": "Кришка вимита та почищена. Тачпад.",
        "description_good_ua": "",
        "description_fail_ua": "",

        "flaw_perfect": "",
        "flaw_good": "",
        "flaw_fail": "",

        "flaw_perfect_ua": "",
        "flaw_good_ua": "",
        "flaw_fail_ua": "",
    },
    {
        "name": 'Направляющие матрицы %s' % (model_name),
        "name_ua": 'Направляючі матриці %s' % (model_name),

        "description_small": f"Направляющие матрицы к ноутбуку {model_name}, оригинальные, {state}",
        "description_small_ua": f"Направляючі матриці до ноутбука {model_name}, оригінальні, {state_ua}",

        "keywords": "направляющие матрицы, матрица, направляющие к матрице, направляющие экрана, стойки, стойки матрицы, стойки экрана",
        "keywords_ua": "направляючі матриці, матрица, направляючі до матриці, направляючі екрану, стійки, стійки матриці, стійки екрану",
        "portal": "Части корпуса ноутбука",
        
        "description_perfect": "",
        "description_good": "",
        "description_fail": "",

        "description_perfect_ua": "",
        "description_good_ua": "",
        "description_fail_ua": "",

        "flaw_perfect": "",
        "flaw_good": "",
        "flaw_fail": "",

        "flaw_perfect_ua": "",
        "flaw_good_ua": "",
        "flaw_fail_ua": "",
    },
    {
        "name": 'Кнопка включения %s (вкл/выкл)' % (model_name),
        "name_ua": 'Кнопка включення (живлення) %s (вкл/викл)' % (model_name),

        "description_small": f"Кнопка включения к ноутбуку {model_name}, оригинальная, {state}",
        "description_small_ua": f"Кнопка живлення до ноутбука {model_name}, оригінальна, {state_ua}",

        "keywords": "кнопка включения, кнопка питания",
        "keywords_ua": "кнопка включення, кнопка живлення",
        "portal": "Части корпуса ноутбука",
        
        "description_perfect": "Кнопка вымыта и почищена.",
        "description_good": "",
        "description_fail": "",

        "description_perfect_ua": "Кнопка вимита та почищена.",
        "description_good_ua": "",
        "description_fail_ua": "",

        "flaw_perfect": "",
        "flaw_good": "",
        "flaw_fail": "",

        "flaw_perfect_ua": "",
        "flaw_good_ua": "",
        "flaw_fail_ua": "",
    },
    {
        "name": "Соединительная плата %s" % (model_name),
        "name_ua": "З'єднуюча плата %s" % (model_name),

        "description_small": f"Соединительная плата к ноутбуку {model_name}, оригинальная, {state}",
        "description_small_ua": f"З'єднуюча плата до ноутбука {model_name}, оригінальна, {state_ua}",

        "keywords": "плата, соединительная плата",
        "keywords_ua": "плата, з'єднуюча плата",
        "portal": "Адаптеры и платы расширения портов",
        
        "description_perfect": "Кнопка вымыта и почищена.",
        "description_good": "",
        "description_fail": "",

        "description_perfect_ua": "Кнопка вимита та почищена.",
        "description_good_ua": "",
        "description_fail_ua": "",

        "flaw_perfect": "",
        "flaw_good": "",
        "flaw_fail": ""
        ,
        "flaw_perfect_ua": "",
        "flaw_ugood_a": "",
        "flaw_ufail_a": "",
    },
    {
        "name": "Шлейф нотбука %s" % (model_name),
        "name_ua": "Шлейф ноутбуку %s" % (model_name),

        "description_small": f"Шлейф к ноутбуку {model_name}, оригинальная, {state}",
        "description_small_ua": f"Шлейф до ноутбука {model_name}, оригінальна, {state_ua}",

        "keywords": "шлейф, кабель, провод, соединительный шлейф",
        "keywords_ua": "шлейф, кабель, провід, з'єднуючий шлейф",
        "portal": "Части корпуса ноутбука",
        
        "description_perfect": "Кнопка вымыта и почищена.",
        "description_good": "",
        "description_fail": "",

        "description_perfect_ua": "Кнопка вимита та почищена.",
        "description_good_ua": "",
        "description_fail_ua": "",

        "flaw_perfect": "",
        "flaw_good": "",
        "flaw_fail": ""
        ,
        "flaw_perfect_ua": "",
        "flaw_ugood_a": "",
        "flaw_ufail_a": "",
    },
    {
        "name": "Датчик закрытия крышки (кнопка) %s" % (model_name),
        "name_ua": "Датчик закриття кришки (кнопка) %s" % (model_name),

        "description_small": f"Датчик закрытия крышки к ноутбуку {model_name}, оригинальная, {state}",
        "description_small_ua": f"Датчик закриття кришки до ноутбука {model_name}, оригінальна, {state_ua}",

        "keywords": "датчик, кнопка, датчик закрытия, датчик закрытия крышки",
        "keywords_ua": "датчик, кнопка, датчик закриття, датчик закриття кришки",
        "portal": "Адаптеры и платы расширения портов",
        
        "description_perfect": "",
        "description_good": "",
        "description_fail": "",

        "description_perfect_ua": "",
        "description_good_ua": "",
        "description_fail_ua": "",

        "flaw_perfect": "",
        "flaw_good": "",
        "flaw_fail": ""
        ,
        "flaw_perfect_ua": "",
        "flaw_ugood_a": "",
        "flaw_ufail_a": "",
    },
    {
        "name": 'Заглушка кардридера %s' % (model_name),
        "name_ua": 'Заглушка кардрідера %s' % (model_name),

        "description_small": f"Заглушка кардридера к ноутбуку {model_name}, оригинальная, {state}",
        "description_small_ua": f"Заглушка кардрідера до ноутбука {model_name}, оригінальна, {state_ua}",

        "keywords": "заглушка кардридера, заглушки, заглушка",
        "keywords_ua": "заглушка кардрідера, заглушки, заглушка",
        "portal": "Части корпуса ноутбука",
        
        "description_perfect": "",
        "description_good": "",
        "description_fail": "",

        "description_perfect_ua": "",
        "description_good_ua": "",
        "description_fail_ua": "",

        "flaw_perfect": "",
        "flaw_good": "",
        "flaw_fail": "",

        "flaw_perfect_ua": "",
        "flaw_good_ua": "",
        "flaw_fail_ua": "",
    },
]

# TODO
# - Заглушка кардридера
