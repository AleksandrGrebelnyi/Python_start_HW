# Есть круг с центром в начале координат и радиусом 4. Пользователь вводит
# с клавиатуры координаты точки x и y. Написать программу, которая
# определит, лежит ли эта точка внутри круга или нет

x, y = float(input('Enter coordinate of x = ')), float(input('Enter coordinate of y = '))
r = 4
if r >= (x ** 2 + y ** 2) ** 0.5:
    print('Include')
else:
    print('Exclude')
