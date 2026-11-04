"""Практическая работа №4, Вариант 14"""
import numpy as np
import sys


def array_size():
    """Ввод размеров текущего размера (Создаётся нулевой массив)"""
    try:
        height = int(input('Введите высоту массива: '))
        width = int(input('Введите ширину массива: '))
    except ValueError:
        return 'Размеры должны быть целыми положительными числами'
    if height <= 0 or width <= 0:
        return 'Размеры должны быть целыми положительными числами'
    zero_array = np.zeros((height, width))
    return zero_array


def create_array(new_array):
    """Создание массива с выбираемым вариантов заполнения"""
    global flag
    if isinstance(new_array, str):
        print('Не указаны размеры массива.')
        return new_array
    print('\nВарианты заполнения массива:\n'
          '1 - Вручную\n'
          '2 - Автоматически\n'
          '3 - Назад\n')
    choice_create = input('Введите желаемый вариант заполнения: ')
    if choice_create == '1':
        rows, columns = new_array.shape
        values = []
        try:
            for row in range(rows):
                values_in_row = []
                for column in range(columns):
                    value = int(input(f'{row+1} строка {column+1} столбец: '))
                    values_in_row.append(value)
                values.append(values_in_row)
        except ValueError:
            print('В массиве могут быть только целые числа')
            return new_array
        print('Значения записаны в массив.')
        flag = True
        return np.array(values)
    elif choice_create == '2':
        print('Массив заполнен автоматически.')
        flag = True
        return np.random.randint(0, 101, new_array.shape)
    elif choice_create == '3':
        return new_array
    else:
        print('Неверная команда.')
        return new_array


def print_array(new_array):
    """Вывод текущего массива"""
    print('Текущий массив:')
    max_len = max(len(str(x)) for row in new_array for x in row)
    for row in new_array:
        print(" ".join(f"{x:>{max_len}}" for x in row))


def functions(new_array):
    """Выполнение функция варианта 14"""
    print('\nСписок функций:\n'
          'a - Заменить все элементы, которые меньше 10, числом 42.\n'
          'b - Преобразовать матрицу: поэлементно вычесть последнюю '
          'строку из всех строк, кроме последней.\n'
          'c - Вывести номера тех строк массива, в которых есть хотя бы '
          'один элемент, равный 10.\n'
          'd - Найти столбец с наибольшей суммой элементов.\n'
          'e - Поменять местами элементы матрицы симметрично '
          'побочной диагонали.\n')
    choice_function = input('Выбор функции: ')
    if choice_function == 'a':
        new_array[new_array < 10] = 42
        return new_array
    elif choice_function == 'b':
        new_array[:-1] = new_array[:-1] - new_array[-1]
        return new_array
    elif choice_function == 'c':
        mask = (new_array == 10).any(axis=1)
        row_indices = np.where(mask)[0]
        if len(row_indices) > 0:
            numbers = ', '.join(str(i + 1) for i in row_indices)
            print(f'Найденные строки: {numbers}')
        else:
            print('Указанных строк в массиве нет')
        return new_array
    elif choice_function == 'd':
        column_sums = new_array.sum(axis=0)
        max_sum = column_sums.max()
        max_columns_indices = np.where(column_sums == max_sum)[0]
        max_columns_numbers = max_columns_indices + 1
        print('Номера столбцов с максимальной суммой:',
              ', '.join(str(x) for x in max_columns_numbers),
              '(сумма:', max_sum, ')')
        return new_array
    elif choice_function == 'e':
        if new_array.shape[0] != new_array.shape[1]:
            print('Функция доступна только для квадратных матриц.')
            return new_array
        n = new_array.shape[0]
        for i in range(n):
            for j in range(n - 1 - i):
                new_array[i, j], new_array[n - 1 - j, n - 1 - i] = (
                    new_array[n - 1 - j, n - 1 - i], new_array[i, j])
        return new_array
    else:
        print('Такой функции не существует')
        return new_array


def menu():
    """Меню программы"""
    while True:
        global array, flag
        print('\nВыбор действий:\n'
              '1 - Ввод размера\n'
              '2 - Создание массива\n'
              '3 - Просмотр заданного массива\n'
              '4 - Выполнение функций\n'
              '5 - Выход\n')
        choice = input('Введите действие: ')
        if choice == '1':
            array = array_size()
            if isinstance(array, np.ndarray):
                flag = False
                print('Размеры массивы зафиксированы.')
            else:
                print(array)
        elif choice == '2':
            array = create_array(array)
        elif choice == '3':
            if flag:
                print_array(array)
            else:
                print('Массив не был создан.')
        elif choice == '4':
            if flag:
                array = functions(array)
            else:
                print('Массив не был создан.')
        elif choice == '5':
            sys.exit()
        else:
            print('Неверная команда.')


array = ''
flag = False
menu()
