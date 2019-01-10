__autor__ = 'Dmitrii Dubrovskii'
import re


def test_contact_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.lname == contact_from_edit_page.lname
    assert contact_from_home_page.fname == contact_from_edit_page.fname
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_email_from_home_page == filter_email(contact_from_edit_page)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_page(contact_from_edit_page)

def filter_email(contact):
    return '\n'.join(filter(lambda x: x != "",
                            map(lambda x: clear(x), filter(lambda x: x is not None, [contact.email, contact.email2, contact.email3]))))

def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones_like_on_page(contact):
    return '\n'.join(filter(lambda x: x != "",
                            map(lambda x: clear(x), filter(lambda x: x is not None, [contact.home, contact.mobile, contact.work, contact.phone2]))))
