import os
import re
import random

filepath = os.path.join("c:/Users/Ivanlogin888/Desktop/Python/Python_semiar_lectures/Base_Phone_book",'Users_data.txt')

arr_id = []

# Функция открытия и записи в файл инвормации (если файл уже есть то мы добавляем в него данные)
def zapis(arr):
    a = random.randint(100000, 10000000)
    if a not in arr_id:
        arr_id.append(a)
    dict = {0: 'ID:', 1: 'Фамилия:', 2: 'Имя:', 3: 'Отчество:', 4: 'Номер:'}
    counter = 1
    if os.path.exists(filepath):
        with open(filepath,'a',encoding = 'utf-8') as f:
            f.writelines('-'*5 + 'Пользователь' + '-'*5 + '\n')
            f.writelines(dict[0] + ' ' + str(a) + '\n')
            for i in arr:
                f.writelines(dict[counter] + ' ' + i + '\n')
                counter += 1
            f.write('\n')
            return print(f'Данные пользователя были успешно добавлены!')         
    else:
        with open(filepath,'w+',encoding = 'utf-8') as f:
            f.writelines('-'*5 + 'Пользователь' + '-'*5 + '\n')
            f.writelines(dict[0] + ' ' + str(a) + '\n')
            for i in arr:
                f.writelines(dict[counter] + ' ' + i + '\n')
                counter += 1
            f.write('\n')
            return print(f'Данные пользователя были успешно добавлены!')
            
# Функция поиска Данных пользователя и их печати
def read_search(teg):
    # arr_scndnames = []
    if os.path.exists(filepath):
        with open(filepath,'r',encoding = 'utf-8') as f:
            # if teg.isalpha():
            #     new_array = [re.sub('\s+','',line) for line in f.readlines()]
                # for j in range(0,(len(new_array)//7)):
                    # temp_arr = []
                    # for i in range(len(new_array[j+4*j])+1,len(new_array[(j+4*j)+4])+1):
                        # if teg in new_array[i]:
                        #     # temp_arr = new_array[i-1:i+3]
                        #     print(new_array)
                        #     temp_arr.append(new_array[i-1])
                        #     temp_arr.append(new_array[i])
                        #     temp_arr.append(new_array[i+1])
                        #     temp_arr.append(new_array[i+2])
                        #     temp_arr.append(new_array[i+3])
                    # arr_scndnames.append(temp_arr)
                        # return print(arr_scndnames)  
            new_array = [re.sub('\s+','',line) for line in f.readlines()]
            print(f'По ващему запросу {teg} удалось найти:')
            for j in range(0,1):
                for i in range(0,len(new_array)):
                    if teg in new_array[i]:
                        print(f'\n {new_array[i]} \n {new_array[i+1]} \n {new_array[i+2]} \n {new_array[i+3]}')
    else: return print('Файла не существует!')

# print(f"По вашему запросу '{teg}' \n'*'{teg}' \n'*'{arr_scndnames}", sep='\n')

# Функция Чтения всех
def read_all():
    with open(filepath,'r',encoding = 'utf-8') as f:
        for line in f:
            print(line[:-1])

# Функция удаления данных пользователя из файла
def delete(teg):
    check = False
    with open(filepath,'r',encoding = 'utf-8') as f:
        arr = [line for line in f.readlines()]
        for i in range(len(arr)):
            if teg in arr[i]:
                check = True
                if teg.isalpha():
                    arr[i-2], arr[i-1], arr[i], arr[i+1], arr[i+2], arr[i+3], arr[i+4] = '', '', '', '', '', '', ''
                if teg.isdigit():
                    arr[i-1], arr[i], arr[i+1], arr[i+2], arr[i+3], arr[i+4], arr[i+5] = '', '', '', '', '', '', ''
        if check == True:
            with open(filepath,'w',encoding = 'utf-8') as f:
                f.writelines(arr)
                return print(f'Данные пользователей "{teg}" были успешно удалены!')
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
                if diction == '1': arr[i+1] = dict[diction] + ' ' + new_teg + '\n'
                if diction == '2': arr[i+2] = dict[diction] + ' '  + new_teg + '\n'
                if diction == '3': arr[i+3] = dict[diction] + ' '  + new_teg + '\n'
                if diction == '4': arr[i+4] = dict[diction] + ' '  + new_teg + '\n'    
    if check == True:               
        with open(filepath,'w',encoding = 'utf-8') as f:
            f.writelines(arr)
            return print(f'Данные пользователя "{teg}" были успешно изменены!')
    else: return print(f'По вашему запросу "{teg}" ничего не найдено!')