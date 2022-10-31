# Să se scrie o funcție ce primește ca parametru un string my_path.
# Dacă parametrul reprezintă calea către un fișier, se vor returna ultimele 20 
# de caractere din conținutul fișierului. Dacă parametrul reprezintă calea către un director,
#  se va returna o listă de tuple (extensie, count), sortată descrescător după count, 
#  unde extensie reprezintă extensie de fișier, iar count - numărul de fișiere cu acea extensie. 
#  Lista se obține din toate fișierele (recursiv) din directorul dat ca parametru. 

import os


def ex3(my_path):
    extensions = [] #lista
    ans = []
    if os.path.isdir(my_path):
        for root, directories, files in os.walk(my_path): #itereaza prin fiecare director din calea specificata
            for file in files: #pentru fiecare director, creeaaa o alta lsita directories care contine toate fisierele din acel director
                file_name, file_extension = os.path.splitext(file) #itereaza prin fisiere si face split intre nume-fisier si extensie
                if file_extension != '':
                    extensions.append(file_extension)
        unique_extensions = set(extensions) #ia extensiile o singura data
        for ext in unique_extensions: #pentru fiecare extensie , ii atribuie valoarea lui ans pentru a fi sortate 
            ans.append((ext, extensions.count(ext)))
        return ans

    elif os.path.isfile(my_path):
        fd = open(my_path, 'r').read() #deschide pentru citire
        for i in range(len(fd) - 20, len(fd)):
            ans.append(fd[i])
            # fd.close()   
        return ans
         


if __name__ == '__main__':
    print(ex3("C:\\Users\\spacm\\Desktop\\PYTHON-Lab\\Lab4Python\\ex6.py"))

