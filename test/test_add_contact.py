# -*- coding: utf-8 -*-
__autor__ = 'Dmitrii Dubrovskii'
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(fname="Arnold", lname="Schwarzenegger", nick="Arni", title="Actor and governor",
                      company="Hollywood", address="Los Angeles, USA", mobile="+1234567890", home="+9876543210",
                      work="01234567", email="arni@hollywood.com", bday="30", bmonth="July",
                      byear="1947", address2="mansion near LA", phone2="5558882221", notes="bla-bla-bla")
    app.contact.create(contact)
    assert len(old_contacts)+1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.contact_id_or_max) == sorted(new_contacts, key=Contact.contact_id_or_max)


#def test_add_empty_contact(app):
#    old_contacts = app.contact.get_contact_list()
#    contact = Contact(fname="", lname="", nick="", title="",
#                           company="", address="", sellphone="", email="",
#                           bday=None, bmonth=None, byear=None, address2="", notes="")
#    app.contact.create(contact)
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts)+1 == len(new_contacts)
#    old_contacts.append(contact)
#    assert sorted(old_contacts, key=Contact.contact_id_or_max) == sorted(new_contacts, key=Contact.contact_id_or_max)
