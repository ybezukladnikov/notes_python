import CRUD
import menu
import check

def main_func():

    while True:
        menu_item = menu.menu()
        match menu_item:
            case 0:
                break
            case 1: CRUD.show_notes()
            case 2: CRUD.create_note(check.check_new_note())


