list_1 = []
if not list_1:
    list_1 = [0]
    print(list_1)
else:
    sum_list = sum(list_1[::2])
    result = sum_list * list_1[-1]
    print(result)