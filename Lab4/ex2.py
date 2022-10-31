import os

# Să se scrie o funcție ce primește ca argumente două căi: director si fișier. 
# Implementati functia astfel încât în fișierul de la calea fișier să fie scrisă pe câte o linie,
# calea absolută a fiecărui fișier din interiorul directorului de la calea folder, ce incepe cu litera A. 

def ex2(director, fisier):
    try:
        with open(fisier,"w") as f: #deschide pentru scriere
            for el in os.listdir(director): #itereaza prin toate fisierele din diredctor
                name = os.path.join(director,el) #os.path pentru a gasi calea la fiecare fisierr din director
                if os.path.isfile(name) and el.startswith("A"): #va printa cate o linie din fiecare fisier care incepe cu A, daca exista
                    print(repr(os.path.abspath(name)+os.linesep)) #os.linesep pentru a face split la linii in cuvinte pentru a printa intr-o singura linie
                    f.write(os.path.abspath(name)+os.linesep) #scrie in fisier
        f.close()            
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    print(ex2(".", "b.b"))

