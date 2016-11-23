import requests
import re

url = 'http://image.baidu.com/search/index'
date = {
    'cl': '2',
    'ct': '201326592',
          'fp': 'result',
          'gsm': '1e',
          'ie': 'utf-8',
          'ipn': 'rj',
          'istype': '2',
          'lm': '-1',
          'nc': '1',
          'oe': 'utf-8',
          'pn': '30',
          'queryword': '唯美意境图片',
          'rn': '30',
          'st': '-1',
          'tn': 'resultjson_com',
          'word': '唯美意境图片'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0',
    'Accept': 'text/plain, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'X-Requested-With': 'XMLHttpRequest',
    'Referer': 'http://image.baidu.com/search/index?ct=201326592&cl=2&st=-1&lm=-1&nc=1&ie=utf-8&tn=baiduimage&ipn=r&rps=1&pv=&fm=rs3&word=%E5%94%AF%E7%BE%8E%E6%84%8F%E5%A2%83%E5%9B%BE%E7%89%87&ofr=%E9%AB%98%E6%B8%85%E6%91%84%E5%BD%B1',
    'Cookie': 'BDqhfp=%E5%94%AF%E7%BE%8E%E6%84%8F%E5%A2%83%E5%9B%BE%E7%89%87%26%26NaN-1undefined-1undefined%26%260%26%261; Hm_lvt_737dbb498415dd39d8abf5bc2404b290=1455016371,1455712809,1455769605,1455772886; PSTM=1454309602; BAIDUID=E5493FD55CFE5424BA25B1996943B3B6:FG=1; BIDUPSID=B7D6D9EFA208B7B8C7CB6EF8F827BD4E; BDUSS=VSeFB6UXBmRWc3UEdFeXhKOFRvQm4ySmVmTkVEN2N0bldnM2o5RHdyaE54ZDlXQVFBQUFBJCQAAAAAAAAAAAEAAABzhCtU3Mbj5cfl0e8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAE04uFZNOLhWZW; H_PS_PSSID=1447_18282_17946_15479_12166_18086_10634; Hm_lpvt_737dbb498415dd39d8abf5bc2404b290=1455788775; firstShowTip=1; BDRCVFR[-pGxjrCMryR]=mk3SLVN4HKm; BDRCVFR[dG2JNJb_ajR]=mk3SLVN4HKm',
    'Connection': 'keep-alive'
}


def get_page(url, date, headers):
    page = requests.get(url, date, headers=headers).text
    return page


def get_img(page, headers):
    reg = re.compile('http://.*?\.jpg')
    imglist = re.findall(reg, page)[::3]
    x = 0
    for imgurl in imglist:
        with open('E:/Pic/%s.jpg' % x, 'wb') as file:
            file.write(requests.get(imgurl, headers=headers).content)
            x += 1

if __name__ == '__main__':
    page = get_page(url, date, headers)
    get_img(page, headers)
