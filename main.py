# main.py
from time import sleep

import config
import service
from models.action import Action
from models.menu import Menu

main_menu, manager_menu, user_admin_menu, car_admin_menu, lease_application_admin_menu, lease_details_admin_menu, customer_menu = None, None, None, None, None, None, None

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

def query_all_cars_action(user):
    service.query_all_cars(user)


def lease_application_query_action(user):
    service.lease_application_query(user)


def lease_audit_application_action(user):
    service.lease_audit_application(user)


def lease_details_query_action(user):
    service.lease_details_query(user)

def customer_view_cars_action(user):
    service.customer_view_cars(user)

def customer_view_all_cars_action(user):
    service.customer_view_all_cars(user)


def customer_book_car_action(user):
    service.customer_book_car(user)


def customer_order_history_action(user):
    service.customer_order_history(user)


def customer_exit_action(user):
    return -1

def lease_details_exit_action(user):
    return -1


def lease_application_exit_action(user):
    return -1


def car_admin_exit_action(user):
    return -1


def exit_action():
    language = config.get_language() 
    print(language.MAIN_PAGE_MESSAGES["thank_prompt"])
    exit(0)


def manager_exit_action(user):
    language = config.get_language() 
    print(language.MANAGER_MAIN_PAGE["thank_prompt"])
    sleep(1)
    return -1


def user_admin_exit_action(user):
    return -1


# define instances of Menu
def create_menus():
    language = config.get_language() # 

    main_menu = Menu(
        language.MAIN_PAGE_MESSAGES["welcome_tip"] + "\n" + language.OPTION_TIPS,
        [
            Action(language.MAIN_PAGE_MESSAGES["register_option"], register_action),
            Action(language.MAIN_PAGE_MESSAGES["login_option"], login_action),
            Action(language.MAIN_PAGE_MESSAGES["exit_option"], exit_action),
        ]
    )

    manager_menu = Menu(
        language.MANAGER_MAIN_PAGE["welcome_tip"],
        [
            Action(language.MANAGER_MAIN_PAGE["user_admin_option"], user_admin_action),
            Action(language.MANAGER_MAIN_PAGE["car_admin_option"], car_admin_action),
            Action(language.MANAGER_MAIN_PAGE["lease_application_admin_option"], lease_application_admin_action),
            Action(language.MANAGER_MAIN_PAGE["lease_details_admin_option"], lease_details_admin_action),
            Action(language.MANAGER_MAIN_PAGE["exit_option"], manager_exit_action),
        ]
    )

    user_admin_menu = Menu(
        language.MANAGER_USER_PAGE["user_admin_welcome_tip"],
        [
            Action(language.MANAGER_USER_PAGE["create_user_option"], create_user_action),
            Action(language.MANAGER_USER_PAGE["delete_user_option"], delete_user_action),
            Action(language.MANAGER_USER_PAGE["update_user_option"], update_user_action),
            Action(language.MANAGER_USER_PAGE["query_user_option"], query_user_action),
            Action(language.MANAGER_USER_PAGE["exit_option"], user_admin_exit_action),
        ]
    )

    car_admin_menu = Menu(
        language.MANAGER_CAR_PAGE["car_admin_welcome_tip"],
        [
            Action(language.MANAGER_CAR_PAGE["create_car_option"], careate_car_action),
            Action(language.MANAGER_CAR_PAGE["delete_car_option"], delete_car_action),
            Action(language.MANAGER_CAR_PAGE["update_car_option"], update_car_action),
            Action(language.MANAGER_CAR_PAGE["query_car_option"], query_car_action),
            Action(language.MANAGER_CAR_PAGE["query_all_cars_option"], query_all_cars_action),
            Action(language.MANAGER_CAR_PAGE["exit_option"], car_admin_exit_action),
        ]
    )

    lease_application_admin_menu = Menu(
        language.MANAGER_LEASE_APPLICATION_PAGE["lease_application_admin_welcome_tip"],
        [
            Action(language.MANAGER_LEASE_APPLICATION_PAGE["query_application_option"], lease_application_query_action),
            Action(language.MANAGER_LEASE_APPLICATION_PAGE["audit_application_option"], lease_audit_application_action),
            Action(language.MANAGER_LEASE_APPLICATION_PAGE["exit_option"], lease_application_exit_action),
        ]
    )

    lease_details_admin_menu = Menu(
        language.MANAGER_LEASE_DETAILS_PAGE["lease_details_admin_welcome_tip"],
        [
            Action(language.MANAGER_LEASE_DETAILS_PAGE["query_details_option"], lease_details_query_action),
            Action(language.MANAGER_LEASE_DETAILS_PAGE["exit_option"], lease_details_exit_action),
        ]
    )

    customer_menu = Menu(
        language.CUSTOMER_MAIN_PAGE["welcome_tip"],
        [
            Action(language.CUSTOMER_MAIN_PAGE["view_cars_option"], customer_view_cars_action),
            Action(language.CUSTOMER_MAIN_PAGE["view_all_cars_option"], customer_view_all_cars_action),
            Action(language.CUSTOMER_MAIN_PAGE["book_car_option"], customer_book_car_action),
            Action(language.CUSTOMER_MAIN_PAGE["order_history_option"], customer_order_history_action),
            Action(language.CUSTOMER_MAIN_PAGE["exit_option"], customer_exit_action),
        ]
    )

    return main_menu, manager_menu, user_admin_menu, car_admin_menu, lease_application_admin_menu, lease_details_admin_menu, customer_menu




def main():
    # initialize language
    language_choice = config.get_language_choice()
    config.initialize_language(language_choice)

    # create menus
    global main_menu, manager_menu, user_admin_menu, car_admin_menu, lease_application_admin_menu, lease_details_admin_menu, customer_menu
    main_menu, manager_menu, user_admin_menu, car_admin_menu, lease_application_admin_menu, lease_details_admin_menu, customer_menu = create_menus()

    main_menu.run()


if __name__ == "__main__":
    main()
