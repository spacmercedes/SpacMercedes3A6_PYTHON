def ex10(*args):
    return list(zip(*args))


if __name__ == '__main__':
    print(ex10([1,2,3], [5,6,7], ["a", "b", "c"]))