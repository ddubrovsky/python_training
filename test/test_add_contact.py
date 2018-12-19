# -*- coding: utf-8 -*-
__autor__ = 'Dmitrii Dubrovskii'
import pytest
from model.contact import Contact
from fixture.application_contact import ApplicationContact


@pytest.fixture
def app(request):
    fixture = ApplicationContact()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
    app.session_contact.login(username="admin", password="secret")
    app.contact.fill_contact_form(Contact(fname="Arnold", lname="Schwarzenegger", nick="Arni", title="Actor and governor",
                           company="Hollywood", address="Los Angeles, USA", sellphone="+1234567890", email="arni@hollywood.com",
                           bday="30", bmonth="July", byear="1947", address2="mansion near LA", notes="bla-bla-bla"))
    app.session_contact.logout()

def test_add_empty_contact(app):
    app.session_contact.login(username="admin", password="secret")
    app.contact.fill_contact_form(Contact(fname="", lname="", nick="", title="",
                           company="", address="", sellphone="", email="",
                           bday="-", bmonth="-", byear="-", address2="", notes=""))
    app.session_contact.logout()
