from seleniumpagefactory.Pagefactory import PageFactory
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class AdminPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
            'Admin_menu': (By.XPATH, "//a[@class='oxd-main-menu-item']")
        }

    def click_button(self):
        self.Admin_menu.click()

# class AdminPage(PageFactory):
#     def __init__(self, driver):
#         self.driver = driver
#
#
#     admin_menu = (By.XPATH, "//a[@class='oxd-main-menu-item']")
#
#
#
#     def click_admin(self):
#         self.admin_menu.click()
