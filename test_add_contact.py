# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import unittest
from contact import Contact

class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def open_home_page(self, driver):
            driver.get("http://localhost/addressbook/edit.php")

    def login(self, wd, username, password):
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").send_keys(password)

    def open_add_contact_page(self, wd):
            wd.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Password:'])[1]/following::input[2]").click()

    def fill_contact_form(self, wd, contact):
        wd.find_element_by_name("firstname").send_keys(contact.fname)
        wd.find_element_by_name("lastname").send_keys(contact.lname)
        wd.find_element_by_name("nickname").send_keys(contact.nick)
        wd.find_element_by_name("title").send_keys(contact.title)
        wd.find_element_by_name("company").send_keys(contact.company)
        wd.find_element_by_name("address").send_keys(contact.address)
        wd.find_element_by_name("mobile").send_keys(contact.sellphone)
        wd.find_element_by_name("email").send_keys(contact.email)
        Select(wd.find_element_by_name("bday")).select_by_visible_text(contact.bday)
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact.bmonth)
        wd.find_element_by_name("byear").send_keys(contact.byear)
        wd.find_element_by_name("address2").send_keys(contact.address2)
        wd.find_element_by_name("notes").send_keys(contact.notes)
        #submit_contact_creation
        wd.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Notes:'])[1]/following::input[1]").click()

    def return_to_home_page(self, wd):
        wd.find_element_by_link_text("home").click()

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def test_add_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.open_add_contact_page(wd)
        self.fill_contact_form(wd, Contact(fname="Arnold", lname="Schwarzenegger", nick="Arni", title="Actor and governor",
                               company="Hollywood", address="Los Angeles, USA", sellphone="+1234567890", email="arni@hollywood.com",
                               bday="30", bmonth="July", byear="1947", address2="mansion near LA", notes="bla-bla-bla"))
        self.return_to_home_page(wd)
        self.logout(wd)

    def test_add_empty_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.open_add_contact_page(wd)
        self.fill_contact_form(wd, Contact(fname="", lname="", nick="", title="",
                               company="", address="", sellphone="", email="",
                               bday="-", bmonth="-", byear="-", address2="", notes=""))
        self.return_to_home_page(wd)
        self.logout(wd)

    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
