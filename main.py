from parser import Parser
from config import settings


# страница, с которой начнется парсинг
start_url = settings.start_url

# логин и пароль юзера для авторизации
username = settings.login
password = settings.password

# запуск приложения
parser = Parser(start_url=start_url, username=username, password=password)
parser.write_data()
