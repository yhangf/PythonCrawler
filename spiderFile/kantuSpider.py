import re
import os
import time

import requests as rq


def get_all_page(page):
    url = 'http://52kantu.cn/?page={}'.format(page)
    html = rq.get(url).text
    
    return html


def get_img_url(html):
    regex = re.compile('<mip-img src="(.*?)"')
    img_url_list = re.findall(regex, html)
    
    return img_url_list


def down_img(img_url, s):
    if not os.path.exists('./img'):
        os.mkdir('./img')
    with open('./img/{}.jpg'.format(
              img_url.split('.')[1].split('/')[-1]), 'wb'
             ) as fp:

        fp.write(s.get(img_url, timeout=5).content)


def main(all_page, s):
    for page in range(1, all_page):
        try:
            html = get_all_page(page)
            img_url_list = get_img_url(html)
            [down_img(img_url, s) for img_url in img_url_list]
            time.sleep(5)
        except:
            pass
        
            
        
if __name__ == '__main__':
    s = rq.Session()
    main(320, s)    
