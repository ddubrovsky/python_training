__autor__ = 'Dmitrii Dubrovskii'
from selenium.webdriver.support.ui import Select


class ContactHelper:

    def __init__(self, app):
        self.app = app


    def open_add_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Password:'])[1]/following::input[2]").click()

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.open_add_contact_page()
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
        self.return_to_home_page()

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
