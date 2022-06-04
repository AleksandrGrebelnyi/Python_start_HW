# Используя словарь, напишите программу, которая выведет на экран название дня
# недели по его номеру. (1 - «Monday»)

create_week = {
    1: 'Monday',
    2: 'Tuesday',
    3: 'Wednesday',
    4: 'Tuesday',
    5: 'Friday',
    6: 'Saturday',
    7: 'Sunday',
}
print(create_week.get(5))