print('Консольный файловый менеджер: ')
import os
import shutil
import sys
from famous_persons import get_person_and_question
import pickle

FILE_NAME_LISTDIR = 'listdir.txt'
file_name = []
dir_name = []

while True:
    print('1. создать папку')
    print('2. удалить файл/папку')
    print('3. копировать файл/папку')
    print('4. просмотр содержимого рабочей директории')
    print('5. посмотреть только папки')
    print('6. посмотреть только файлы')
    print('7. просмотр информации об операционной системе')
    print('8. создатель программы')
    print('9. играть в викторину')
    print('10. мой банковский счет')
    print('11. смена рабочей директории')
    print('12. сохранить содержимое рабочей директории в файл')
    print('13. выход')

    choice = input('Выберите пункт меню: ')
    if choice == '1':
        name_folder = input('Введите название папки: ')
        # проверка на существование
        if not os.path.exists(name_folder):
            os.mkdir(name_folder)
            print(f'Папка {name_folder} создана')
        else:
            print(f'Папка с именем {name_folder} уже существует')

    elif choice == '2':
        delete_folder = input('Введите название файла/папки, который(ую) необходимо удалить:  ')
        os.rmdir(delete_folder)
        print(f'Папка {delete_folder} удалена')

    elif choice == '3':
        copy_folder = input('Введите название файла/папки, который(ую) необходимо копировать:  ')
        new_folder = input('Введите новое название файла/папки:  ')
        if os.path.exists(copy_folder) and not os.path.exists(new_folder):
            shutil.copy(copy_folder, new_folder)

    elif choice == '4':
        print('Текущая директория: ', os.getcwd())

    elif choice == '5': # посмотреть папки
        dirs_view = [d for d in os.listdir('.') if os.path.isdir(d)]
        print(dirs_view)

    elif choice == '6': # посмотреть файлы
        files_view = [f for f in os.listdir('.') if os.path.isfile(f)]
        print(files_view)

    elif choice == '7':
        print('My OS is', sys.platform, '(', os.name, ')')

    elif choice == '8':
        print('Программу создала: Туз Любовь')

    elif choice == '9':
        rounds = int(input('Сколько раз вы хотите играть?'))

        for i in range(rounds):
            get_person_and_question()

        print('Пока!')
    elif choice == '10':
        import shop

    elif choice == '11':
        print(f'Вы находитесь {os.getcwd()}')
        new_directory = input('введите название рабочей папки: ')
        os.mkdir(new_directory)
        path = os.path.join(os.getcwd(), new_directory)
        os.chdir(path)
        print(f'А теперь вы находитесь {os.getcwd()}')

    elif choice == '12':
        content = os.listdir()
        for direct in content:
            if os.path.isdir(direct):
                dir_name.append(direct)
            if os.path.isfile(direct):
                file_name.append(direct)
        with open(FILE_NAME_LISTDIR, 'wb') as f:
            pickle.dump(dir_name, f)
            pickle.dump(file_name, f)

    elif choice == '13':
        break
    else:
        print('Неверный пункт меню')


''' ЗАДАНИЕ 2
5. В программе консольный файловый менеджер есть пункт "просмотр содержимого рабочей директории";
6. Добавить пункт "сохранить содержимое рабочей директории в файл";
 
7. При выборе этого пункта создать файл listdir.txt (если он есть то пересоздать) и сохранить туда содержимое рабочей директории следующим образом: сначала все файлы, потом все папки, пример как может выглядеть итоговый файл.
 
 
files: victory.py, bill.py, main.py
dirs: modules, packages'''