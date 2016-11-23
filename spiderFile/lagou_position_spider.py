import json
import requests as rq
import pandas as pd

kw = input('请输入抓取的职位名称：')
lagou_url = 'http://www.lagou.com/jobs/positionAjax.json?first=false&pn={0}&kd={1}'
lagou_python_data = []
for i in range(1, 31):
    print('抓取第{0}页'.format(i))
    lagou_url_ = lagou_url.format(i, kw)
    lagou_data = json.loads(rq.get(lagou_url_).text)
    lagou_python_data.extend(lagou_data['content']['positionResult']['result'])

position_data = pd.DataFrame(lagou_python_data)
position_data.to_csv('./招聘{0}职位.csv'.format(kw), index=False)
print('数据已保存到本地文件')
