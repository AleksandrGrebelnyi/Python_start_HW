# Выведите на экран все числа в диапазоне от 1 до 100 кратные 7

for i in range(1, 100):
    if not i % 7:  # put 'not' instead of '== 0'
        print(i, end=' ')


