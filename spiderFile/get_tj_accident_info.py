import re
import joblib
import asyncio
import aiohttp
import requests as rq
from bs4 import BeautifulSoup

def yield_all_page_url(root_url, page=51):
    """生成所有的页面url
    @param root_url: 首页url
    type root_url: str
    @param page: 爬取的页面个数
    type page: int
    """
    # 观察网站翻页结构可知
    page_url_list = [f"{root_url}index_{i}.html" for i in range(1, page)]
    # 添加首页url
    page_url_list.insert(0, root_url)
    return page_url_list

async def get_info_page_url(url, session):
    regex = re.compile("<a href='./(.*?)'\s+title=")
    async with session.get(url) as response:
        html = await response.text()
        url_part_list = re.findall(regex, html)
        return url_part_list
    
async def get_all_info_page_url(root_url, page_url_list):
    tasks, all_info_page_url_list = [], []
    # 控制协程并发量
    async with asyncio.Semaphore(50) as semaphore:
        async with aiohttp.ClientSession() as session:
            for url in page_url_list:
                tasks.append(get_info_page_url(url, session))
            done, pendding = await asyncio.wait(tasks)
    all_info_page_url_list = [root_url+url_part for r in done 
                              for url_part in r.result()]
    return all_info_page_url_list


def get_data(url):
    title_regex = re.compile('<meta name="ArticleTitle" content="(.*?)" />')
    html = rq.get(url, headers=HEADERS).content.decode("utf-8")
    soup = BeautifulSoup(html)    
    title = re.search(title_regex, html)
    content_1 = soup.find("div", class_="TRS_UEDITOR TRS_WEB")
    content_2 = soup.find("div", class_="view TRS_UEDITOR trs_paper_default trs_word")
    content_3 = soup.find("div", class_="view TRS_UEDITOR trs_paper_default trs_web")
    if content_1:
        content = content_1.text
    elif content_2:
        content = content_2.text
    elif content_3:
        content = content_3.text
    else:
        content = ""
    return {"title": title.groups()[0], "content": content}

def get_all_data(all_info_page_url_list):
    all_data = []
    for i, url in enumerate(all_info_page_url_list):
        all_data.append(get_data(url))
        print(i, url, all_data[-1])
    joblib.dump(all_data, "all_data.joblib")


if __name__ == "__main__":
    root_url = "http://yjgl.tj.gov.cn/ZWGK6939/SGXX3106/"
    agent_part_1 = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    agent_part_2 = "(KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"
    HEADERS = {"Host": "yjgl.tj.gov.cn",
               "Connection": "keep-alive",
               "User-Agent": agent_part_1 + agent_part_2,
               "Referer": "http://static.bshare.cn/"}
    page_url_list = yield_all_page_url(root_url, page=51)
    all_info_page_url_list = asyncio.run(get_all_info_page_url(root_url, page_url_list))
    joblib.dump("all_info_page_url_list", all_info_page_url_list)
