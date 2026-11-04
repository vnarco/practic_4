import sys


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
            print(f'Выполнение функции {choice}')
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
menu()