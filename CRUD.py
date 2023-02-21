import pymysql

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
                    data.append([row['id'], num+1, row['title_notes'],row['body_notes'][:20]+"...", row['created_at'], row['changed_at']])
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




