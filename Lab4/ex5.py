import os

#  Să se scrie o funcție care primește ca argumente două șiruri de caractere, target și to_search și
#  returneaza o listă de fișiere care conțin to_search. Fișierele se vor căuta astfel: dacă target este un fișier, 
#  se caută doar in fișierul respectiv iar dacă este un director se va căuta recursiv in toate fișierele din acel director. 
#  Dacă target nu este nici fișier, nici director, se va arunca o excepție de tipul ValueError cu un mesaj corespunzator.

#cauta "os" in fisiere

def ex5(target, to_search):
    ans = [] 
    try:
        if os.path.isfile(target): #cauta fisier care sa contina target in oath
            data = open(target, 'r').read() #deschide pentru citire -> citeste
            if to_search in data:
                return [os.path.abspath(target)] #returneaza calea fisierului care contin target-ul cautat

        elif os.path.isdir(target): #daca e intr-n director cu fisiere
            for root, directories, files in os.walk(target):
                for file in files: # itereaza prin fisiere pentru a gasit targetul in continut
                    if to_search in open(os.path.join(root, file), 'r').read(): #deschide pentru citire 
                        ans.append(os.path.abspath(os.path.join(root, file))) #pastreaaza caile la fisierele care contin target - ul 
            return ans
        else:
            data.close()
            raise
          
    except Exception as e: #daca nu e nici fisier nici director
        print("This is not a file/directory\n")
        print(e)


if __name__ == '__main__':
    print(ex5("C:\\Users\\spacm\\Desktop\\PYTHON-Lab\\Lab4Python", "os"))