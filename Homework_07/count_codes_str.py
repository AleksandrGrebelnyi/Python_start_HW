# Напишите программу, которая вычислит сумму всех кодов символов
# строки.

r = 'Hello world'
x = list(map(lambda t: ord(t), r))
print(x)
print(sum(x))
