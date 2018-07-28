# __author__ = 'zhanghzhiyuan'
# -*-coding:utf-8-*-
import sys,os
reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append(os.path.abspath('../..'))
from uiapptest.app import util
from uiapptest.app.mytest import Myunittest
from uiapptest.app.dirver import Driver
from uiapptest.app.testcase import Testcase
import unittest

'''
===========说明============
功能:测试用例定义
入口:ecxel表格测试用例
==========================
'''

class TestLogin(Myunittest):
    """汽车之家:登录测试"""

    testcaseList = util.getXlsTestCase('login')
    for testcase in testcaseList:
        # 判断测试用例是否执行 1——执行,0——不执行;
        exec (util.FUNC_TEMPLATE.format(func=testcase['case_id'],
                                   casename=testcase['case_name'],
                                   onecase=testcase,
                                   sheetname='login',
                                   state=testcase['state']
                                   ))

if __name__ == '__main__':
    unittest.main()