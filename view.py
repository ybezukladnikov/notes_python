from prettytable import PrettyTable

def output_data(data):

    mytable = PrettyTable()
    # имена полей таблицы
    mytable.field_names = ["ID", "Имя заметки", "Краткое содержание заметки", "Дата создания", "Дата последнего изменения"]
    # добавление данных по одной строке за раз
    for row in data:
        mytable.add_row([row[1], row[2], row[3], row[4], row[5]])

    # вывод таблицы в терминал
    print(mytable)