# Выведите на экран «песочные часы», максимальная ширина которых
# считывается с клавиатуры (число нечетное). В примере ширина равна 5.
# *****
#  ***
#   *
#  ***

width = int(input('Enter any odd number: '))
k = 1  # this variable help us with spaces
for i in range(width, 0, -2):
    print(' ' * k + '*' * i)
    k += 1

k -= 1
for j in range(3, width + 1, 2):
    k -= 1
    print(' ' * (k) + '*' * j)








