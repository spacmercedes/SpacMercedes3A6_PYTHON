"""
Write a function that, for a text given as a parameter, censures words that begin and end with vowels.
Censorship means replacing characters from odd positions with *.
"""

from typing import List
import re


def cenzurare(s):
    low_s = s.group(0).lower()
    if not (low_s[0] in "aeiou" and low_s[-1] in "aeiou"):
        return s.group(0)
    return "".join([ch if idx%2 == 0 else '*' for idx,ch in enumerate(s.group(0))])


def ex_6(text):
    return re.sub("\w+",cenzurare,text)


if __name__ == '__main__':
   print(ex_6("ana are mere rosii")) 