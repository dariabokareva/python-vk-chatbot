from command_enum import Command, Message
import re


class Commander:

    def __init__(self):

        # Для запоминания последней команды
        self.last_command = None

        # Для запомминания ответов пользователя
        self.last_ans = None

    def input(self, msg):
        """
        Функция принимающая сообщения пользователя
        :param msg: Сообщение
        :return: Ответ пользователю, отправившему сообщение
        """
        # if msg in Command.start.value:
        if re.search('начать', msg):
            self.last_command = Command.start
            return Message.start_msg.value

        if self.last_command in [Command.description, Command.kids, Command.teenagers]:
            if re.search('11|12|13', msg):
                self.last_command = Command.kids
                return Message.kids_msg.value

            elif re.search('14|15|16', msg):
                self.last_command = Command.teenagers
                return Message.teenagers_msg.value

            elif re.search('0|назад', msg):
                self.last_command = None
                return Message.start_msg.value

            else:
                self.last_command = Command.description
                return Message.wrong_msg.value

        if re.search('1|о мероприятии|описание', msg) and self.last_command != Command.reg:
            self.last_command = Command.description
            return Message.description_msg.value

        if re.search('2|возраст|лет', msg) and self.last_command != Command.reg:
            self.last_command = Command.age
            return Message.age_msg.value

        if re.search('3|цены|цена|стоимость', msg) and self.last_command != Command.reg:
            self.last_command = Command.cost
            return Message.cost_msg.value

        if re.search('4|расписание', msg) and self.last_command != Command.reg:
            self.last_command = Command.schedule
            return Message.schedule_msg.value

        if re.search('записаться', msg):
            self.last_command = Command.reg
            return Message.reg_msg.value

        if self.last_command == Command.reg:
            self.last_command = Command.age
            return Message.thx_msg.value

        return 'Я не знаю такой команды &#128532;'
