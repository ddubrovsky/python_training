__author__ = 'Dmitrii'
from sys import maxsize

class Contact:

    def __init__(self, fname=None, lname=None, nick=None, title=None, company=None, address=None, mobile=None,
                 home = None, work = None, fax = None, all_phones = None, email=None, email2=None, email3=None,
                 bday="-", bmonth="-", byear="-", address2=None, phone2 = None, notes=None, contact_id = None,
                 all_phones_from_home_page = None, all_email=None, all_email_from_home_page = None):
        self.fname = fname
        self.lname = lname
        self.nick = nick
        self.title = title
        self.company = company
        self.address = address
        self.mobile = mobile
        self.work = work
        self.phone2 = phone2
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.address2 = address2
        self.notes = notes
        self.contact_id = contact_id
        self.home = home
        self.all_phones = all_phones
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_email = all_email
        self.all_email_from_home_page = all_email_from_home_page

    def __repr__(self):
        return "%s:%s:%s:%s:%s" % (self.contact_id, self.lname, self.fname, self.all_phones, self.all_email)

    def __eq__(self, other):
        return (self.contact_id is None or other.contact_id is None or self.contact_id == other.contact_id, self.lname == other.lname, self.fname == other.fname)

    def contact_id_or_max(self):
        if self.contact_id:
            return int(self.contact_id)
        else:
            return maxsize
