import requests
import re

url = 'http://image.baidu.com/search/index'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Referer': 'http://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&fm=detail&lm=-1&st=-1&sf=2&fmq=&pv=&ic=0&nc=1&z=&se=&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E9%AB%98%E6%B8%85%E6%91%84%E5%BD%B1&oq=%E9%AB%98%E6%B8%85%E6%91%84%E5%BD%B1&rsp=-1',
    'Cookie': 'HOSUPPORT=1; UBI=fi_PncwhpxZ%7ETaMMzY0i9qXJ9ATcu3rvxFIc-a7KI9byBcYk%7EjBVmPGIbL3LTKKJ2D17mh5VfJ5yjlCncAb2yhPI5sZM51Qo7tpCemygM0VNUzuTBJwYF8OYmi3nsCCzbpo5U9tLSzkZfcQ1rxUcJSzaipThg__; HISTORY=fec845b215cd8e8be424cf320de232722d0050; PTOKEN=ff58b208cc3c16596889e0a20833991d; STOKEN=1b1f4b028b5a4415aa1dd9794ff061d312ad2a822d52418f3f1ffabbc0ac6142; SAVEUSERID=0868a2b4c9d166dc85e605f0dfd153; USERNAMETYPE=3; PSTM=1454309602; BAIDUID=E5493FD55CFE5424BA25B1996943B3B6:FG=1; BIDUPSID=B7D6D9EFA208B7B8C7CB6EF8F827BD4E; BDUSS=VSeFB6UXBmRWc3UEdFeXhKOFRvQm4ySmVmTkVEN2N0bldnM2o5RHdyaE54ZDlXQVFBQUFBJCQAAAAAAAAAAAEAAABzhCtU3Mbj5cfl0e8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAE04uFZNOLhWZW; H_PS_PSSID=1447_18282_17946_18205_18559_17001_17073_15479_12166_18086_10634; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; BDRCVFR[X_XKQks0S63]=mk3SLVN4HKm; BDRCVFR[dG2JNJb_ajR]=mk3SLVN4HKm',
}


def get_html(url, headers):
    data = {
        'cl': '2',
        'ct': '201326592',
              'face': '0',
              'fp': 'result',
              'gsm': '200001e',
              'ic': '0',
              'ie': 'utf-8',
              'ipn': 'rj',
              'istype': '2',
              'lm': '-1',
              'nc': '1',
              'oe': 'utf-8',
              'pn': '30',
              'queryword': '高清摄影',
              'rn': '30',
              'st': '-1',
              'tn': 'resultjson_com',
              'word': '高清摄影'
    }

    page = requests.get(url, data, headers=headers).text
    return page


def get_img(page, headers):
    #     img_url_list = []
    reg = re.compile('http://.*?\.jpg')
    imglist1 = re.findall(reg, page)
    imglist2 = imglist1[0: len(imglist1): 3]
    #   [img_url_list.append(i) for i in imglist if not i in img_url_list]
    x = 0
    for imgurl in imglist2:
        bin = requests.get(imgurl, headers=headers).content
        with open('./%s.jpg' % x, 'wb') as file:
            file.write(bin)
            x += 1

if __name__ == '__main__':
    page = get_html(url, headers)
    get_img(page, headers)
