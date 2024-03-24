from reader import DataReader
import re


class Parser:
    def __init__(self, start_url, username, password):
        self.start_url = start_url
        self.username = username
        self.password = password
        self.reader = DataReader(username=self.username, password=self.password)

    def write_data(self):
        path = ''
        page = 1
        while path is not None:
            json_data = self.reader.data_reader(start_url=self.start_url, path=path)
            with open('result_file.txt', 'a', encoding='utf-8') as file:
                users_info = self.parse_data(json_data['objects'], page=page)
                file.write(users_info)
            path = json_data['meta']['next']
            page += 1
        print('Обработка завершена')

    def parse_data(self, data, page):
        result = ''
        for obj in data:
            if obj['phones']:
                phone = obj['phones'][0]['phone']
                if phone not in self.reader.phones:
                    name = obj['full_name']
                    name = re.sub(r'\[([a-z]+)\]', '', name)
                    result += f'{name} {phone}\n'
                self.reader.phones.add(phone)
        print(f'Страница {page} обработана')
        return result
