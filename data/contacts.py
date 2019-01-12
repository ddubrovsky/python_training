# -*- coding: utf-8 -*-
__autor__ = 'Dmitrii Dubrovskii'
from model.contact import Contact


testdata = [
    Contact(fname="fname1", lname="lname1", nick="nick1", title="title1", company="company1", address="address1",
            mobile="mobile1", home="home1", work="work1", email="email1", bday='bday1', bmonth='bmonth1',
            byear='byear1', address2="address21", phone2="phone21", notes="notes1"),
    Contact(fname="fname2", lname="lname2", nick="nick2", title="title2", company="company2", address="address2",
            mobile="mobile2", home="home2", work="work2", email="email2", bday='bday2', bmonth='bmonth2',
            byear='byear1', address2="address22", phone2="phone22", notes="notes2")
]