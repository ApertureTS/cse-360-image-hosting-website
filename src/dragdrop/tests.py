# from django.test import TestCase
# # -*- coding: utf-8 -*-
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import Select
# from selenium.common.exceptions import NoSuchElementException
# from selenium.common.exceptions import NoAlertPresentException
# import unittest, time, re


# # Create your tests here.

# # testing user registration, then logging in, and navigating to images
# # 
# # currently getting Selenium errors for uploading gif images
# class UserRegisterLoginUploadNavigateToImages(unittest.TestCase):
#     def setUp(self):
#         self.driver = webdriver.Firefox()
#         self.driver.implicitly_wait(30)
#         self.base_url = "http://127.0.0.1:8000/"
#         self.verificationErrors = []
#         self.accept_next_alert = True
    
#     def test_user_register_login_upload_navigate_to_images(self):
#         driver = self.driver
#         driver.get(self.base_url + "/")
#         driver.find_element_by_xpath("//input[@value='Register']").click()
#         driver.find_element_by_id("id_username").clear()
#         driver.find_element_by_id("id_username").send_keys("asjdasjd12837123")
#         driver.find_element_by_id("id_email").clear()
#         driver.find_element_by_id("id_email").send_keys("asjdasjd12837123@gmail.com")
#         driver.find_element_by_id("id_password").clear()
#         driver.find_element_by_id("id_password").send_keys("Asd123")
#         driver.find_element_by_id("id_password1").clear()
#         driver.find_element_by_id("id_password1").send_keys("Asd123")
#         driver.find_element_by_id("id_name").clear()
#         driver.find_element_by_id("id_name").send_keys("Asd123ispass")
#         driver.find_element_by_css_selector("input[type=\"submit\"]").click()
#         driver.find_element_by_id("id_username").clear()
#         driver.find_element_by_id("id_username").send_keys("asjdasjd128371234")
#         driver.find_element_by_id("id_email").clear()
#         driver.find_element_by_id("id_email").send_keys("asjdasjd128371234@gmail.com")
#         driver.find_element_by_id("id_password").clear()
#         driver.find_element_by_id("id_password").send_keys("Asd1234")
#         driver.find_element_by_id("id_password1").clear()
#         driver.find_element_by_id("id_password1").send_keys("Asd1234")
#         driver.find_element_by_css_selector("input[type=\"submit\"]").click()
#         driver.find_element_by_id("id_username").clear()
#         driver.find_element_by_id("id_username").send_keys("asjdasjd128371234")
#         driver.find_element_by_id("id_password").clear()
#         driver.find_element_by_id("id_password").send_keys("Asd1234")
#         driver.find_element_by_css_selector("input[type=\"submit\"]").click()
#         # ERROR: Caught exception [Error: locator strategy either id or name must be specified explicitly.]
#         driver.find_element_by_xpath("(//input[@name='redirect'])[2]").click()
#         driver.find_element_by_name("redirect").click()
    
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