def ex4(note,poz,start):
    res=[] #listarta goala
    res.append(note[start]) #adauga elementul cu index start din listarta note in listarta res
    n = len(note) #lungimea listei cu note
    for i in range(len(poz)): 
        start+=poz[i] #lui start ii dam pozitia cu care sa inceapa
        if start >n-1:
            start-=n #scade lungimea listei de notw din var st
        elif start <0:
            start+=n
        res.append(note[start])
    return res

if __name__ == '__main__':
    print(ex4(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2))