# -*- coding: utf-8 -*-
__autor__ = 'Dmitrii Dubrovskii'
from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n =5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


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

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)
with open(file, 'w') as out:
    jsonpickle.set_encoder_options('json', indent=2)
    out.write(jsonpickle.encode(testdata))
