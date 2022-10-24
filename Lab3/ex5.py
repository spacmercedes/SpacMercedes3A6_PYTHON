# The validate_dict function that receives as a parameter a set of tuples 
# ( that represents validation rules for a dictionary that has strings as keys and values)
#  and a dictionary. A rule is defined as follows: (key, "prefix", "middle", "suffix"). 
#  A value is considered valid if it starts with "prefix", "middle" is inside the value 
#  (not at the beginning or end) and ends with "suffix". 
#  The function will return True if the given dictionary matches all the rules, False otherwise.
from typing import Set

#ia un set de tuple si un dictionar
def ex5(tuple_set: Set[tuple], dictionary: dict) -> bool:

#face loop prin setul de tuple. Pentru fiecarre tupla din set, functia obtine valoarea asociata cu regula din dictionar
#pentru fiecrae tupla, extrage valoarea din dicctionar si verifica daca coincide cu regula specificata
    for rule in tuple_set:
        value = dictionary.get(rule[0])
        if value is None:
            return False
            #daca valoarea nu incepe cu prima litera din regula sau cu ultima litera din regula, return fals
            #altfel e adevarat
        if not value.startswith(rule[1]) \
                or not value.endswith(rule[3]) \
                or not rule[2] in value \
                or value.startswith(rule[2]) \
                or value.endswith(rule[2]):
            return False
    return True

if __name__ == '__main__':
   print(ex5(
    {("l", "", "1", " "), ("s", "d", "3", "d")},
    {'a': {'a': "3"}, 's': "d3d", '.': "1", 'k': "1", 'h': "1", 'l': " 1 ", 'p': "2", ' ': "2", 'A': "1", 'n': "1"}
))