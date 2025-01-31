from utils.decorators import new_page
from . import user_admin, car_admin, lease_admin
import tabulate
import datetime
import config

@new_page
def login():
    language = config.get_language()
    username = input(language.USER_PAGE["input_username_prompt"])
    password = input(language.USER_PAGE["input_password_prompt"])
    user = user_admin.login(username, password)
    if user is None:
        print(language.USER_PAGE["invalid_input_tip"])
    else:
        print(language.USER_PAGE["login_success_tip"])
    input(language.PENDING_PROMPT)
    return user

@new_page
def register():
    language = config.get_language()
    username = input(language.USER_PAGE["input_username_prompt"])
    password = input(language.USER_PAGE["input_password_prompt"])
    user = user_admin.register(username, password)
    if user != None:
        print(language.USER_PAGE["register_success_tip"])
    else:
        print(language.USER_PAGE["register_fail_tip"])
    input(language.PENDING_PROMPT)


@new_page
def create_user(user):
    language = config.get_language()
    username = input(language.MANAGER_USER_PAGE["user_admin_add_user_prompt"])
    password = input(language.MANAGER_USER_PAGE["user_admin_add_password_prompt"])
    role_type = input(language.MANAGER_USER_PAGE["user_admin_add_role_prompt"])
    user = user_admin.create_user(username, password, role_type)
    if user != None:
        print(language.MANAGER_USER_PAGE["user_admin_add_success_tip"])
    else:
        print(language.MANAGER_USER_PAGE["user_admin_add_fail_tip"])
    input(language.PENDING_PROMPT)


@new_page
def delete_user(user):
    language = config.get_language()
    username = input(language.MANAGER_USER_PAGE["user_admin_delete_user_prompt"])
    user = user_admin.delete_user(username)
    if user != None:
        print(language.MANAGER_USER_PAGE["user_admin_delete_success_tip"])
    else:
        print(language.MANAGER_USER_PAGE["user_admin_delete_fail_tip"])
    input(language.PENDING_PROMPT)

@new_page
def update_user(user):
    language = config.get_language()
    username = input(language.MANAGER_USER_PAGE["user_admin_update_username_prompt"])
    password = input(language.SKIP_TIP + language.MANAGER_USER_PAGE["user_admin_update_password_prompt"])
    role_type = input(language.SKIP_TIP + language.MANAGER_USER_PAGE["user_admin_update_role_prompt"])
    user = user_admin.update_user(username, password, role_type)
    if user != None:
        print(language.MANAGER_USER_PAGE["user_admin_update_success_tip"])
    else:
        print(language.MANAGER_USER_PAGE["user_admin_update_fail_tip"])
    input(language.PENDING_PROMPT)


@new_page
def query_user(user):
    language = config.get_language()
    # this function can be used to query users with optional conditions
    username = input(language.MANAGER_USER_PAGE["user_admin_query_username_prompt"])
    role_type = input(language.MANAGER_USER_PAGE["user_admin_query_role_prompt"])
    users = user_admin.query_user(username, role_type)
    if len(users) == 0:
        print(language.MANAGER_USER_PAGE["user_admin_query_no_result_tip"])
    else:
        print(language.MANAGER_USER_PAGE["user_admin_query_columns"])
        headers = ["id", "username", "role_type", "deleted_flag", "created_time", "deleted_time", "updated_time"]
        rows = []
        for user in users:
            rows.append([user.id, user.username, user.role_type, user.deleted_flag, user.created_time, user.deleted_time, user.updated_time])
        print(tabulate.tabulate(rows, headers=headers, tablefmt="grid"))
        print(language.MANAGER_USER_PAGE["user_admin_query_success_tip"] + str(len(users)))
    input(language.PENDING_PROMPT)


def create_car(user):
    language = config.get_language()
    make = input(language.MANAGER_CAR_PAGE["car_admin_make_prompt"])
    model = input(language.MANAGER_CAR_PAGE["car_admin_model_prompt"])
    year = input(language.MANAGER_CAR_PAGE["car_admin_year_prompt"])
    mileage = input(language.MANAGER_CAR_PAGE["car_admin_mileage_prompt"])
    daily_rent = input(language.MANAGER_CAR_PAGE["car_admin_daily_rent_prompt"])
    extra_fee = input(language.MANAGER_CAR_PAGE["car_admin_extra_fee_prompt"])
    min_lease_limit = input(language.MANAGER_CAR_PAGE["car_admin_min_leasing_days_prompt"])
    max_lease_limit = input(language.MANAGER_CAR_PAGE["car_admin_max_leasing_days_prompt"])
    # input validation
    if make == "" or model == "" or year == "" or mileage == "" or daily_rent == "" or extra_fee == "" or min_lease_limit == "" or max_lease_limit == "":
        print(language.MANAGER_CAR_PAGE["car_admin_input_error"])
        return
    # judge whether daily_rent and extra_fee are numbers
    if not daily_rent.isnumeric() or not extra_fee.isnumeric:
        print(language.MANAGER_CAR_PAGE["car_admin_input_error"])
        return
    success = car_admin.create_car(make, model, year, mileage, daily_rent, extra_fee, min_lease_limit, max_lease_limit)
    if success:
        print(language.MANAGER_CAR_PAGE["car_admin_add_success_tip"])
    else:
        print(language.MANAGER_CAR_PAGE["car_admin_add_failure_tip"])
    input(language.PENDING_PROMPT)


def delete_car(user):
    language = config.get_language()
    id = input(language.MANAGER_CAR_PAGE["car_admin_id_prompt"])
    if id == "":
        print(language.MANAGER_CAR_PAGE["car_admin_input_error"])
        return
    success = car_admin.delete_car(id)
    if success:
        print(language.MANAGER_CAR_PAGE["car_admin_delete_success_tip"])
    else:
        print(language.MANAGER_CAR_PAGE["car_admin_delete_fail_tip"])
    input(language.PENDING_PROMPT)



def update_car(user):
    language = config.get_language()
    id = input(language.MANAGER_CAR_PAGE["car_admin_id_prompt"])
    make = input(language.SKIP_TIP + language.MANAGER_CAR_PAGE["car_admin_make_prompt"])
    model = input(language.SKIP_TIP + language.MANAGER_CAR_PAGE["car_admin_model_prompt"])
    year = input(language.SKIP_TIP + language.MANAGER_CAR_PAGE["car_admin_year_prompt"])
    mileage = input(language.SKIP_TIP + language.MANAGER_CAR_PAGE["car_admin_mileage_prompt"])
    daily_rent = input(language.SKIP_TIP + language.MANAGER_CAR_PAGE["car_admin_daily_rent_prompt"])
    extra_fee = input(language.SKIP_TIP + language.MANAGER_CAR_PAGE["car_admin_extra_fee_prompt"])
    min_lease_limit = input(language.SKIP_TIP + language.MANAGER_CAR_PAGE["car_admin_min_leasing_days_prompt"])
    max_lease_limit = input(language.SKIP_TIP + language.MANAGER_CAR_PAGE["car_admin_max_leasing_days_prompt"])
    # input validation
    if id == "":
        print(language.MANAGER_CAR_PAGE["car_admin_input_error"])
        return
    # judge whether daily_rent and extra_fee are numbers
    if daily_rent != "" and not daily_rent.isnumeric():
        print(language.MANAGER_CAR_PAGE["car_admin_input_error"])
        return
    if extra_fee != "" and not extra_fee.isnumeric():
        print(language.MANAGER_CAR_PAGE["car_admin_input_error"])
        return
    success = car_admin.update_car(id, make, model, year, mileage, daily_rent, extra_fee, min_lease_limit, max_lease_limit)
    if success:
        print(language.MANAGER_CAR_PAGE["car_admin_update_success_tip"])
    else:
        print(language.MANAGER_CAR_PAGE["car_admin_update_failure_tip"])
    input(language.PENDING_PROMPT)


def query_car(user):
    language = config.get_language()
    # this function can be used to query cars with optional conditions
    make = input(language.SKIP_TIP + language.MANAGER_CAR_PAGE["car_admin_make_prompt"])
    model = input(language.SKIP_TIP + language.MANAGER_CAR_PAGE["car_admin_model_prompt"])
    year = input(language.SKIP_TIP + language.MANAGER_CAR_PAGE["car_admin_year_prompt"])
    min_mileage = input(language.SKIP_TIP + language.MANAGER_CAR_PAGE["car_admin_query_min_mileage_prompt"])
    max_mileage = input(language.SKIP_TIP + language.MANAGER_CAR_PAGE["car_admin_query_max_mileage_prompt"])
    min_rent = input(language.SKIP_TIP + language.MANAGER_CAR_PAGE["car_admin_query_min_rent_prompt"])
    max_rent = input(language.SKIP_TIP + language.MANAGER_CAR_PAGE["car_admin_query_max_rent_prompt"])
    available = input(language.SKIP_TIP + language.MANAGER_CAR_PAGE["car_admin_query_available_prompt"])
    if available == "":
        available = None
    cars = car_admin.query_car(make, model, year, min_mileage, max_mileage, min_rent, max_rent, available)
    if len(cars) == 0:
        print(language.MANAGER_CAR_PAGE["car_admin_query_no_result_tip"])
    else:
        headers = ["id", "make", "model", "manufactured_year", "mileage", "daily_rent", "extra_fee", "min_lease_limit", "max_lease_limit"]
        rows = []
        for car in cars:
            rows.append([car.id, car.make, car.model, car.manufactured_year, car.mileage, car.daily_rent, car.extra_fee, car.min_lease_limit, car.max_lease_limit])
        print(tabulate.tabulate(rows, headers=headers, tablefmt="grid"))
        print(language.MANAGER_CAR_PAGE["car_admin_query_success_tip"] + str(len(cars)))
    input(language.PENDING_PROMPT)


def lease_application_query(user):
    language = config.get_language()
    # query all lease applications pending to be audited
    app_details = lease_admin.lease_application_query(user)
    if len(app_details) == 0:
        print(language.MANAGER_LEASE_APPLICATION_PAGE["lease_application_admin_query_no_result_tip"])
    else:
        headers = ["id", "user_id", "username", "car_id", "make", "model", "start_time", "end_time", "total_fee", "approved_flag", "created_time", "updated_time"]
        rows = []
        for detail in app_details:
            rows.append([detail.id, detail.user_id, detail.username, detail.car_id, detail.make, detail.model, detail.lease_start_time, detail.lease_end_time, detail.rent, detail.approved_flag, detail.created_time, detail.updated_time])
        print(tabulate.tabulate(rows, headers=headers, tablefmt="grid"))
        print(language.MANAGER_LEASE_APPLICATION_PAGE["lease_application_admin_query_success_tip"] + str(len(app_details)))
    input(language.PENDING_PROMPT)




def lease_audit_application(user):
    language = config.get_language()
    # audit a lease application
    application_id = input(language.MANAGER_LEASE_APPLICATION_PAGE["lease_application_lease_detail_id_prompt"])
    audit_type = input(language.MANAGER_LEASE_APPLICATION_PAGE["lease_application_audit_type_prompt"])
    message = ""
    if audit_type == "2":
        message = input(language.MANAGER_LEASE_APPLICATION_PAGE["lease_application_audit_message_prompt"])
    if application_id == "":
        print(language.MANAGER_LEASE_APPLICATION_PAGE["lease_application_admin_input_error"])
        return
    success = lease_admin.lease_audit_application(application_id, audit_type, message)
    if success:
        print(language.MANAGER_LEASE_APPLICATION_PAGE["lease_application_admin_audit_success_tip"])
    else:
        print(language.MANAGER_LEASE_APPLICATION_PAGE["lease_application_admin_audit_fail_tip"])
    input(language.PENDING_PROMPT)


def lease_details_query(user):
    language = config.get_language()
    # query lease details with optional conditions (user_id, car_id)
    user_id = input(language.SKIP_TIP + language.MANAGER_LEASE_APPLICATION_PAGE["lease_application_query_user_id_prompt"])
    car_id = input(language.SKIP_TIP + language.MANAGER_LEASE_APPLICATION_PAGE["lease_application_query_car_id_prompt"])
    lease_details = lease_admin.lease_details_query(user_id, car_id)
    if len(lease_details) == 0:
        print(language.MANAGER_LEASE_APPLICATION_PAGE["lease_application_query_no_result_tip"])
    else:
        headers = ["id", "user_id", "username", "car_id", "make", "model", "lease_start_time", "lease_end_time", "approved_flag", "created_time", "updated_time"]
        rows = []
        for detail in lease_details:
            rows.append([detail.id, detail.user_id, detail.car_id, detail.lease_start_time, detail.lease_end_time, detail.approved_flag, detail.created_time, detail.updated_time])
        print(tabulate.tabulate(rows, headers=headers, tablefmt="grid"))
        print(language.MANAGER_LEASE_APPLICATION_PAGE["lease_application_query_success_tip"] + str(len(lease_details)))
    input(language.PENDING_PROMPT)


def customer_view_cars(user):
    language = config.get_language()
    # view all cars with optional conditions
    make = input(language.SKIP_TIP+ language.CUSTOMER_MAIN_PAGE["customer_view_cars_make_prompt"])
    model = input(language.SKIP_TIP+ language.CUSTOMER_MAIN_PAGE["customer_view_cars_model_prompt"])
    year = input(language.SKIP_TIP+ language.CUSTOMER_MAIN_PAGE["customer_view_cars_year_prompt"])
    min_mileage = input(language.SKIP_TIP+ language.CUSTOMER_MAIN_PAGE["customer_view_cars_min_mileage_prompt"])
    max_mileage = input(language.SKIP_TIP+ language.CUSTOMER_MAIN_PAGE["customer_view_cars_max_mileage_prompt"])
    min_rent = input(language.SKIP_TIP+ language.CUSTOMER_MAIN_PAGE["customer_view_cars_min_rent_prompt"])
    max_rent = input(language.SKIP_TIP+ language.CUSTOMER_MAIN_PAGE["customer_view_cars_max_rent_prompt"])
    cars = car_admin.query_car(make, model, year, min_mileage, max_mileage, min_rent, max_rent, 1)
    if len(cars) == 0:
        print(language.CUSTOMER_MAIN_PAGE["customer_view_cars_no_result_tip"])
    else:
        headers = ["id", "make", "model", "manufactured_year", "mileage", "daily_rent", "extra_fee", "min_lease_limit", "max_lease_limit"]
        rows = []
        for car in cars:
            rows.append([car.id, car.make, car.model, car.manufactured_year, car.mileage, car.daily_rent, car.extra_fee, car.min_lease_limit, car.max_lease_limit])
        print(tabulate.tabulate(rows, headers=headers, tablefmt="grid"))
        print(language.CUSTOMER_MAIN_PAGE["customer_view_cars_success_tip"] + str(len(cars)))
    input(language.PENDING_PROMPT)


def customer_book_car(user):
    language = config.get_language()
    # book a car
    car_id = input(language.CUSTOMER_MAIN_PAGE["customer_book_car_id_prompt"])
    start_time = input(language.CUSTOMER_MAIN_PAGE["customer_book_car_start_time_prompt"])
    end_time = input(language.CUSTOMER_MAIN_PAGE["customer_book_car_end_time_prompt"])
    # check whether the car is available
    car = car_admin.query_car_by_id(car_id)
    if car is None:
        print(language.CUSTOMER_MAIN_PAGE["customer_book_car_not_available_tip"])
        return
    # judge whether the lease period is valid
    if start_time == "" or end_time == "":
        print(language.CUSTOMER_MAIN_PAGE["customer_book_car_input_error"])
        return
    start_time = datetime.datetime.strptime(start_time, "%Y-%m-%d")
    end_time = datetime.datetime.strptime(end_time, "%Y-%m-%d")
    if start_time >= end_time:
        print(language.CUSTOMER_MAIN_PAGE["customer_book_car_input_error"])
        return
    # compute interval days
    interval_days = (end_time - start_time).days
    if ((car.min_lease_limit > 0 and interval_days < car.min_lease_limit)
            or (0 < car.max_lease_limit < interval_days)):
        print(language.CUSTOMER_MAIN_PAGE["customer_book_invalid_interval_days_tip"]+ str(car.min_lease_limit) + " / " + str(car.max_lease_limit))
        return
    # compute total fee based on daily rent and extra fee
    total_fee = (end_time - start_time).days * car.daily_rent + car.extra_fee
    # make user confirm the booking
    confirm = input(language.CUSTOMER_MAIN_PAGE["customer_book_car_confirm_prompt"] + str(total_fee) + " (y/n)")
    if confirm == "y":
        success = lease_admin.add_application(user.id, car_id, start_time.strftime("%Y-%m-%d 00:00:00"), end_time.strftime("%Y-%m-%d 00:00:00"), total_fee)
        if success:
            print(language.CUSTOMER_MAIN_PAGE["customer_book_car_success_tip"])
        else:
            print(language.CUSTOMER_MAIN_PAGE["customer_book_car_fail_tip"])
    else:
        print(language.CUSTOMER_MAIN_PAGE["customer_book_car_cancel_tip"])


def customer_order_history(user):
    language = config.get_language()
    # query order history
    orders = lease_admin.lease_details_query(user.id, "")
    if len(orders) == 0:
        print(language.CUSTOMER_MAIN_PAGE["customer_order_history_no_result_tip"])
    else:
        headers = ["id", "user_id", "username", "car_id", "make", "model", "lease_start_time", "lease_end_time", "interval_days", "rent", "deleted_flag", "created_time", "updated_time", "deleted_time", "approved_flag", "refusal_reason"]
        rows = []
        for order in orders:
            rows.append([order.id, order.user_id, order.username, order.car_id, order.make, order.model, order.lease_start_time, order.lease_end_time, order.interval_days, order.rent, order.deleted_flag, order.created_time, order.updated_time, order.deleted_time, order.approved_flag, order.refusal_reason])
        print(tabulate.tabulate(rows, headers=headers, tablefmt="grid"))
        print(language.CUSTOMER_MAIN_PAGE["customer_order_history_success_tip"] + str(len(orders)))
    input(language.PENDING_PROMPT)
