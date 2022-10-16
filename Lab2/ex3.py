def ex3(a, b):
    return (list(set(a) & set(b)), list(set(a) | set(b)), list(set(a) - set(b)), list(set(b) - set(a)))

if __name__ == '__main__':
    print(ex3("abc", "bcd"))