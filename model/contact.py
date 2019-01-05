__author__ = 'Dmitrii'
from sys import maxsize

class Contact:

    def __init__(self, fname=None, lname=None, nick=None, title=None, company=None, address=None, sellphone=None,
                 email=None, bday="-", bmonth="-", byear="-", address2=None, notes=None, contact_id = None):
        self.fname = fname
        self.lname = lname
        self.nick = nick
        self.title = title
        self.company = company
        self.address = address
        self.sellphone = sellphone
        self.email = email
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.address2 = address2
        self.notes = notes
        self.contact_id = contact_id

    def __repr__(self):
        return "%s:%s:%s" % (self.contact_id, self.lname, self.fname)

    def __eq__(self, other):
        return (self.contact_id is None or other.contact_id is None or self.contact_id == other.contact_id, self.lname == other.lname, self.fname == other.fname)

    def contact_id_or_max(self):
        if self.contact_id:
            return int(self.contact_id)
        else:
            return maxsize
