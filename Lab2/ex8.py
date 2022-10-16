def ex8(x=1, l=[], flag=True): #numarul x, lista l
    return [list(filter(lambda c: (ord(c) % x == 0) == flag, s)) for s in l]
#returneaza o lista de liste. fiecare in lista returnata contine toate elementele din l
#care au valoare la indexul specificat de x, adica nr par in ascii

if __name__ == '__main__':
    print(ex8(2, ["test", "hello", "lab002"],False))