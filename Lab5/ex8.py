# Decorator - permit sa impachetam o fucntie cu scopul de a extinde comportamentul functiei impachetate
# E o functie care care ia alta functie si ii extinde comportamentul fara a ii modifica comportamentul
# face wrapping la un obiect
# totul e un obiect, functia e un obiect, de asta o putem da ca parametru

def multiply_by_two(x):
    return x * 2


def add_numbers(a, b):
    return a + b


def print_arguments(function):
    def f(*args,**kwargs):
        print(args,kwargs)
        return function(*args, **kwargs)
    return f

augmented_multiply_by_two = print_arguments(multiply_by_two)
x = augmented_multiply_by_two(10)
print(x)
augmented_add_numbers = print_arguments(add_numbers)
x = augmented_add_numbers(3, 4)
print(x)
#b


def multiply_output(function):
    def f(*args,**kwargs):
        return 2*function(*args,**kwargs)
    return f


def multiply_by_three(x):
    return x * 3


augmented_multiply_by_three = multiply_output(multiply_by_three)
x = augmented_multiply_by_three(10)  # this will return 2 * (10 * 3)
print(x)
#c


def augment_function(function,decorators):
    def f(*args,**kwargs):
        result = function
        for deco in decorators:
            result = deco(result)
        return result(*args, **kwargs)
    return f


decorated_function = augment_function(add_numbers, [print_arguments, multiply_output])
x=decorated_function(3,4)
print(x)

# if __name__ == '__main__':
  
    # def sum_digits(x):
    #     return sum(map(int, str(x)))

  