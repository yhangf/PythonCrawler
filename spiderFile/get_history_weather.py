import re
import pandas as pd
import requests as rq
from bs4 import BeautifulSoup


def get_data(url):
    html = rq.get(url).content.decode("gbk")
    soup = BeautifulSoup(html, "html.parser")
    tr_list = soup.find_all("tr")
    dates, conditions, temperatures = [], [], []
    for data in tr_list[1:]:
        sub_data = data.text.split()
        dates.append(sub_data[0])
        conditions.append("".join(sub_data[1:3]))
        temperatures.append("".join(sub_data[3:6]))
    _data = pd.DataFrame()
    _data["日期"] = dates
    _data["天气状况"] = conditions
    _data["气温"] = temperatures
    return _data

# 获取广州市2019年第一季度天气状况
data_1_month = get_data("http://www.tianqihoubao.com/lishi/guangzhou/month/201901.html")
data_2_month = get_data("http://www.tianqihoubao.com/lishi/guangzhou/month/201902.html")
data_3_month = get_data("http://www.tianqihoubao.com/lishi/guangzhou/month/201903.html")


data = pd.concat([data_1_month, data_2_month, data_3_month]).reset_index(drop=True)

data.to_csv("guangzhou_history_weather_data.csv", index=False, encoding="utf-8")
