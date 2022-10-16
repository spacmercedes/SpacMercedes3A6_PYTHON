"""Ex 11
Write a function that will order a list of string tuples based on the 3rd character of the 2nd element in the tuple.
Example: ('abc', 'bcd'), ('abc', 'zza')] ==> [('abc', 'zza'), ('abc', 'bcd')]
"""

def ex11(strings):
    return sorted(strings, key=lambda x: x[1][2])

if __name__ == "__main__":
    print(ex11([('abc', 'bcd'), ('abc', 'zza')]))

#function then sorts the strings alphabetically based on the first letter of each string