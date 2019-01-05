# -*- coding: utf-8 -*-
__autor__ = 'Dmitrii Dubrovskii'
from model.contact import Contact


def test_add_contact_fname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(fname="test"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(fname="Stich")
    contact.contact_id = old_contacts[0].contact_id
    app.contact.modify_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.contact_id_or_max) == sorted(new_contacts, key=Contact.contact_id_or_max)


#def test_contact_notes(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(fname="test"))
#    old_contacts = app.contact.get_contact_list()
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts) == len(new_contacts)
#    app.contact.modify_first_contact(Contact(notes="Some notes"))
