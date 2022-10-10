import math

def ex1():
    numar = int(input("Indicati numarul de numere: "))
    print("Introduceti numerele: ")
    arr = []

    for i in range(0, numar):
        aux = int(input())
        arr.append(aux)

    for i in range(0, numar - 1):
        arr[i + 1] = math.gcd(arr[i], arr[i + 1])

    return arr[numar - 1]

def ex2():
    str = input("Introdu stringul: ")
    contor = 0
    arr = ["a","e","i","o","u"]
    for i in range(len(str)):
        for j in range(len(arr)):
            if str[i] == arr[j]:
                contor+=1
    return contor

def ex3():
    str1 = input("Primul string: ")
    str2 = input("Al doilea string: ")
    return str2.count(str1)

def ex4():
    str = input("String pliz: ")
    sir = ""
    for i in range(len(str)):
        if ord(str[i]) > 64 and ord(str[i]) < 91:
            sir +="_" + chr(ord(str[i])+ 32)
        else:
            sir += str[i]
    return sir

def ex5():
    return "Not done"

def ex6():
    number=int(input("Introduceeti numarul: "))
    final = number
    reversed=0

    while number != 0:
        print("numarul "+str(number))
        aux = number % 10
        print("auxiliara "+str(aux))
        reversed *= 10
        print("reversed * 10 "+str(reversed))
        reversed += aux
        print("reversed + auxiliara "+str(reversed))
        number = number // 10
        print("Numarul modificat impartit la 10: "+str(number))

    if final == reversed:
        return "Palindrom"
    return "Nu e palindrom"

def ex7():
    str = input("Introdu String: ")
    numere = ""
    for i in range(len(str)):
        if ord(str[i]) > 47 and ord(str[i]) < 58:
            numere += chr(ord(str[i]))
    return numere

def ex8():
    number = int(input("Introdu numar"))
    numarBinar = str(bin(number))
    print(numarBinar)
    contor = 0
    for i in range(len(numarBinar)):
        if numarBinar[i] == "1":
            contor += 1
    return contor

def ex9():
    str = input("Sirul: ").lower()
    m=[]
    for i in range(26):
        m.append(0)
    for i in range(len(str)):
        m[abs(97-ord(str[i]))]+=1
    q=max(m)
    for i in range(26):
        if q==m[i]:
            res=i
    return chr(res+97)

def ex10():
    count = 1
    str = input("Stringul:")
    for i in range(len(str)):
        if str[i] == " ":
            count += 1
    return count

if __name__ == '__main__':
    # print(ex1())
    # print(ex2())
    # print(ex3())
    # print(ex4())
    # print(ex5())
    print(ex6())
    # print(ex7())
    # print(ex8())
    # print(ex9())
    # print(ex10())