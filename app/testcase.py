# -*-coding:utf-8-*-

from app import util
from app.element import Element
import time
import re

class Testcase(Element):
    """测试用例基础类"""
    def __init__(self,driver,testcase,testname):
        self.driver = driver
        self.testcase = testcase
        self.testname = testname
        self.case_id = self.testcase['case_id']
        self.case_name = self.testcase['case_name']
        self.path_value = self.testcase['pathValue']
        self.path_type = self.testcase['pathType']
        self.action = self.testcase['action']
        self.value = self.testcase['value']
        self.expected = self.testcase['expected']

    def get_expected(self,expected):
        if '【' not in expected and '.' in expected:
            return expected
        else:
            # 获取表格中'【 】'里面的的值,返回列表
            value = re.compile('【(.*?)】')
            expected_value = value.findall(str(expected))

            return expected_value

    def log(self,actual_value,results_value):
        #实际结果和执行情况写入表格,记录日志
        actual = util.setResults(self.testname, self.case_id, 'actual', actual_value)
        results = util.setResults(self.testname, self.case_id, 'results', results_value)
        if actual and results:
            print('测试结果写入完成!<' + self.case_id + ':'+ results_value+'>')
        else:
            print('测试结果写入失败')

    def execute_case(self):
        """执行测试用例"""
        #-------------------------------------执行测试用例---------------------------------------
        print('==========开始执行测试用例' + self.case_id + '===========')
        if self.action in ['click','sendkey','swipe','swipe2','back','tag','sleep']:
            # 获取页面元素
            try:
                if self.path_type == 'id':
                    element = self.findById(self.driver,self.path_value)
                if self.path_type == 'name':
                    element = self.findByName(self.driver,self.path_value)
                if self.path_type == 'class':
                    element = self.findByClass(self.driver,self.path_value)
            except BaseException as e:
                print(e)
                raise ValueError('元素定位失败')

            if self.action == 'click':
                element.click()
            elif self.action == 'sendkey':
                try:
                    self.driver.hide_keyboard()
                except BaseException as e:
                    pass
                element.clear()
                element.send_keys(str(self.value))
            elif self.action == 'swipe2':
                start_x = self.value.split(',')[0]
                start_y = self.value.split(',')[1]
                end_x = self.value.split(',')[2]
                end_y = self.value.split(',')[3]
                if not self.Swipe2(start_x,start_y,end_x,end_y):
                    print("滑动失败")
            elif self.action == 'swipe':
                swipe_value = self.value.split(',')
                if not self.Swipe(swipe_value[0], swipe_value[1]):
                    print("滑动失败")
            elif self.action == 'tag':
                if self.Tag(self.driver,self.value):
                    print("点击坐标成功")
                else:
                    print("点击坐标失败")
            elif self.action == 'sleep':
                time.sleep(int(self.value))
            elif self.action == 'back':
                try:
                    self.driver.press_keycode('4')
                except BaseException as e:
                    print('{0},返回失败'.format(e))
        else:
            print("测试用例没有执行动作或未识别执行动作")
            raise ValueError('测试用例没有执行动作或未识别执行动作')
        print('结束' + self.action + '动作')

        # 如果预期结果为空，不进行判断操作
        if self.expected == '':
            self.log(actual_value=u'预期页面显示正常', results_value='pass')
            # self.InsertImg(self.case_name)
            print('==========测试用执行完成' + self.case_id + '===========\n\r')
        else:
            self.compare_result()

    # 结果比较
    def compare_result(self):
        expectedlist = self.get_expected(self.expected)
        #判断预期页面是字符或者是activity
        if isinstance(expectedlist, list):
            for expected in expectedlist:
                # 查找预期页面元素
                try:
                    self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("' + expected + '")')
                    print('预期页面中存在<' + expected +'>元素')
                    # expect = True
                except BaseException:

                    print('预期页面中不存在<' + expected + '>元素')
                    self.InsertImg(self.driver,self.case_name)
                    self.log(actual_value=u'实际页面中不存在:<' + expected+ '>', results_value='fail')
                    print('==========测试用执行完成' + self.case_id + '===========\n\r')
                    msg = '预期界面中不存在<' + expected + '>元素'
                    assert False, msg
        else:
            if self.driver.current_activity == expectedlist:
                print('预期界面中存在<'+expectedlist+'>activity')
            else:
                print('预期界面中不存在<'+expectedlist+'>activity')
                self.InsertImg(self.driver,self.case_name)
                self.log(actual_value=u'预期页面元素显示不正常', results_value='fail')
                print('==========测试用执行完成' + self.case_id + '===========\n\r')
                msg = '预期界面中不存在<'+self.expected+'>activity'
                assert False, msg

        self.log(actual_value=u'预期页面显示正常', results_value='pass')
        print('==========测试用执行完成' + self.case_id + '===========\n\r')
