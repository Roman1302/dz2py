'''Задача 1. Напишите программу, которая принимает на вход вещественное 
или целое число и показывает сумму его цифр. Через строку нельзя решать.
*Пример:*
- 6782 -> 23
- 0,56 -> 11'''
print("***Программа суммы цифр цисла***")
number=[]
number=input("Введите вещественное или целое число: ")
def summ(num):
    res = [i for ele in num for i in ele]
    # print(res)
    if ',' in res:
        res.remove(',')
    elif '.' in res:
        res.remove('.')
    else:
        print(res)
    sum=0
    for i in range(len(res)):
        sum+=int(res[i])
    print("->", sum)

summ(number)