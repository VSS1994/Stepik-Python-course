a = int(input())
b = int(input())
c = 1
while c:
    if c % a == 0 and c % b == 0:
        print(c)
        break
    else:
        c += 1

# В Институте биоинформатики между информатиками и биологами устраивается соревнование. Победителям соревнования
# достанется большой и вкусный пирог. В команде биологов aa человек, а в команде информатиков — bb человек.
# Нужно заранее разрезать пирог таким образом, чтобы можно было раздать кусочки пирога любой команде, выигравшей
# соревнование, при этом каждому участнику этой команды должно достаться одинаковое число кусочков пирога. И так как не
# хочется резать пирог на слишком мелкие кусочки, нужно найти минимальное подходящее число.
# Напишите программу, которая помогает найти это число.
# Программа должна считывать размеры команд (два положительных целых числа aa и bb, каждое число вводится на отдельной
# строке) и выводить наименьшее число dd, которое делится на оба этих числа без остатка.