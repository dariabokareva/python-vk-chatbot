from enum import Enum


class Command(Enum):
    """Класс, содержащий перечисление команд"""

    """Начать"""
    start = ["Начать", "начать", "start", "Start"]

    """ О мероприятии """
    description = ["1", "О мероприятии", "🔥 О мероприятии", "о мероприятии", "описание"]

    """ Возраст """
    age = ["2", "Возраст", "👶 Возраст", "возраст"]

    """ Цена """
    cost = "Цена"

    """ Расписание """
    schedule = "Расписание"

    reg = "Записаться"

    """Возрастная группа 11-13 лет"""
    kids = ["11-13 лет"]

    """Возрастная группа 14-16 лет"""
    teenagers = ["14-16 лет"]


class Message(Enum):
    """Класс, содержащий перечисление сообщений для каждой команды"""

    start_msg = 'вот, что я могу подсказать:\n\n1&#8419; Информацию о мероприятии\n2&#8419; Возраст участников\n' \
                '3&#8419; Стоимость участия\n4&#8419; Расписание\n\nВыбери интересующую тебя команду!'

    description_msg = '&#128165;Образовательный интенсив SMM-kids – это курс для школьников по освоению необходимых ' \
                      'инструментов и созданию стратегии собственного продвижения &#128285;\n\n' \
                      'Курс рассчитан на две возрастные группы.\n' \
                      'Чтобы узнать подробную информацию, укажите возраст вашего ребёнка или выберите возрастную ' \
                      'категорию в меню&#128071;'

    age_msg = 'Курс рассчитан на детей в возрасте от 11 до 16 лет &#128522;'

    cost_msg = '&#128176; Цена курса:\n\n&#9989; При внесении суммы одним платежом – 5800 р.\n' \
               '&#9989; При рассрочке на два платежа – 6000 р.\n' \
               '&#9989; Возможен возврат 13%'

    schedule_msg = '&#128197; Расписание:\n\n&#9999; Вторник/среда/четверг/пятница с 18.00 до 19.30 по согласованию.\n' \
                   '&#9999; 10 встреч, одно занятие в неделю'

    kids_msg = 'Группа 11-13 лет:\n\n' \
               '&#9989; Особенности соц. сетей ВКонтакте, Instagram, Like, YouTube\n' \
               '&#9989; Основы безопасности в соц. сетях\n' \
               '&#9989; Ведение аккаунтов для формирования личного бренда\n' \
               '&#9989; Создание контента на мобильный, бесплатные приложения для фото и видео\n' \
               '&#9989; Копирайтинг и сторителлинг, как написать продающий текст?\n' \
               '&#9989; Как стать блогером и использовать это для получения дохода?\n' \
               '&#9989; Где черпать вдохновение? Примеры успешных аккаунтов kids-блогеров\n' \
               '&#9989; Таргетированная реклама и реклама у блогеров. Продвижение в соц. сетях. ' \
               'Знакомство с рекламным кабинетом ВКонтакте, Instagram.\n' \
               '&#9989; Онлайн сопровождение на протяжении всего курса.\n\n' \
               '0&#8419; или \'Назад\' - Выйти в главное меню'

    teenagers_msg = 'Группа 14-16 лет:\n\n' \
                    '&#9989; Особенности соц. сетей ВКонтакте, Instagram, Facebook, TikTok, YouTube\n' \
                    '&#9989; Создание контента на мобильный, бесплатные приложения для фото и видео\n' \
                    '&#9989; Копирайтинг и сторителлинг, как написать продающий текст?\n' \
                    '&#9989; Варианты заработка в интернете: дизайн, копирайтинг, таргетинг\n' \
                    '&#9989; Где найти заказчика?\n' \
                    '&#9989; Таргетированная реклама и реклама у блогеров. Продвижение в соц. сетях\n' \
                    '&#9989; Создание личного рекламного кабинета ВКонтакте, Instagram и Facebook. ' \
                    'Практическое занятие: создание макета, написание текста, настройка рекламы по тех. заданию\n' \
                    '&#9989; Сбор аудитории ретаргетинга\n&#9989; Онлайн сопровождение на протяжении всего курса\n\n' \
                    '0&#8419; или \'Назад\' - Выйти в главное меню'

    reg_msg = 'Отлично! Напишите контакты (тел., email или др.), по которым менеджер сможет связаться с вами в ' \
              'ближайшее время'

    thx_msg = 'Спасибо за заявку! В ближайшее время с вами свяжется менеджер и сообщит подроности&#128522;'

    wrong_msg = '0&#8419; - Выйти в главное меню'