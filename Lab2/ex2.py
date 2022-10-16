def ex2(arr):
    prime = [] #lista in care voi pastra numerele prime
    q = 0
    thereIsTwo=0
    for i in range(len(arr)): #parcurge numerele din lista
        if arr[i]==2:
            thereIsTwo+=1
        n = arr[i]
        for k in range(1,n): #verifica daca e prim si il pune in lista
            if n%k==0:
                q+=1
        if q == 1:
            prime.append(n)
        q = 0
        
    if thereIsTwo == 1:
        prime.remove(2)
    return prime
    
if __name__ == '__main__':
    print(ex2([3,5,7,9,12]))
