import numpy as np

def array_size():
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
    if isinstance(new_array, str):
        print('Не указаны размеры массива.')
        return new_array
    print('\nВарианты заполнения массива:\n'
          '1 - Вручную\n'
          '2 - Автоматически\n'
          '3 - Назад\n')
    choice_create = int(input('Введите желаемый вариант заполнения: '))
    if choice_create == 1:
        rows, columns = new_array.shape
        values = []
        for row in range(rows):
            values_in_row = []
            for column in range(columns):
                value = int(input(f'{row+1} строка {column+1} столбец: '))
                values_in_row.append(value)
            values.append(values_in_row)
        return np.array(values)
    if choice_create == 2:
        return np.random.randint(0, 101, new_array.shape)
    if choice_create == 3:
        return new_array
    else:
        print(f'Выполнение функции {choice_create}')


def menu():
    while True:
        print('\nВыбор действий:\n'
              '1 - Ввод размера\n'
              '2 - Создание массива\n'
              '3 - Просмотр заданного массива\n'
              '4 - Выполнение функций\n'
              '5 - Выход\n')
        choice = int(input('Введите действие: '))
        if choice == 1:
            array = array_size()
            if isinstance(array, np.ndarray):
                print('Размеры массивы зафиксированы.')
            else:
                print(array)
        elif choice == 2:
            array = create_array(array)
        elif choice == 3:
            print(f'Выполнение функции {choice}')
        elif choice == 4:
            print(f'Выполнение функции {choice}')
        elif choice == 5:
            print(f'Выполнение функции {choice}')
        else:
            print('Ошибка')

array = ''
menu()