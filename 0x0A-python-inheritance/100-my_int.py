#!/usr/bin/python3
""" My int module """


class MyInt(int):
    """ class MyInt """

    def eq(self, other):
        return super().ne(other)

    def ne(self, other):
        return super().eq(other)
