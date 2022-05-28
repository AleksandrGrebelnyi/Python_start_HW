# Создайте список случайных чисел (размером 4 элемента). Создайте второй
# список в два раза больше первого, где первые 4 элемента должны быть равны
# элементам первого списка, а остальные элементы заполните удвоенными
# значением начальных. Например,
# Было → [1,4,7,2]
# Стало → [1,4,7,2,2,8,14,4]

import random
sp = []
for i in range(4):
    sp.append(random.randint(1, 10))  # fill our list with 4 random numbers from 1 to 10
print('Before =>', sp)
sp2 = sp.copy()  # copy our random list
for j in sp2:
    sp.append(j * j)  # add square off our random list ( also we can do j ** 2
print('After =>', sp)





