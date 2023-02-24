from seleniumpagefactory.Pagefactory import PageFactory


class SearchPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
            'Search':( 'XPATH','//input[@placeholder="Search"]')
    }
    def search(self):
        self.Search.click()
    def search_admin(self):
        self.Search.send_keys("admin")
