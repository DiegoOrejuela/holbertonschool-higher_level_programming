#!/usr/bin/python3
"""Module 1-my_list.py | Test-driven development Package
What you should learn from this project:
- What is a superclass, baseclass or parentclass
- What is a subclass"""


class MyList(list):
    """MyList.
    Inheritance: list
    Methods owner: print_sorted"""

    def print_sorted(self):
        """print_sorted - sorted object MyList of int.
        Arguments: Nothing.
        Return: Nothing."""
        cp_my_list = self.copy()
        cp_my_list.sort()
        print(cp_my_list)
