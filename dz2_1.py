'''Задача 1. Напишите программу, которая принимает на вход вещественное 
или целое число и показывает сумму его цифр. Через строку нельзя решать.
*Пример:*
- 6782 -> 23
- 0,56 -> 11'''

import os
clear = lambda: os.system('clear')
clear()
print("***Программа суммы цифр числа***")

def summ(num):
    res = [i for ele in num for i in ele]
    if ',' in res:
        res.remove(',')
    elif '.' in res:
        res.remove('.')
    sum=0
    for i in range(len(res)):
        sum+=int(res[i])
    print("\n->", sum)

try:
    number=input("\nВведите вещественное или целое число: ")
    summ(number)
except:
    print("\nНужно вводить число!")
