from selenium import webdriver
from open_chrome import open_chrome

browser = open_chrome()

#open baidu web and print this url
def open_url(str):
    browser.get(str)
    url = browser.current_url
    print("打开网址：" + url)
    return browser


if __name__ == '__main__':
    open_url('https://h5.qzone.qq.com/groupphoto/index?inqq=3&groupId=724528829')