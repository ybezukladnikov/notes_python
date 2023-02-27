import check


def menu():
    MENU_ITEMS = {
        1: "Показать все заметки",
        2: "Создать заметку",
        3: "Просмотреть/Изменить/Удалить",
        4: "Экспорт в файл (json)",
        0: "Выход"

    }

    print('Приложение Заметки')
    for operNum, operDesc in MENU_ITEMS.items():
        print(f"{operNum}. {operDesc}")

    return check.check_main_menu()

def sub_menu():
    MENU_ITEMS = {
        1: "Просмотр заметки",
        2: "Изменить заметку",
        3: "Удалить заметку",
        0: "Выход в основное меню"


    }

    print('Действия с заметкой')
    for operNum, operDesc in MENU_ITEMS.items():
        print(f"{operNum}. {operDesc}")

    return check.check_sub_menu()








