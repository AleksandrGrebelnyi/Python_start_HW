# Представьте в виде списка списков матрицу
# [ 1, 2 , 3, 4]
# [ 5, 6 , 7, 8]
# [ 9,10, 11, 12]
# [13,14, 15, 16]
# Напишите программу, которая выведет эту матрицу на экран, вычислит и
# выведет сумму элементов этой матрицы. РЕШИЛ 3-мя РАЗНЫМИ ВАРИАНТАМИю 2-ой вариант мой фваритю

# First variant
import numpy as np
sp = np.arange(1, 17)

print(f'{sp[:4]}\n{sp[4:8]}\n{sp[8:12]}\n{sp[12:]}')
print(f'Matrix sum => {sum(sp)}')


# Second variant is only in two lines
import numpy as np  # will use arange and reshape to make matrix
print(f'{np.arange(1, 17).reshape(4, 4)}\nMatrix sum => {np.arange(1, 17).reshape(4, 4).sum()}')


# Third variant is with
sp = []
for i in range(1, 2):
    for j in range(1, 17):
        sp.append(j)
print(f'{sp[:4]}\n{sp[4:8]}\n{sp[8:12]}\n{sp[12:]}\nSumma matrix => {sum(sp)}')
