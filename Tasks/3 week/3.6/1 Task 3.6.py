import requests
with open('dataset_3378_2 (6).txt', 'r') as file:
    link = file.readline().strip()
    reading = requests.get(link).text
    lines = reading.splitlines()
    print(len(lines))

'''
Скачайте файл. В нём указан адрес другого файла, который нужно скачать с использованием модуля requests и посчитать 
число строк в нём.
Используйте функцию get для получения файла (имеет смысл вызвать метод strip к передаваемому параметру, чтобы убрать 
пробельные символы по краям).
После получения файла вы можете проверить результат, обратившись к полю text. Если результат работы скрипта не 
принимается, проверьте поле url на правильность. Для подсчёта количества строк разбейте текст с помощью метода 
splitlines.
В поле ответа введите одно число или отправьте файл, содержащий одно число.
'''