import sqlite3
from models import Car
from utils import db_conn_manager
from utils.decorators import db_connection
import config

# use db_conn_manager to manage db connection
db_manager = db_conn_manager.DBConnectionManager(config.DB_URL, config.POOL_SIZE)

@db_connection
def create_car(cursor, conn, make, model, year, mileage, daily_rent, extra_fee, min_lease_limit, max_lease_limit):
    cursor.execute("insert into car(make, model, manufactured_year, mileage, daily_rent, extra_fee, min_lease_limit, max_lease_limit) values('" + make + "','" + model + "','" + year + "','" + mileage  + "','" + daily_rent + "','" + extra_fee + "','" + min_lease_limit + "','" + max_lease_limit + "')")
    conn.commit()
    return True

@db_connection
def get_car_by_id(cursor, conn, id):
    cursor.execute("select * from car where id = " + id)
    car = cursor.fetchone()
    cursor.close()
    if car == None:
        return None
    car = Car(id=car[0], make=car[1], model=car[2], manufactured_year=car[3], mileage=car[4], daily_rent=car[5], extra_fee=car[6], min_lease_limit=car[7], max_lease_limit=car[8])
    return car

@db_connection
def delete_car(cursor, conn, id):
    car = get_car_by_id(id)
    if car == None:
        return False

    cursor.execute("delete from car where id = " + id)
    conn.commit()
    cursor.close()
    return True

@db_connection
def update_car(cursor, conn, id, make, model, year, mileage, daily_rent, extra_fee, min_lease_limit, max_lease_limit):
    car = get_car_by_id(id)
    if car == None:
        return False
    # some fields may be empty, do not update
    sql = "update car set updated_time = datetime('now') "
    if make != "":
        sql += ", make = '" + make + "'"
    if model != "":
        sql += ", model = '" + model + "'"
    if year != "":
        sql += ", manufactured_year = '" + year + "'"
    if mileage != "":
        sql += ", mileage = '" + mileage + "'"
    if daily_rent != "":
        sql += ", daily_rent = '" + daily_rent + "'"
    if extra_fee != "":
        sql += ", extra_fee = '" + extra_fee + "'"
    if min_lease_limit != "":
        sql += ", min_lease_limit = '" + min_lease_limit + "'"
    if max_lease_limit != "":
        sql += ", max_lease_limit = '" + max_lease_limit + "'"
    sql += " where id = " + id
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    return True

@db_connection
def query_car_by_id(cursor, conn, id):
    cursor.execute("select id, make, model, manufactured_year, mileage, daily_rent, extra_fee, min_lease_limit, max_lease_limit from car where id = " + id)
    car = cursor.fetchone()
    cursor.close()
    if car == None:
        return None
    car = Car(id=car[0], make=car[1], model=car[2], manufactured_year=car[3], mileage=car[4], daily_rent=car[5], extra_fee=car[6], min_lease_limit=car[7], max_lease_limit=car[8])
    return car

@db_connection
def query_car(cursor, conn, make, model, year, min_mileage, max_mileage, min_rent, max_rent, available):
    sql = "select * from car where 1=1 "
    if make != "":
        sql += "and make = '" + make + "' "
    if model != "":
        sql += "and model = '" + model + "' "
    if year != "":
        sql += "and manufactured_year = '" + year + "' "
    if min_mileage != "":
        sql += "and mileage >= " + min_mileage + " "
    if max_mileage != "":
        sql += "and mileage <= " + max_mileage + " "
    if min_rent != "":
        sql += "and daily_rent >= " + min_rent + " "
    if max_rent != "":
        sql += "and daily_rent <= " + max_rent + " "
    if available is not None:
        sql += "and available = " + str(available) + " "
    cursor.execute(sql)
    rows = cursor.fetchall()
    cars = []
    for row in rows:
        car = Car(
            id=row[0],
            make=row[1],
            model=row[2],
            manufactured_year=row[3],
            mileage=row[4],
            daily_rent=row[5],
            extra_fee=row[6],
            min_lease_limit=row[7],
            max_lease_limit=row[8]
        )
        cars.append(car)
    cursor.close()
    return cars