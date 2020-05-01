# Simple chatbot for VK with Python
Простой чат-бот для сообщества ВКонтакте, написанный на *Python* с использованием модуля *vk-api*

## Software stack
* *IDE PyCharm*
* *Python 3.6*
* *vk-api*
* *Long Poll API*

## Deployment
Чтобы запустить бота, необходимо получить ключ доступа вашего сообщества ВКонтакте. Для этого перейдите во вкладку "Управление -> Работа с API" и создайте новый ключ (предоставьте доступ к сообщениям сообщества). Скопируйте ключ в переменную *vk_api_token* в *config.py*. Затем перейдите во вкладку "Long Poll API" и включите его (версия API: 5.50). Включите "Возможности ботов" на странице "Сообщения -> Настройки для ботов", а также добавьте кнопку "Начать". Запустите файл *server_manager.py* и отправьте боту сообщение "Начать".

To run the bot you need to get access token of your vk public - create access token in the settings (enable access to messages), copy your token and paste it in the config.py. Then go to "Long Poll API" on the same page and activate it (API version: 5.50). Check page "Messages -> Settings for the bot".
Run server_manager.py and send message "Start".
