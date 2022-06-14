#  Напишите функцию, которая вернет количество слов в строке текста

def how_many_words(stroka):
    return len(stroka.split())


s = 'Hello my friend, I am learning Python'
print(how_many_words(s))


# new solution
def words(text: str):
    return text.count(' ') + 1

text = 'Hello my friend, I am learning Python'
print(words(text))