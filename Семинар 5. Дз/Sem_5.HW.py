# Задача 26: Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8


# С фиксированной переменной
# def FirstGradeSecond(A, B , grade):
#     grade *= A
#     if B <= 1:
#         print(grade)
#     else:
#         FirstGradeSecond(A, B - 1, grade)

# FirstGradeSecond(int(input('Введите число которое хотите возвести -> ')), int(input('Введите степень числа -> ')), 1)

# Без фиксированной переменной
# def FirstGradeSecond(A, B):
#     if B == 1:
#         return(A)
#     else:
#         return(A * FirstGradeSecond(A, B - 1))

# print(FirstGradeSecond(int(input('Введите число которое хотите возвести -> ')), int(input('Введите степень числа -> '))))

# Задача 28: Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел. Из
# всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.
# 2 2
# 4

def SumFirstAndSecond(A, B):
    if B == 0:
        return(A)
    else:
        return(SumFirstAndSecond(A + 1, B - 1))

print(SumFirstAndSecond(int(input('Введите 1 число -> ')), int(input('Введите 2 число -> '))))