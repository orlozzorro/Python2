"""Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
На вход подается 2 числа через пробел: n m
n - кол-во элементов первого множества.
m - кол-во элементов второго множества.
Затем подаются элементы каждого множества через пробел в виде строки. ! Писать input() не надо

Пример

На входе:


var1 = '5 4' # количество элементов первого и второго множества
var2 = '1 3 5 7 9' # элементы первого множества через пробел
var3 = '2 3 4 5' # элементы второго множества через пробел
На выходе:


3 5
"""
# var1 = '4 4'
# var2 = '5 6 7 8' 
# var3 = '6 7 8 9'

# array1 = map(int, var2.split())
# array2 = map(int, var3.split())
# set1 = set()
# set2 = set()
# for item in array1:
#     set1.add(item)
# for item in array2:
#     set2.add(item)
# print(set1)
# print(set2)
# result = sorted(set1.intersection(set2))
# for item in result:
#     print(item, end = " ")


# mol = [int(x) for x in var1.split()]
# n = mol[0]
# m = mol[1]
# set_1 = set()
# set_2 = set()
# list_1 = list()
# a = [int(x) for x in var2.split()]
# k = set(a)
# for i in k:
#    set_1.add(i)
# b = [int(x) for x in var3.split()]
# k1 = set(b)
# for i in k1:
#    set_2.add(i)
# lok = set_1 & set_2
# kool = list(lok)
# kool.sort()
# for i in kool:
#    print(i, end=' ')

"""
В фермерском хозяйстве в Карелии выращивают чернику. Черника растет на круглой грядке, и кусты черники высажены по окружности грядки. Каждый куст черники имеет урожайность, которая соответствует количеству ягод на этом кусте.

Урожайность черничных кустов представлена в виде списка arr, где arr[i] - это урожайность (количество ягод) i-го куста.

В фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей. Каждый собирающий модуль может собрать ягоды с одного куста и с двух соседних кустов. Собирающий модуль находится перед определенным кустом, и он может выбирать, с какого куста начать сбор ягод.

Ваша задача - написать программу, которая определит максимальное число ягод, которое может собрать один собирающий модуль за один заход, находясь перед некоторым кустом грядки.

Входные данные:

На вход программе подается список arr, где arr[i] (1 ≤ arr[i] ≤ 1000) - урожайность i-го куста черники. Размер списка не превышает 1000 элементов.

Выходные данные:

Программа должна вывести одно целое число - максимальное количество ягод, которое может собрать собирающий модуль, находясь перед некоторым кустом грядки.
"""
#При отправке кода на Выполнение раскомментируйте строку ниже, чтобы задать значения аргументов и вызвать функцию

#При отправке решения на Проверку закомментируйте эту строку обратно - система автоматически подставит разные значения аргументов и вызовет функцию для проверки

#arr = [5, 8, 6, 4, 9, 2, 7, 3]

# Введите ваше решение ниже
arr = [5, 8, 6, 4, 9, 2, 7, 3]
# max = -1

# for item in range(len(arr)-1):
#     if item == 0:
#         sum = arr[item] + arr[item +1] + arr[len(arr)-1]
#         print(item)
#     elif item == len(arr):
#         sum = arr[item] + arr[item -1] + arr[0]
#         print(item)
#     elif item != 0 and item != len(arr) - 1:
#         sum = arr[item-1] + arr[item] + arr[item + 1]
#         print(item)

#     if sum > max:
#         max = sum
# print(max)
arr_count = list()
for i in range(len(arr) - 1):
    arr_count.append(arr[i - 1] + arr[i] + arr[i + 1])
    print(arr[i - 1] + arr[i] + arr[i + 1])
    print(i)
arr_count.append(arr[-2] + arr[-1] + arr[0])

print(arr[-2])