__autor__ = 'Dmitrii Dubrovskii'
from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper


class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(2)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def is_session_valid(self):
        try:
            self.wd.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='home'])[1]/preceding::a[3]")
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        if (wd.current_url):
            wd.get("http://localhost/addressbook/")
        else:
            pass

    def destroy(self):
        self.wd.quit()