"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = "SUBLIST"
SUPERLIST = "SUPERLIST"
EQUAL = "EQUAL"
UNEQUAL = "UNEQUAL"


def sublist(list_one, list_two):
    """
    Return the sublist category of the first list in relation to the second.

    :param list_one: list of integers
    :param list_two: list of integers
    :return: one of SUBLIST, SUPERLIST, EQUAL or UNEQUAL
    """
 
    if list_one == list_two:
        return EQUAL
    elif is_sublist(list_one, list_two):
        return SUPERLIST
    elif is_sublist(list_two, list_one):
        return SUBLIST
    else:
        return UNEQUAL


def is_sublist(list_one, list_two):
    """
    Return True if list_one is a sublist of list_two, False otherwise.

    :param list_one: list of integers
    :param list_two: list of integers
    :return: True if list_one is a sublist of list_two, False otherwise
    """
    
    for i in range(len(list_one) - len(list_two) + 1):
        if not list_two or list_two == list_one[i:i + len(list_two)]:
            return True
    return False

            
