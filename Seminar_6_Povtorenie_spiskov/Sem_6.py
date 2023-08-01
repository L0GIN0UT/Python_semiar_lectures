# Задача №39. Решение в группах
# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива
# Ввод: 
# 7
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1 
# Вывод:
# 3 3 2 12
#(каждое число вводится с новой строки)

# n = int(input('Введите кол-во элементов первого множества -> '))
# arr_frst = [input('Введите элемент 1 списка -> ') for i in range(0,n)]
# m = int(input('Введите кол-во элементов второго множества -> '))
# arr_scnd = [input('Введите элемент 2 списка -> ') for j in range(0,m)]
# res = [i for i in arr_frst if i not in arr_scnd]
# print(res)

def make_list(n) -> list[int]:
    result = []
    for i in range(n):
        result.append(int(input(f"введите {i + 1}-й элемент ")))
    return result

def exercise_39():
   """Задача №39
   Даны два массива чисел. Требуется вывести те элементы
   первого массива (в том порядке, в каком они идут в первом
   массиве), которых нет во втором массиве. Пользователь вводит
   число N - количество элементов в первом массиве, затем N
   чисел - элементы массива. Затем число M - количество
   элементов во втором массиве. Затем элементы второго массива
   Ввод:
   7
   3 1 3 4 2 4 12
   6
   4 15 43 1 15 1 (каждое число вводится с новой строки)
   Вывод:
   3 3 2 12"""
   n = int(input("Введите размер первого массива "))
   list1 = make_list(n)
   m = int(input("Введите размер второго массива "))
   list2 = make_list(m)
   for i in list1:
       if i not in list2:
           print(i, end=" ")

def task039():
    m = int(input("Введите длину списка m: "))
    n = int(input("Введите длину списка n: "))
    list_m = list_creator(m)
    list_n =list_creator(n)
    res_list = set_from_list(list_m, list_n)
    print(*res_list)

def list_creator(x):
    my_list = []
    for i in range(0, x):
        my_list.append(int(input(f"Введите элемент списка из {x} элементов: ")))
    return my_list

def set_from_list(list_m, list_n):
    my_list = [list_m[i] for i in range(len(list_m)) if list_m[i] not in list_n]
    return my_list

# task039()

# Задача №41. Решение в группах
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при
# этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив
# состоит из целых чисел.
# Ввод: 5
# 1 2 3 4 5       
# Вывод: 0
# Ввод: 5 
#  1 5 1 5 1
# Вывод: 2
# (каждое число вводится с новой строки)

# 1 вариант
# while True:
#     n = int(input('Введите кол-во элементов множества -> '))
#     if n > 0:
#         break

# while True:
#     arr = input('Введите элементы массива через пробел -> ').split()
#     if len(arr) == n:
#         break

# counter = 0
# for i in range(2, len(arr)):
#     if arr[i - 2] < arr[i - 1] and arr[i] < arr[i - 1]:
#         counter += 1

# print(counter)

# Вариант 2
# n = int(input('Введите кол-во элементов множества -> '))
# arr = [input('Введите элемент массива -> ') for i in range(0, n)]
# res = [1 for i in range(0,len(arr)) if arr[i - 2] < arr[i - 1] and arr[i] < arr[i - 1]]
# print(sum(res))

# Задача №43. Решение в группах
# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных
# строках.
# Ввод:           Вывод:
# 1 2 3 2 3       2

# 1 варианат
# string = input('Введите элементы списка через пробел -> ').split()
# dict = {}
# for i in string:
#     if i in dict:
#         dict[i] += 1  
#     else:
#         dict[i] = 1

# counter = 0
# for key, value in dict.items():
#     counter += (value//2)
# print(f'Код нашел - {counter} пар в вашем списке!')
#4-6 3-3 5-
# 2 вариант
# n = int(input('Введите кол-во элементов множества -> '))
# string = [int(input('Введите кэлемент множества -> ')) for i in range(0,n)]  # 1 1 2 1 2 -- 4
# counter = [1 for i in range(0,len(string)) for j in range(i+1,len(string)) if string[i] == string[j]]
# print(sum(counter))


# 3 вариант
# string = input('Введите элементы списка через пробел -> ').split()
# dict = {}
# for i in string:
#     if i in dict:
#         dict[i] += 1  
#     else:
#         dict[i] = 1

# counter = 0
# for key, val in dict.items():
#     counter += ((val)*(val-1))//2  
# print(counter)

# Задача №45. Решение в группах
# Два различных натуральных числа n и m называются
# дружественными, если сумма делителей числа n
# (включая 1, но исключая само n) равна числу m и
# наоборот. Например, 220 и 284 – дружественные числа.    220 - 1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110 = 284
# По данному числу k выведите все пары дружественных      284 - 1, 2, 4, 71, 142 = 220
# чисел, каждое из которых не превосходит k. Программа
# получает на вход одно натуральное число k, не
# превосходящее 105
# . Программа должна вывести все
# пары дружественных чисел, каждое из которых не
# превосходит k. Пары необходимо выводить по одной в
# строке, разделяя пробелами. Каждая пара должна быть
# выведена только один раз (перестановка чисел новую
# пару не дает).
# Ввод: Вывод:
# 300 220 284

# while True:
#     k = int(input('Введите K -> '))
#     if k > 0 and k < 100000:
#         break


# def sumdivider(n):      # 220 - 2, 4, 5, 10, 11, 20, 22, 44, 55, 110
#     sum = 1
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             sum += i + n//i
#     return sum
# # print(sumdivider(k))

# for i in range(1,k):
#     j = sumdivider(i)
#     if i == sumdivider(j) and i < j < k:
#         print(f'Пара дружественных чисел {i, j} в пределе {k}')

# Пара дружественных чисел (220, 284) в пределе 99999
# Пара дружественных чисел (1184, 1210) в пределе 99999
# Пара дружественных чисел (2620, 2924) в пределе 99999
# Пара дружественных чисел (5020, 5564) в пределе 99999
# Пара дружественных чисел (6232, 6368) в пределе 99999
# Пара дружественных чисел (10744, 10856) в пределе 99999
# Пара дружественных чисел (12285, 14595) в пределе 99999
# Пара дружественных чисел (17296, 18416) в пределе 99999
# Пара дружественных чисел (63020, 76084) в пределе 99999
# Пара дружественных чисел (66928, 66992) в пределе 99999
# Пара дружественных чисел (67095, 71145) в пределе 99999
# Пара дружественных чисел (69615, 87633) в пределе 99999
# Пара дружественных чисел (79750, 88730) в пределе 99999
# КОД РАБОТАЛ ОКОЛО 3 - 5 МИНУТ!!!

