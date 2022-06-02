# Выведите на экран 10 строк со значением числа Pi. В первой строке
# должно быть 2 знака после запятой, во второй 3 и так далее

from math import pi
for i in range(2, 12):
    print(f'{pi:.{i}f}')


# for i in range(2, 12):
#     print(round(pi, i))


# print(pi)
# print(f'{pi:.2f}\n{pi:.3f}\n{pi:.4f}\n{pi:.5f}\n{pi:.6f}\n{pi:.7f}\n{pi:.8f}\n{pi:.9f}\n{pi:.10f}')






