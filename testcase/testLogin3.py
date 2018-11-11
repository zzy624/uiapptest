# -*-coding:utf-8-*-

from app import mytest
import unittest
# from app.element import Element

class TestLogin(mytest.Myunittest):
    """登录测试"""

    def test1(self):
        """第1步"""
        self.dr.find_element_by_id('com.cubic.autohome:id/owner_main_RadioButton').click()
        self.InsertImg(self.dr,u"第1步")
        # self.assertEqual(1,2,"不相等")

    def test2(self):
        """第2步"""
        self.dr.find_element_by_id('com.autohome.main.me:id/owner_guest_login').click()

    def test3(self):
        """第3步"""
        self.dr.find_element_by_id('com.autohome.main.me:id/change_old_owner_login').click()

    def test4(self):
        """第4步"""
        self.dr.find_element_by_id('com.autohome.main.me:id/owner_login_input_usr').send_keys('18611740012')

    def test5(self):
        """第5步"""
        self.dr.find_element_by_id('com.autohome.main.me:id/owner_login_pwd_container').send_keys('qingchezhijia123')

    def test6(self):
        """第6步"""
        self.dr.find_element_by_id('com.autohome.main.me:id/owner_login_commit').click()



if __name__ == '__main__':
    unittest.main()