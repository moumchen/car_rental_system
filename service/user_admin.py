import sqlite3
from models import *
from utils.decorators import db_connection

def login(username, password):
    users = get_user_by_username(username)
    if len(users) != 0 and users[0].password == password:
        return users[0]
    else:
        return None

@db_connection
def get_user_by_username(cursor, conn, username):
    cursor.execute("select * from user where username = '" + username + "' and deleted_flag = 0")
    rows = cursor.fetchall()
    users = []
    for row in rows:
        user = User(
            id=row[0],
            username=row[1],
            password=row[2],
            role_type=row[3],
            deleted_flag=row[4],
            created_time=row[5],
            deleted_time=row[6],
            updated_time=row[7]
        )
        users.append(user)
    return users

@db_connection
def register(cursor, conn, username, password):
    users = get_user_by_username(username)
    if len(users) != 0:
        return None
    cursor.execute("insert into user(username, password, role_type, deleted_flag) values('" + username + "','" + password + "', 0, 0)")
    return User()

def create_user(cursor, conn, username, password, role_type):
    users = get_user_by_username(username)
    if len(users) != 0:
        return None
    cursor.execute("insert into user(username, password, role_type, deleted_flag) values('" + username + "','" + password + "', " + role_type + ", 0)")
    return users[0]

@db_connection
def delete_user(cursor, conn, username):
    users = get_user_by_username(username)
    if len(users) == 0:
        return None
    cursor.execute("update user set deleted_flag = 1 where username = '" + username + "'")
    return users[0]

@db_connection
def update_user(cursor, conn, username, password, role_type):
    users = get_user_by_username(username)
    if len(users) == 0:
        return None
    # password or role_type may be empty, do not update
    if password == "" and role_type == "":
        return None
    sql = "update user set update_time = datetime('now') "
    if password != "":
        sql += ",password = '" + password + "' "
    if role_type != "":
        sql += ",role_type = " + role_type + " "
    sql += "where username = '" + username + "'"
    cursor.execute(sql)
    return users[0]

@db_connection
def query_user(cursor, conn, username, role_type):
    sql = "select * from user where deleted_flag = 0 "
    if username != "":
        sql += "and username = '" + username + "' "
    if role_type != "":
        sql += "and role_type = " + role_type + " "
    cursor.execute(sql)
    rows = cursor.fetchall()
    users = []
    for row in rows:
        user = User(
            id=row[0],
            username=row[1],
            password=row[2],
            role_type=row[3],
            deleted_flag=row[4],
            created_time=row[5],
            deleted_time=row[6],
            updated_time=row[7]
        )
        users.append(user)
    return users
