# coding:utf-8
from common.base import BasePage
from selenium import webdriver
# 定位博客的登录页面
login_url = "https://passport.cnblogs.com/user/signin"
# 定义LoginPage类，继承BasePage类
class LoginPage(BasePage):
    # 统一将登录页面元素定位放到下面
    user_loc = ("id", "input1") # 输入用户名框
    psw_loc = ("id", "input2") # 定位密码框
    button_loc = ("id", "signin") # 定位登录按钮
    tip_loc = ("id", "tip_btn")  # 获取提示语

    # 统一将登录也其他元素写在下面
    find_loc = ("link text", "找回") # 找回密码按钮
    reset_loc = ("link text", "重置") # 重置按钮
    remember_loc = ("id", "remember_me") # 下次自动登录
    zhuece_loc = ("link text", "立即注册") # 定位立即注册
    fankui_loc = ("link text", "反馈问题") # 反馈问题按钮

    # 定位输入账号方法
    def input_username(self, text):
        # 因为已经继承了BasePage类，可以调用他的send_keys方法
        # 输入用户名
        self.send_keys(self.user_loc, text, is_clear=False)

    def input_psw(self, text):
        # 因为已经继承了BasePage类，可以调用他的send_keys方法
        # 输入密码
        self.send_keys(self.psw_loc, text,is_clear=True)

    def click_login_button(self):
        # 因为已经继承了BasePage类，可以调用他的click方法
        # 点击登录按钮
        self.click(self.button_loc)

    def get_tip(self):
        # 因为已经继承了BasePage类，调用获取元素文本的方法
        # 获取提示语
        t = self.get_text(self.tip_loc)
        return t

    def click_find(self):
        # 因为已经继承了BasePage类，可以调用他的click方法
        # 找回密码
        self.click(self.find_loc)

    def click_reset(self):
        # 因为已经继承了BasePage类，可以调用他的click方法
        # 重置按钮
        self.click(self.reset_loc)

    def click_remember(self):
        # 因为已经继承了BasePage类，可以调用他的click方法
        # 下次自动登录
        self.click(self.remember_loc)

if __name__ == "__main__":
    driver = webdriver.Firefox()
    login_driver = LoginPage(driver)
    login_driver.open(login_url)
    login_driver.input_username("xxxx")
    login_driver.input_psw("xxxx")
    login_driver.click_login_button()
    t = login_driver.get_tip()
    print(t)













