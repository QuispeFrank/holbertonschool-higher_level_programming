#!/usr/bin/python3
"""Class MyInt"""


class MyInt(int):
    """Reverse"""

    def __eq__(self, other):
        return super().__ne__(other)

    def __ne__(self, other):
        return super().__eq__(other)
