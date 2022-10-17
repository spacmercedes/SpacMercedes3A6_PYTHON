from typing import List
#diagonala principala
# def ex5(arr): 
#     n = len(arr)
#     for i in range(n):
#         for j in range(n):
#             if (i==j):
#                 arr[i][j] = 0
    
#     return arr

def ex5(matrix: List[List[int]]) -> List[List[int]]:
    return [[matrix[i][j] if i >= j 
            else 0 for i in range(len(matrix))]
            for j in range(len(matrix[0]))]

if __name__ == '__main__':
    
   matrix = [
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1]
]
print(ex5(matrix))
