```shell
                      (                                                                        
                     )\ )          )    )               (                       (             
                    (()/( (     ( /( ( /(               )\   (       )  (  (    )\   (   (    
                    /(_)))\ )  )\()))\())  (    (    (((_)  )(   ( /(  )\))(  ((_) ))\  )(   
                    (_)) (()/( (_))/((_)\   )\   )\ ) )\___ (()\  )(_))((_)()\  _  /((_)(()\  
                    | _ \ )(_))| |_ | |(_) ((_) _(_/(((/ __| ((_)((_)_ _(()((_)| |(_))   ((_)
                    |  _/| || ||  _|| ' \ / _ \| ' \))| (__ | '_|/ _` |\ V  V /| |/ -_) | '_|
                    |_|   \_, | \__||_||_|\___/|_||_|  \___||_|  \__,_| \_/\_/ |_|\___| |_|   
                    |__/  
                                                                —————— by yanghangfeng
```
# <p align="center">PythonCrawler: 用  python编写的爬虫项目集合:bug:</p>

<p align="center">
    <a href="https://github.com/yhangf/PythonCrawler/blob/master/LICENSE">
        <img src="https://img.shields.io/cocoapods/l/EFQRCode.svg?style=flat">
        </a>
    <a href="">
        <img src="https://img.shields.io/badge/未完-间断性更新-orange.svg">
        </a>
    <a href="https://github.com/python/cpython">
        <img src="https://img.shields.io/badge/language-python-ff69b4.svg">
        </a>
    <a href="https://github.com/yhangf/PythonCrawler">
    <img src="https://img.shields.io/github/stars/yhangf/PythonCrawler.svg?style=social&label=Star">
        </a>
    <a href="https://github.com/yhangf/PythonCrawler">
    <img src="https://img.shields.io/github/forks/yhangf/PythonCrawler.svg?style=social&label=Fork">
        </a>
</p>


# spiderFile模块简介

1.    [baidu_sy_img.py](https://github.com/yhangf/PythonCrawler/blob/master/spiderFile/baidu_sy_img.py): **抓取百度的`高清摄影`图片。**
2.    [baidu_wm_img.py](https://github.com/yhangf/PythonCrawler/blob/master/spiderFile/baidu_wm_img.py): **抓取百度图片`唯美意境`模块。**
3.    [get_photos.py](https://github.com/yhangf/PythonCrawler/blob/master/spiderFile/get_photos.py): **抓取百度贴吧某话题下的所有图片。**
4.    [get_web_all_img.py](https://github.com/yhangf/PythonCrawler/blob/master/spiderFile/get_web_all_img.py): **抓取整个网站的图片。**
5.    [lagou_position_spider.py](https://github.com/yhangf/PythonCrawler/blob/master/spiderFile/lagou_position_spider.py): **任意输入关键字，一键抓取与关键字相关的职位招聘信息，并保存到本地文件。**
6.    [student_img.py](https://github.com/yhangf/PythonCrawler/blob/master/spiderFile/student_img.py): **基于本学校官网的url漏洞，获取所有注册学生学籍证件照。**
7.    [JD_spider.py](https://github.com/yhangf/PythonCrawler/blob/master/spiderFile/JD_spider.py): **大批量抓取京东商品id和标签。**
8.    [ECUT_pos_html.py](https://github.com/yhangf/PythonCrawler/blob/master/spiderFile/ECUT_pos_html.py): **抓取学校官网所有校园招聘信息，并保存为html格式，图片也会镶嵌在html中。**
9.    [ECUT_get_grade.py](https://github.com/yhangf/PythonCrawler/blob/master/spiderFile/ECUT_get_grade.py): **模拟登陆学校官网，抓取成绩并计算平均学分绩。**
10.    [github_hot.py](https://github.com/yhangf/PythonCrawler/blob/master/spiderFile/github_hot.py): **抓取github上面热门语言所对应的项目，并把项目简介和项目主页地址保存到本地文件。**
11.    [xz_picture_spider.py](https://github.com/yhangf/PythonCrawler/blob/master/spiderFile/xz_picture_spider.py): **应一位知友的请求，抓取某网站上面所有的写真图片。**
12.    [one_img.py](https://github.com/yhangf/PythonCrawler/blob/master/spiderFile/one_img.py): **抓取one文艺网站的图片。**
13.    [get_baike.py](https://github.com/yhangf/PythonCrawler/blob/master/spiderFile/get_baike.py): **任意输入一个关键词抓取百度百科的介绍。**
14.    [kantuSpider.py](https://github.com/yhangf/PythonCrawler/blob/master/spiderFile/kantuSpider.py): **抓取看图网站上的所有图片。**
15.    [fuckCTF.py](https://github.com/yhangf/PythonCrawler/blob/master/spiderFile/fuckCTF.py): **通过selenium模拟登入合天网站，自动修改原始密码。**
16.    [one_update.py](https://github.com/yhangf/PythonCrawler/blob/master/spiderFile/one_update.py): **更新抓取one文艺网站的代码，添加一句箴言的抓取。**
17.    [get_history_weather.py](https://github.com/yhangf/PythonCrawler/blob/master/spiderFile/get_history_weather.py): **抓取广州市2019年第一季度的天气数据。**

---
# spiderAPI模块简介

#### 本模块提供一些网站的API爬虫接口，功能可能不是很全因此可塑性很大智慧的你如果有兴趣可以继续改进。

##### 1.大众点评

```python
from spiderAPI.dianping import *

'''
citys = {
    '北京': '2', '上海': '1', '广州': '4', '深圳': '7', '成都': '8', '重庆': '9', '杭州': '3', '南京': '5', '沈阳': '18', '苏州': '6', '天津': '10','武汉': '16', '西安': '17', '长沙': '344', '大连': '19', '济南': '22', '宁波': '11', '青岛': '21', '无锡': '13', '厦门': '15', '郑州': '160'
}

ranktype = {
    '最佳餐厅': 'score', '人气餐厅': 'popscore', '口味最佳': 'score1', '环境最佳': 'score2', '服务最佳': 'score3'
}
'''

result=bestRestaurant(cityId=1, rankType='popscore')#获取人气餐厅

shoplist=dpindex(cityId=1, page=1)#商户风云榜

restaurantlist=restaurantList('http://www.dianping.com/search/category/2/10/p2')#获取餐厅

```

##### 2.获取代理IP
爬取[代理IP](http://proxy.ipcn.org)
```python
from spiderAPI.proxyip import get_enableips

enableips=get_enableips()

```

##### 3.百度地图

百度地图提供的API,对查询有一些限制，这里找出了web上查询的接口。
```python
from spiderAPI.baidumap import *

citys=citys()#获取城市列表
result=search(keyword="美食", citycode="257", page=1)#获取搜索结果

```

##### 4.模拟登录github
```python
from spiderAPI.github import GitHub

github = GitHub()
github.login() # 这一步会提示你输入用户名和密码
github.show_timeline() # 获取github主页时间线
# 更多的功能有待你们自己去发掘
```

##### 5.拉勾网
```python
from spiderAPI.lagou import *

lagou_spider(key='数据挖掘', page=1) # 获取关键字为数据挖掘的招聘信息
```
