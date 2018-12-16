# -*- coding: utf-8 -*-
__autor__ = 'Dmitrii Dubrovskii'
import pytest
from contact import Contact
from application_contact import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.fill_contact_form(Contact(fname="Arnold", lname="Schwarzenegger", nick="Arni", title="Actor and governor",
                           company="Hollywood", address="Los Angeles, USA", sellphone="+1234567890", email="arni@hollywood.com",
                           bday="30", bmonth="July", byear="1947", address2="mansion near LA", notes="bla-bla-bla"))
    app.logout()

def test_add_empty_contact(app):
    app.login(username="admin", password="secret")
    app.fill_contact_form(Contact(fname="", lname="", nick="", title="",
                           company="", address="", sellphone="", email="",
                           bday="-", bmonth="-", byear="-", address2="", notes=""))
    app.logout()
