# Дан список [0,5,2,4,7,1,3,19]. Написать программу для подсчета нечетных
# чисел в нем. Добавил от себя для практики список всех нечетных чисел и сумму всех нечетных чисел.
# 2 variants of solutions

sp = [0, 5, 2, 4, 7, 1, 3, 19]
res = list(filter(lambda x: x % 2, sp))  # func filter(func, sequence) help find odd numbers
print(f'Amount of odd numbers => {len(res)}\nSumma of odd numbers => {sum(res)}\nList of odd numbers => {res}')


sp = [0, 5, 2, 4, 7, 1, 3, 19]
sp2 = []
count = 0
total = 0
for i in range(len(sp)):
    if sp[i] % 2:
        count += 1
        total += sp[i]
        sp2.append(sp[i])
print(f'Amount of odd numbers is => {count}\nList of odd numbers => {sp2}\nSumma of odd numbers => {total}')

