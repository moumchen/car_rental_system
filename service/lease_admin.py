import sqlite3
from models import LeaseDetail
from utils.decorators import db_connection

@db_connection
def lease_application_query(cursor, conn, user):
    # join user and car table to get username and car make, model
    cursor.execute("select ld.id, u.username, c.make, c.model, ld.lease_start_time, ld.lease_end_time, ld.rent, ld.approved_flag, ld.refusal_reason, u.id, c.id from lease_details ld join user u on ld.user_id = u.id join car c on ld.car_id = c.id where ld.deleted_flag = 0")
    rows = cursor.fetchall()
    lease_details = []
    for row in rows:
        lease_detail = LeaseDetail()
        lease_detail.id = row[0]
        lease_detail.username = row[1]
        lease_detail.make = row[2]
        lease_detail.model = row[3]
        lease_detail.lease_start_time = row[4]
        lease_detail.lease_end_time = row[5]
        lease_detail.rent = row[6]
        lease_detail.approved_flag = row[7]
        lease_detail.refusal_reason = row[8]
        lease_detail.user_id = row[9]
        lease_detail.car_id = row[10]
        lease_details.append(lease_detail)
    cursor.close()
    return lease_details



@db_connection
def lease_audit_application(cursor, conn, application_id, approved_flag, refusal_reason):
    # update lease_details table, set approved_flag and refusal_reason
    cursor.execute("update lease_details set approved_flag = " + str(approved_flag) + ", refusal_reason = '" + refusal_reason + "' where id = " + str(application_id))
    # if refused, update car table, set available to 1
    if approved_flag == 2:
        cursor.execute("update car set available = 1 where id = (select car_id from lease_details where id = " + str(application_id) + ")")
    return True

@db_connection
def lease_details_query(cursor, conn, user_id, car_id):
    # join user and car table to get username and car make, model
    # user_id and car_id may be empty, if empty, ignore them
    sql = "select ld.id, u.username, c.make, c.model, ld.lease_start_time, ld.lease_end_time, ld.rent, ld.approved_flag, ld.refusal_reason, u.id, c.id from lease_details ld join user u on ld.user_id = u.id join car c on ld.car_id = c.id where ld.deleted_flag = 0 "
    if user_id != "":
        sql += "and u.id = " + str(user_id) + " "
    if car_id != "":
        sql += "and c.id = " + str(car_id) + " "
    cursor.execute(sql)
    rows = cursor.fetchall()
    lease_details = []
    for row in rows:
        lease_detail = LeaseDetail()
        lease_detail.id = row[0]
        lease_detail.username = row[1]
        lease_detail.make = row[2]
        lease_detail.model = row[3]
        lease_detail.lease_start_time = row[4]
        lease_detail.lease_end_time = row[5]
        lease_detail.rent = row[6]
        lease_detail.approved_flag = row[7]
        lease_detail.refusal_reason = row[8]
        lease_detail.user_id = row[9]
        lease_detail.car_id = row[10]
        lease_details.append(lease_detail)
    return lease_details

@db_connection
def add_application(cursor, conn, user_id, car_id, start_time, end_time, total_fee):
    # insert a new application
    cursor.execute("insert into lease_details (user_id, car_id, lease_start_time, lease_end_time, rent, approved_flag) values (" + str(user_id) + ", " + str(car_id) + ", '" + start_time + "', '" + end_time + "', " + str(total_fee) + ", 0)")
    # update car table, set available to 0
    cursor.execute("update car set available = 0 where id = " + str(car_id))
    return True
