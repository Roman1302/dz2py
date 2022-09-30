'''Задача 2. Напишите программу, которая принимает на вход число N 
и выдает набор произведений чисел от 1 до N.
*Пример:*
- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)'''

print("***Программа вывода набора произвежений от 1 до N***")



def array(numer):
    lis=[]
    res = 1
    for i in range(numer) :
        res *= (i+1)
        # print(res)
        lis.append(res)
        # print(lis)
    return lis

try:
    num=int(input("\nВведите целое число N: "))
    print("\n", array(num))
except:
    print("\nНужно вводить число!")
