""""
Write a function called process that receives a variable number of keyword arguments

The function generates the first 1000 numbers of the Fibonacci sequence and then processes them in the following way:

If the function receives a parameter called filters, this will be a list of predicates (function receiving an argument and returning True/False) 
and will retain from the generated numbers only those for which the predicates are True. 

If the function receives a parameter called limit, it will return only that amount of numbers from the sequence. 

If the function receives a parameter called offset, it will skip that number of entries from the beginning of the result list. 

The function will return the processed numbers.
"""

def generate_fibonacci(n: int) -> list:
   
    return_list = [0, 1]
    if n < 0:
        raise ValueError("generating first n fibonacci numbers failed, n is negative")
    else:
        for i in range(2, n):
            return_list.append(return_list[i - 2] + return_list[i - 1])
    return return_list[0:n]


def sum_digits(x):
    return sum(map(int, str(x)))


def process(**kwargs):

    fibonacci_sequence = generate_fibonacci(1000)
    try:
        if "filters" in kwargs.keys():
            for f in kwargs["filters"]:
                fibonacci_sequence = list(filter(f, fibonacci_sequence))
        if "offset" in kwargs.keys():
            fibonacci_sequence = fibonacci_sequence[kwargs["offset"]:]
        if "limit" in kwargs.keys():
            fibonacci_sequence = fibonacci_sequence[:kwargs["limit"]]
    except Exception as e:
        print("Error at processing:", e)
    return fibonacci_sequence


if __name__ == '__main__':
    print(
    process(
        filters=[lambda item: item % 2 == 0, lambda item: item == 2 or 4 <= sum_digits(item) <= 20],
        limit=2,
        offset=2
    )
)