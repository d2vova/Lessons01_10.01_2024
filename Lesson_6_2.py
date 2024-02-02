my_dict_1 = {"Key_1": 1, "key_2": 2, "key_3": 3}
my_dict_2 = {"key_2": 10, "key_3": 30, "d": 40}

common_keys = list(set(my_dict_1.keys()) & set(my_dict_2.keys()))
print("shared keys: ", common_keys)

unique_keys_first = [key for key in my_dict_1.keys() if key not in my_dict_2]
print("unique keys: ", unique_keys_first)

new_dict = {key: my_dict_1[key] for key in my_dict_1 if key not in my_dict_2}
print("new dict with unique:", new_dict)

merged_dict = {}

for key, value in my_dict_1.items():
    if key in my_dict_2:
        merged_dict[key] = [value, my_dict_2[key]]
    else:
        merged_dict[key] = value

for key, value in my_dict_2.items():
    if key not in my_dict_1:
        merged_dict[key] = value

print("merged dict: ", merged_dict)
