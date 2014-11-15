# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

# tests user login
# 
# errors with username user_id 
class UnittestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://127.0.0.1:8000/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_unittest_login(self):
        driver = self.driver
        driver.get(self.base_url + "/login/?csrfmiddlewaretoken=CRYUwSdKmSB15rKlt7lXvsiqbFCLiTJt")
        # ERROR: Caught exception [Error: locator strategy either id or name must be specified explicitly.]
        # ERROR: Caught exception [Error: locator strategy either id or name must be specified explicitly.]
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()



# tests user registration
# 
# errors with username user_id 
# class UserRegister(unittest.TestCase):
#     def setUp(self):
#         self.driver = webdriver.Firefox()
#         self.driver.implicitly_wait(30)
#         self.base_url = "http://127.0.0.1:8000/"
#         self.verificationErrors = []
#         self.accept_next_alert = True
    
#     def test_user_register(self):
#         driver = self.driver
#         driver.get(self.base_url + "/")
#         driver.find_element_by_xpath("//input[@value='Register']").click()
#         driver.find_element_by_id("id_username").clear()
#         driver.find_element_by_id("id_username").send_keys("1234")
#         driver.find_element_by_id("id_email").clear()
#         driver.find_element_by_id("id_email").send_keys("1234@gmail.com")
#         driver.find_element_by_id("id_password").clear()
#         driver.find_element_by_id("id_password").send_keys("1234")
#         driver.find_element_by_id("id_password1").clear()
#         driver.find_element_by_id("id_password1").send_keys("1234")
#         driver.find_element_by_id("id_name").clear()
#         driver.find_element_by_id("id_name").send_keys("1234")
#         driver.find_element_by_css_selector("input[type=\"submit\"]").click()
#         driver.find_element_by_id("id_username").clear()
#         driver.find_element_by_id("id_username").send_keys("1234")
#         driver.find_element_by_id("id_password").clear()
#         driver.find_element_by_id("id_password").send_keys("1234")
#         driver.find_element_by_css_selector("input[type=\"submit\"]").click()
    
#     def is_element_present(self, how, what):
#         try: self.driver.find_element(by=how, value=what)
#         except NoSuchElementException, e: return False
#         return True
    
#     def is_alert_present(self):
#         try: self.driver.switch_to_alert()
#         except NoAlertPresentException, e: return False
#         return True
    
#     def close_alert_and_get_its_text(self):
#         try:
#             alert = self.driver.switch_to_alert()
#             alert_text = alert.text
#             if self.accept_next_alert:
#                 alert.accept()
#             else:
#                 alert.dismiss()
#             return alert_text
#         finally: self.accept_next_alert = True
    
#     def tearDown(self):
#         self.driver.quit()
#         self.assertEqual([], self.verificationErrors)

# if __name__ == "__main__":
#     unittest.main()




# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class RegisteringUsers(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://127.0.0.1:8000/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_registering_users(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_xpath("//input[@value='Register']").click()
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys("1234")
        driver.find_element_by_id("id_email").clear()
        driver.find_element_by_id("id_email").send_keys("1234@gmail.com")
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys("1234")
        driver.find_element_by_id("id_password1").clear()
        driver.find_element_by_id("id_password1").send_keys("1234")
        driver.find_element_by_id("id_name").clear()
        driver.find_element_by_id("id_name").send_keys("1234")
        driver.find_element_by_css_selector("input[type=\"submit\"]").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
