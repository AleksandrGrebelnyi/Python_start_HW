# Напишите программу для очистки текста от html-тэгов. Больше о html-
# тэгах https://html5book.ru/html-tags/
# Также необходимо учесть пару особенностей:
# - помимо одинарных тэгов, есть парные тэги, например <div> </div>, т.е.
# первый тэг открывающий , а второй закрывающий.
# - тэг внутри себя, может содержать кучу доп. информации.
# Например <div id="rcnt" style="clear:both;position:relative;zoom:1">

html_text = '<p>5 < 4</p> Hi<div id="rcnt" style="clear:both;position:relative;zoom:1">'
tag_del = ['p', 'a', 'h1', 'div']
for tag in tag_del:
    while f'<{tag}' in html_text:
        start = html_text.find(f'<{tag}')
        stop = html_text.find(f'>', start + 1)
        html_text = html_text.replace(html_text[start: stop + 1], '')
        html_text = html_text.replace(f'</{tag}>', '')

print(html_text)


import bleach

tag_text = '<p>5 < 4</p> Hi<div id="rcnt" style="clear:both;position:relative;zoom:1">'
print(bleach.clean(tag_text, tags=[], strip=True))


# tag_text = '<p>Hello, <b>World</b></p> Hi<div id="rcnt" style="clear:both;position:relative;zoom:1">'
tag_text = '<p>5 < 4</p> Hi<div id="rcnt" style="clear:both;position:relative;zoom:1">'
while '>' in tag_text:
    x1, x2 = tag_text.find('<'), tag_text.find('>')
    tag_text = tag_text.replace(tag_text[x1:x2 + 1], '')
print(tag_text)



