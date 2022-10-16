"""Ex 9
Write a function that receives as paramer a matrix which represents the heights of the spectators in a stadium
and will return a list of tuples (line, column) each one representing a seat of a spectator which can't see the game.
A spectator can't see the game if there is at least one taller spectator standing in front of him. All the seats are occupied.
All the seats are at the same level.
Row and column indexing starts from 0, beginning with the closest row from the field.
"""

"""
Functia parcurge fiecare rand si coloana din matrice. Pentru fiecare celula
din rand, fucntia compara valoaraea acelei celule cu valoarea aceleaiasi celule
din randul anterior. Daca valoarea din radndul curent e mai mare
ca cea din radnul anterior, atunci adaduuga in rezultat

"""

def ex9(matrix):
    result = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            for k in range(i):
                if matrix[k][j] >= matrix[i][j]:
                    result.append((i, j))
                    break
    return result


if __name__ == "__main__":
    matrix =    [[1, 2, 3, 2, 1, 1],
                [2, 4, 4, 3, 7, 2],
                [5, 5, 2, 5, 6, 4],
                [6, 6, 7, 6, 7, 5]]

    print(ex9(matrix))