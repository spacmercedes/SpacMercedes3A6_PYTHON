from typing import List


def ex6(*lists: List, x: int) -> List:
  
    q = [] #lista goala
    for i in lists:
        q += i 
    return list(set([i for i in q if q.count(i) == x]))

#returneaza o lista formata prin a lua toti itemii din q care sunt cu countul specificat de x
if __name__ == '__main__':
    print(ex6([1, 2, 3], [1, 2, 3], [4, 4, 4], [5, 5, 5, 5], x=2))
