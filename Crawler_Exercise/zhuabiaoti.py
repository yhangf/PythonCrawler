import urllib.request  
import re  
  
########################################################  
#  
# fetch函数功能：抓取“陕西建筑招标网”的第一页“招标公告”页面，输出公告名字  
#   
#             参数baseUrl是要访问的网站地址   
#  
########################################################  
  
def fetch(baseUrl):  
  
    # 第1步：模拟浏览器发送请求  
    data = urllib.request.urlopen(baseUrl).read()  #二进制字节形式  
    data = data.decode('utf-8')    
  
    # 第2步：页面返回后，利用正则表达式提取想要的内容  
    nameList=[]  
    nameList = re.compile(r'target="_blank" title="(.*?)"',re.DOTALL).findall(data)  
  
    # 第3步：返回在页面上析取的“标题名”  
    return nameList  
      
#######     执行    ########   
if __name__ =="__main__":  
     
    #要抓取的网页地址  
    url = "http://www.sxszbb.com/sxztb/jyxx/001001/MoreInfo.aspx?CategoryNum=001001"  
  
    #存放到名字列表中  
    NameList = fetch(url)  
  
    # 输出 NameList  
    Length = len(NameList)  
    for i in range(0, Length):  
        print("标题名%d:%s\n"%(i+1, NameList[i])) 