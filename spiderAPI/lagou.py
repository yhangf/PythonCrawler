import json
import requests as rq


def lagou_spider(key=None, page=None):
    lagou_url = 'http://www.lagou.com/jobs/positionAjax.json?first=false&pn={0}&kd={1}'
    lagou_python_data = []
    for i in range(page):
        print('抓取第{0}页'.format(i + 1))
        lagou_url_ = lagou_url.format(i, key)
        lagou_data = json.loads(rq.get(lagou_url_).text)
        lagou_python_data.extend(lagou_data['content']['positionResult']['result'])
    return lagou_python_data
