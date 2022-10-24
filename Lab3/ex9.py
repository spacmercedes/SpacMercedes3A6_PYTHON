# Write a function that receives a variable number of positional 
# arguments and a variable number of keyword arguments adn will return the number
#  of positional arguments whose values can be found among keyword arguments values.

#returneaza de cate ori argumentul p apare in lista de pozitii
#daca pozitia e in lista de argumente, count se increment
def ex9(*positions, **arguments) -> int:
  
    count = 0
    for p in positions: #loop prin fievcare pozitie
        if p in arguments.values(): 
            count += 1
    return count

if __name__ == '__main__':
    print(ex9(1, 2, 3, 4, x=1, y=2, z=3, w=5))