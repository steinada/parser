import requests


class Authorization:
    def __init__(self, url, username, password):
        self.csrftoken = None
        self.sessionid = None
        self.url = url
        self.username = username
        self.password = password
        self.get_cookies(url=self.url, username=self.username, password=self.password)

    def get_cookies(self, url, username, password):
        authorize = requests.post(url, data={'username': username, 'password': password})

        if authorize.status_code == 200:
            token = authorize.cookies
            self.csrftoken = token.get('csrftoken')
            self.sessionid = token.get('sessionid')
        else:
            print('Ошибка авторизации')
