# coding:utf-8
from common.base import BasePage
from selenium import webdriver

find_url = "https://passport.cnblogs.com/GetUsername.aspx"

class FindPage(BasePage):
    find_loc = ("class name", "topic_title")

    def get_find_text(self):
        t = self.get_text(self.find_loc)
        return t

if __name__ == "__main__":
    driver = webdriver.Firefox()
    find_driver = FindPage(driver)
    find_driver.open("https://passport.cnblogs.com/GetUsername.aspx")
    t = find_driver.get_find_text()
    print(t)