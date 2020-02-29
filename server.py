import vk_api
import vk_api.vk_api
import random
from vk_api.longpoll import VkLongPoll
from vk_api.longpoll import VkEventType
from command_enum import Message
from commander import Commander
import sheet
import datetime
import pytz


class Server:

    def start(self):
        for event in self.long_poll.listen():  # Слушаем сервер
            # Пришло новое сообщение
            if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
                if event.user_id not in self.users:
                    self.users[event.user_id] = Commander()

                user_id = event.user_id
                username = self.get_user_name(user_id)[0]
                lastname = self.get_user_name(user_id)[1]
                user = username + " " + lastname
                link = "vk.com/id" + str(user_id)
                message_out = self.users[event.user_id].input(event.text.lower())
                kbd = open("keyboard.json", "r", encoding="UTF-8").read()

                if message_out in [Message.description_msg.value, Message.kids_msg.value, Message.teenagers_msg.value,
                                   Message.wrong_msg.value]:
                    kbd = open("keyboard_age.json", "r", encoding="UTF-8").read()

                if message_out == Message.start_msg.value:
                    message_out = username + ", " + Message.start_msg.value
                self.send_message(user_id, message_out, kbd)

                if message_out in [Message.cost_msg.value, Message.schedule_msg.value, Message.reg_msg.value,
                                   Message.thx_msg.value]:
                    if message_out == Message.cost_msg.value:
                        message = 'Цена'
                    elif message_out in [Message.thx_msg.value, Message.reg_msg.value]:
                        message = 'Хочу записаться'
                    else:
                        message = 'Расписание'

                    if link in sheet.df["Link"].values:
                        sheet.df['Message'] = sheet.np.select([sheet.df['Link'] == link], [message],
                                                              sheet.df['Message'])
                        if message_out == Message.thx_msg.value:
                            sheet.df['Other'] = sheet.np.select([sheet.df['Link'] == link], [event.text],
                                                                  sheet.df['Other'])
                        result = sheet.dataframe_to_list(sheet.df)
                        sheet.sheet_append(sheet.sheet, result)
                    else:
                        time = datetime.datetime.now(tz=pytz.timezone('Europe/Moscow'))
                        if message_out == Message.thx_msg.value:
                            data = [time.strftime("%d/%m/%Y %H:%M"), user, link, message, event.text]
                        else:
                            data = [time.strftime("%d/%m/%Y %H:%M"), user, link, message, '']
                        result = sheet.df_append(sheet.df, data)[1]
                        sheet.df = sheet.df_append(sheet.df, data)[0]
                        sheet.sheet_append(sheet.sheet, result)
                    sheet.df.to_csv("copy.csv", encoding="UTF-8-sig")

    def __init__(self, api_token, server_name: str = "Empty"):  # параметр group_id
        self.server_name = server_name

        # Для Long Poll
        self.vk = vk_api.VkApi(token=api_token)

        # Для использования Long Poll API
        self.long_poll = VkLongPoll(self.vk)

        # Для вызова методов vk_api
        self.vk_api = self.vk.get_api()

        self.users = {}

    def send_message(self, send_id, message, keyboard):
        """
        Отправка сообщения через метод messages.send
        :param send_id: vk id пользователя, который получит сообщение
        :param message: содержимое отправляемого письма
        :param keyboard: клавиатура для пользователя
        :return: None
        """
        return self.vk_api.messages.send(user_id=send_id,
                                         message=message,
                                         random_id=random.randint(0, 2048),
                                         keyboard=keyboard)

    def get_user_name(self, user_id):
        """ Функция, возвращающая имя и фамилию пользователя"""
        user_name = self.vk_api.users.get(user_id=user_id)[0]['first_name']
        user_lastname = self.vk_api.users.get(user_id=user_id)[0]['last_name']
        return user_name, user_lastname
