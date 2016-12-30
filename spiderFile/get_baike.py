import re
import requests as rq

def get_baidubaike():

    keyword = input('please input wordkey:')
    url = 'http://baike.baidu.com/item/{}'.format(keyword)
    html = rq.get(url).content.decode('utf-8')

    regex = re.compile('content="(.*?)">')
    words = re.findall(regex, html)[0]
    return words

if __name__ == '__main__':
    words = get_baidubaike()
    print(words)




