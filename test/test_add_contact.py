# -*- coding: utf-8 -*-
__autor__ = 'Dmitrii Dubrovskii'
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(Contact(fname="Arnold", lname="Schwarzenegger", nick="Arni", title="Actor and governor",
                           company="Hollywood", address="Los Angeles, USA", sellphone="+1234567890", email="arni@hollywood.com",
                           bday="30", bmonth="July", byear="1947", address2="mansion near LA", notes="bla-bla-bla"))
    assert len(old_contacts)+1 == app.contact.count()


def test_add_empty_contact(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(Contact(fname="", lname="", nick="", title="",
                           company="", address="", sellphone="", email="",
                           bday="-", bmonth="-", byear="-", address2="", notes=""))
    assert len(old_contacts) + 1 == app.contact.count()
