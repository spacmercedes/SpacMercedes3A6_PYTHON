import os

# Să se scrie o funcție care are același comportament ca funcția de la exercițiul anterior, 
# cu diferența că primește un parametru în plus: o funcție callback, care primește un parametru,
# iar pentru fiecare eroare apărută în procesarea fișierelor, se va apela funcția respectivă cu instanța excepției ca parametru.

def callback(exception): #adaugam exceptia
    print(exception)


def ex6(target, to_search, callback): #la fel ca ex5.py
    ans = []
    try:
        if os.path.isfile(target):
            data = open(target, 'r').read()
            if to_search in data:
                return [os.path.abspath(target)]

        elif os.path.isdir(target):
            for root, directories, files in os.walk(target):
                for file in files:
                    if to_search in open(os.path.join(root, file), 'r').read():
                        ans.append(os.path.abspath(os.path.join(root, file)))
            data.close()            
            return ans

    except Exception as e:
        callback(e)


if __name__ == '__main__':
    print(ex6("C:\\Users\\spacm\\Desktop\\PYTHON-Lab\\Lab4Python\\ex8.py", "os", callback))