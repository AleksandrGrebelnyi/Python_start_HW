# Для себя треугольник нарисовал;)

def draw_triangle(width):
    for i in range(1, width + 1, 2):
        print(' ' * ((width - i) // 2) + '*' * i)


draw_triangle(15)