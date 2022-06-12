# Для себя решил сделать ромбик;)
from datetime import datetime

def timeit(func):
    def wraper():
        return result

    return wraper

def draw_rhombus(width):
    start = datetime.now()
    for i in range(1, width + 1, 2):
        print(' ' * ((width - i) // 2) + '*' * i)

    for j in range(width, 1, -2):
        print(((width - j) // 2) * ' ' + (j - 1) * '*')
    print(datetime.now() - start)

draw_rhombus(20)
