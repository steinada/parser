import requests
from authorization import Authorization


class DataReader:
    def __init__(self, username, password):
        self.phones = set()
        self.username = username
        self.password = password
        self.authorization = Authorization(url='https://123.farfor.pw/users/e/login/',
                                           username=self.username, password=self.password)

    def data_reader(self, start_url, path=None):
        if path == '':
            url = start_url
        else:
            url = f'https://123.farfor.pw{path}'
        request = requests.get(url, cookies={'csrftoken': self.authorization.csrftoken,
                                             'sessionid': self.authorization.sessionid})
        request_json = request.json()
        return request_json
