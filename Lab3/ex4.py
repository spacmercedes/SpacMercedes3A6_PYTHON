# The build_xml_element function receives the following parameters: tag, content, and key-value elements given
#  as name-parameters. Build and return a string that represents the corresponding XML element.
#   Example: build_xml_element ("a", "Hello there", href =" http://python.org ", _class =" my-link ", id= " someid ") 
#   returns  the string = "<a href=\"http://python.org \ "_class = \" my-link \ "id = \" someid \ "> Hello there </a>"

def ex4(tag, content, **elements):
    result = f'<{tag}' #resultatul va fi de tip string formatat ca un tag

    for elem in elements.items(): #itereaza ptin itemii din dictionarul "elements" si seteaza variabila elem cu valoarea fiecarui item
        result += f' {elem[0]} = "{elem[1]}"' #adauga o linie noua si adauga valoarea elementului elem[0] la result, urmata de valoarea lui elem[1]

    result += f'> {content} </a>' #adauga valoarea lui content la result, + link
    return result



if __name__ == "__main__":
    print(ex4("a", "Hello there", href ="http://python.org", _class ="my-link", id= "someid"))
