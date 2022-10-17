from typing import List


def ex6(*lists: List, x: int) -> List:
  
    united_lists = []
    for i in lists:
        united_lists += i
    return list(set([i for i in united_lists if united_lists.count(i) == x]))

if __name__ == '__main__':
    print(ex6([1, 2, 3], [1, 2, 3], [4, 4, 4], [5, 5, 5, 5], x=2))
