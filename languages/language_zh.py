"""
    This file contains system prompts in Chinese
"""

# system messages
OPTION_TIPS = "请选择以下选项: "
INPUT_PROMPT = "请输入您的选项: "
INVALID_INPUT_PROMPT = "无效输入，请检查。"
PENDING_PROMPT = "按Enter键继续..."
SKIP_TIP = "(直接按Enter键跳过此项) "

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
    "welcome_tip": "欢迎使用汽车租赁系统！",
    "register_option": "1. 注册新用户账号",
    "login_option": "2. 登录系统",
    "exit_option": "3. 退出系统",
    "thank_prompt": "\n感谢您的使用，再见！"
}

USER_PAGE = {
    "input_username_prompt": "请输入您的用户名: ",
    "input_password_prompt": "请输入您的密码: ",
    "invalid_input_tip": "用户名或密码无效，请检查。",
    "login_success_tip": "登录成功！",
    "register_success_tip": "注册成功！",
    "register_fail_tip": "注册失败，用户名已被使用。"

}

MANAGER_MAIN_PAGE = {
    "welcome_tip": "欢迎来到管理员管理系统！",
    "user_admin_option": "1. 用户管理",
    "car_admin_option": "2. 车辆管理",
    "lease_application_admin_option": "3. 租赁申请管理",
    "lease_details_admin_option": "4. 租赁详情管理",
    "exit_option": "5. 返回主页面",
    "thank_prompt": "\n感谢您使用管理系统，再见！",
}

MANAGER_USER_PAGE = {
    "user_admin_welcome_tip": "欢迎来到系统用户管理！ ",
    "create_user_option": "1. 创建新用户",
    "delete_user_option": "2. 删除用户",
    "update_user_option": "3. 更新用户",
    "query_user_option": "4. 按条件查询用户",
    "exit_option": "5. 返回管理员主页面",

    "user_admin_add_user_prompt": "请输入用户名: ",
    "user_admin_add_password_prompt": "请输入密码: ",
    "user_admin_add_role_prompt": "请输入角色类型 (请输入 0 或 1, 0 -> 顾客 1 -> 管理员): ",
    "user_admin_add_success_tip": "添加用户成功！",
    "user_admin_add_fail_tip": "添加用户失败，用户名已被使用。",

    "user_admin_delete_user_prompt": "请输入您要删除的用户名: ",
    "user_admin_delete_success_tip": "删除用户成功！",
    "user_admin_delete_fail_tip": "删除用户失败，用户名不存在。",

    "user_admin_update_username_prompt": "请输入您要更新的用户名: ",
    "user_admin_update_password_prompt": "请输入新密码: ",
    "user_admin_update_role_prompt": "请输入新角色类型 (请输入 0 或 1, 0 -> 顾客 1 -> 管理员): ",
    "user_admin_update_success_tip": "更新用户成功！",
    "user_admin_update_fail_tip": "更新用户失败，用户名不存在。",

    "user_admin_query_username_prompt": "请输入您要查询的用户名 (直接按Enter键忽略此项): ",
    "user_admin_query_role_prompt": "请输入您要查询的角色类型 (请输入 0 或 1, 0 -> 顾客 1 -> 管理员，直接按Enter键忽略此项): ",
    "user_admin_query_success_tip": "查询用户成功！总数:",
    "user_admin_query_no_result_tip": "没有用户符合条件。",
    "user_admin_query_columns": "id | 用户名 | 密码 | 角色类型 | 删除标记 | 创建时间 | 删除时间 | 更新时间"

}

MANAGER_CAR_PAGE = {
    "car_admin_welcome_tip": "欢迎来到系统车辆管理！ ",
    "create_car_option": "1. 创建新车辆",
    "delete_car_option": "2. 删除车辆",
    "update_car_option": "3. 更新车辆",
    "query_car_option": "4. 按条件查询车辆",
    "exit_option": "5. 返回管理员主页面",

    "car_admin_id_prompt": "请输入车辆ID: ",
    "car_admin_make_prompt": "请输入车辆品牌: ",
    "car_admin_model_prompt": "请输入车辆型号: ",
    "car_admin_year_prompt": "请输入车辆年份: ",
    "car_admin_mileage_prompt": "请输入车辆里程数: ",
    "car_admin_manufacturer_prompt": "请输入车辆制造商: ",
    "car_admin_daily_rent_prompt": "请输入车辆日租金: ",
    "car_admin_extra_fee_prompt": "请输入车辆额外费用: ",
    "car_admin_min_leasing_days_prompt": "请输入车辆最小租赁天数: ",
    "car_admin_max_leasing_days_prompt": "请输入车辆最大租赁天数: ",
    "car_admin_input_error": "无效输入，请检查。",
    "car_admin_add_success_tip": "添加车辆成功！",
    "car_admin_add_failure_tip": "添加车辆失败，请检查输入或联系系统管理员。",

    "car_admin_update_success_tip": "更新车辆成功！",
    "car_admin_update_failure_tip": "更新车辆失败，请确保车辆ID存在。",

    "car_admin_delete_car_prompt": "请输入您要删除的车辆ID: ",
    "car_admin_delete_success_tip": "删除车辆成功！",
    "car_admin_delete_failure_tip": "删除车辆失败，请确保车辆ID存在。",

    "car_admin_query_min_mileage_prompt": "请输入您要查询的车辆最小里程数: ",
    "car_admin_query_max_mileage_prompt": "请输入您要查询的车辆最大里程数: ",
    "car_admin_query_min_rent_prompt": "请输入您要查询的车辆最小日租金: ",
    "car_admin_query_max_rent_prompt": "请输入您要查询的车辆最大日租金: ",
    "car_admin_query_make_prompt": "请输入您要查询的车辆品牌: ",
    "car_admin_query_model_prompt": "请输入您要查询的车辆型号: ",
    "car_admin_query_year_prompt": "请输入您要查询的车辆年份: ",
    "car_admin_query_available_prompt": "请输入您要查询的车辆可用状态 (请输入 0 或 1, 0 -> 不可用 1 -> 可用): ",
    "car_admin_query_success_tip": "查询车辆成功！总数:",
    "car_admin_query_no_result_tip": "没有车辆符合条件。",

}

MANAGER_LEASE_APPLICATION_PAGE = {

    "lease_application_admin_welcome_tip": "欢迎来到系统租赁申请管理！ ",
    "query_application_option": "1. 查询待审核的租赁申请",
    "audit_application_option": "2. 审核租赁申请",
    "exit_option": "3. 返回管理员主页面",

    "lease_application_admin_query_no_result_tip": "没有租赁申请符合条件。",
    "lease_application_admin_query_success_tip": "查询租赁申请成功！总数:",

    "lease_application_lease_detail_id_prompt": "请输入申请的租赁详情ID: ",
    "lease_application_audit_type_prompt": "请输入审核结果 (请输入 1 或 2, 1 -> 批准 2 -> 拒绝): ",
    "lease_application_audit_message_prompt": "请输入拒绝原因 (直接按Enter键跳过此项): ",
    "lease_application_admin_audit_success_tip": "审核租赁申请成功！",
    "lease_application_admin_audit_fail_tip": "审核租赁申请失败，请检查输入或联系系统管理员。",
    "lease_application_admin_input_error": "无效输入，请检查。",
    "lease_application_query_user_id_prompt": "请输入您要查询的租赁申请的用户ID: ",
    "lease_application_query_car_id_prompt": "请输入您要查询的租赁申请的车辆ID: ",
    "lease_application_query_no_result_tip": "没有租赁申请符合条件。",
    "lease_application_query_success_tip": "查询租赁申请成功！总数:",


}

MANAGER_LEASE_DETAILS_PAGE = {

    "lease_details_admin_welcome_tip": "欢迎来到系统租赁详情管理！ ",
    "query_details_option": "1. 查询租赁详情",
    "exit_option": "2. 返回管理员主页面",

    "lease_details_query_user_id_prompt": "请输入您要查询的租赁详情的用户ID: ",
    "lease_details_query_car_id_prompt": "请输入您要查询的租赁详情的车辆ID: ",
    "lease_details_query_no_result_tip": "没有租赁详情符合条件。",
    "lease_details_query_success_tip": "查询租赁详情成功！总数:",

}
CUSTOMER_MAIN_PAGE = {
    "welcome_tip": "欢迎来到顾客系统！",
    "view_cars_option": "1. 查看可用车辆",
    "book_car_option": "2. 预订车辆",
    "order_history_option": "3. 查看订单历史",
    "exit_option": "4. 返回主页面",

    "thank_prompt": "\n感谢您使用顾客系统，再见！",
    "customer_view_cars_make_prompt": "请输入您要查询的车辆品牌: ",
    "customer_view_cars_model_prompt": "请输入您要查询的车辆型号: ",
    "customer_view_cars_year_prompt": "请输入您要查询的车辆年份: ",
    "customer_view_cars_min_mileage_prompt": "请输入您要查询的车辆最小里程数: ",
    "customer_view_cars_max_mileage_prompt": "请输入您要查询的车辆最大里程数: ",
    "customer_view_cars_min_rent_prompt": "请输入您要查询的车辆最小日租金: ",
    "customer_view_cars_max_rent_prompt": "请输入您要查询的车辆最大日租金: ",

    "customer_view_cars_no_result_tip": "没有车辆符合条件。",
    "customer_view_cars_success_tip": "查询车辆成功！总数:",

    "customer_book_car_id_prompt": "请输入您要预订的车辆ID: ",
    "customer_book_car_start_time_prompt": "请输入租赁开始时间 (格式: 日-月-年): ",
    "customer_book_car_end_time_prompt": "请输入租赁结束时间 (格式: 日-月-年): ",
    "customer_book_car_confirm_prompt": "请确认预订，请注意总费用为 ",
    "customer_book_car_not_available_tip": "车辆当前不可用或不存在，请检查。",
    "customer_book_car_cancel_tip": "取消订单。",
    "customer_book_car_success_tip": "提交车辆预订申请成功！",
    "customer_book_car_failure_tip": "预订车辆失败，请检查输入或联系系统管理员。",
    "customer_book_invalid_interval_days_tip": "租赁天数不符合限制。最小和最大天数: ",

    "customer_order_history_no_result_tip": "没有订单符合条件。",
    "customer_order_history_success_tip": "查询订单成功！总数:",

    "customer_book_car_input_error": "无效输入，请检查。",
}
