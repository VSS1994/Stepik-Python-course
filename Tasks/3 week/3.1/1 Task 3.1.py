def f(x):
    if x <= - 2:
        a = 1 - (x + 2) * (x + 2)
    elif -2 < x and x <= 2:
        a = - x/2
    elif x > 2:
        a = (x - 2) * (x - 2) + 1
    return a

# Напишите функцию f(x), которая возвращает значение следующей функции, определённой на всей числовой прямой/
