account = 0  # счет
history = {}

while True:
    print(f'На вашем счете: {account} руб.')
    print('1. пополнение счета')
    print('2. покупка')
    print('3. история покупок')
    print('4. выход')

    choice = input('Выберите пункт меню: ')
    if choice == '1':
        quantity = int(input('\nВведите сумму для пополнения счета '))
        account += quantity

    elif choice == '2':
        purchase = int(input('\nВведите сумму покупки: '))
        if purchase > account:
            print('Недостаточно средств')
        else:
            account -= purchase
            history[input('Введите название товара: ')] = purchase

    elif choice == '3':
        if len(history) > 0:
            print('\nИстория покупок:')
            for key, val in history.items():
                print(f'{key} --> {val} р.')
        else:
            print('\nСписок покупок пока пуст!')
    elif choice == '4':
        break
    else:
        print('Неверный пункт меню')