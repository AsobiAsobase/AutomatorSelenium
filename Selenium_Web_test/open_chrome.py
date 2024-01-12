from selenium import webdriver
from setting_ChromeOptions import setting_opt, setting_service

def open_chrome():
    opt = setting_opt()
    service = setting_service()
    browser = webdriver.Chrome(options=opt, service=service)
    #browser.maximize_window()
    return browser

if __name__ == '__main__':
    open_chrome()