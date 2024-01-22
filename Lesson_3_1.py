number_1 = int(input("Введіть перше число: "))
number_2 = int(input("Введіть друге число: "))
operaciya = input("Введіть операцію (\"+\", \"-\", \"*\", \"/\"): ")
if operaciya == "+":
    print("Ваш результат:")
    print(number_1+number_2)
elif operaciya == "-":
    print("Ваш результат:")
    print(number_1 - number_2)
elif operaciya == "*":
    print("Ваш результат:")
    print(number_1 * number_2)
elif operaciya == "/":
    if number_2 != 0:
        print("Ваш результат:")
        print(number_1 / number_2)
    else:
        print("Ділити на 0 не можна. Введіть іншу цифру, або зменіть операцію")

