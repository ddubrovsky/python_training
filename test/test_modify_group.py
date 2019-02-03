# -*- coding: utf-8 -*-
__autor__ = 'Dmitrii Dubrovskii'
from model.group import Group
import random


def test_add_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    group_mod = random.choice(old_groups)
    group = Group(name="New group2")
    app.group.modify_group_by_id(group_mod.id, group)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    for i in range(len(old_groups)):
        if old_groups[i].id == group_mod.id:
            old_groups[i] = group
    assert old_groups == new_groups
    if check_ui:
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

#def test_group_header(app):
#    if app.group.count() == 0:
#        app.group.create(Group(name="test"))
#    old_groups = app.group.get_group_list()
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)
#    app.group.modify_first_group(Group(header="New header"))
