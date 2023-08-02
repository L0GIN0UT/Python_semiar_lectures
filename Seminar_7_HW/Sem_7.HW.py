# Задача 34: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку
# разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам
# стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число
# гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного
# слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг
# от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе
# напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не
# в порядке
# Ввод: 
# пара-ра-рам рам-пам-папам па-ра-па-дам
# Вывод:
# Парам пам-пам

# Старая версия

def rhitm(sentence):
    dict = {'а': 0, 'у': 0, 'о': 0, 'ы': 0, 'и': 0, 'я': 0, 'э': 0, 'ю': 0, 'ё': 0, 'е': 0}
    count = 0
    for word in sentence:
        dict = dict.fromkeys(dict,0)
        for i in word:
            for key in dict:
                if i == key:
                    dict[i] += 1
        if sum(dict.values()) % 2 == 0:
            count += 1
    if count == len(sentence):
        print('Парам пам-пам')
    else:
        print('Пам парам')

# rhitm(input('Введите предложение -> ').split())

# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и
# столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
# которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте,
# почему не с нуля). Примечание: бинарной операцией называется любая операция, у которой
# ровно два аргумента, как, например, у операции умножения.
# Ввод: Вывод:
# print_operation_table(lambda x, y: x * y) 
#  1 2 3 4 5 6
#  2 4 6 8 10 12
#  3 6 9 12 15 18
#  4 8 12 16 20 24
#  5 10 15 20 25 30
#  6 12 18 24 30 36 

# Универсальный (ДЛИННЫЙ)
def operation_table(operation):
    if operation == '+':
        return lambda x, y: (x - 1) + (y - 1)
    if operation == '-':
        return lambda x, y: x - y
    if operation == '*':
        return lambda x, y: x * y
    if operation == '/':
        return lambda x, y: round(x / y,2)

def print_operation_table(operation, num_rows, num_columns):
    for i in range(1, num_rows + 1):
        for j in range(1, num_columns + 1):
            print(operation(i, j), end = ' ')
        print()

# print_operation_table(operation_table(str(input('Введите операцию (+,-,*,/) -> '))), num_rows = int(input('Введите кол-во строк -> ')), num_columns = int(input('Введите кол-во столбцов -> '))) 

# Конкретно ТЗ

# def print_operation_table(operation, num_rows, num_columns):
#     for i in range(1, num_rows + 1):
#         for j in range(1, num_columns + 1):
#             print(operation(i, j), end = ' ')
#         print()

# print_operation_table(lambda x, y: x * y, int(input('Введите кол-во строк -> ')), int(input('Введите кол-во столбцов -> ')))