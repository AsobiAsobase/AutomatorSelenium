import datetime
import time

from open_web_with_url import open_url
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

target_time = datetime.datetime(2024, 1, 10, 17, 44, 59, 355000)


def qun_find_target_element(url_str):
    browser = open_url(url_str)
    time.sleep(5)
    browser.find_element(By.XPATH, '//*[@id="js-feeds-list"]/li[1]/div/div[4]/p/a[1]').click()
    browser.find_element(By.XPATH, '//*[@id="$1_content_content"]').send_keys("test send key in web by automator. " +
                                                                              "target time：" + str(target_time))
    send_xpath = '//*[@id="js-feeds-list"]/li[1]/div/div[4]/div[3]/div/div[2]/div[1]/div/div/div/div[4]/div[4]/a[2]'
    target_element = browser.find_element(By.XPATH, send_xpath)
    return target_element


def target_send_message(target_element):
    current_time = datetime.datetime.now()
    while True:
        current_time = datetime.datetime.now()
        if current_time >= target_time:
            target_element.click()
            print(current_time)
            break


if __name__ == '__main__':
    element = qun_find_target_element('https://h5.qzone.qq.com/groupphoto/index?inqq=3&groupId=724528829')
    target_send_message(element)
