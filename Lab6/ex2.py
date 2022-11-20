"""
Write a function that receives as a parameter a regex string, a text string and a whole number x,
and returns those long-length x substrings that match the regular expression.

"""
import re
from typing import List

def ex2(regex: str, input_text: str, x: int) -> List[str]:
  
    return [i for i in re.findall(regex, input_text) if len(i) == x]



if __name__ == "__main__":
    print(ex2(r"\w+", "text, ana, are mere", 3))