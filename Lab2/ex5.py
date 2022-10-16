def ex5(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n):
            if (i==j):
                arr[i][j] = 0
    
    return arr


  

if __name__ == '__main__':
    
    matrix = ([1,1,1,1,1],
          [1,1,1,1,1],
          [1,1,1,1,1],
          [1,1,1,1,1],
          [1,1,1,1,1]) 

    print(ex5(matrix))