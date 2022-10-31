from typing import List
import os

# Să se scrie o funcție ce primește un parametru cu numele dir_path. 
# Acest parametru reprezintă calea către un director aflat pe disc. 
# Funcția va returna o listă cu toate căile absolute ale fișierelor aflate în rădăcina directorului dir_path.

def ex_8(dir_path: str) -> List[str]:
   
    try:
        if os.path.isfile(dir_path): #verifica daca e fisier si riidica o exceptie
            raise Exception("path is file, not dir")
            #daca gaseste un fisier retunreaza calea absoluta, itereaza prin fisiere din acele directorii, doar daca sunt fisisre
        return [os.path.abspath(f) for f in os.listdir(dir_path) if os.path.isfile(f)]
        #va returna o lista cu toate fisierele din director
    except Exception as e:
        print(e)

if __name__ == '__main__':
   print(ex_8("."))