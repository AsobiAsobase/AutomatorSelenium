from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


# set Chrome options
def setting_opt():
    opt = Options()
    opt.binary_location = r"D:\chrome-win64\chrome.exe"
    # keep browser open
    opt.add_experimental_option("detach", True)
    return opt


# set specified chromedriver
def setting_service():
    service = Service(executable_path=r"D:\chrome-win64\chromedriver.exe")
    return service
