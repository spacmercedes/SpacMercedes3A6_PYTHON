
# Compare two dictionaries without using the operator "==" returning True or False. 
# (Attention, dictionaries must be recursively covered because they can contain other containers, such as dictionaries, lists, sets, etc.)

from typing import List, Set, Tuple
from collections.abc import Iterable
def sunt_egale(d_1, d_2, depth ):
     if type(d_1) == type(d_2): #verifica daca sunt de acelasi tip
         if type(d_1) is dict:
            #daca sunt de acelasi ttip, verifica daca cheile in dictionare sunt la fel
            #daca nu sunt la fel, tine cont de diferente intr-o lista
             same = True
             differences = []
             #pentru fiecare cheie in primul dictionar, verifca daca cheia din al doilea dictionar e la fel
             for label_1, label_2 in zip(sorted(d_1.keys()), sorted(d_2.keys())):
                 if label_1 != label_2:
                     same = False
                     #daca cheia in al doilea dicitonar nu e la fel, adauga urmatoarea diferenta
                     differences.append((label_1, label_2, "depth = " + str(depth), "au chei diferite"))
                     continue
                    #daca sunt orice diferente intre chei in diciotnsre, returneaza fals
                 verify_equal = sunt_egale(d_1[label_1], d_2[label_1], depth + 1)
                 if not verify_equal[0]:
                     same = False
                     differences += verify_equal[1]
             else:
                 return same, differences
         if d_1 != d_2:
             return False, [(d_1, d_2, "depth = " + str(depth), "nu sunt egale")]
         else:
             return True, []
     else:
         return False, [(d_1, d_2, "depth = " + str(depth), "tipuri diferite")]

def ex3(d_1: dict, d_2: dict) -> list:
     return sunt_egale(d_1, d_2, 0)[1]

d_1 = {'a': {'b': 0}, 's': 4, '.': 1, 'e': 1, 'h': 1, 'l': 1, 'p': 2, ' ': 2, 'A': 1, 'n': 1}
d_2 = {'a': {'a': 3}, 's': 2, '.': 1, 'e': 1, 'h': 1, 'l': 1, 'p': 2, ' ': 2, 'A': 1, 'n': 1}

print(ex3(d_1, d_2))