# -*-coding:utf-8-*-
import os
import time
from fractions import Fraction
from appium.webdriver.common.touch_action import TouchAction

class Element(object):
    def findById(self, driver, id):
        print("元素通过 ID 定位")
        return driver.find_element_by_id(id)

    def findByName(self, driver, name):
        return driver.find_element_by_android_uiautomator('new UiSelector().text("' + name + '")')

    def findByClass(self, driver, className):
        return driver.find_element_by_class_name(className)

    def findByIds(self, driver, id, index):
        return driver.find_elements_by_id(id)[index]

    def findByNames(self, driver, name, index):
        return driver.find_elements_by_android_uiautomator('new UiSelector().text("' + name + '")')[index]

    def findByClasses(self, driver, className, index):
        return driver.find_elements_by_class_name(className)[index]

    def InsertImg(self, driver, file_name):
        file_path = os.path.dirname(__file__).split('/app')[0] + '/data/image/' + file_name + '.png'
        if driver.get_screenshot_as_file(file_path):
            print("截图保留至:{0}".format(file_path))
        else:
            print("截图保留失败")

    def script(self, driver, src):
        return driver.execute_script(src)

    def Tag(self, driver, value):
        """
        :param driver:
        :param value: (x,y,duration)
        :return:
        """

        #获取点击坐标
        if '，' in value:
            value = value.replace('，',',')
        tag_value = eval(value)
        #判断是否存在长按时间
        if len(tag_value) >2:
            duration = tag_value[2]
        else:
            duration = None
        tag_x = tag_value[0]
        tag_y = tag_value[1]
        #分辨率换算
        ratioX = float("%.2f" % (float(1080) / float(320)))
        ratioY = float("%.2f" % (float(1920) / float(760)))
        #换算后的坐标
        start_x = float("%.2f" % (float(tag_x) / ratioX))
        start_y = float("%.2f" % (float(tag_y) / ratioY))

        time.sleep(2)
        action = TouchAction(driver)
        try:
            if duration:
                duration = duration * 1000
                action.long_press(x=start_x, y=start_y, duration=duration).release()
            else:
                # TouchAction(self.driver).press(None, x, y).release().perform()
                action.tap(x=start_x, y=start_y)
            action.perform()
            return True
        except BaseException as e:
            print(e)
            return False

    def Swipe2(self, driver, start_x, start_y, end_x, end_y, duration=200):
        time.sleep(3)
        try:
            driver.swipe(start_x, start_y, end_x, end_y, duration)
            return True
        except BaseException as e:
            print(e)
            return False

    def Swipe(self, driver, direction, value, during=200):
        """
        swipe UP
        :param during:
        :return:
        """
        time.sleep(3)
        window_size = driver.get_window_size()
        width = window_size.get("width")
        height = window_size.get("height")
        if direction == 'down':
            x1 = width/2
            y1 = 60
            x2 = width/2
            i = (Fraction(1) - Fraction(value))
            if i == 0:
                y2 = height-1
            else:
                y2 = width * i.numerator / i.denominator
            try:
                driver.swipe(x1,y1,x2,y2, during)
                return True
            except Exception as e:
                print(e)
                return False
        elif direction == 'up':
            x1 = width/2
            y1 = height-1
            x2 = width/2
            i = (Fraction(1) - Fraction(value))
            if i == 0:
                y2 = 1
            else:
                y2 = width * i.numerator / i.denominator
            try:
                driver.swipe(x1,y1,x2,y2, during)
                return True
            except Exception as e:
                print(e)
                return False
        elif direction == 'right':
            x1 = 1
            y1 = height/2
            y2 = height/2
            i = (Fraction(1) - Fraction(value))
            if i == 0:
                y2 = width-1
            else:
                y2 = width * i.numerator / i.denominator
            try:
                driver.swipe(x1,y1,x2,y2, during)
                return True
            except Exception as e:
                print(e)
                return False
        elif direction == 'left':
            x1 = width-1
            y1 = height/2
            y2 = height/2
            i = (Fraction(1) - Fraction(value))
            if i == 0:
                x2 = 1
            else:
                x2 = width * i.numerator / i.denominator
            try:
                driver.swipe(x1,y1,x2,y2, during)
                return True
            except Exception as e:
                print(e)
                return False
        else:
            return False

