from functions import *

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
        choise = input('Введите действие (1,2,3,4,5,6) -> ').lower()
        if choise == '1': return zapis(checking_for_input_length(input('Введите Фамилию Имя Отчество и Номер телефона человека через пробел -> ').split()))
        if choise == '2': return read_search(input('Введите Фамилию человека которого вы ищите -> '))
        if choise == '3': return delete(input('Внимание: Если введете Фамилию.\nПрограмма удалит всех Однофамильцев\nВведите Фамилию или ID человека для удаления его данных -> '))
        if choise == '4': return change(input('Введите ID человека для замены его данных -> '), input('Введите что вы хотите изменить (1 - Фамилия, 2 - Имя, 3 - Отчество, 4 - Номер) -> ') , input('Введите новые данные -> '))
        if choise == '5': return read_all() 
        if choise == '6': exit()