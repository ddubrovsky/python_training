#import mysql.connector
from fixture.orm import ORMFixture
from model.group import Group

#connection = mysql.connector.connect(host="127.0.0.1", database="addressbook", user="root", password="")
db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

try:
    l = db.get_contacts_in_group(Group(id="84"))
    for item in l:
        print(item)
    print(len(l))

finally:
    pass #db.destroy()