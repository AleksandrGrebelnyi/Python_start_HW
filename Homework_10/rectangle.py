# Реализуйте функцию рисующую на экране прямоугольник из звездочек «*». Ее
# параметрами будут целые числа, которые описывают длину и ширину такого
# прямоугольника.

def draw_rectangle(lenght, width):
    for i in range(1, lenght + 1):
        if i == 1 or i == lenght:
            print('*' * width)
        else:
            print('*' + ' ' * (width - 2) + '*')


draw_rectangle(10, 6)