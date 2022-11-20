"""
Write a function that recursively scrolls a directory and displays those files whose name matches a regular expression 
given as a parameter or contains a string that matches the same expression. Files that satisfy both conditions will be prefixed with ">>"
"""
from typing import List
import re
import os
def ex_8(path: str, regex: str) -> List[str]:
   
    match_list = []
    try:
        for root, d, f in os.walk(path):
            for i in f:
                file_path = os.path.join(root, i)
                bool_1 = re.match(regex, file_path)
                bool_2 = re.match(regex, open(file_path, "r").read())
                if bool_1 and bool_2:
                    match_list.append(">>" + file_path)
                elif bool_1 or bool_2:
                    match_list.append(file_path)
    except Exception as e:
        SystemError(e)
    return match_list

if __name__ == '__main__':
  
    print(ex_8(".", ".*example.*"))