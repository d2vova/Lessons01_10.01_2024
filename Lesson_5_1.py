# _ => True
# x => True
# get_value => True
# get value => False
# get!value => False
# some_super_puper_value => True
# Get_value => False
# get_Value => False
# getValue => False
# 3m => False
# m3 => True

def valid(my_str_1):                                 # тут також?
    result = False
    if my_str_1.isidentifier():
        if my_str_1 == "_" or my_str_1.islower():
            result = True
    return result
my_str_1 = input("Input variable name: ")            # а чого воно тут лається, не розумію.
print(valid(my_str_1))
