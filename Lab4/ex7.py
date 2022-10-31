import os

# Să se scrie o funcție care primește ca parametru un șir de caractere care reprezintă calea
# către un fișer si returnează un dicționar cu următoarele cămpuri: full_path = calea absoluta catre fisier, 
# file_size = dimensiunea fisierului in octeti, file_extension = extensia fisierului (daca are) sau "",
# can_read, can_write = True/False daca se poate citi din/scrie in fisier.

def ex_7(file_path: str) -> dict: #va retruna un dcitonar
   
    try:
        if os.path.isdir(file_path): #verifica daca calea e un director
            raise Exception("path is dir") #ridica o exceptie
        return {
            "full_path": os.path.abspath(file_path), #calea absoluta
            "file_size": os.path.getsize(file_path), #marimea in bytes
            "file_extension": os.path.splitext(file_path)[-1][1:], #preia extensia
            "can_read": os.access(file_path, os.R_OK), #verifica daca poate fi citit
            "can_write": os.access(file_path, os.W_OK), #verifica daca poate fi scris
        }
    except Exception as e:
        print(e)


if __name__ == '__main__':
    print(ex_7("Desktop\PYTHON-Lab\Lab4Python\ex7.py"))
