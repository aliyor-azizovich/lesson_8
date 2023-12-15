"""
Задача №33. Решение в группах
Хакер Василий получил доступ к классному журналу и
хочет заменить все свои минимальные оценки на
максимальные. Напишите программу, которая
заменяет оценки Василия, но наоборот: все
максимальные – на минимальные.
Input: 5 -> 1 3 3 3 4
Output: 1 3 3 3 1
"""

# решение 1 - через цикл с доп. массивом
lst = [4, 1, 3, 3, 3]
min_el = min(lst)
max_el = max(lst)
res = []
for el in lst:
    if el == max_el:
        res.append(min_el)
    else:
        res.append(el)
print(res)


# решение 2 - через рекурсию с доп. массивом
def recur(lst, res=[], min_el=min(lst), max_el=max(lst)):
    if len(lst) == 0:
        return res
    if lst[0] == max_el:
        res.append(min_el)
    else:
        res.append(lst[0])

    return recur(lst[1:])


print(recur(lst))


# решение 3 - через рекурсию без доп. массива
def replace_eval(lst, min_eva=min(lst), max_eva=max(lst)):
    if not lst:
        return []
    elif lst[0] == max_eva:
        lst[0] = min_eva
    return [lst[0]] + replace_eval(lst[1:])


print(replace_eval(lst))
