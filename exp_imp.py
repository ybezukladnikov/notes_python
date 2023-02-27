import json
from pathlib import Path
import datetime

import pymysql


import check
import menu
import view
from config import host, user, password, db_name


def export():
    try:
        connection = pymysql.connect(
            host=host,
            port=3306,
            user=user,
            password=password,
            database=db_name,
            cursorclass=pymysql.cursors.DictCursor,
            charset = 'utf8'
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
                    temp_dict = {}
                    temp_dict = {
                        'Порядковый номер': num+1,
                        'id': row['id'],
                        'Заголовок': row['title_notes'],
                        'Тело заметки': row['body_notes'],
                        'Дата создания' : row['created_at'].strftime("%Y-%m-%d %H:%M:%S"),
                        'Дата последнего изменения' : row['changed_at'].strftime("%Y-%m-%d %H:%M:%S")
                    }
                    # data.append(
                    #     [row['id'],
                    #      num+1,
                    #      row['title_notes'],
                    #      row['body_notes'],
                    #      row['created_at'].strftime("%Y-%m-%d %H:%M:%S"),
                    #      row['changed_at'].strftime("%Y-%m-%d %H:%M:%S")])
                    count = num+1
                    data.append(temp_dict)
                if count == 0:
                    print(f'\033[30m\033[42m\033[4m Нет записей для экспорта. \033[0m')
                else:
                    with open(
                            "export_file.json",
                            'w', encoding="utf-8"
                    ) as f:

                        for chunk in json.JSONEncoder(ensure_ascii=False, indent=4).iterencode(data):
                            f.write(chunk)
                    print(f'\033[30m\033[42m\033[4m Всего экспортировано {count} заметок. \033[0m')

                print("#" * 20)

        finally:
            connection.close()

    except Exception as ex:
        print("Connection refused...")
        print(ex)


def import_file():
    try:
        with open("import_file.json", "r") as read_file:
            data_import = json.load(read_file)

        print("#" * 20)
    except Exception:
        raise RuntimeError("Проблемы с файлом")
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

        try:
            with connection.cursor() as cursor:
                delet_query = f"DELETE FROM notes;"
                cursor.execute(delet_query)
                connection.commit()
                count = 0
                for row in data_import:
                    insert_query = f"INSERT INTO `notes` (title_notes, body_notes) VALUES ('{row['Заголовок']}', '{row['Тело заметки']}');"
                    cursor.execute(insert_query)
                    connection.commit()
                    count+=1
                print(f'\033[30m\033[42m\033[4m Импортировано {count} заметок. \033[0m')

        finally:
            connection.close()

    except Exception as ex:
        print("Connection refused...")
        print(ex)