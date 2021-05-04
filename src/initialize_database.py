from database_connection import get_database_connection
from services.tracker_service import tracker_service


def drop_tables(connection):
    cursor = connection.cursor()

    cursor.execute(''' drop table if exists users ''')

    connection.commit()


def create_tables(connection):
    cursor = connection.cursor()

    cursor.execute(''' create table users (username text primary key, password text);''')


    connection.commit()


def initialize_database():
    connection = get_database_connection()

    drop_tables(connection)
    tracker_service.delete_courses()
    tracker_service.delete_notes()
    create_tables(connection)

if __name__ == "__main__":
    initialize_database()
