# -*- coding: utf-8 -*-
__autor__ = 'Dmitrii Dubrovskii'
from model.contact import Contact
import random


def test_add_contact_fname(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(fname="test"))
    old_contacts = db.get_contact_list()
    contact_mod = random.choice(old_contacts)
    contact = Contact(fname="Stich")
    app.contact.modify_contact_by_id(contact_mod.contact_id, contact)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    for i in range(len(old_contacts)):
        if old_contacts[i].contact_id == contact_mod.contact_id:
            old_contacts[i] = contact
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(old_contacts, key=Contact.contact_id_or_max) == sorted(new_contacts, key=Contact.contact_id_or_max)

#def test_contact_notes(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(fname="test"))
#    old_contacts = app.contact.get_contact_list()
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts) == len(new_contacts)
#    app.contact.modify_first_contact(Contact(notes="Some notes"))
