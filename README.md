#### Dmitry Atroshchenko
#### Description: Homework 5
#### Date: 20/11/2023
#### My version Python 3.11



# 1. Функция get_ranges
Функция `get_ranges` принимает на вход непустой список уникальных целых чисел `input_list`, отсортированных по возрастанию, и "сворачивает" этот список в строку, представляя диапазоны последовательных целых чисел.
### Применение
#### python
```
get_ranges([0, 1, 2, 3, 4, 7, 8, 10])  # Вывод: "0-4, 7-8, 10"
get_ranges([4, 7, 10])                # Вывод: "4, 7, 10"
get_ranges([2, 3, 8, 9])               # Вывод: "2-3, 8-9"
```

### Описание функции
#### Входные данные
- `input_list`: Непустой список уникальных целых чисел, отсортированных по возрастанию.
#### Вывод
- Возвращает строку, представляющую свернутые диапазоны последовательных целых чисел, разделенные запятыми и пробелами.
#### Алгоритм
1. Инициализация пустого списка (`final_ranges`) для хранения окончательных свернутых диапазонов.
2. Инициализация переменных (`start_range` и `end_range`) для отслеживания начала и конца диапазона.
3. Итерация по входному списку.
-Если текущее число последовательно концу текущего диапазона, обновляем `end_range`.\
-Если не последовательно, проверяем, равны ли `start_range` и `end_range`.\
-Если равны, добавляем одно число в `final_ranges`.\
-Если не равны, добавляем диапазон в формате "start_range-end_range" в `final_ranges`.\
-Сброс `start_range` и `end_range` до текущего числа.
4. После завершения цикла проверяем последний диапазон и добавляем его в `final_ranges`.
5. Объединение списка `final_ranges` в строку с разделителями запятая и пробелом.
### Пример
#### python
```
result = get_ranges([0, 1, 2, 3, 4, 7, 8, 10])
print(result)  # Вывод: "0-4, 7-8, 10"
```
**Примечание**: Если входной список пуст, функция возвращает пустую строку. Данный код эффективно сворачивает последовательные целые числа в диапазоны и предоставляет удобное представление для таких последовательностей.  


# 1. Функция standardise_phones
Функция `standardise_phones` принимает любое количество нестандартизированных телефонных номеров и возвращает список стандартизированных номеров в том порядке, в котором они были введены. Если число не является номером, функция возвращает пустой список.
### Применение
#### python
```
standardise_phones("298884455")                               # Вывод: ["+375298884455"]
standardise_phones("(29)888-44-55", "8029 8885555", "+375299998877", "375299998867")  # Вывод: ["+375298884455", "+375298885555", "+375299998877", "+375299998867"]
standardise_phones("298884asd45")                             # Вывод: []
```

### Описание функции
#### Входные данные
- `*args`: Любое количество нестандартизированных телефонных номеров.
#### Вывод
- Возвращает список стандартизированных номеров в том порядке, в котором они были введены.
#### Алгоритм
1. Инициализация пустого списка (`standardised_numbers`) для хранения стандартизированных номеров.
2. Итерация по аргументам функции.  
-Если аргумент - целое число, преобразовать его в строку.\
-Удалить все символы, кроме цифр, из строки номера.\
-Проверить, является ли строка числовой строкой.\
-Проверить, достаточно ли цифр в номере (больше или равно 9).\
-Убрать код "80", если он есть.\
-Добавить префикс "+375", если его нет.\
-Добавить знак "+" в начало номера.\
-Добавить стандартизированный номер в список `standardised_numbers`.  
3. Вернуть список `standardised_numbers`.
### Пример
#### python
```
result = standardise_phones("(29)888-44-55", "8029 8885555", "+375299998877", "375299998867")
print(result)  # Вывод: ["+375298884455", "+375298885555", "+375299998877", "+375299998867"]
```
**Примечание**: Если входной аргумент не является числом или не соответствует требованиям номера телефона, функция возвращает пустой список.
