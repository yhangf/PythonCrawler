import re
import requests as rq

ROOT_URL = "http://wufazhuce.com/one/"
URL_NUM = 14

def yield_url(ROOT_URL, URL_NUM):
    return ROOT_URL + str(URL_NUM)

def get_html(url):
    return rq.get(url).content.decode("utf-8")

def get_data(html):
    img_url_regex = re.compile('<img src="(.*?)" alt="" />')
    cite_regex = re.compile('<div class="one-cita">(.*?)</div>', re.S)
    img_url = re.findall(img_url_regex, html)[0]
    cite = re.findall(cite_regex, html)[0].strip()
    return img_url, cite                        

def save_data(img_url, cite, URL_NUM):
    with open("./{}.jpg".format(URL_NUM), "wb") as fp:
        fp.write(rq.get(img_url).content)
    with open("./cite{}.txt".format(URL_NUM), "w") as fp:
        fp.write(cite)
    return URL_NUM + 1

def main(ROOT_URL, URL_NUM, number):
    for _ in range(number):
        url = yield_url(ROOT_URL, URL_NUM)
        html = get_html(url) 
        img_url, cite = get_data(html) 
        URL_NUM = save_data(img_url, cite, URL_NUM)
        
if __name__ == "__main__":
    try:
        main(ROOT_URL, URL_NUM, 20)
    except:
        pass
