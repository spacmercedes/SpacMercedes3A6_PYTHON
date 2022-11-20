"""
Write a function that receives as a parameter the path to an xml document and an attrs dictionary and returns 
those elements that have as attributes all the keys in the dictionary and values ​​the corresponding values.
 For example, if attrs={"class": "url", "name": "url-form", "data-id": "item"} the items selected will be those tags
  whose attributes are class="url" si name="url-form" si data-id="item".
"""
import re
from typing import List

def ex_4(path_to_xml,attrs):

    result = []
    with open(path_to_xml,"r") as f_d:
        for el in re.findall("<\w+.*?>",f_d.read()):
            if(all([re.search(item[0]+"\s*=\s*\""+item[1] + "\"",el,flags=re.I) for item in attrs.items()])):
                result+=[el]
    return result


if __name__ == '__main__':
    print(ex_4("example.xml", {"class": "url", "name": "url-form", "data-id": "item"}))