import pymysql
from config import host, user, password, db_name

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
        # create table
        with connection.cursor() as cursor:
            create_table_query = "CREATE TABLE `notes`(id int AUTO_INCREMENT," \
                                 " title_notes varchar(32) NOT NULL," \
                                 " body_notes TEXT NOT NULL," \
                                 " created_at DATETIME DEFAULT NOW()," \
                                 " changed_at DATETIME DEFAULT NOW()," \
                                 " is_deleted BIT DEFAULT 0, PRIMARY KEY (id));"
            cursor.execute(create_table_query)
            print("Table created successfully")
    finally:
        connection.close()


except Exception as ex:
    print("Connection refused...")
    print(ex)