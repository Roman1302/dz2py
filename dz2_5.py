'''Задача 5 НЕОБЯЗАТЕЛЬНАЯ. Напишите программу для проверки истинности утверждения
 ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат. 
 Количество предикатов генерируется случайным образом от 5 до 11, 
 проверяем это утверждение 10 раз, с помощью модуля time выводим на экран , 
 сколько времени отработала программа.'''


import time
start_time = time.time()

import os
clear = lambda: os.system('clear')
clear()

print("**Проверки истинности утверждения \n¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z \nдля всех значений предикат**")
print('x y z')
for i in range(10):
    for x in 0, 1:
        for y in 0, 1:
            for z in 0, 1:
                if (not (x or y or z)) == (not x and not y and not z):
                    print(x, y, z, "-> Истина")
                else:
                    print(x, y, z, "-> Ложь")
    print(i) # main()
print("--- %s seconds ---" % (time.time() - start_time))