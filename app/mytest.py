# -*-coding:utf-8-*-

import unittest
import time
from dirver import Driver

class Myunittest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.dr = Driver()
        # cls.dr.implicitly_wait(30)
        return cls.dr

    @classmethod
    def tearDownClass(cls):
        time.sleep(2)
        cls.dr.quit()

    # 每执行一个测试用例，就重启开启一次 appium Session（现象-重启app）
    # def setUp(self):
    #     self.dr = Driver()
    #     self.dr.implicitly_wait(30)
    #     return self.dr
    #
    # def tearDown(self):
    #     self.dr.quit()


if __name__ == '__main__':
    Myunittest()