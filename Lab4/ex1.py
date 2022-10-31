
# Să se scrie o funcție ce primeste un singur parametru, director, 
# ce reprezintă calea către un director. 
# Funcția returnează o listă cu extensiile unice sortate crescator ---------
# (in ordine alfabetica) a fișierelor din directorul dat ca parametru.

import os

def ex1(dir): #directorul ca parametru
    ans = set() #creez un set 
    for root, directories, files in os.walk(dir): #parcurg directorul cu functia os.walk()
        for file in files: #itereaza prin fisiere
            file_name, file_extensions = os.path.splitext(file) #cu os.path, preluam denumirea si ii facem split in nume si extensie
            if file_extensions != '':
                ans.add(file_extensions) #adaug extensiile la ans pentru afisare
    return sorted(ans)

if __name__ == '__main__':
    print(ex1("C:\\Users\\spacm\\Desktop\\PYTHON-Lab"))

    