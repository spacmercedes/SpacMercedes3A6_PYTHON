# def ex6(*lists, count):

#     all_lists = []
#     return_list = []
#     for lst in lists:
#         all_lists+=lst
#     for item in all_lists:
#         if all_lists.count(item) == count and item not in return_list:
#             return_list.append(item)

#     return return_list


# if __name__ == '__main__':
#     print([1,2,3], [2,3,4],[4,5,6], 3)

def elements(x, *lists):
    newList = []
    for l in lists:
        newList += l
    return [e for e in set(newList) if newList.count(e) == x]


if __name__ == '__main__':
    print(elements(2, [1, 2, 3], [2, 3, 4], [4, 5, 6], [4, 1, "test"]))