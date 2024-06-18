import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    return conn

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def insert_user(conn, user):
    """ Create a new user """
    sql = ''' INSERT INTO Users(username,email)
              VALUES(?,?) '''
    cur = conn.cursor()
    cur.execute(sql, user)
    conn.commit()
    return cur.lastrowid

def insert_role(conn, role):
    """ Create a new role """
    sql = ''' INSERT INTO Roles(role_name)
              VALUES(?) '''
    cur = conn.cursor()
    cur.execute(sql, role)
    conn.commit()
    return cur.lastrowid

def main():
    database = "my_app.db"

    sql_create_users_table = """ CREATE TABLE IF NOT EXISTS Users (
                                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                                        username TEXT NOT NULL,
                                        email TEXT NOT NULL,
                                        created_at TEXT DEFAULT CURRENT_TIMESTAMP
                                    ); """

    sql_create_roles_table = """CREATE TABLE IF NOT EXISTS Roles (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    role_name TEXT NOT NULL
                                );"""

    sql_create_user_roles_table = """CREATE TABLE IF NOT EXISTS User_Roles (
                                        user_id INTEGER NOT NULL,
                                        role_id INTEGER NOT NULL,
                                        PRIMARY KEY (user_id, role_id),
                                        FOREIGN KEY (user_id) REFERENCES Users (id),
                                        FOREIGN KEY (role_id) REFERENCES Roles (id)
                                    );"""

    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        # create users table
        create_table(conn, sql_create_users_table)

        # create roles table
        create_table(conn, sql_create_roles_table)

        # create user_roles table
        create_table(conn, sql_create_user_roles_table)

        # insert a user
        user = ('testuser', 'testuser@example.com')
        user_id = insert_user(conn, user)

        # insert a role
        role = ('admin',)
        role_id = insert_role(conn, role)

    else:
        print("Error! cannot create the database connection.")

if __name__ == '__main__':
    main()
