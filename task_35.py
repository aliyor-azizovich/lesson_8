"""
Задача №35. Решение в группах
Напишите функцию, которая принимает одно число и
проверяет, является ли оно простым
Напоминание: Простое число - это число, которое
имеет 2 делителя: 1 и n(само число)
Input: 5
Output: yes
"""


# решение 1 - через цикл
def is_prime(some_num):
    checker = True

    for i in range(2, some_num):
        if some_num % i == 0:
            checker = False

    return checker


print(is_prime(9))


# решение 2 - через рекурсию
def is_prime(some_num, checker=True, i=2):
    if i < some_num:
        if some_num % i == 0:
            checker = False

        return is_prime(some_num, checker, i + 1)
    return checker


print(is_prime(8))
