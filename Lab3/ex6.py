# Write a function that receives as a parameter a list and returns a tuple 
# (a, b), representing the number of unique elements in the list, and b representing the number of 
# duplicate elements in the list (use sets to achieve this objective).


#calculeaza lungimea listei primita ca parametru si diferenta dintre lungimea listei
#si lungimea setuluide itemi unici in lista
def ex6(l):
    s = set(l)
    return (len(s), len(l) - len(s))


if __name__ == "__main__":
    l = ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'b', 'c', 'd', 'e']
    print(ex6(l))