# -*-coding:utf-8-*-
from appium import webdriver
import time

def Driver():
    desired_caps = {'platformName': 'Android',
                    'platformVersion': '4.4.2',
                    'deviceName': 'test',
                    'appPackage': 'com.cubic.autohome',
                    'appActivity': '.LogoActivity',
                    'unicodeKeyboard': True,
                    'resetKeyboard': True,
                    'noReset': False,
                    }

    dr = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    dr.implicitly_wait(30)

    return dr

if __name__ == '__main__':
    d = Driver()
    time.sleep(2)
    d.quit()

