from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# from Page.PIM import PimPage
from login import LoginPage
from search import SearchPage
from admin import AdminPage

s = Service('/path/to/chromedriver')
driver = webdriver.Chrome(service=s)


def test_browserstack():
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()
    driver.implicitly_wait(10)

    login = LoginPage(driver)
    login.select_username()
    login.select_password()
    login.click_login()
    time.sleep(10)

    search = SearchPage(driver)
    search.search()
    search.search_admin()


    admin = AdminPage(driver)
    admin.click_button()

    # pim = PimPage(driver)
    # pim.click_pim()
    # pim.select_empname()
    time.sleep(10)


test_browserstack()