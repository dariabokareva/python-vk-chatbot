from enum import Enum


class Command(Enum):
    """Класс, содержащий перечисление команд"""

    """Начать"""
    start = ["Начать", "начать", "start", "Start"]

    """ О мероприятии """
    description = ["1", "О мероприятии"]

    """ Возраст """
    age = ["2", "Возраст"]

    """ Цена """
    cost = "Цена"

    """ Расписание """
    schedule = "Расписание"

    """ Запись """
    reg = "Записаться"

    """Возрастная группа 11-13 лет"""
    kids = ["11-13 лет"]

    """Возрастная группа 14-16 лет"""
    teenagers = ["14-16 лет"]


class Message(Enum):
    """Класс, содержащий перечисление сообщений для каждой команды"""

    start_msg = 'вот, что я могу подсказать:\n\n1&#8419; Информацию о мероприятии\n2&#8419; Возраст участников\n' \
                '3&#8419; Стоимость участия\n4&#8419; Расписание\n\nВыбери интересующую тебя команду!'

    description_msg = 'Some description'

    age_msg = 'Age'

    cost_msg = 'Cost'

    schedule_msg = 'Schedule'

    kids_msg = 'Kids description'

    teenagers_msg = 'Teenagers description'

    reg_msg = 'Leave a request'

    thx_msg = 'Thanks for request'

    wrong_msg = '0&#8419; - Go back'
