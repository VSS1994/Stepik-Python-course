a = list(input().split())
b = input()
if b not in a:
    print('Отсутствует')
for i in range(len(a)):
    if a[i] == b:
        print(i, '', end='')

# Напишите программу, которая считывает список чисел lstlst из первой строки и число xx из второй строки, которая
# выводит все позиции, на которых встречается число xx в переданном списке lstlst.
# Позиции нумеруются с нуля, если число xx не встречается в списке, вывести строку "Отсутствует"
# (без кавычек, с большой буквы).
# Позиции должны быть выведены в одну строку, по возрастанию абсолютного значения.