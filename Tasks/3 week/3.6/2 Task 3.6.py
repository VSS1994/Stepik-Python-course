import requests
link = 'https://stepic.org/media/attachments/course67/3.6.3/'
with open('dataset_3378_3.txt') as file:
    nxt_file = file.readline().strip()
a = requests.get(nxt_file)
a = link + a.text
flag = True
while(flag):
    a = requests.get(a)
    if (a.text.count('.txt')):
        a = link + a.text
    else:
        flag = False
        print(a.text)

'''
Имеется набор файлов, каждый из которых, кроме последнего, содержит имя следующего файла.
Первое слово в тексте последнего файла: "We".
Скачайте предложенный файл. В нём содержится ссылка на первый файл из этого набора.
Все файлы располагаются в каталоге по адресу:
https://stepic.org/media/attachments/course67/3.6.3/
Загрузите содержимое ﻿последнего файла из набора, как ответ на это задание.
'''
