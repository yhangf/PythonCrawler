import requests
from bs4 import BeautifulSoup
import json


headers = {
    'Host': "github.com",
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:44.0) Gecko/20100101 Firefox/44.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive'
}


class GitHub():

    def __init__(self):
        self.session = requests.session()
        self.timeline = []
        self.name = ''
        self.user = ''
        self.passwd = ''

    def login(self):
        self.user = input('please input username:')
        self.passwd = input('please input password:')
        html = self.session.get('https://github.com/login', headers=headers).text
        authenticity_token = BeautifulSoup(html, 'lxml').find(
            'input', {'name': 'authenticity_token'}).get('value')
        data = {
            'commit': "Sign+in",
            'utf8': "✓",
            'login': self.user,
            'password': self.passwd,
            'authenticity_token': authenticity_token
        }
        html = self.session.post('https://github.com/session', data=data, headers=headers).text
        self.name = BeautifulSoup(html, 'lxml').find(
            'strong', {'class': 'css-truncate-target'}).get_text()

    def get_timeline(self, page=1):
        html = self.session.get(
            'https://github.com/dashboard/index/{page}?utf8=%E2%9C%93'.format(page=page), headers=headers).text
        table = BeautifulSoup(html, 'lxml').find(
            'div', id='dashboard').find_all('div', {'class': 'alert'})
        for item in table:
            line = {}
            line['thing'] = item.find('div', {'class': 'title'}).get_text(
            ).replace('\r', '').replace('\n', '')
            line['time'] = item.find('relative-time').get('datetime')
            self.timeline.append(line)

    def show_timeline(self):
        keys = ['who', 'do', 'to', 'time']
        for line in self.timeline:
            text = line['time'] + ' ' + line['thing']
            print('*' + text + ' ' * (80 - len(text) - 2) + '*')
            print('*-*-*' * 16)

    def overview(self, user=None):
        if user == None:
            user = self.name
        html = self.session.get('https://github.com/' + user, headers=headers).text
        return overview

    
