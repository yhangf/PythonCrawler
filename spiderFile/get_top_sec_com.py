import re
import os
import time
import joblib
import asyncio
import aiohttp
import requests as rq

import pandas as pd
import matplotlib.pyplot as plt

class getTopSecCom:
    def __init__(self, top=None):
        self.headers = {"Referer": "http://quote.eastmoney.com/",
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"}
        self.bk_url = "http://71.push2.eastmoney.com/api/qt/clist/get?cb=jQuery1124034348162124675374_1612595298605&pn=1&pz=85&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&fid=f62&fs=b:BK0655&fields=f12,f14&_=1612595298611"
        self.shares_api = "https://xueqiu.com/S/"
        self.top = top
        if not os.path.exists("./useful_sec_com_list"):
            self.useful_sec_com_list = self.get_sec_com_code()
        else:
            with open("./useful_sec_com_list", "rb") as fp:
                self.useful_sec_com_list = joblib.load(fp)
                
    def get_sec_com_code(self):
        html = rq.get(self.bk_url, headers=self.headers).content.decode("utf-8")
        sec_com_list = eval(re.findall("\[(.*?)\]", html)[0])
        useful_sec_com_list = [[i["f12"], i["f14"]] for i in sec_com_list if "ST" not in i["f14"]]
        
        # 0和3开头的为深证上市股票前缀为sz，6开头的为上证上市股票前缀为sh
        for sec_com in useful_sec_com_list:
            if sec_com[0][0] == "6":
                sec_com[0] = "sh" + sec_com[0]
            else:
                sec_com[0] = "sz" + sec_com[0]
        with open("useful_sec_com_list", "wb") as fp:
            joblib.dump(useful_sec_com_list, fp)
        return useful_sec_com_list

    async def async_get_shares_details(self, sec_com, url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=self.headers) as response:
                html = await response.text()
                market_value = re.search("<td>总市值：<span>(.*?)亿</span>", html)
                if market_value:
                    return [*sec_com, market_value.groups()[0]]
                
    async def async_get_all_shares(self):
        tasks = []
        for sec_com in self.useful_sec_com_list:
            url = self.shares_api + sec_com[0]
            tasks.append(
                asyncio.create_task(
                    self.async_get_shares_details(sec_com, url)
                )
            )
        done, pendding = await asyncio.wait(tasks)
        return [share.result() for share in done if share.result()]
    
    def get_shares_details(self):
        all_shares = []
        for sec_com in self.useful_sec_com_list:
            url = self.shares_api + sec_com[0]
            response = rq.get(url, headers=self.headers).content.decode("utf-8")
            market_value = re.search("<td>总市值：<span>(.*?)亿</span>", response)
            if market_value:
                all_shares.append([*sec_com, market_value.groups()[0]])
        return all_shares
    
    def yield_picture(self, save_path):
        # all_shares = self.get_shares_details() # 同步代码
        all_shares = asyncio.run(self.async_get_all_shares()) # 异步代码
        df = pd.DataFrame(all_shares, columns=["股票代码", "公司", "市值(亿)"])
        df["市值(亿)"] = df["市值(亿)"].astype(float)
        date = time.strftime("%Y年%m月%d日", time.localtime())
        df.sort_values(by="市值(亿)", ascending=False, inplace=True)
        df.index = range(1, df.shape[0]+1)
        
        plt.rcParams['font.sans-serif'] = ['SimHei']  
        plt.rcParams['axes.unicode_minus'] = False
            
        
        fig = plt.figure(dpi=400)
        ax = fig.add_subplot(111, frame_on=False)
        ax.xaxis.set_visible(False)  
        ax.yaxis.set_visible(False)
        _ = pd.plotting.table(ax, df, loc="best", cellLoc="center")
        ax.set_title(f"{date}A股网安版块公司市值排名", fontsize=10)        
        plt.savefig(save_path, bbox_inches="tight")

if __name__ == "__main__":
    m = getTopSecCom()
    m.yield_picture("rank.png")
