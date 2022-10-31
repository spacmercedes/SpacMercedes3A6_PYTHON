import os

# Să se scrie o funcție ce returnează o listă cu extensiile unice a fișierelor 
# din directorul dat ca argument la linia de comandă (nerecursiv). 
# Lista trebuie să fie sortată crescător.

def ex4(path):
    ans = set()
    for root, directories, files in os.walk(path): #itereaza prin toate directoarele din cale
        for file in files: #itereaza prin fisiere din director
            file_name, file_extension = os.path.splitext(file) #split nume fisier si extensie
            if file_extension != '':
                ans.add(file_extension) #starnge extensiile 
        break

    return sorted(ans)


if __name__ == '__main__':
    cale = input("Enter the path: ")
    print(ex4(cale))

# "C:\\Users\\spacm\\Desktop\\PYTHON-Lab\\Lab4Python"