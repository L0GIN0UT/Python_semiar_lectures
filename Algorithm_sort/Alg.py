# Алгоритм Бинарного Поиска/Binar Search Algoritm(B.S.A.)

def binary_search(list, item):
    low = 0  # <== Начало массива
    high = len(list) - 1  # <==  # <== Конец массива

    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:  # <== Если То что ищем равно Среднему
            return mid
        if guess > item: # <== Если То что ищем меньше Среднего
            high = mid - 1
        else:  # <== Если То что ищем меньше Среднего
            low = mid + 1
    return None

# Алгоритм Быстрой Сортировки/Quick Sort Algoritm(Q.S.A.)

def quicksort(array):
    if len(array) < 2:
        return array
    else:
        start_point = array[0] # <== старт с 1 символа
        less = [i for i in array[1:] if i <= start_point] # <== Перенос влево если меньше чем Старт 
        greater = [i for i in array[1:] if i > start_point] # <== Перенос вправо если больше чем Старт
        return quicksort(less) + [start_point] + quicksort(greater) # <== Возвращаем в массив отсортированных соседей
    

# Алгоритм Сортировки Слиянием/Merge Sort Algoritm(M.S.A.)

def mergesort(array): 
    if len(array) > 1: 
        mid = len(array)//2
        left = array[:mid] 
        right = array[mid:]
        mergesort(left) 
        mergesort(right) 

        i = j = k = 0

        while i < len(left) and j < len(right): 
            if left[i] < right[j]: 
                array[k] = left[i] 
                i += 1
            else: 
                array[k] = right[j] 
                j += 1
            k += 1

        while i < len(left): 
            array[k] = left[i] 
            i += 1
            k += 1

        while j < len(right): 
            array[k] = right[j] 
            j += 1
            k += 1

# Алгоритм Кнута-Морриса-Пратта (КМП-алгоритм)/KMP Algorithm

def KMPalgorithm(text, word):
    pi = [0]*len(word) # <-- Максимальная совпадающая ДЛИНА суфикса, относительно i-го элемента образа
    i = 1
    j = 0   
    while i < len(word):
        if word[j] == word[i]: # сравнение элемента из слова с эл из текста(счетчик)
            pi[i] = j+1 # если да то прибавляем единицу в массив и увеличиваем i и j
            i += 1
            j += 1
        else: # если нет то сравниваем j с 0 если да то начинаем отчет заново
            if j == 0: 
                pi[i] = 0
                i += 1
            else:
                j = pi[j-1]  # иначе возвращаемся в предыдущий элемент в слове

    print(f'Максимальная длина суффикса - {max(pi)}')

    message = len(word)
    message_text = len(text)

    i = 0
    j = 0
    while i < message_text:
        if text[i] == word[j]:
            i += 1
            j += 1
            if j == message:
                print(f'Слово/элемент ({word}) найдено')
                break
        else:
            if j > 0:
                j = pi[j-1]
            else:
                i += 1

    if i == message_text and j != message:
        print(f'Слово/элемент ({word}) не найдено')






