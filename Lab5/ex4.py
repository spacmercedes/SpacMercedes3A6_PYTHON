"""
Write a function that receives a variable number of arguments and keyword arguments.
 The function returns a list containing only the arguments which are dictionaries,
  containing minimum 2 keys and at least one string key with minimum 3 characters.
"""
def ex_4(*args, **kwargs) -> list:
   
    return [
               i for i in args
               if type(i) == dict and len(i) > 1 and max([0] + [len(x) for x in i.keys() if type(x) == str]) > 2 #verifica daca e dictionar , daca is macar 2 chei si daca cheia are 3 ch
           ] + [
               i for i in kwargs.values()
               if type(i) == dict and len(i) > 1 and max([0] + [len(x) for x in i.keys() if type(x) == str]) > 2
           ]

if __name__ == '__main__':
    print(ex_4(
    {1: 2, 3: 4, 5: 6},
    {'a': 5, 'b': 7, 'c': 'e'},
    {2: 3},
    [1, 2, 3],
    {'abc': 4, 'def': 5},
    3764,
    dictionar={'ab': 4, 'ac': 'abcde', 'fg': 'abc'},
    test={1: 1, 'test': True}
))

# "C:\\Users\\spacm\\Desktop\\PYTHON-Lab\\Lab4Python"