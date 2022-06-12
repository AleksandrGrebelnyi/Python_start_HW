# Для себя нарисовал песочные часы;) с функцией проверки
# времени исполнения кода

from datetime import datetime


def work_time(func):
    def wrapper(*args):
        start = datetime.now()
        result = func(*args)
        print(datetime.now() - start)
        return result
    return wrapper


@work_time
def draw_clock(width):
    for i in range(width, 1, -2):
        print(((width - i) // 2) * ' ' + '*' * i)

    for j in range(2, width, 2):
        print(((width - j) // 2) * ' ' + '*' * j)


draw_clock(10)