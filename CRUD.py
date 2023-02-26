import datetime

import pymysql

import check
import menu
import view
from config import host, user, password, db_name


def show_notes():
    try:
        connection = pymysql.connect(
            host=host,
            port=3306,
            user=user,
            password=password,
            database=db_name,
            cursorclass=pymysql.cursors.DictCursor
        )
        print("successfully connected...")
        print("#" * 20)
        data =[]
        try:
            with connection.cursor() as cursor:
                select_all_rows = "SELECT * FROM `notes` WHERE is_deleted = 0 "
                cursor.execute(select_all_rows)
                count = 0
                rows = cursor.fetchall()
                for num, row in enumerate(rows):
                    data.append([row['id'], num+1, row['title_notes'],row['body_notes'], row['created_at'], row['changed_at']])
                    count = num+1
                view.output_data(data)
                print(f'\033[30m\033[42m\033[4m Всего {count} заметок. \033[0m')

                print("#" * 20)

        finally:
            connection.close()

    except Exception as ex:
        print("Connection refused...")
        print(ex)

def create_note(note):
    try:
        connection = pymysql.connect(
            host=host,
            port=3306,
            user=user,
            password=password,
            database=db_name,
            cursorclass=pymysql.cursors.DictCursor
        )
        print("successfully connected...")
        print("#" * 20)
        title = note[0]
        body = note[1]
        try:
            with connection.cursor() as cursor:
                insert_query = f"INSERT INTO `notes` (title_notes, body_notes) VALUES ('{title}', '{body}');"
                cursor.execute(insert_query)
                connection.commit()
                print(f'\033[30m\033[42m\033[4m Заметка успешно создана \033[0m')

        finally:
            connection.close()

    except Exception as ex:
        print("Connection refused...")
        print(ex)


def view_ch_del():
    try:
        connection = pymysql.connect(
            host=host,
            port=3306,
            user=user,
            password=password,
            database=db_name,
            cursorclass=pymysql.cursors.DictCursor
        )
        print("successfully connected...")
        print("#" * 20)
        data =[]
        try:
            with connection.cursor() as cursor:
                select_all_rows = "SELECT * FROM `notes` WHERE is_deleted = 0 "
                cursor.execute(select_all_rows)
                count = 0
                rows = cursor.fetchall()
                for num, row in enumerate(rows):
                    data.append([row['id'], num+1, row['title_notes'],row['body_notes'], row['created_at'], row['changed_at']])
                    count = num+1
                view.output_data(data)
                print(f'\033[30m\033[42m\033[4m Всего {count} заметок. \033[0m')

                print("#" * 20)
                while True:
                    sub_menu_item = menu.sub_menu()
                    match sub_menu_item:
                        case 0:
                            break
                        case 1:
                            item_note = check.check_num_note()
                            view.view_note(data,item_note)
                            break
                        case 2:
                            item_note = check.check_num_note()
                            id_note = -1
                            for row in data:
                                if row[1] == item_note:
                                    id_note = row[0]
                            if  id_note == -1:
                                print("Такой заметки нет в списке")
                                break
                            data_ch = datetime.datetime.now()
                            ch_note = check.check_ch_note()
                            update_query = f"UPDATE `notes` SET title_notes = '{ch_note[0]}' WHERE id = '{id_note}';"
                            cursor.execute(update_query)
                            update_query = f"UPDATE `notes` SET body_notes = '{ch_note[1]}' WHERE id = '{id_note}';"
                            cursor.execute(update_query)
                            update_query = f"UPDATE `notes` SET changed_at = '{data_ch}' WHERE id = '{id_note}';"
                            cursor.execute(update_query)
                            connection.commit()
                            break
                        case 3:
                            item_note = check.check_num_note()
                            id_note = -1
                            for row in data:
                                if row[1] == item_note:
                                    id_note = row[0]
                            if id_note == -1:
                                print("Такой заметки нет в списке")
                                break
                            update_query = f"UPDATE `notes` SET is_deleted = '1' WHERE id = '{id_note}';"
                            cursor.execute(update_query)
                            connection.commit()
                            break


        finally:
            connection.close()

    except Exception as ex:
        print("Connection refused...")
        print(ex)



