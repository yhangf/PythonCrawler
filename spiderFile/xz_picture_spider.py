import re
import os
import requests


def Spidermain(page=11):
    '''
    本爬虫的爬取策略为深度优先（DFS）
    '''
    main_url_ = 'http://www.rosiok.com/app/list_12_{0}.html'
    for _ in range(1, page + 1):
        main_url = main_url_.format(_)
        domain_url = 'http://www.rosiok.com{0}'
        start_html = requests.get(main_url).content.decode('gb2312')
        kids_url_regex = re.compile('<strong><a href=\'(.*?)\'>')
        kids_url = [domain_url.format(i) for i in re.findall(kids_url_regex, start_html)]
        for kid_url in kids_url:
            all_pic_urls = []
            pic_html = requests.get(kid_url).content.decode('gb2312')
            # 抓取标题
            title_regex = re.compile('<title>(.*?)</title>')
            title = re.findall(title_regex, pic_html)[0]
            # 抓取封面图片url
            parent_pic_regex = re.compile('<img src="(.*?)" width="796" height="531" alt')
            parent_pic = re.findall(parent_pic_regex, pic_html)
            # 抓取封面所对应的子图片url
            kids_pic_regex = re.compile('class="a" src="(.*?)" />')
            kids_pic_url = re.findall(kids_pic_regex, pic_html)
            # 合并封面url列表和子图url列表
            all_pic_urls.extend(parent_pic)
            all_pic_urls.extend(kids_pic_url)
            # 下载并存储图片
            if not os.path.exists('./{0}'.format(title)):
                os.mkdir('./{0}'.format(title))
                s = requests.Session()
                for count, pic_url in enumerate(all_pic_urls):
                    with open('./{0}/{1}.jpg'.format(title, count), 'wb') as file:
                        try:
                            file.write(s.get(pic_url, timeout=5).content)
                        except:
                            pass

if __name__ == '__main__':
    Spidermain()
