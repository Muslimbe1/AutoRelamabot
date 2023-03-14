import psycopg2


def add_user(tg_id, full_name, username):
    try:
        connection = psycopg2.connect(
            user="postgres",
            password="Muslim_444",
            host="127.0.0.1",
            port="5432",
            database="Tg_bot"
        )
        cursor = connection.cursor()
        sql = """INSERT INTO Tg_user (tg_id, full_name, username) VALUES (%s, %s, %s)"""
        cursor.execute(sql, (tg_id, full_name, username))
        connection.commit()

        cursor.close()
        connection.close()




    except psycopg2.Error as error:
        print("Error", error)


def create_table():
    try:
        connection = psycopg2.connect(
            user="postgres",
            password="Muslim_444",
            host="127.0.0.1",
            port="5432",
            database="Tg_bot"
        )
        cursor = connection.cursor()
        sql = """CREATE TABLE Tg_user(
        id SERIAL NOT NULL,
        tg_id BIGINT  NOT NULL UNIQUE,
        full_name VARCHAR(100) NOT NULL,
        username VARCHAR(50)
        );"""
        cursor.execute(sql)
        connection.commit()
        print("JAdval yaratildi")
        cursor.close()
        connection.close()




    except psycopg2.Error as error:
        print("Error", error)

# create_table()
