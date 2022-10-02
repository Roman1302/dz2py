'''Задача 3. Реализуйте алгоритм перемешивания списка. 
Список размерностью 10 задается случайными целыми числами, 
выводится на экран, затем перемешивается, опять выводится на экран. 
SHUFFLE нельзя юзать!'''

import os
clear = lambda: os.system('clear')
clear()

print("***Программа перемешивания случайных чисел***\n")

from random import randint
list_length = 10 
a,b = 10,99
lst = [None] * list_length
for i in range(list_length):
    lst[i] = randint(a,b)
print(lst)

tmp = []
while len(tmp) < list_length:
    x = randint(0, 9)
    if x not in tmp:
        tmp.append(x)
# print(tmp)

lst_new = [None] * list_length
for q in range(list_length):
    lst_new[q] = lst[tmp[q]]
print(lst_new)
