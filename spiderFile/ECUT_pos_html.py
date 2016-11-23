import requests
import re from bs4
import BeautifulSoup as bs


def crawl_all_main_url(page=10):
 # 默认抓取官网前十页招聘信息的url
 all_url_list = []
 for _ in range(1, page+1):
     url = 'http://zjc.ecit.edu.cn/jy/app/newslist.php?BigClassName=%D5%D0%C6%B8%D0%C5%CF%A2&Page={0}'.format(_)
     page_html = requests.get(url).text
     x_url_reg = re.compile('<a class="t_13px" href="(.*?)"')
     x_url = re.findall(x_url_reg, page_html)
     main_url = ['http://zjc.ecit.edu.cn/jy/app/{0}'.format(i)
        for i in x_url] all_url_list.extend(main_url)
        return all_url_list
    def get_title(son_url): # 判断该网页是否为校园招聘
        html = requests.get(son_url).content.decode('gbk')
        explain_text_reg = re.compile('<h1 class="newstitle">(.*?)</h1>')
        explain_text = re.findall(explain_text_reg, html)[0]
        if ('时间' and '地点') in explain_text:
            return True
        else: pass
    def save_html():
        all_url_list = crawl_all_main_url()
        for son_url in all_url_list:
            if get_title(son_url):
                text_html = requests.get(son_url).content.decode('gbk')
                domain_url = 'http://zjc.ecit.edu.cn/jy'
                img_url_reg = re.compile('border=0 src="\.\.(.*?)"')
                child_url = re.findall(img_url_reg, text_html)
                if child_url != []:
                    img_url = domain_url + child_url[0]
                    re_url = 'src="..{0}"'.format(child_url[0])
                    end_url = 'src="{0}"'.format(img_url)
                    end_html = text_html.replace(re_url, end_url)
                    soup = bs(end_html, 'lxml')
                    text_div = soup.find_all('div', id='main')[0]
                    with open('./{0}.html'.format(son_url[-11:]), 'wb') as file:
                        text_html = '<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">U职网提供数据咨询服务 <html xmlns="http://www.w3.org/1999/xhtml"> <head> <meta http-equiv="Content-Type" content="text/html; charset=utf-8" /> </head> {0} </body>'.format(text_div) file.write(text_html.encode('utf-8'))
                    else:
                        with open('./{0}.html'.format(son_url[-11:]), 'wb') as file:
                            html = requests.get(son_url).content.decode('gbk')
                            soup = bs(text_html, 'lxml')
                            text_div = soup.find_all('div', id='main')[0]
                            text_html = '<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">U职网提供数据咨询服务 <html xmlns="http://www.w3.org/1999/xhtml"> <head> <meta http-equiv="Content-Type" content="text/html; charset=utf-8" /> </head> {0} </body>'.format(text_div)
                            file.write(text_html.encode('utf-8'))
                            else: continue
if __name__ == '__main__':
save_html()
