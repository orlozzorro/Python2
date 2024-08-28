# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам стоит написать программу.

# Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами.
# Фразы отделяются друг от друга пробелами.

# Стихотворение  Винни-Пух передаст вам автоматически в переменную stroka в виде строки. В ответе напишите Парам пам-пам, если с ритмом все в порядке и Пам парам, если с ритмом все не в порядке.
# Если фраза только одна, то ритм определить не получится и необходимо вывести: Количество фраз должно быть больше одной!.

# Пример

# На входе:


stroka = 'пара-ра-рам рам-пам-папам па-ра-па-дам'
# На выходе:
# def vowel_counter(phrases):
#     vowels = ['у', 'е', 'ы', 'а', 'э', 'я', 'и', 'ю']
#     list_counters = []
#     for item in phrases:
#         count = 0
#         for letter in item:
#             if letter.lower() in vowels:
#                 count +=1
#         list_counters.append(count)
#     return list_counters

# # Парам пам-пам
# phrase_list = stroka.split(' ')
# if (len(phrase_list) == 1):
#     print("Количество фраз должно быть больше одной!")
# list_of_counts = vowel_counter(phrase_list)
# my_flag = True
# for i in range(len(list_of_counts) - 1):
#     if list_of_counts[i] != list_of_counts[i + 1]:
#         my_flag = False
# if my_flag:
#     print('Парам пам-пам')
# else:
#     print('Пам парам')


# vowels = ['а', 'е', 'ё', 'и', 'й', 'о', 'у', 'ы', 'э', 'ю', 'я']
# phrases = stroka.split()
# if len(phrases) < 2:
#     print('Количество фраз должно быть больше одной!')
# else:
#     countVowels = []

#     for i in phrases:
#         countVowels.append(len([x for x in i if x.lower() in vowels]))

#     if countVowels.count(countVowels[0]) == len(countVowels):
#         print('Парам пам-пам')
#     else:
#         print('Пам парам')


# Напишите функцию print_operation_table(operation, num_rows, num_columns), которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца. По умолчанию номер столбца и строки = 9.
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны.
# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).
# Если строк меньше двух, выдайте текст
# ОШИБКА! Размерности таблицы должны быть больше 2!.
# Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.
# Между элементами должен быть 1 пробел, в конце строки пробел не нужен.
# Пример
# На входе:
# print_operation_table(lambda x, y: x * y, 3, 3)
# На выходе:


# 1 2 3
# 2 4 6 
# 3 6 9
# def print_operation_table(operation, numrows, numcolumns):
#     if numrows < 2:
#         print('ОШИБКА! Размерности таблицы должны быть больше 2!')
#     else:
#         for row in range(1, numrows + 1):
#             my_list =[]
#             for column in range(1, numcolumns + 1):
#                 my_list.append(operation(row,column))
#             print(*my_list)
# print_operation_table(lambda x, y: x * y, 9, 9)

def print_operation_table(operation, num_rows=9, num_columns=9):
    result = []
    if num_rows < 2 or num_columns < 2:
        print('ОШИБКА! Размерности таблицы должны быть больше 2!')
    else:
        for i in range(1, num_rows + 1):
            for j in range(1, num_columns + 1):
                if j != num_columns :
                    result.append(f'{operation(i, j)} ')
                else:
                    result.append(operation(i, j))
            result.append('\n')
        print(''.join([str(i) for i in result[:len(result) - 1]]))
