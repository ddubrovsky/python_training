# -*- coding: utf-8 -*-
__autor__ = 'Dmitrii Dubrovskii'
from model.group import Group


def test_add_group(app):
    app.group.create(Group(name="bxbhxhhdf", header="hxdfhdhd", footer="dhxdfhfdfh"))


def test_add_empty_group(app):
   app.group.create(Group(name="", header="", footer=""))
