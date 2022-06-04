# Напишите программу, которая переведет целое число (от 1 до 100) из римской
# записи в обычные цифры.
# Например: XXII -> 22. Made 2 solutions

# first solution

import roman

n = input()
print(roman.fromRoman(n))


# second solution

number = input('Enter: ')

rome_arab = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100}
sp = []
for num in number:
    sp.append(rome_arab.get(num))
if (1 in sp and 5 in sp and sp.index(1) < sp.index(5)) or (1 in sp and 10 in sp and sp.index(1) < sp.index(10)):
    print('Arabian number is =>', sum(sp) - 2)
else:
    print('Arabian number is =>', sum(sp))


