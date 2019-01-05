__author__ = 'Dmitrii'


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
        return self.contact_id == other.conid and self.lname == other.lname and self.fname == other.fname
