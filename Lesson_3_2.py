list_1 = [1, 5, 7, 9, 10]

if len(list_1) > 0:
    new_list_1 = list_1.copy()
    new_list_1.insert(0, new_list_1.pop(-1))
    print("list_1: ", list_1)
    print("new_list_1: ", new_list_1)
else:
    print("list_1: ", list_1)
