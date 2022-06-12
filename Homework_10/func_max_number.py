# Напишите функцию, которая вернет максимальное число из списка чисел.
from random import randint

def max_number(sp):
    return max(sp)

sp = [randint(1,100) for i in range(10)]
print(sp)  # сгенерированный список
print(max_number(sp))