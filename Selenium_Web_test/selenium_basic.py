import time

from open_web_with_url import open_url
from selenium.webdriver.common.by import By

#open baidu web and back the tab
def chrome_back(str):
    browser = open_url(str)
    time.sleep(5)
    #browser.find_element(By.XPATH, '//*[@id="kw"]').send_keys('百度')
    browser.find_element(By.XPATH, '//*[@id="qlogin_list"]/a').click()
    #browser.back()
    #browser.quit()

if __name__ == '__main__':
    chrome_back('https://h5.qzone.qq.com/groupphoto/index?inqq=3&groupId=724528829')