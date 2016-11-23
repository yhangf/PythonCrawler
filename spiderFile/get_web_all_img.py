import re
import time
import requests


def get_html(url, headers):
    html = requests.get(url, timeout=100, headers=headers).text
    return html


def get_main_url(html):
    reg = re.compile('http://.*?\.jpg')
    main_imglist = re.findall(reg, html)
    return main_imglist


def get_son_url(html):
    initurl = 'http://www.woyaogexing.com'
    reg = re.compile('/tupian/weimei/\d+/\d+\.html')
    son_urllist_init = re.findall(reg, html)
    son_urlist = set(son_urllist_init)
    son_url_final = []
    for son_url in son_urlist:
        son_url_final.append(initurl + son_url)
    return son_url_final  # 结果是所有含有图片的网页地址


def get_all_sonurl(son_url_final, headers):
    son_imglist = []
    for sonurl in son_url_final:
        son_html = requests.get(sonurl, timeout=100, headers=headers).text
        son_reg = re.compile('http://.*?\.jpg')
        son_imglist1 = re.findall(son_reg, son_html)
        for temp in son_imglist1:
            son_imglist.append(temp)
    return son_imglist  # 结果是所有子网页图片的地址


def get_all_img(main_imglist, son_imglist, headers):
    global x  # 使用全局变量使每次的变量不清除，这个问题有待完美解决！
    for imgurl in main_imglist:
        son_imglist.append(imgurl)
    for imgurl in son_imglist:
        with open('E:/Pic2/%s.jpg' % x, 'wb') as file:
            file.write(requests.get(imgurl, timeout=100, headers=headers).content)
            time.sleep(0.1)
            x += 1


def turn_page():
    page_list = ['http://www.woyaogexing.com/tupian/weimei/index.html']
    for i in range(1, 7):
        page_list.append('http://www.woyaogexing.com/tupian/weimei/index_' + str(i) + '.html')
    return page_list

if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0',
        'Accept': 'text/plain, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate',
        'Cookie': 'bdshare_firstime=1456041345958; Hm_lvt_a077b6b44aeefe3829d03416d9cb4ec3=1456041346; Hm_lpvt_a077b6b44aeefe3829d03416d9cb4ec3=1456048504',
    }
    x = 0
    page_list = ['http://www.woyaogexing.com/tupian/weimei/index.html']
    for i in range(2, 20):
        page_list.append('http://www.woyaogexing.com/tupian/weimei/index_' + str(i) + '.html')
    for p in range(6):
        html = get_html(page_list[p], headers)
        main_imglist = get_main_url(html)
        son_url_final = get_son_url(html)
        son_imglist = get_all_sonurl(son_url_final, headers)
        get_all_img(main_imglist, son_imglist, headers)
