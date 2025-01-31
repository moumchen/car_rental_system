import threading
from config import  *
import os, platform
from utils import db_conn_manager

# use db_conn_manager to manage db connection
db_conn_manager = db_conn_manager.DBConnectionManager(DB_URL, POOL_SIZE)

thread_local = threading.local()
if (not hasattr(thread_local, "LANGUAGE")):
    thread_local.LANGUAGE = "en"  # default language is English
language = thread_local.LANGUAGE
if language == "jp":
    from languages.language_jp import *
elif language == "zh":
    from languages.language_zh import *
else:
    from languages.language_en import *

def new_page(func):
    """
        It is a decorator to print system logo and clean information on screen
    :return: wrapper
    """
    def wrapper(*args, **kwargs):
        # judge what the current system is, and execute different command to clear info
        current_os = platform.system()
        if current_os == "Windows":
            os.system('cls')  # Windows 系统使用 cls
        else:
            os.system('clear')  # Linux 和 macOS 系统使用 clear

        print(MAIN_PAGE_MESSAGES["system_logo"])
        return func(*args, **kwargs)

    return wrapper


def db_connection(func):
    """
        It is a decorator to connect to the database
    :return: wrapper
    """
    def wrapper(*args, **kwargs):
        cursor, conn = db_conn_manager.get_cursor();
        result = func(cursor, conn, *args, **kwargs)
        conn.commit()
        cursor.close()
        db_conn_manager.release_connection(conn)
        return result

    return wrapper

