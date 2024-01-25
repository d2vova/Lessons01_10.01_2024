list = [0, 3, 5, 0, 4, 6, 0, 9]
index = 0
for i in range(len(list)):
    if list[i] != 0:
        list[i], list[index] = list[index], list[i]
        index += 1
print(list)
