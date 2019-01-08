__autor__ = 'Dmitrii Dubrovskii'
from selenium.webdriver.support.ui import Select
from model.contact import Contact
import re

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_add_contact_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/edit.php")) and not len (wd.find_elements_by_name("photo")) > 0:
            wd.find_element_by_link_text("add new").click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def change_field_select(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(text)

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.fname)
        self.change_field_value("lastname", contact.lname)
        self.change_field_value("nickname", contact.nick)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("home", contact.home)
        self.change_field_value("work", contact.work)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email)
        self.change_field_select("bday", contact.bday)
        self.change_field_select("bmonth", contact.bmonth)
#        Select(wd.find_element_by_name("bday")).select_by_visible_text(contact.bday)
#        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact.bmonth)
        self.change_field_value("byear", contact.byear)
        self.change_field_value("address2", contact.address2)
        self.change_field_value("notes", contact.notes)

    def submit_contact_creation(self):
        wd = self.app.wd
        wd.find_element_by_name("submit").click()

    def create(self, contact):
        wd = self.app.wd
        self.open_add_contact_page()
        self.fill_contact_form(contact)
        self.submit_contact_creation()
        self.return_to_home_page()
        self.contact_cache = None

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_index(index)
        #click delete
        wd.find_element_by_xpath("//div/div[4]/form[2]/div[2]/input").click()
        #submit deletion
        wd.switch_to_alert().accept()
        self.return_to_home_page()
        self.contact_cache = None

    def modify_first_contact(self):
        self.modify_contact_by_index(0)

    def modify_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_index(index)
        self.open_modification_form(index)
        self.fill_contact_form(new_contact_data)
        wd.find_element_by_name("update").click()
        self.return_to_home_page()
        self.contact_cache = None

    def open_modification_form(self, index):
        wd = self.app.wd
        #self.app.open_home_page()
        #wd.find_element_by_css_selector("td.center:nth-child(8) > a:nth-child(1) > img:nth-child(1)").click()
        wd.find_elements_by_css_selector('img[alt="Edit"]')[index].click()

    def return_to_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/")) and len(wd.find_elements_by_link_text("Send e-Mail")) > 0:
            wd.find_element_by_link_text("home page").click()

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

#    def get_contact_list(self):
#        if self.contact_cache is None:
#            wd = self.app.wd
#            self.app.open_home_page()
#            self.contact_cache = []
#            for row in wd.find_elements_by_name('entry'):
#                cells = row.find_element_by_tag_name('td')
#                lastname = cells[1].text
#                firstname = cells[2].text
#                id = cells[0].find_element_by_tag_name('input').get_attribute('value')
#                all_phones = cells[5].text.splitlines()
#                self.contact_cache.append(Contact(lname=lastname, fname=firstname, contact_id=id,
#                                                  homephone=all_phones[0], sellphone=all_phones[1],
#                                                  workphone=all_phones[2], secondaryphone=all_phones[3]))
#        return list(self.contact_cache)

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_xpath("//tr[@name='entry']"):
                id = element.find_element_by_css_selector("td.center").find_element_by_name("selected[]").get_attribute("value")
                lastname = element.find_element_by_xpath(".//td[2]").text
                firstname = element.find_element_by_xpath(".//td[3]").text
                all_phones = element.find_element_by_xpath(".//td[6]").text.splitlines()
                self.contact_cache.append(Contact(lname=lastname, fname=firstname, contact_id=id,
                                                  home=all_phones[0], mobile=all_phones[1],
                                                  work=all_phones[2], fax=all_phones[3]))
        return list(self.contact_cache)


    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name('entry')[index]
        cell = row.find_elements_by_tag_name('td')[7]
        cell.find_element_by_tag_name('a').click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name('entry')[index]
        cell = row.find_elements_by_tag_name('td')[6]
        cell.find_element_by_tag_name('a').click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name('firstname').get_attribute('value')
        lastname = wd.find_element_by_name('lastname').get_attribute('value')
        id = wd.find_element_by_name('id').get_attribute('value')
        home = wd.find_element_by_name('home').get_attribute('value')
        mobile = wd.find_element_by_name('mobile').get_attribute('value')
        work = wd.find_element_by_name('work').get_attribute('value')
        fax = wd.find_element_by_name('fax').get_attribute('value')
        return Contact(fname=firstname, lname=lastname, contact_id=id,
                       home=home, mobile=mobile, work=work, fax=fax)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        wd.find_elements_by_css_selector('img[alt="Details"]')[index].click()
        text = wd.find_element_by_id("content").text
        home = re.search("H: (.*)", text).group(1)
        mobile = re.search("M: (.*)", text).group(1)
        work = re.search("W: (.*)", text).group(1)
        fax = re.search("F: (.*)", text).group(1)
        return Contact(home=home, mobile=mobile, work=work, fax=fax)
