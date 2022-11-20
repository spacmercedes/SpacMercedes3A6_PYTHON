"""
Write a function that extracts the words from a given text as a parameter.
A word is defined as a sequence of alpha-numeric characters.
"""
import re
from typing import List


def ex1(input_text: str) -> List[str]:
  
    return re.findall(r"[a-zA-Z0-9]+", input_text) # gaseste toate caracterele si returneaza o lista cu cuvintele gasite

if __name__ == "__main__":
    print(ex1("text, ana, are mere"))