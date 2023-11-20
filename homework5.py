# Dmitry Atroshchenko
# Description: Homework 5
# Date: 19/11/2023
# My version Python 3.11


# Реализовать функцию get_ranges которая получает на вход непустой список неповторяющихся целых чисел,
# отсортированных по возрастанию, которая этот список “сворачивает”.
# get_ranges([0, 1, 2, 3, 4, 7, 8, 10])  #  "0-4, 7-8, 10"
# get_ranges([4,7,10])  # "4, 7, 10"
# get_ranges([2, 3, 8, 9])  # "2-3, 8-9"


def get_ranges(input_list):
    # Проверяем, пуст ли входной список
    if not input_list:
        return ""

    # Инициализируем пустой список для хранения конечных диапазонов
    final_ranges = []

    # Инициализируем переменные для отслеживания начала и конца диапазона
    start_range = end_range = input_list[0]

    # Итерируем по входному списку
    for num in input_list[1:]:
        # Проверяем, является ли текущее число последовательным концу текущего диапазона
        if num == end_range + 1:
            end_range = num
        else:
            # Если не последовательно, проверяем, совпадают ли начало и конец диапазона
            if start_range == end_range:
                # Если диапазон состоит из одного числа, добавляем его в список final_ranges
                final_ranges.append(str(start_range))
            else:
                # Если в диапазоне больше одного числа, добавляем его в формате "начало-конец" в список final_ranges
                final_ranges.append(f"{start_range}-{end_range}")
            # Сбрасываем начало и конец диапазона до текущего числа
            start_range = end_range = num

    # После цикла проверяем последний диапазон
    if start_range == end_range:
        final_ranges.append(str(start_range))
    else:
        final_ranges.append(f"{start_range}-{end_range}")

    # Объединяем список final_ranges в строку с разделителями запятая и пробел
    return ', '.join(final_ranges)


# Напсать функцию standardise_phones которая принимает любое
# количество нестандартизированных телефонных номеров и возвращает
# список стандартизированных номеров в том порядке в котором они были
# введены. А если число не является номером - возвращает пустой список
# standardise_phones("298884455") # ["+375298884455"]
# standardise_phones("(29)888-44-55","8029 8885555","+375299998877","375299998867") # ["+375298884455","+375298885555","+375299998877","+375299998867"]
# standardise_phones("298884asd45") # []


import re


def standardise_phones(*args):
    standardised_numbers = []

    for number in args:
        # Если аргумент - целое число, преобразуем его в строку
        if isinstance(number, int):
            number = str(number)

        # Удаляем все символы, кроме цифр
        number = re.sub(r'\D', '', number)

        # Проверяем, является ли номер числовой строкой
        if not number.isdigit():
            return []

        # Проверяем, достаточно ли цифр в номере
        if len(number) < 9:
            return []

        # Убираем код "80", если он есть
        if number.startswith('80'):
            number = number.replace("80", "")

        # Добавляем префикс "+375", если его нет
        if not number.startswith('375'):
            number = '375' + number

        # Добавляем знак "+" в начало номера
        if not number.startswith('+'):
            number = '+' + number

        standardised_numbers.append(number)

    return standardised_numbers


# Создайте функцию rope_product, которая берёт позитивный цельный номер,
# который представляет собой длину верёвки. Длина этой
# верёвки может быть разделена на любое количество более
# малых цельных чисел. Верните максимальный продукт умножения
# малых цельных чисел. Решение не должно пользоваться циклами!
# rope_product(1) -> 1
# rope_product(4) -> 4
# rope_product(5) -> 6
# rope_product(6) -> 9
# rope_product(7) -> 12
# rope_product(11) -> 54


def dec(rope_product):
    def wrapper(*args, **kwargs):
        if len(args) == 1:
            # Если передано только одно значение, возвращаем результат как обычно
            return rope_product(*args, **kwargs)
        else:
            # Если передано несколько значений, возвращаем результаты в виде списка
            return [rope_product(arg, **kwargs) for arg in args]

    return wrapper


@dec
def rope_product(n):
    if n <= 4:
        return n

    # Инициализация массива для хранения максимальных произведений
    max_products = [0] * (n + 1)
    max_products[1] = 1
    max_products[2] = 2
    max_products[3] = 3
    max_products[4] = 4

    # Заполняем массив максимальных произведений
    for i in range(5, n + 1):
        max_val = 0
        for j in range(1, i // 2 + 1):
            product = max_products[j] * max_products[i - j]
            if product > max_val:
                max_val = product
        max_products[i] = max_val

    return max_products[n]


# Создайте декоратор который позволит функции rope_product
# вернуть лиш один ответ если задано одно число и много ответов списком если
# введённых значений будет несколько! И добавьте его к функции rope_product
# не меняя решения из предыдущего решения!
# rope_product(8) -> 18
# rope_product(7,11,23,45,32) -> [12, 54, 4374, 14348907, 118098]
# здесь можно пользоваться циклами