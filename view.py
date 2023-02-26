from prettytable import PrettyTable

def output_data(data):

    mytable = PrettyTable()
    # имена полей таблицы
    mytable.field_names = ["ID", "Имя заметки", "Краткое содержание заметки", "Дата создания", "Дата последнего изменения"]
    # добавление данных по одной строке за раз
    for row in data:
        mytable.add_row([row[1], row[2], row[3][:20]+"...", row[4], row[5]])

    # вывод таблицы в терминал
    print(mytable)

def view_note(data, num_note):
    array = []
    for row in data:
        if row[1] == num_note:
            array = row

    print(f'\033[30m\033[42m\033[4m Заголовок: \033[0m')
    print(array[2])
    print(f'\033[30m\033[42m\033[4m Содержание заметки: \033[0m')
    print(array[3])


