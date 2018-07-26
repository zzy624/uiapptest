# -*-coding:utf-8-*-
import os
from fractions import Fraction
from appium.webdriver.common.touch_action import TouchAction


class Element(object):
    def findById(self, dirver, id):
        print("元素通过 ID 定位")
        return dirver.find_element_by_id(id)

    def findByName(self, dirver, name):
        return dirver.find_element_by_android_uiautomator('new UiSelector().text("' + name + '")')

    def findBycClass(self, dirver, className):
        return dirver.find_element_by_class_name(className)

    def findByIds(self, dirver, id, index):
        return dirver.find_element_by_id(id)[index]

    def findByNames(self, dirver, name, index):
        return dirver.find_element_by_android_uiautomator('new UiSelector().text("' + name + '")')[index]

    def findBycClasses(self, dirver, className, index):
        return dirver.find_element_by_class_name(className)[index]

    def InsertImg(self, dirver, file_name):
        file_path = os.path.dirname(__file__).split('/app')[0] + '/data/' + file_name + '.png'
        if dirver.get_screenshot_as_file(file_path):
            print("截图保留至:{0}".format(file_path))
        else:
            print("截图保留失败")

    def script(self, dirver, src):
        return dirver.execute_script(src)

    def Tag(self, dirver, x, y, duration):
        time.sleep(2)
        action = TouchAction(dirver)
        try:
            if duration:
                duration = duration * 1000
                action.long_press(x=x, y=y, duration=duration).release()
            else:
                # TouchAction(self.dirver).press(None, x, y).release().perform()
                action.tap(x=x, y=y)
            action.perform()
            return True
        except BaseException as e:
            print(e)
            return False

    def Swipe2(self, dirver, start_x, start_y, end_x, end_y, duration=200):
        time.sleep(3)
        try:
            dirver.swipe(start_x, start_y, end_x, end_y, duration)
            return True
        except BaseException as e:
            print(e)
            return False

    def Swipe(self, dirver, direction, value, during=200):
        """
        swipe UP
        :param during:
        :return:
        """
        time.sleep(3)
        window_size = dirver.get_window_size()
        width = window_size.get("width")
        height = window_size.get("height")
        if direction == 'down':
            i = Fraction(1) - Fraction(value)
            try:
                dirver.swipe(width / 2, height * 3 / 4, width / 2, height * i.numerator / i.denominator, during)
                return True
            except Exception as e:
                print(e)
                return False
        elif direction == 'up':
            i = Fraction(value)
            try:
                dirver.swipe(width / 2, height / 4, width / 2, height * i.numerator / i.denominator, during)
                return True
            except Exception as e:
                print(e)
                return False
        elif direction == 'right':
            i = Fraction(1, 4) + Fraction(value)
            try:
                dirver.swipe(width / 4, height / 2, width * i.numerator / i.denominator, height / 2, during)
                return True
            except Exception as e:
                print(e)
                return False
        elif direction == 'left':
            i = (Fraction(3, 4) - Fraction(value))
            try:
                dirver.swipe(width * 3 / 4, height / 2, width * i.numerator / i.denominator, height / 2, during)
                return True
            except Exception as e:
                print(e)
                return False
        else:
            return False
