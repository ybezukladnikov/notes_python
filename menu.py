import check


def menu():
    MENU_ITEMS = {
        1: "Показать все заметки",
        2: "Создать заметку",
        0: "Выход"

    }

    print('Приложение Заметки')
    for operNum, operDesc in MENU_ITEMS.items():
        print(f"{operNum}. {operDesc}")

    return check.check_main_menu()








