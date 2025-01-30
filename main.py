# main.py
from time import sleep
from config import *
from language_en import *
import service
from models.action import Action
from models.menu import Menu


# define actions for each option
def register_action():
    service.register()


def login_action():
    user = service.login()
    if user is None:
        return
    elif user.role_type == 1:
        manager_menu.run(user)
    else:
        customer_menu.run(user)


def user_admin_action(user):
    user_admin_menu.run(user)


def car_admin_action(user):
    car_admin_menu.run(user)


def lease_application_admin_action(user):
    lease_application_admin_menu.run(user)


def lease_details_admin_action(user):
    lease_details_admin_menu.run(user)


def create_user_action(user):
    service.create_user(user)


def delete_user_action(user):
    service.delete_user(user)


def update_user_action(user):
    service.update_user(user)


def query_user_action(user):
    service.query_user(user)


def careate_car_action(user):
    service.create_car(user)


def delete_car_action(user):
    service.delete_car(user)


def update_car_action(user):
    service.update_car(user)


def query_car_action(user):
    service.query_car(user)


def lease_application_query_action(user):
    service.lease_application_query(user)


def lease_audit_application_action(user):
    service.lease_audit_application(user)


def lease_details_query_action(user):
    service.lease_details_query(user)


def lease_details_exit_action(user):
    return -1


def lease_application_exit_action(user):
    return -1


def car_admin_exit_action(user):
    return -1


def exit_action():
    print(MAIN_PAGE_MESSAGES["thank_prompt"])
    exit(0)


def manager_exit_action(user):
    print(MANAGER_MAIN_PAGE["thank_prompt"])
    sleep(1)
    return -1


def user_admin_exit_action(user):
    return -1


# define instances of Menu
main_menu = Menu(
    MAIN_PAGE_MESSAGES["welcome_tip"] + "\n" + OPTION_TIPS,
    [
        Action(MAIN_PAGE_MESSAGES["register_option"], register_action),
        Action(MAIN_PAGE_MESSAGES["login_option"], login_action),
        Action(MAIN_PAGE_MESSAGES["exit_option"], exit_action),
    ]
)

manager_menu = Menu(
    MANAGER_MAIN_PAGE["welcome_tip"],
    [
        Action(MANAGER_MAIN_PAGE["user_admin_option"], user_admin_action),
        Action(MANAGER_MAIN_PAGE["car_admin_option"], car_admin_action),
        Action(MANAGER_MAIN_PAGE["lease_application_admin_option"], lease_application_admin_action),
        Action(MANAGER_MAIN_PAGE["lease_details_admin_option"], lease_details_admin_action),
        Action(MANAGER_MAIN_PAGE["exit_option"], manager_exit_action),
    ]
)

user_admin_menu = Menu(
    MANAGER_USER_PAGE["user_admin_welcome_tip"],
    [
        Action(MANAGER_USER_PAGE["create_user_option"], create_user_action),
        Action(MANAGER_USER_PAGE["delete_user_option"], delete_user_action),
        Action(MANAGER_USER_PAGE["update_user_option"], update_user_action),
        Action(MANAGER_USER_PAGE["query_user_option"], query_user_action),
        Action(MANAGER_USER_PAGE["exit_option"], user_admin_exit_action),
    ]
)

car_admin_menu = Menu(
    MANAGER_CAR_PAGE["car_admin_welcome_tip"],
    [
        Action(MANAGER_CAR_PAGE["create_car_option"], careate_car_action),
        Action(MANAGER_CAR_PAGE["delete_car_option"], delete_car_action),
        Action(MANAGER_CAR_PAGE["update_car_option"], update_car_action),
        Action(MANAGER_CAR_PAGE["query_car_option"], query_car_action),
        Action(MANAGER_CAR_PAGE["exit_option"], car_admin_exit_action),
    ]
)

lease_application_admin_menu = Menu(
    MANAGER_LEASE_APPLICATION_PAGE["lease_application_admin_welcome_tip"],
    [
        Action(MANAGER_LEASE_APPLICATION_PAGE["query_application_option"], lease_application_query_action),
        Action(MANAGER_LEASE_APPLICATION_PAGE["audit_application_option"], lease_audit_application_action),
        Action(MANAGER_LEASE_APPLICATION_PAGE["exit_option"], lease_application_exit_action),
    ]
)

lease_details_admin_menu = Menu(
    MANAGER_LEASE_DETAILS_PAGE["lease_details_admin_welcome_tip"],
    [
        Action(MANAGER_LEASE_DETAILS_PAGE["query_details_option"], lease_details_query_action),
        Action(MANAGER_LEASE_DETAILS_PAGE["exit_option"], lease_details_exit_action),
    ]
)

customer_menu = Menu(
    CUSTOMER_MAIN_PAGE["welcome_tip"],
    [
        Action(CUSTOMER_MAIN_PAGE["view_cars_option"], lambda user: None),
        Action(CUSTOMER_MAIN_PAGE["book_car_option"], lambda user: None),
        Action(CUSTOMER_MAIN_PAGE["view_cars_option"], lambda user: None),
        Action(CUSTOMER_MAIN_PAGE["view_cars_option"], lambda user: None),

    ]
)


def main():
    main_menu.run()


if __name__ == "__main__":
    main()
