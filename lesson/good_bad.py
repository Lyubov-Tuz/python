import sys


def author_info():
    return 'Author Leo'


def get_number():
    number = input('Введите число')
    return int(number) ** 2


if __name__ == '__main__':
    while True:
        print('0. Выход')
        print('1. Info')

        choise = input('Выберите пункт меню')
        if choise == '0':
            sys.exit(0)
        elif choise == '1':
            print(author_info())
        else:
            print('неверный пункт меню')
