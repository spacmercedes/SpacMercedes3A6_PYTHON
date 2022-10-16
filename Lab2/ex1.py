def ex1(n):

    q = [] #lista goala
    for i in range(n):
        if(i==0):
            q.append(0)
        if(i==1):
            q.append(1)
        else:
            q.append(q[i]+q[i-1]) #suma nr curent si a celui anterior
    q.pop(0) #elimina primul numar din lsita
    return q
    
    


if __name__ == '__main__':
    print(ex1(6))