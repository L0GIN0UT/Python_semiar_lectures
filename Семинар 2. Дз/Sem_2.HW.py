import random
import math
# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.
# 5 -> 1 0 1 1 0
# 2

# while True:
#     n = int(input('Введите кол-во монет на столе -> '))
#     if n == 0:
#         print(0)
#         break
#     if n > 0:
#         break
#
# coins_arr = []
# count_one = 0
# count_zero = 0
#
# while n > 0:
#     coins_arr.append(random.randint(0, 1))
#     n -= 1
# print(coins_arr)
#
# for i in range(0,len(coins_arr) - 1):
#     if coins_arr[i] == 0:
#         count_zero += 1
#     else:
#         count_one += 1
#
# if count_one > count_zero:
#     print(f'Минимальное кол-во монет которое'
#           f' надо перевернуть - {count_zero}')
# else:
#     print(f'Минимальное кол-во монет которое'
#           f' надо перевернуть - {count_one}')


# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя –
# школьница. Петя помогает Кате по математике. Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
# этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа.
# 4 4 -> 2 2
# 5 6 -> 2 3

# Защита от дурака
while True:
    amount = int(input('Введите СУММУ 2-х чисел -> '))
    if amount == 0:
        print('1-ое и 2-е загаданное число равны 0')
        exit()
    composition = int(input('Введите ПРОИЗВЕДЕНИЕ 2-х чисел -> '))
    if amount > 0 and composition > 0:
        break
    elif composition == 0:
        print('Одно из загаданных чисел 0, а второе может быть ЛЮБЫМ!')
        exit()

D = (amount**2) - (4 * composition)
first_num = (amount + math.isqrt(D))//2
second_num = amount - first_num # ИЛИ second_num = (amount - math.isqrt(D))/2

print(f'1-ое загаданное число это - {first_num}'
      f' , а 2-ое загаданное число это - {second_num}')



# Задача 14: Требуется вывести все целые степени двойки (т.е. числа
# вида 2k
# ), не превосходящие числа N.
# 10 -> 1 2 4 8

# while True:
#     n = int(input('Введите число -> '))
#     if n > 0:
#         break
#
# rank_of_two = 1
# rank_arr = []
#
# while rank_of_two < n:
#     rank_arr.append(rank_of_two)
#     rank_of_two *= 2
#
# print(rank_arr)