# -*- coding: utf-8 -*-
__autor__ = 'Dmitrii Dubrovskii'
from model.contact import Contact


def test_add_contact_fname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(fname="test"))
    old_contacts = app.contact.get_contact_list()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    app.contact.modify_first_contact(Contact(fname="Stich"))


def test_contact_notes(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(fname="test"))
    old_contacts = app.contact.get_contact_list()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    app.contact.modify_first_contact(Contact(notes="Some notes"))
