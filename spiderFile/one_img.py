import re
import requests

temp = 'http://wufazhuce.com/one/'
count = 1
for i in range(14, 1580):
    url = temp + str(i)
    page = requests.get(url).text
    reg = re.compile('<img src="(http://.*?)" alt="" />')
    img_url = re.findall(reg, page)
    if img_url != []:
        with open('./{}.jpg'.format(count), 'wb') as file:
            try:
                img_data = requests.get(img_url[0]).content
                file.write(img_data)
                count += 1
            except:
                pass
print('OK!')


















