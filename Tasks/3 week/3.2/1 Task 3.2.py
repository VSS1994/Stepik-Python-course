def update_dictionary(d, key, value):
    if key in d.keys():
        d[key] += [value]
    elif key not in d.keys():
        a = key * 2
        if a in d.keys():
            d[a] += [value]
        elif a not in d.keys():
            d[a] = [value]

# Напишите функцию update_dictionary(d, key, value), которая принимает на вход словарь dd и два числа: keykey и
# valuevalue.
# Если ключ keykey есть в словаре dd, то добавьте значение valuevalue в список, который хранится по этому ключу.
# Если ключа keykey нет в словаре, то нужно добавить значение в список по ключу 2 * key2∗key. Если и ключа 2 * key2∗key
# нет, то нужно добавить ключ 2 * key2∗key в словарь и сопоставить ему список из переданного элемента [value][value].
# Требуется реализовать только эту функцию, кода вне её не должно быть.
# Функция не должна вызывать внутри себя функции input и print.