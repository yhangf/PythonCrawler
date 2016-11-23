import requests
import re
import pandas as pd

def get_data():
    jj_url1 = 'http://search.jd.com/s_new.php?keyword=%E5%AE%B6%E5%B1%85%E7%94%A8%E5%93%81&enc=utf-8&qrst=1&rt=1&stop=1&pt=1&vt=2&sttr=1&offset=6&page='
    jj_url2 = '&s=53&click=0'
    bt_ = []
    _id = []
    url_list = []
    for i in range(1, 10, 2):
        jj_url = jj_url1 + str(i) + jj_url2
        url_list.append(jj_url)
        html = requests.get(jj_url).content.decode('utf-8')
        reg1 = re.compile('<a target="_blank" title="(.*?)"')
        reg2 = re.compile('<i class="promo-words" id="(.*?)"></i>')
        bt = re.findall(reg1, html)
        id_ = re.findall(reg2, html)
        bt_.extend(bt)
        _id.extend(id_)
    return bt_, _id

def split_str(_id):
    zid = []
    for _ in _id:
        zid.append(_.split('_')[2])
    return zid

def save_data(zid, bt_):
    data = pd.DataFrame({
            '标题': bt_,
            'ID': zid
            })
    data.to_excel('./家居用品.xlsx', index=False)

def start_main():
    bt_, _id = get_data()
    zid = split_str(_id)
    save_data(zid, bt_)

if __name__ == '__main__':
    start_main()
