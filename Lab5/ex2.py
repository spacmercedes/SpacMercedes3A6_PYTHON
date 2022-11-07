#Create a function and an anonymous function that receive a variable
 #number of arguments. Both will return the sum of the values of the keyword arguments.


anonymous_function = lambda *args, **kwargs: sum(kwargs.values()) # creaaza o fucntie anonima care primeste o lista si dictionar si returneaza 
#suma pentru dicitonar


def my_function(*args, **kwargs): #primeste lista si dictionar si retruneaza suma pentru dictionar
    return sum(kwargs.values())

if __name__ == "__main__":
    result_1 = anonymous_function(1, 2, c=3, d=8, e=6)
    result_2 = my_function(1, 2, c=3, d=4)
    print(result_1, result_2)