__author__ = 'Dmitrii'


class Contact:

    def __init__(self, fname=None, lname=None, nick=None, title=None, company=None, address=None, sellphone=None,
                 email=None, bday="-", bmonth="-", byear="-", address2=None, notes=None):
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