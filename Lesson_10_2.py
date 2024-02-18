# Ваша функція is_even повинна повертати True якщо число парне, і False якщо число непарне.
#
# Вхідні дані: Ціле число.
#
# Вихідні дані: Логічний тип.


def is_even(digit):
    """ Перевірка чи є парним число """
    return digit % 2 == 0

# is_even = lambda digit: digit % 2 == 0          # lambda

assert is_even(2) == True, 'Test1'
assert is_even(5) == False, 'Test2'
assert is_even(0) == True, 'Test3'
print('OK')
