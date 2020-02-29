from server import Server
from config import vk_api_token


server1 = Server(vk_api_token, "server1")
# vk_api_token - API токен, который мы ранее создали
# "server1" - имя сервера

server1.start()
