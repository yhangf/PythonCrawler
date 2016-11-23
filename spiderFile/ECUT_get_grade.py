import re
import requests
import numpy as np
import pandas as pd


def warn(*args, **kw): pass
import warnings
warnings.warn = warn

print('*' * 30 + '东华理工大学' + '*' * 30)
print('*' * 30 + '作者:杨航锋' + '*' * 30)
print('*' * 30 + '版本:v1.0' + '*' * 30)
print('\n')
print('请输你学号:')
username = input()
print('请输入密码:')
password = input()
print('\n')

login_url = 'https://cas.ecit.cn/index.jsp?service=http://portal.ecit.cn/Authentication'


def get_LT(login_url):
    html = requests.get(login_url, verify=False).text
    regex = re.compile('<input type="hidden" name="lt" value="(.*?)" />')
    lt = re.findall(regex, html)[0]
    return lt

LT = get_LT(login_url)

data = {
    'lt': LT,
    'password': password,
    'username': username
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Connection': 'keep-alive',
    'Host': 'cas.ecit.cn',
    'Referer': 'https://cas.ecit.cn/index.jsp?service=http://portal.ecit.cn/Authentication',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:48.0) Gecko/20100101 Firefox/48.0'
}

s = requests.Session()
s.post(login_url, data=data, headers=headers, verify=False)
html = s.get('http://jw.ecit.cn').text
reg = re.compile('<a href="(.*?)">')
start_url = re.findall(reg, html)[0]
s.post(start_url)

grade_url = 'http://jw.ecit.cn/gradeLnAllAction.do?type=ln&oper=qbinfo&lnxndm=2016-2017%D1%A7%C4%EA%B5%DA%D2%BB%D1%A7%C6%DA(%C1%BD%D1%A7%C6%DA)#qb_2016-2017%E5%AD%A6%E5%B9%B4%E7%AC%AC%E4%B8%80%E5%AD%A6%E6%9C%9F(%E4%B8%A4%E5%AD%A6%E6%9C%9F)'
grade_html = s.get(grade_url).text

cloumn_name_reg = re.compile('<th align="center" width="10%" class="sortable">\s*(.*?)\s*</th>')
cloumn_name = re.findall(cloumn_name_reg, grade_html)[0:7]
del cloumn_name[3]

grade_reg = re.compile('<td align="center">\s*(.*?)\s*</td>')
grade_pre_list = re.findall(grade_reg, grade_html)
grade_pre1_list = [i for i in grade_pre_list if not i.startswith('&nbsp')]
grade_list = []
for _ in grade_pre1_list:
    if not _.startswith('<p'):
        grade_list.append(_)
    else:
        reg_ = re.compile('<p align="center">(.*?)&nbsp;</P>')
        grade = re.findall(reg_, _)[0]
        grade_list.append(grade)

grade_data_ = pd.DataFrame()
grade_data = np.array(grade_list).reshape(-1, 6)
for i, j in zip(cloumn_name, range(6)):
    grade_data_[i] = grade_data[:, j]

print('1:打印最新的五门成绩')
print('2:保存所有的成绩到本地文件夹')
print('3:打印学位课成绩并计算平均学分绩')
print('\n')
select = input('请输入你的请求:')
if select == '1':
    print(grade_data_[-5:])
elif select == '2':
    grade_data_.to_csv('./grade_data.csv', index=False)
    print('成绩已保存在运行此程序的文件夹')
elif select == '3':
    xw_grade = grade_data_[(grade_data_['课程名'] == '*数学分析(I)') | (grade_data_['课程名'] == '高等代数(I)') |
                           (grade_data_['课程名'] == 'C语言程序设计基础') | (grade_data_['课程名'] == '大学英语（II）') |
                           (grade_data_['课程名'] == '*常微分方程') | (grade_data_['课程名'] == '*概率论') |
                           (grade_data_['课程名'] == '数据结构')]
    print(xw_grade)
    print('\n')
    avg_grade = np.sum((xw_grade.学分.astype(float) * xw_grade.成绩.astype(float))) / \
        np.sum(xw_grade.学分.astype(float))
    print('平均学分绩={0}'.format(avg_grade))
    input('按任意键结束')
