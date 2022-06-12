#  Напишите функцию, которая вернет количество слов в строке текста

def how_many_words(stroka):
    return len(stroka.split())


s = 'Hello my friend, I am learning Python'
print(how_many_words(s))