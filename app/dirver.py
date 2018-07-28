# -*-coding:utf-8-*-
from appium import webdriver
import time

def Driver():
    desired_caps = {'platformName': 'Android',
                    'platformVersion': '4.4.2',
                    'deviceName': '192.168.31.171:5555',
                    'appPackage': 'com.cubic.autohome',
                    'appActivity': '.LogoActivity',
                    'unicodeKeyboard': True,
                    'resetKeyboard': True,
                    'noReset': False,
                    # 'newCommandTimeout': 100
                    }

    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    driver.implicitly_wait(100)

    return driver

if __name__ == '__main__':
    d = Driver()
    time.sleep(2)
    d.quit()

