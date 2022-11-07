"""
Using functions, anonymous functions, list comprehensions and filter, 
implement three methods to generate a list with all the vowels in a given string.
"""
import re
from typing import List

def ex_3_v_1(input_string: str) -> list: #inputul va fi str si imi returneaza o lista
    return [x for x in input_string if x in "aeiou"] 


def ex_3_v_2(input_string: str) -> list: #fct anonima
    return list(filter(lambda x: x in "aeiou", input_string))


def ex_3_v_3(input_string: str) -> list: #list comprehension
  
    filter_array = [True if x in "aeiou" else False for x in input_string] #face un array de True False
    return [i for (i, j) in zip(input_string, filter_array) if j] # returneaza doar tuplele care au true, adica vocale


def ex_3_v_4(input_string: str) -> list: #filter
  
    return re.findall('[aeiou]', input_string) # findall - gaseste toate aoiou din input string


if __name__ == '__main__':
    v_1 = ex_3_v_1("Programming in Python is fun")
    v_2 = ex_3_v_2("Programming in Python is fun")
    v_3 = ex_3_v_3("Programming in Python is fun")
    v_4 = ex_3_v_4("Programming in Python is fun")
    print(v_1, v_2, v_3, v_4, sep='\n')


