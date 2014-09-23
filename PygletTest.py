# -*- coding: utf-8 -*-
__author__ = 'eeneku'

people = {"paavo": {"allowed": True}, "pentti": {"allowed": False}}

for name in people:
    if people[name]["allowed"]:
        print (name + " is allowed")
    else:
        print (name + " is not allowed")


def print_this(arg=False):
    print (arg)

print_this()
print_this(True)
print_this(False)
print_this("moi!")
print_this(1+34+12)