import numpy as np

def ex7(list):
    q=[]
    palindroame=[]
    n =len(list)
    for i in range(n):
        q.append(int(str(list[i])[::-1])) #adauga inversul listei la sf listei q
        if list[i]==q[i]:
            palindroame.append(list[i])
    return len(palindroame), np.max(palindroame)
    
    


if __name__ == '__main__':
    print(ex7([121,24,999,34]))