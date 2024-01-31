while True:
    num_1 = input("Input num 1: ")
    operaciya = input("Input action: ")
    num_2 = input("Input num 2: ")

    if not num_1.isdigit() or operaciya not in ("+", "-", "/", "*") or not num_2.isdigit():
        print('Invalid input')
        continue

    num_1 = float(num_1)
    num_2 = float(num_2)
    result = 0

    if operaciya == "+":
        result = num_1 + num_2
    elif operaciya == "-":
        result = num_1 - num_2
    elif operaciya == "*":
        result = num_1 * num_2
    elif operaciya == "/":
        if num_2 != 0:
            result = num_1 / num_2
        else:
            print("You cannot divide by 0")

    print(f"Result:\n{result}")

    cont = input("Continue Y/N?")
    if cont.lower() != "y":
        print("Close Program")
        break