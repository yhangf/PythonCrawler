from spider import SpiderHTML
import re,os,sys,time,urllib,random,http
'''
抓取淘宝模特的靓图
'''

class TaobaommSpider(SpiderHTML):
    #抓取起始页，结束页，每个妹子抓取的图片数量
    def __init__(self,pageStart, pageEnd,limit_img):
        self._pageStart = int(pageStart)
        self._pageEnd = int(pageEnd)+1
        self._limit = limit_img
        self.__url = 'https://mm.taobao.com/json/request_top_list.htm?page='
        self.__dir = r'E:\taobaomm'

    def start(self):
        for page in range(self._pageStart,self._pageEnd):
            url = self.__url + str(page)
            contents = self.getUrl(url,'gbk')
            lists = contents.find_all('div',class_='personal-info')
            for girl in lists:
                info = girl.find('a',attrs={'class':'lady-name'})
                avatar = girl.find('a',class_='lady-avatar')

                girlinfo = {}
                girlinfo['name'] = info.string  
                girlinfo['age'] = info.find_next_sibling('em').strong.string  
                girlinfo['city'] = info.find_next('span').string
                girlinfo['url'] = 'https:'+avatar['href']
                #去除掉缩小的图片
                girlinfo['avatar'] = 'https:'+re.sub('_\d+x\d+\.\w+$','',avatar.img['src']) 
                imgType = os.path.splitext(girlinfo['avatar'])[1]
                logInfo = '找到一位MM：{name},{age}岁，她在{city}'.format(**girlinfo)
                print(logInfo)
                tmpDir = os.path.join(self.__dir,girlinfo['name']+'-'+girlinfo['age']+'-'+girlinfo['city'])
                if(os.path.exists(tmpDir)):
                    print('已经获得过信息，去找下一位')
                    continue
                #以名字命名，保存图片和基本信息
                self.saveImg(girlinfo['avatar'],os.path.join(tmpDir,'avatar'+imgType))
                print('正在进入她的个人中心获取私图')

                gilrsCenter = self.getUrl(girlinfo['url'],'gbk')
                imgs = gilrsCenter.find('div',class_='mm-aixiu-content').find_all('img')
                i = 0
                for img in imgs:
                    i = i + 1
                    if i % 5 == 0:
                        print('正在获取第{i}张图'.format(i=i))
                    try:
                        imgurl = 'https:'+img['src']
                        extend_name = os.path.splitext(img['src'])[1]
                        if extend_name == '.gif':
                            continue    #一般都是表情图，略过
                        self.saveImg(imgurl,os.path.join(tmpDir,str(i)+extend_name))
                    except urllib.error.HTTPError as e:
                        pass
                    except KeyError as e:
                        pass
                    except http.client.IncompleteRead:
                        pass

                    if i >= self._limit:
                        pass    #若要限制每个模特抓图的张数，此处改为break
                time.sleep(random.random()*2)


if __name__ == '__main__':
    page, limit, paramsNum= 1, 0, len(sys.argv)
    if paramsNum>=4:
        page, pageEnd, limit = sys.argv[1], sys.argv[2], int(sys.argv[3])
    elif paramsNum == 2:
        page = sys.argv[1]
        pageEnd = page
    else:
        page,pageEnd = 1,1

    if limit <5:
        limit = 20
    spider = TaobaommSpider(page,pageEnd,limit)
    spider.start()
