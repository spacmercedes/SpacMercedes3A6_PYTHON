"""
Write a function with one parameter which represents a list.
The function will return a new list containing all the numbers found in the given list.
"""

import re

def ex_5(input_list: list) -> list:

    return re.findall(r"[0-9]+\.?[0-9]*", str(input_list)) #gaseste toate numere cu findall din input list transformat in string


if __name__ == '__main__':
    print(ex_5(
    [1, "2", {"3": "a"}, {4, 5}, 5, 6, 3.0]
))
