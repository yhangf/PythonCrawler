import requests
from bs4 import BeautifulSoup

url = 'http://tieba.baidu.com/p/4178314700'


def GetHtml(url):
    html = requests.get(url).text
    return html


def GetImg(html):
    soup = BeautifulSoup(html, 'html.parser')
    imglist = []
    for photourl in soup.find_all('img'):
        imglist.append(photourl.get('src'))
    x = 0
    for imgurl in imglist:
        with open('E:/Pic/%s.jpg' % x, 'wb') as file:
            file.write(requests.get(imgurl).content)
            x += 1

if __name__ == '__main__':
    html = GetHtml(url)
    GetImg(html)
