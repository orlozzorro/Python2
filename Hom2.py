"""Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
решкой, а некоторые – гербом. Определите минимальное число
монеток, которые нужно перевернуть, чтобы все монетки были
повернуты вверх одной и той же стороной. Выведите минимальное
количество монет, которые нужно перевернуть"""

# coins = [0, 1, 0, 1, 1, 0]
# orel = 0
# reshka = 0
# for i in range(len(coins)):
#     if coins[i] == 1:
#         orel += 1
#     else:
#         reshka += 1
# if orel < reshka:
#     print(orel)
# else:
#     print(reshka)


# count_zero = 0
# count_one = 0

# for coin in coins:
#     if coin == 0:
#         count_zero += 1
#     else:
#         count_one += 1

# if count_one > count_zero:
#     print(count_zero)
# else:
#     print(count_one)


""""Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя –
школьница. Петя помогает Кате по математике. Он задумывает два
натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
этого Петя делает две подсказки. Он называет сумму этих чисел S и их
произведение P. Помогите Кате отгадать задуманные Петей числа.
"""

# s = 12
# p = 27
# str = ""
# for i in range(s // 2 + 1):
#     x = i
#     y = s - x
#     if x * y == p:
#         str = str + f"{x} {y} "
# print(str)

# solutions = []
# for i in range(1, 1001):
#     for j in range(1, 1001):
#         if s == i + j and p == i * j:
#             solutions.append((min(i, j), max(i, j)))
# solutions = list(set(solutions))

# for solution in solutions:
#     print(solution[0], solution[1])




"""Требуется вывести все целые степени двойки (т.е. числа
вида 2k
), не превосходящие числа N.
"""

n=15
sum = 0
i = -1
while sum < n:
    i += 1
    sum = 2 ** i
    if sum <= n:
        print(sum)