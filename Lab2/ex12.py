def ex1(n):

    q = []
    for i in range(n):
        if(i==0):
            q.append(0)
        if(i==1):
            q.append(1)
        else:
            q.append(q[i]+q[i-1])
    q.pop(0)
    return q
    
    


if __name__ == '__main__':
    print(ex1(6))