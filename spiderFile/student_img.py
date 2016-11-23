import requests

"""
思路：去官网自己的主页，看自己的照片的url然后你懂的。
"""
url = ''
banji = []
zhuanye = []
for a in range(10):
    for b in range(10):
        banji.append(str(a) + '0' + str(b))
for c in range(10):
    zhuanye.append('20' + str(c))

for year in range(2011, 2015):
    for xh in zhuanye:
        for nj in banji:
            for i in range(1, 35):
                if i < 10:
                    xuehao = str(year) + str(xh) + str(nj) + '0' + str(i)
                    student_url = url + xuehao
                    with open('E:/student_img/%s.jpeg' % xuehao, 'wb') as file:
                        file.write(requests.get(student_url).content)
                else:
                    xuehao = str(year) + str(xh) + str(nj) + str(i)
                    student_url = url + xuehao
                    with open('E:/student_img/%s.jpeg' % xuehao, 'wb') as file:
                        file.write(requests.get(student_url).content)
print('OK!')
