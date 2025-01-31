"""
    This file contains system prompts in English
"""

# system messages
OPTION_TIPS = "Please choose the following options: "
INPUT_PROMPT = "Please input your option: "
INVALID_INPUT_PROMPT = "Invalid input, please check."
PENDING_PROMPT = "Press Enter to continue..."
SKIP_TIP = "(Simply press Enter to skip this item) "

MAIN_PAGE_MESSAGES = {
    "system_logo": r'''
       _____             _____            _        _    _____           _                 
      / ____|           |  __ \          | |      | |  / ____|         | |                
     | |     __ _ _ __  | |__) |___ _ __ | |_ __ _| | | (___  _   _ ___| |_ ___ _ __ ___  
     | |    / _` | '__| |  _  // _ \ '_ \| __/ _` | |  \___ \| | | / __| __/ _ \ '_ ` _ \ 
     | |___| (_| | |    | | \ \  __/ | | | || (_| | |  ____) | |_| \__ \ ||  __/ | | | | |
      \_____\__,_|_|    |_|  \_\___|_| |_|\__\__,_|_| |_____/ \__, |___/\__\___|_| |_| |_|
                                                               __/ |                      
                                                              |___/   Made by Yanqian Chen                
    ''',
    "welcome_tip": "Welcome to use car rental system!",
    "register_option": "1. Register a new user account",
    "login_option": "2. Login to the system",
    "exit_option": "3. Exit the system",
    "thank_prompt": "\nThank you for using, see you next time!"
}

USER_PAGE = {
    "input_username_prompt": "Please input your username: ",
    "input_password_prompt": "Please input your password: ",
    "invalid_input_tip": "Username or password is invalid, please check.",
    "login_success_tip": "Login successfully!",
    "register_success_tip": "Register successfully!",
    "register_fail_tip": "Register failed, the username has been used."

}

MANAGER_MAIN_PAGE = {
    "welcome_tip": "Welcome to admin manager system!",
    "user_admin_option": "1. User management",
    "car_admin_option": "2. Car management",
    "lease_application_admin_option": "3. Lease application management",
    "lease_details_admin_option": "4. Lease details management",
    "exit_option": "5. Back to main page",
    "thank_prompt": "\nThank you for using manager system, see you next time!",
}

MANAGER_USER_PAGE = {
    "user_admin_welcome_tip": "Welcome to manage system users! ",
    "create_user_option": "1. Create a new user",
    "delete_user_option": "2. Delete a user",
    "update_user_option": "3. Update a user",
    "query_user_option": "4. Query users by optional conditions",
    "exit_option": "5. Back to admin main page",

    "user_admin_add_user_prompt": "Please input the username: ",
    "user_admin_add_password_prompt": "Please input the password: ",
    "user_admin_add_role_prompt": "Please input the role type (please input 0 or 1, 0 -> customer 1 -> admin): ",
    "user_admin_add_success_tip": "Add user successfully!",
    "user_admin_add_fail_tip": "Add user failed, the username has been used.",

    "user_admin_delete_user_prompt": "Please input the username you want to delete: ",
    "user_admin_delete_success_tip": "Delete user successfully!",
    "user_admin_delete_fail_tip": "Delete user failed, the username does not exist.",

    "user_admin_update_username_prompt": "Please input the username you want to update: ",
    "user_admin_update_password_prompt": "Please input the new password: ",
    "user_admin_update_role_prompt": "Please input the new role type (please input 0 or 1, 0 -> customer 1 -> admin): ",
    "user_admin_update_success_tip": "Update user successfully!",
    "user_admin_update_fail_tip": "Update user failed, the username does not exist.",

    "user_admin_query_username_prompt": "Please input the username you want to query (Simply press enter to ignore this item): ",
    "user_admin_query_role_prompt": "Please input the role type you want to query (please input 0 or 1, 0 -> customer 1 -> admin, simply press Enter to ignore this item): ",
    "user_admin_query_success_tip": "Query user successfully! total count:",
    "user_admin_query_no_result_tip": "no user meets the conditions.",
    "user_admin_query_columns": "id | username | password | role_type | deleted_flag | created_time | deleted_time | updated_time"

}

MANAGER_CAR_PAGE = {
    "car_admin_welcome_tip": "Welcome to manage system cars! ",
    "create_car_option": "1. Create a new car",
    "delete_car_option": "2. Delete a car",
    "update_car_option": "3. Update a car",
    "query_car_option": "4. Query cars by optional conditions",
    "query_all_cars_option": "5. Query all cars",
    "exit_option": "6. Back to admin main page",

    "car_admin_id_prompt": "Please input the id of the car: ",
    "car_admin_make_prompt": "Please input the make of the car: ",
    "car_admin_model_prompt": "Please input the model of the car: ",
    "car_admin_year_prompt": "Please input the year of the car: ",
    "car_admin_mileage_prompt": "Please input the mileage of the car: ",
    "car_admin_manufacturer_prompt": "Please input the manufacturer of the car: ",
    "car_admin_daily_rent_prompt": "Please input the daily rent of the car: ",
    "car_admin_extra_fee_prompt": "Please input the extra fee of the car: ",
    "car_admin_min_leasing_days_prompt": "Please input the minimum leasing days of the car: ",
    "car_admin_max_leasing_days_prompt": "Please input the maximum leasing days of the car: ",
    "car_admin_input_error": "Invalid input, please check.",
    "car_admin_add_success_tip": "Add car successfully!",
    "car_admin_add_failure_tip": "Add car failed, please check the input or contact the system administrator.",

    "car_admin_update_success_tip": "Update car successfully!",
    "car_admin_update_failure_tip": "Update car failed, please make sure that the car id exists.",

    "car_admin_delete_car_prompt": "Please input the id of the car you want to delete: ",
    "car_admin_delete_success_tip": "Delete car successfully!",
    "car_admin_delete_failure_tip": "Delete car failed, please make sure that the car id exists.",

    "car_admin_query_min_mileage_prompt": "Please input the minimum mileage of the car you want to query: ",
    "car_admin_query_max_mileage_prompt": "Please input the maximum mileage of the car you want to query: ",
    "car_admin_query_min_rent_prompt": "Please input the minimum daily rent of the car you want to query: ",
    "car_admin_query_max_rent_prompt": "Please input the maximum daily rent of the car you want to query: ",
    "car_admin_query_make_prompt": "Please input the make of the car you want to query: ",
    "car_admin_query_model_prompt": "Please input the model of the car you want to query: ",
    "car_admin_query_year_prompt": "Please input the year of the car you want to query: ",
    "car_admin_query_available_prompt": "Please input the available status of the car you want to query (please input 0 or 1, 0 -> not available 1 -> available): ",
    "car_admin_query_success_tip": "Query car successfully! total count:",
    "car_admin_query_no_result_tip": "no car meets the conditions.",

}

MANAGER_LEASE_APPLICATION_PAGE = {

    "lease_application_admin_welcome_tip": "Welcome to manage system lease applications! ",
    "query_application_option": "1. Query lease applications pending to be audited",
    "audit_application_option": "2. Audit a lease application",
    "exit_option": "3. Back to admin main page",

    "lease_application_admin_query_no_result_tip": "no lease application meets the conditions.",
    "lease_application_admin_query_success_tip": "Query lease application successfully! total count:",

    "lease_application_lease_detail_id_prompt": "Please input the lease detail id of the application: ",
    "lease_application_audit_type_prompt": "Please input the audit result (please input 1 or 2, 1 -> approve 2 -> refuse): ",
    "lease_application_audit_message_prompt": "Please input the refusal reason (Simply press Enter to skip this item): ",
    "lease_application_admin_audit_success_tip": "Audit lease application successfully!",
    "lease_application_admin_audit_fail_tip": "Audit lease application failed, please check the input or contact the system administrator.",
    "lease_application_admin_input_error": "Invalid input, please check.",
    "lease_application_query_user_id_prompt": "Please input the user id of the lease application you want to query: ",
    "lease_application_query_car_id_prompt": "Please input the car id of the lease application you want to query: ",
    "lease_application_query_no_result_tip": "no lease application meets the conditions.",
    "lease_application_query_success_tip": "Query lease application successfully! total count:",


}

MANAGER_LEASE_DETAILS_PAGE = {

    "lease_details_admin_welcome_tip": "Welcome to manage system lease details! ",
    "query_details_option": "1. Query lease details",
    "exit_option": "2. Back to admin main page",

    "lease_details_query_user_id_prompt": "Please input the user id of the lease details you want to query: ",
    "lease_details_query_car_id_prompt": "Please input the car id of the lease details you want to query: ",
    "lease_details_query_no_result_tip": "no lease details meets the conditions.",
    "lease_details_query_success_tip": "Query lease details successfully! total count:",

}
CUSTOMER_MAIN_PAGE = {
    "welcome_tip": "Welcome to customer system!",
    "view_cars_option": "1. View available cars by conditions",
    "view_all_cars_option": "2. View all available cars",
    "book_car_option": "3. Book a car",
    "order_history_option": "4. View order history",
    "exit_option": "5. Back to main page",

    "thank_prompt": "\nThank you for using customer system, see you next time!",
    "customer_view_cars_make_prompt": "Please input the make of the car you want to query: ",
    "customer_view_cars_model_prompt": "Please input the model of the car you want to query: ",
    "customer_view_cars_year_prompt": "Please input the year of the car you want to query: ",
    "customer_view_cars_min_mileage_prompt": "Please input the minimum mileage of the car you want to query: ",
    "customer_view_cars_max_mileage_prompt": "Please input the maximum mileage of the car you want to query: ",
    "customer_view_cars_min_rent_prompt": "Please input the minimum daily rent of the car you want to query: ",
    "customer_view_cars_max_rent_prompt": "Please input the maximum daily rent of the car you want to query: ",

    "customer_view_cars_no_result_tip": "no car meets the conditions.",
    "customer_view_cars_success_tip": "Query car successfully! total count:",

    "customer_book_car_id_prompt": "Please input the id of the car you want to book: ",
    "customer_book_car_start_time_prompt": "Please input the start time of the lease (format: yyyy-mm-dd): ",
    "customer_book_car_end_time_prompt": "Please input the end time of the lease (format: yyyy-mm-dd): ",
    "customer_book_car_confirm_prompt": "Please confirm to order it, please notice the total fee is ",
    "customer_book_car_not_available_tip": "The car is not available now or doesn't exist, please check.",
    "customer_book_car_cancel_tip": "Cancel the order.",
    "customer_book_car_success_tip": "Submit a application for booking the car successfully!",
    "customer_book_car_failure_tip": "Book car failed, please check the input or contact the system administrator.",
    "customer_book_invalid_interval_days_tip": "The rental days limit is not met. minimum and maximum days: ",

    "customer_order_history_no_result_tip": "no order meets the conditions.",
    "customer_order_history_success_tip": "Query order successfully! total count:",

    "customer_book_car_input_error": "Invalid input, please check.",
}
