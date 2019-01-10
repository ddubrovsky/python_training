# -*- coding: utf-8 -*-
__autor__ = 'Dmitrii Dubrovskii'
from model.contact import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_string_just_letters(prefix, maxlen):
    symbols = string.ascii_letters
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_string_just_digits(prefix, maxlen):
    symbols = string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_string_email(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(fname="", lname="", nick="", title="", company="", address="", mobile="", home="", work="", email="",
                    bday=None, bmonth=None, byear=None, address2="", phone2="", notes="")] + [
    Contact(fname=random_string_just_letters('firstname', 7), lname=random_string_just_letters('lastname', 12),
            nick=random_string('nick', 5), title=random_string_just_letters('title', 5), company=random_string('company', 10),
            address=random_string('address', 10), mobile=random_string_just_digits('mobile', 11), home=random_string_just_digits('home', 7),
            work=random_string_just_digits('work', 7), email=random_string_email('email', 5) + "@.yandex.com",
            email2=random_string_email('email2', 5) + "@.yahoo.com", email3=random_string_email('email3', 5) + "@.gmail.com",
            notes=random_string('notes', 35))
    for i in range (5)
]


@pytest.mark.parametrize('contact', testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts)+1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.contact_id_or_max) == sorted(new_contacts, key=Contact.contact_id_or_max)
