# Module Imports
import mariadb
import sys

# Connect to MariaDB Platform
def connect():
    try:
        conn = mariadb.connect(
            user="friendsdb",
            password="1234",
            host="127.0.0.1",
            port=3306,
            database="friends"

        )
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)
    return conn

# Get Cursor
def get_cursor():
    conn = connect()
    return conn.cursor()

def add_user(name, user_name, e_mail, phone, gender, password, friends, date_of_birth):
    cursor = get_cursor()
    cursor.execute(f"INSERT INTO friends.`user`(name, user_name, e_mail, phone, gender, password, friends, date_of_birth) VALUES ('{name}', '{user_name}', '{e_mail}', {phone}, '{gender}', '{password}', '{friends}', '{date_of_birth}');")
    cursor.execute("COMMIT;")

def get_user(value, field, select='*'):
    cursor = get_cursor()
    cursor.execute(f"SELECT {select} FROM friends.`user` WHERE {field} = '{value}';")
    return cursor.fetchall()

def change_user():
    pass
#add_user("John Doe", "John", "john@nowhere.com", 123456789, "M", "test12345", "1,23,45,67,89,100", "2020-03-01")
