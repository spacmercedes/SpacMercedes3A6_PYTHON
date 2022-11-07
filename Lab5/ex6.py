"""
Write a function that receives a list with integers as parameter 
that contains an equal number of even and odd numbers that are in no specific order.
 The function should return a list of pairs (tuples of 2 elements) of numbers (Xi, Yi) 
 such that Xi is the i-th even number in the list and Yi is the i-th odd number
"""

from typing import List

def ex_6(input_list: List[int]) -> List[tuple]:
 #face lista cu pare si imapre si face zip pentu a le cupla
    odd_numbers = [x for x in input_list if x % 2 == 0]
    even_numbers = [x for x in input_list if x % 2 == 1]
    return list(zip(odd_numbers, even_numbers))


if __name__ == '__main__':
    print(ex_6(
    [1, 3, 5, 2, 8, 7, 4, 10, 9, 2]
))
