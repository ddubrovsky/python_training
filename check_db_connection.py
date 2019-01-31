#import mysql.connector
from fixture.db import Dbfixture

#connection = mysql.connector.connect(host="127.0.0.1", database="addressbook", user="root", password="")
db = Dbfixture(host="127.0.0.1", name="addressbook", user="root", password="")

try:
    contacts = db.get_contact_list()
    for contact in contacts:
        print(contact)
    print(len(contacts))

finally:
    db.destroy()