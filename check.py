def check_main_menu():
    while True:
        try:
            num = int(input('Введите номер пункта, который хотите выполнить: '))
            if 0<=num<=6:break
            else:
                print('Такого пункта меню нет!')
                print("\033[31m {}\033[0m".format('Такого пункта меню нет! Попробуйте снова.'))
                continue
        except ValueError:
            print("\033[31m {}\033[0m" .format('Вы ввели некорректное число! Попробуйте снова.'))


    return num

def check_sub_menu():
    while True:
        try:
            num = int(input('Введите номер пункта, который хотите выполнить: '))
            if 0<=num<=3:break
            else:
                print('Такого пункта меню нет!')
                print("\033[31m {}\033[0m".format('Такого пункта меню нет! Попробуйте снова.'))
                continue
        except ValueError:
            print("\033[31m {}\033[0m" .format('Вы ввели некорректное число! Попробуйте снова.'))


    return num

def check_new_note():
    note =[]
    while True:
        title = input('Введите заголовок заметки (не должен быть пустым): ')
        if len(title) > 0 : break
        else:
            print("\033[31m {}\033[0m".format('Вы ввели пустой заголовок.'))
            continue
    note.append(title)
    while True:
        body = input('Введите содержание заметки (не должен быть пустым): ')
        if len(body) > 0 : break
        else:
            print("\033[31m {}\033[0m".format('Вы ввели пустой заголовок.'))
            continue

    note.append(body)
    return note

def check_ch_note():
    note =[]
    while True:
        title = input('Введите новый заголовок заметки (не должен быть пустым): ')
        if len(title) > 0 : break
        else:
            print("\033[31m {}\033[0m".format('Вы ввели пустой заголовок.'))
            continue
    note.append(title)
    while True:
        body = input('Введите новое содержание заметки (не должен быть пустым): ')
        if len(body) > 0 : break
        else:
            print("\033[31m {}\033[0m".format('Вы ввели пустой заголовок.'))
            continue

    note.append(body)
    return note

def check_num_note():
    while True:
        try:
            num = int(input('Введите id заметки: '))
            if 1<=num<=100:break
            else:
                print("\033[31m {}\033[0m".format('Такой заметки нет! Попробуйте снова.'))
                continue
        except ValueError:
            print("\033[31m {}\033[0m" .format('Вы ввели некорректное число! Попробуйте снова.'))


    return num