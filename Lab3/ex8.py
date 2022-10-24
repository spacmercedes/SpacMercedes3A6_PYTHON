#  Write a function that receives a single dict parameter named mapping. 
#  This dictionary always contains a string key "start". Starting with the value 
#  of this key you must obtain a list of objects by iterating over mapping in the following way: 
#  the value of the current key is the key for the next value, until you find a loop (a key that was visited before).
#   The function must return the list of objects obtained as previously described.

def ex8(mapping: dict) -> set:
   #dicctionar mapping si o lista goala visited
    visited = []
    current = 'start'
    values = set()
    #loop prin dictionar, adaugand fiecare caracter la visited daca nu a fost vizitat
    #apoi adauga integerul corespunx=zataor la setul "values"

    #verifica daca current a ajuns la sfarsitul dictioanrului , daca da , se opreste
    #daca nu, current eeste pasat la urmatoarea variabila si incepe din nou
    while True:
        if current in visited:
            return values
        visited.append(current)
        current = mapping[current]
        values.add(current)


if __name__ == '__main__':
   print(ex8({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}))
