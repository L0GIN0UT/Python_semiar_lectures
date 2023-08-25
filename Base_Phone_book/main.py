from interface import *
clear = lambda: os.system('cls' if os.name=='nt' else 'clear')

while True:
    clear()
    print('Выберите действие: \n 1 - Записать данные в файл \n 2 - Найти данные по Фамилии \n 3 - Удалить данные  \n 4 - Изменить данные \n 5 - Вывод всего списка \n 6 - Остановить программу')
    choose()
    input('Введите ENTER чтобы продолжить!')