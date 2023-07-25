import re
# Задача №25. Решение в группах
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию
# .split()


# string = input('Введите элементы списка через пробел -> ').split()

# dict = {}
# result = ''
# for i in string:
#     if i not in dict:
#         dict[i] = 0
#         result += str(i) + ' '
#     else:
#         dict[i] += 1
#         result += str(i) + '_' + str(dict[i]) + ' '
# print(dict)
# print(result)



# string = input('Введите элементы списка через пробел -> ').split()
# dict = {}
# res = ''
# for i in string:
#     if i in dict:
#         dict[i] += 1
#         res += str(i) + '_'+ str(dict[i]) + ' '
#     else:
#         dict[i] = 0
#         res += str(i) + ' '
# print(res)

# Дан текст. Выведите слово, которое в этом тексте встречается чаще всего.
# Если таких слов несколько, выведите то, 
# которое меньше в лексикографическом порядке.

# She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells

# string = re.split(' |\\.', input('Введите текст -> ').lower())
# string.sort()
# dict = {}
# for i in string:
#     if i not in dict:
#         dict[i] = 1
#     else:
#         dict[i] += 1

# max_val = 0
# max_key = ''
# for key, value in dict.items():
#     if value > max_val:
#         max_val = value
#         max_key = key
# print(f'Слово которое чаще всего встречалось - {max_key}, оно встретилось - {max_val} раз/раза!' )



# Задача №27. Решение в группах
# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells
# Output: 13

# print(len(set(re.split(' |\\.', input('Введите текст -> ').lower()))))

# Задача №29. Решение в группах
# Ваня и Петя поспорили, кто быстрее решит
# следующую задачу: “Задана последовательность
# неотрицательных целых чисел. Требуется определить
# значение наибольшего элемента
# последовательности, которая завершается первым
# встретившимся нулем (число 0 не входит в
# последовательность)”. Однако 2 друга оказались не
# такими смышлеными. Никто из ребят не смог до
# конца сделать это задание. Они решили так: у кого
# будет меньше ошибок в коде, тот и выиграл спор. За
# помощью товарищи обратились к Вам, студентам.
# Примечание: Программные коды на следующих
# слайдах

# Ваня:
# n = int(input(" a"))
# max_number = 1000
# while n != 0:
#     n = int(input(" b"))
#     if max_number > n:  # выводит 0 потому что  если n < 
#         max_number = n  # то его мы и добавляем
# print(max_number)

# Петя:
# n = int(input())
# max_number = -1
# while n < 0: # задание не для отрицательных числео
#     n = int(input()) # любое число которое мы вводим > 0 
#     if max_number < n: # следовательно оно е зпходит в цикл
#         n = max_number
# print(n) 

# arr = []
# while True:
#     n = int(input('Введите число из списка (0 заканчивает запись) -> '))
#     if n > 0:
#         arr.append(n)
#     elif n == 0:
#         break
# print(f'Максимально значение в списке - {max(arr)}')

n = 1
max_number = 0
while n > 0:
    n = int(input()) 
    if max_number < n:
        max_number = n
    elif n == 0:
        break
print(max_number) 