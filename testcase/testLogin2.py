# -*-coding:utf-8-*-

from app import mytest
import unittest

class TestLogin(mytest.Myunittest):
    """登录测试"""

    def test1(self):
        """第一步"""
        self.dr.find_element_by_id('com.cubic.autohome:id/owner_main_RadioButton').click()
        self.assertEqual(1,2,"不相等")

        self.dr.find_element_by_id('com.autohome.main.me:id/owner_guest_login').click()
        self.dr.find_element_by_id('com.autohome.main.me:id/change_old_owner_login').click()
        self.dr.find_element_by_id('com.autohome.main.me:id/owner_login_input_usr').send_keys('18611740012')
        self.dr.find_element_by_id('com.autohome.main.me:id/owner_login_pwd_container').send_keys('qingchezhijia123')
        self.dr.find_element_by_id('com.autohome.main.me:id/owner_login_commit').click()

    def test2(self):
        """第二步"""
        self.dr.find_element_by_id('com.autohome.main.me:id/owner_guest_login').click()
        self.dr.find_element_by_id('com.autohome.main.me:id/change_old_owner_login').click()
        self.dr.find_element_by_id('com.autohome.main.me:id/owner_login_input_usr').send_keys('18611740012')
        self.dr.find_element_by_id('com.autohome.main.me:id/owner_login_pwd_container').send_keys('qingchezhijia123')
        self.dr.find_element_by_id('com.autohome.main.me:id/owner_login_commit').click()



if __name__ == '__main__':
    unittest.main()