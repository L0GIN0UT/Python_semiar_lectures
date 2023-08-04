
# Простые примеры
# def f(n):
#     return n**2

# def f1(n):
#     return n%2 == 0


# pre_arr = input().split()
# print(pre_arr)
# pre_arr = list(map(int, pre_arr))
# arr = list(map(f, pre_arr))
# arr = list(map(lambda x: x**2, pre_arr))
# print(arr)
# x=5
# per = x%2==0
# print(per)
# arr = list(filter(f1, pre_arr))
# arr = list(filter(lambda x: x%2==0, pre_arr))
# print(arr)


# arr1= [1, 2, 3, 4, 5]
# arr2= [11, 22, 33, 44, 55, 66]


# arr3 = list(zip(arr1, arr2))
# arr3.append("asfsadf")
# print(arr3)


# arr = [11, 22, 33, 44, 55, 66]
# arr_res = list(enumerate(arr))
# print(arr_res)


# Задача №47. Решение в группах
# У вас есть код, который вы не можете менять (так часто бывает, когда код в глубине
# программы используется множество раз и вы не хотите ничего сломать):
# transformation = <???>
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
# transormed_values = list(map(transformation, values))
# Единственный способ вашего взаимодействия с этим кодом - посредством задания
# функции transformation.
# Однако вы поняли, что для вашей текущей задачи вам не нужно никак преобразовывать
# список значений, а нужно получить его как есть.
# Напишите такое лямбда-выражение transformation, чтобы transformed_values получился
# копией values.
# Пример ввода и вывода данных представлены на следующем
# слайде
# Задача №47. Решение в группах
# Ввод:
# values = [1, 23, 42, ‘asdfg’]
# transformed_values = list(map(trasformation, values))
# if values == transformed_values:
#  print(‘ok’)
# else:
#  print(‘fail’)
# Вывод:
# ok

# def transformation(values):
#     return lambda x: x

# values = [1, 23, 42, 'asdfg']
# transformed_values = list(map(transformation(values), values))
# if values == transformed_values: print('OK') 
# else: print('FAIL')


# Или

# values = [1, 23, 42, 'asdfg']
# transformed_values = list(map(lambda x: x, values))
# if values == transformed_values: print('OK') 
# else: print('FAIL')



# Задача №49. Решение в группах
# Планеты вращаются вокруг звезд по эллиптическим орбитам.
# Назовем самой далекой планетой ту, орбита которой имеет
# самую большую площадь. Напишите функцию
# find_farthest_orbit(list_of_orbits), которая среди списка орбит
# планет найдет ту, по которой вращается самая далекая
# планета. Круговые орбиты не учитывайте: вы знаете, что у
# вашей звезды таких планет нет, зато искусственные спутники
# были были запущены на круговые орбиты. Результатом
# функции должен быть кортеж, содержащий длины полуосей
# эллипса орбиты самой далекой планеты. Каждая орбита
# представляет из себя кортеж из пары чисел - полуосей ее
# эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b,
# где a и b - длины полуосей эллипса. При решении задачи
# используйте списочные выражения. Подсказка: проще всего
# будет найти эллипс в два шага: сначала вычислить самую
# большую площадь эллипса, а затем найти и сам эллипс,
# имеющий такую площадь. Гарантируется, что самая далекая
# планета ровно одна
# Пример ввода и вывода данных представлены на
# следующем слайде
# Задача №49. Решение в группах
# Ввод:
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*find_farthest_orbit(orbits))
# Вывод:
# 2.5 10

def find_farthest_orbit(orbits):
    arr_orbits = [i for i in orbits if i[0] != i[1]]
    areas = [(i[0]*i[1]) for i in arr_orbits]
    return arr_orbits[areas.index(max(areas))]
print(find_farthest_orbit([(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]))



# Задача №51. Решение в группах
# Напишите функцию same_by(characteristic, objects), которая
# проверяет, все ли объекты имеют одинаковое значение
# некоторой характеристики, и возвращают True, если это так.
# Если значение характеристики для разных объектов
# отличается - то False. Для пустого набора объектов, функция
# должна возвращать True. Аргумент characteristic - это
# функция, которая принимает объект и вычисляет его
# характеристику.
# Ввод: Вывод:
# values = [0, 2, 10, 6]
# if same_by(lambda x: x % 2, values):
# print(‘same’)
# else:
# print(‘different’)


# def same_by(characteristic, objects):
#     counter = [1 for i in objects if i % 2 == 0]
#     if sum(counter) == len(objects): return True
#     else: return False

# values = [0, 2, 10, 6]
# if same_by(lambda x: x % 2, values): print('same')
# else: print('different')


# Дан список
# в отдельном списке вывести буквы
# в другом цифры

# arr = [1, 'abfdjksdagf', 2, 'ugfuisgf']
# arr_1 = list(filter(lambda x: type(x) == int, arr))
# arr_2 = list(filter(lambda x: type(x) == str, arr))
# print(arr_1, arr_2)

# arr_in = input('Введите строку -> ').split()
# arr_1 = list(filter(lambda x: x.isdigit(), arr_in))
# arr_2 = list(filter(lambda x: x.isalpha(), arr_in))
# print(arr_1, arr_2)

# 2) Дано вещественное число, показать сумму его цифр.
# n = '1.658376486790'.replace('.','')
# print(sum(list(map(int, n))))

# print(sum(list(map(int, '1.658376486790'.replace('.','')))))


# num = 3.12
# stroka = str(num)

# res = list(filter(lambda x: x != ".", stroka))
# res = sum(list(map(int, res)))

# дан список целых чисел 
# оставить только 2значные числа

arr = map(int,input('Введите число').split())
arr_res = list(filter(lambda x: x in range(10,100), arr))
print(arr_res)

# print(list(filter(lambda x: x in range(10,100), map(int,input('Введите число -> ').split()))))

