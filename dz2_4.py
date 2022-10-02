'''Задача 4 НЕОБЯЗАТЕЛЬНАЯ. Напишите программу, которая принимает на вход N, 
и координаты двух точек и находит расстояние между ними в N-мерном пространстве.'''

import os
clear = lambda: os.system('clear')
clear()
print("***Программа находит расстояние между ними в N-мерном пространстве***")


def array(np):
    for i in range(np):
        x=[]
        y=[]
        x.append(input("Введите x: "))
        y.append(input("Введите y: "))
        # print(lis)
    return x, y
nr=int(input("\nВведите N-мерном пространства: "))
array(nr)
print(array)

# try:
#     number=input("\nВведите вещественное или целое число: ")
#     summ(number)
# except:
#     print("\nНужно вводить число!")