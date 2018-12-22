# -*- coding: utf-8 -*-
__autor__ = 'Dmitrii Dubrovskii'
from model.group import Group


def test_add_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.modify_first_group(Group(name="New group"))

def test_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.modify_first_group(Group(header="New header"))