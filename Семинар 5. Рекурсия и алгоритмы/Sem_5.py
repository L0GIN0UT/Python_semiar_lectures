# Задача №31. Решение в группах
# Последовательностью Фибоначчи называется
# последовательность чисел a0
# , a1
# , ..., an
# , ..., где
# a0
#  = 0, a1
#  = 1, ak
#  = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21
# Задание необходимо решать через рекурсию

# def FibbonachyNumber(value):
#     if value <= 1:                  
#         return 1
#     else:
#         return (FibbonachyNumber(value - 1) + FibbonachyNumber(value - 2))

# while True:
#     n = int(input('Введите интересующую вас Номер числа Фиббоначи -> '))
#     if n < 1:
#         print('Вы ввели отрицательное число или 0')
#     else:
#         break
# print(f'Число Фибонначи в позиции {n} - {FibbonachyNumber(n)}')

# Задача №33. Решение в группах
# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

# БЕЗ РЕКУРСИИ

# while True:
#     n = int(input('Кол-во оценок -> '))
#     if n < 1:
#         print('Вам не нужно менять оценки')
#     else:
#         break

# arr = []
# while n > 0:
#     b = int(input('Введите оценку -> '))
#     arr.append(b)
#     n -= 1
# print(arr)

# max_val = max(arr)
# min_val = min(arr)

# for i in range(0, len(arr)):
#     if arr[i] == max_val:
#         arr[i] = min_val
# print(arr)

# Вариант 2 кортеж мин макс

# my_list = [1, 2, 3, 4, 5, 5, 5, 5]

# def min_max(my_list):
#     min = max = my_list[0]
#     for i in my_list:
#         if i>max:
#             max=i
#         if i<min:
#             min = i
#     return (min, max)

# # min, max = min_max(my_list)

# def change_min_max(my_list, temp):
#     for i in range(len(my_list)):
#         if my_list[i]==temp[1]:
#             my_list[i]=temp[0]
#     return my_list

# print (change_min_max(my_list, min_max(my_list)))


# Задача №35. Решение в группах
# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes 

# число делится на числа от 2 до (числа//2)+1
 
# В терминале вводим pip install sympy
# import sympy
# print(sympy.isprime(int(input('Введите число -> '))))

# def CommonOrNot(value):
#     if value == 2:
#         return ('yes')
#     for i in range(2,(value//2) + 1):
#         if value % i == 1:
#             print('yes')
#             exit()
#     print('no')

# CommonOrNot(int(input('Введите число -> ')))

# Примеры простых чисел до 100: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97.

# 2 вариант
# def CheckingProstNum (num):
#     for i in range(2, int(num**0.5)+1): #единицу добавляем для получения следующего целого числа после квадратного корня
#         if num % i == 0:
#             return ("Число не простое")
#     return ("Число простое") #число простое по умолчанию!

# n = int(input("Введите число N для проверки простоты: "))
# print(CheckingProstNum(n))


# Задача №37. Решение в группах
# Дано натуральное число N и
# последовательность из N элементов.
# Требуется вывести эту последовательность в
# обратном порядке.
# Примечание. В программе запрещается
# объявлять массивы и использовать циклы
# (даже для ввода и вывода).
# Input: 2 -> 3 4
# Output: 4 3

def ReverseString(value):
    n = int(input('Введите элемент -> '))
    if value > 1:
        ReverseString(value - 1)
    print(n, end = ' ')

ReverseString(int(input('Введите колличество элементов -> ')))    


# 2 вариант
# def Reverse(num):
#     if num == 0:
#         return ""
#     number = input("Введите число: ")
#     return f"{Reverse(num-1)}{number} " #пробел в конце, потому что идём в обратную сторону
    

# n = int(input("Введите число N элементов: "))
# print(Reverse(n))