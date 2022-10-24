
def ex7(*args):
    result = {}
    #itereaza prin fiecare argument, si creeaza o noua pereche cheie/valoare in dictionarul rezultat
    #cheia fiind reprezentarea in string a primului argument si valoarea e reprez in str a celuui de al doilea arg
    for i in range(len(args)):
        for j in range(i+1, len(args)):
            result[str(args[i]) + " | " + str(args[j])] = args[i] | args[j]
            result[str(args[i]) + " & " + str(args[j])] = args[i] & args[j]
            result[str(args[i]) + " - " + str(args[j])] = args[i] - args[j]
            result[str(args[j]) + " - " + str(args[i])] = args[j] - args[i]
    return result

if __name__ == '__main__':
    print(ex7({1, 2}, {2, 3}))
