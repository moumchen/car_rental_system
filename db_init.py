"""
    This py file is to initialize tables and data or reset the whole system:
    1. if table exists, it will remove the table and create a new table
    2. add default admin user data
"""
import sqlite3

if __name__ == '__main__':
    conn = sqlite3.connect("db/car_rental_system.db")
    cursor = conn.cursor()

    with open("car_rental_system.sql", "r") as f:
        sql_script = f.read()

    cursor.executescript(sql_script)

    conn.commit()
    conn.close()

