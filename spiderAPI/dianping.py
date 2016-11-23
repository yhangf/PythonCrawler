import requests
import json
import os
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:39.0) Gecko/20100101 Firefox/39.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive'}


def bestRestaurant(cityId=1, rankType='popscore'):
    html = requests.get('http://www.dianping.com/mylist/ajax/shoprank?cityId=%s&shopType=10&rankType=%s&categoryId=0' %
                        (cityId, rankType), headers=headers).text
    result = json.loads(html)['shopBeans']
    return result


def getCityId():
    citys = {'北京': '2', '上海': '1', '广州': '4', '深圳': '7', '成都': '8', '重庆': '9', '杭州': '3', '南京': '5', '沈阳': '18', '苏州': '6', '天津': '10',
             '武汉': '16', '西安': '17', '长沙': '344', '大连': '19', '济南': '22', '宁波': '11', '青岛': '21', '无锡': '13', '厦门': '15', '郑州': '160'}
    return citys


def getRankType():
    RankType = {'最佳餐厅': 'score', '人气餐厅': 'popscore',
                '口味最佳': 'score1', '环境最佳': 'score2', '服务最佳': 'score3'}
    return RankType


def dpindex(cityId=1, page=1):
    url = 'http://dpindex.dianping.com/dpindex?region=&category=&type=rank&city=%s&p=%s' % (
        cityId, page)
    html = requests.get(url, headers=headers).text
    table = BeautifulSoup(html, 'lxml').find(
        'div', attrs={'class': 'idxmain-subcontainer'}).find_all('li')
    result = []
    for item in table:
        shop = {}
        shop['name'] = item.find('div', attrs={'class': 'field-name'}).get_text()
        shop['url'] = item.find('a').get('href')
        shop['num'] = item.find('div', attrs={'class': 'field-num'}).get_text()
        shop['addr'] = item.find('div', attrs={'class': 'field-addr'}).get_text()
        shop['index'] = item.find('div', attrs={'class': 'field-index'}).get_text()
        result.append(shop)
    return result


def restaurantList(url):
    html = requests.get(url, headers=headers, timeout=30).text.replace('\r', '').replace('\n', '')
    table = BeautifulSoup(html, 'lxml').find('div', id='shop-all-list').find_all('li')
    result = []
    for item in table:
        shop = {}
        soup = item.find('div', attrs={'class': 'txt'})
        tit = soup.find('div', attrs={'class': 'tit'})
        comment = soup.find('div', attrs={'class': 'comment'})
        tag_addr = soup.find('div', attrs={'class': 'tag-addr'})
        shop['name'] = tit.find('a').get_text()
        shop['star'] = comment.find('span').get('title')
        shop['review-num'] = comment.find('a',
                                          attrs={'class': 'review-num'}).get_text().replace('条点评', '')
        shop['mean-price'] = comment.find('a', attrs={'class': 'mean-price'}).get_text()
        shop['type'] = tag_addr.find('span', attrs={'class': 'tag'}).get_text()
        shop['addr'] = tag_addr.find('span', attrs={'class': 'addr'}).get_text()
        try:
            comment_list = soup.find('span', attrs={'class': 'comment-list'}).find_all('span')
        except:
            comment_list = []
        score = []
        for i in comment_list:
            score.append(i.get_text())
        shop['score'] = score
        tags = []
        try:
            for i in tit.find('div', attrs={'class': 'promo-icon'}).find_all('a'):
                try:
                    tags += i.get('class')
                except:
                    tags.append(i.get('class')[0])
        except:
            pass
        shop['tags'] = tags
        result.append(shop)
    return result
