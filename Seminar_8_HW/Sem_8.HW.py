import os.path
import re


# ВНИМАНИЕ ИЗМЕНИТЕ ПУТЬ В filepath ДЛЯ КОРРЕКТОЙ РАБОТЫ ПРОГРАММЫ
filepath = os.path.join("c:/Users/Ivanlogin888/Desktop/Python/Python_semiar_lectures/Seminar_8_HW",'Users_data.txt')

# Функция для проверки длины сообщения пользователя
def checking_for_input_length(arr):
    if len(arr) > 4:
        arr = arr[:4]
    if len(arr) < 4:
        a = len(arr)
        while a < 4:
            arr.append('None')
            a += 1
    return arr

# Функция для выбора функций
def choose():
    while True:
        choise = input('Введите действие (1,2,3,4,5) -> ').lower()
        if choise == '1': return zapis(checking_for_input_length(input('Введите Фамилию Имя Отчество и Номер телефона человека через пробел -> ').split()))
        if choise == '2': return read_search(input('Введите Фамилию человека которого вы ищите -> '))
        if choise == '3': return delete(input('Введите Фамилию человека для удаления его данных -> '))
        if choise == '4': return change(input('Введите Фамилию человека для замены его данных -> '), input('Введите что вы хотите изменить (1 - Фамилия, 2 - Имя, 3 - Отчество, 4 - Номер) -> ') , input('Введите новые данные -> '))
        if choise == '5': exit() 

# Функция открытия и записи в файл инвормации (если файл уже есть то мы добавляем в него данные)
def zapis(arr):
    dict = {0: 'Фамилия:', 1: 'Имя:', 2: 'Отчество:', 3: 'Номер:'}
    counter = 0
    if os.path.exists(filepath):
        with open(filepath,'a',encoding = 'utf-8') as f:
            f.writelines('-'*5 + 'Пользователь' + '-'*5 + '\n')
            for i in arr:
                f.writelines(dict[counter] + ' ' + i + '\n')
                counter += 1
            f.write('\n')
            return print(f'Данные пользователя были успешно добавлены!')         
    else:
        with open(filepath,'w+',encoding = 'utf-8') as f:
            f.writelines('-'*5 + 'Пользователь' + '-'*5 + '\n')
            for i in arr:
                f.writelines(dict[counter] + ' ' + i)
                f.write('\n')
                counter += 1
            f.write('\n')
            return print(f'Данные пользователя были успешно добавлены!')
            
# Функция поиска Данных пользователя и их печати
def read_search(teg):
     with open(filepath,'r',encoding = 'utf-8') as f:
        new_array = [re.sub('\s+','',line) for line in f.readlines()]
        for i in range(0,len(new_array)):
            if teg in new_array[i]:
                return print(f'По ващему запросу {teg} удалось найти: \n {new_array[i]} \n {new_array[i+1]} \n {new_array[i+2]} \n {new_array[i+3]}')
        return print(f'По вашему запросу "{teg}" ничего не найдено')

# Функция удаления данных пользователя из файла
def delete(teg):
    check = False
    with open(filepath,'r',encoding = 'utf-8') as f:
       arr = [line for line in f.readlines()]
       for i in range(len(arr)):
           if teg in arr[i]:
               check = True
               arr[i-1], arr[i], arr[i+1], arr[i+2], arr[i+3], arr[i+4] = '', '', '', '', '', ''
    if check == True:
        with open(filepath,'w',encoding = 'utf-8') as f:
            f.writelines(arr)
            return print(f'Данные пользователя "{teg}" были успешно удалены!')
    return print(f'По вашему запросу "{teg}" ничего не найдено!')

# Функция изменения данных в файле
def change(teg, diction, new_teg):
    check = False
    dict = {'1': 'Фамилия:', '2': 'Имя:', '3': 'Отчество:', '4': 'Номер:'}
    if diction not in dict.keys():
        return print(f'Ваше значение "{diction}" не подходит условию!')
    with open(filepath,'r',encoding = 'utf-8') as f:
        arr = [line for line in f.readlines()]
        for i in range(len(arr)):
            if teg in arr[i]:
                check = True
                if diction == '1': arr[i] = dict[diction] + ' ' + new_teg + '\n'
                if diction == '2': arr[i+1] = dict[diction] + ' '  + new_teg + '\n'
                if diction == '3': arr[i+2] = dict[diction] + ' '  + new_teg + '\n'
                if diction == '4': arr[i+3] = dict[diction] + ' '  + new_teg + '\n'    
    if check == True:               
        with open(filepath,'w',encoding = 'utf-8') as f:
            f.writelines(arr)
            return print(f'Данные пользователя "{teg}" были успешно изменены!')
    else: return print(f'По вашему запросу "{teg}" ничего не найдено!')

while True:
    print('Выберите действие: \n 1 - Записать данные в файл \n 2 - Найти данные по Фамилии \n 3 - Удалить данные  \n 4 - Изменить данные \n 5 - Остановить программу')
    choose()
    input('Введите ENTER чтобы продолжить!')


