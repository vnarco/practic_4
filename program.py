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
            print(f'Выполнение функции {choice}')
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