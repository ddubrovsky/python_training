# -*- coding: utf-8 -*-
__autor__ = 'Dmitrii Dubrovskii'
from model.group import Group
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])
    #генератор случайных строк

testdata = [Group(name="", header="", footer="")] + [
    #+5 контактов со случайными значениями
    Group(name=random_string('name', 10), header=random_string('header', 20), footer=random_string('footer', 20))
    for i in range (5)
    # или 3 параметра пробегают по двум возможным значениям(пусто или случайное)
    #Group(name=name, header=header, footer=footer)
    #for name in ["", random_string('name', 10)]
    #for header in ["", random_string('header', 20)]
    #for footer in ["", random_string('footer', 20)]
]

@pytest.mark.parametrize('group', testdata, ids=[repr(x) for x in testdata])
def test_add_group(app, group):
    old_groups = app.group.get_group_list()
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
