
# system messages
OPTION_TIPS = "以下のオプションを選択してください: "
INPUT_PROMPT = "オプションを入力してください: "
INVALID_INPUT_PROMPT = "入力が無効です、確認してください。"
PENDING_PROMPT = "Enterキーを押して続行..."
SKIP_TIP = "(この項目をスキップするにはEnterキーを押してください) "

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
    "welcome_tip": "カーレンタルシステムへようこそ！",
    "register_option": "1. 新規ユーザーアカウントを登録",
    "login_option": "2. システムにログイン",
    "exit_option": "3. システムを終了",
    "thank_prompt": "\nご利用ありがとうございました、またお会いしましょう！"
}

USER_PAGE = {
    "input_username_prompt": "ユーザー名を入力してください: ",
    "input_password_prompt": "パスワードを入力してください: ",
    "invalid_input_tip": "ユーザー名またはパスワードが無効です、確認してください。",
    "login_success_tip": "ログインに成功しました！",
    "register_success_tip": "登録に成功しました！",
    "register_fail_tip": "登録に失敗しました、このユーザー名は既に使用されています。"

}

MANAGER_MAIN_PAGE = {
    "welcome_tip": "管理者管理システムへようこそ！",
    "user_admin_option": "1. ユーザー管理",
    "car_admin_option": "2. 車両管理",
    "lease_application_admin_option": "3. リース申請管理",
    "lease_details_admin_option": "4. リース詳細管理",
    "exit_option": "5. メインページに戻る",
    "thank_prompt": "\n管理者システムのご利用ありがとうございました、またお会いしましょう！",
}

MANAGER_USER_PAGE = {
    "user_admin_welcome_tip": "システムユーザーの管理へようこそ！",
    "create_user_option": "1. 新規ユーザーを作成",
    "delete_user_option": "2. ユーザーを削除",
    "update_user_option": "3. ユーザーを更新",
    "query_user_option": "4. オプション条件でユーザーを検索",
    "exit_option": "5. 管理者メインページに戻る",

    "user_admin_add_user_prompt": "ユーザー名を入力してください: ",
    "user_admin_add_password_prompt": "パスワードを入力してください: ",
    "user_admin_add_role_prompt": "役割タイプを入力してください (0または1を入力、0 -> 顧客 1 -> 管理者): ",
    "user_admin_add_success_tip": "ユーザーの追加に成功しました！",
    "user_admin_add_fail_tip": "ユーザーの追加に失敗しました、このユーザー名は既に使用されています。",

    "user_admin_delete_user_prompt": "削除したいユーザー名を入力してください: ",
    "user_admin_delete_success_tip": "ユーザーの削除に成功しました！",
    "user_admin_delete_fail_tip": "ユーザーの削除に失敗しました、このユーザー名は存在しません。",

    "user_admin_update_username_prompt": "更新したいユーザー名を入力してください: ",
    "user_admin_update_password_prompt": "新しいパスワードを入力してください: ",
    "user_admin_update_role_prompt": "新しい役割タイプを入力してください (0または1を入力、0 -> 顧客 1 -> 管理者): ",
    "user_admin_update_success_tip": "ユーザーの更新に成功しました！",
    "user_admin_update_fail_tip": "ユーザーの更新に失敗しました、このユーザー名は存在しません。",

    "user_admin_query_username_prompt": "検索したいユーザー名を入力してください (この項目を無視するにはEnterキーを押してください): ",
    "user_admin_query_role_prompt": "検索したい役割タイプを入力してください (0または1を入力、0 -> 顧客 1 -> 管理者、この項目を無視するにはEnterキーを押してください): ",
    "user_admin_query_success_tip": "ユーザーの検索に成功しました！合計件数:",
    "user_admin_query_no_result_tip": "条件に一致するユーザーはいません。",
    "user_admin_query_columns": "id | ユーザー名 | パスワード | 役割タイプ | 削除フラグ | 作成時間 | 削除時間 | 更新時間"

}

MANAGER_CAR_PAGE = {
    "car_admin_welcome_tip": "システム車両の管理へようこそ！",
    "create_car_option": "1. 新規車両を作成",
    "delete_car_option": "2. 車両を削除",
    "update_car_option": "3. 車両を更新",
    "query_car_option": "4. オプション条件で車両を検索",
    "query_all_cars_option": "5. 全ての車両を表示",
    "exit_option": "6. 管理者メインページに戻る",

    "car_admin_id_prompt": "車両のIDを入力してください: ",
    "car_admin_make_prompt": "車両のメーカーを入力してください: ",
    "car_admin_model_prompt": "車両のモデルを入力してください: ",
    "car_admin_year_prompt": "車両の年式を入力してください: ",
    "car_admin_mileage_prompt": "車両の走行距離を入力してください: ",
    "car_admin_manufacturer_prompt": "車両の製造元を入力してください: ",
    "car_admin_daily_rent_prompt": "車両の日額レンタル料金を入力してください: ",
    "car_admin_extra_fee_prompt": "車両の追加料金を入力してください: ",
    "car_admin_min_leasing_days_prompt": "車両の最小リース日数を入力してください: ",
    "car_admin_max_leasing_days_prompt": "車両の最大リース日数を入力してください: ",
    "car_admin_input_error": "入力が無効です、確認してください。",
    "car_admin_add_success_tip": "車両の追加に成功しました！",
    "car_admin_add_failure_tip": "車両の追加に失敗しました、入力内容を確認するかシステム管理者にお問い合わせください。",

    "car_admin_update_success_tip": "車両の更新に成功しました！",
    "car_admin_update_failure_tip": "車両の更新に失敗しました、車両IDが存在することを確認してください。",

    "car_admin_delete_car_prompt": "削除したい車両のIDを入力してください: ",
    "car_admin_delete_success_tip": "車両の削除に成功しました！",
    "car_admin_delete_failure_tip": "車両の削除に失敗しました、車両IDが存在することを確認してください。",

    "car_admin_query_min_mileage_prompt": "検索したい車両の最小走行距離を入力してください: ",
    "car_admin_query_max_mileage_prompt": "検索したい車両の最大走行距離を入力してください: ",
    "car_admin_query_min_rent_prompt": "検索したい車両の最小日額レンタル料金を入力してください: ",
    "car_admin_query_max_rent_prompt": "検索したい車両の最大日額レンタル料金を入力してください: ",
    "car_admin_query_make_prompt": "検索したい車両のメーカーを入力してください: ",
    "car_admin_query_model_prompt": "検索したい車両のモデルを入力してください: ",
    "car_admin_query_year_prompt": "検索したい車両の年式を入力してください: ",
    "car_admin_query_available_prompt": "検索したい車両の利用可能ステータスを入力してください (0または1を入力、0 -> 利用不可 1 -> 利用可能): ",
    "car_admin_query_success_tip": "車両の検索に成功しました！合計件数:",
    "car_admin_query_no_result_tip": "条件に一致する車両はありません。",

}

MANAGER_LEASE_APPLICATION_PAGE = {

    "lease_application_admin_welcome_tip": "システムリース申請の管理へようこそ！",
    "query_application_option": "1. 審査待ちのリース申請を検索",
    "audit_application_option": "2. リース申請を審査",
    "exit_option": "3. 管理者メインページに戻る",

    "lease_application_admin_query_no_result_tip": "条件に一致するリース申請はありません。",
    "lease_application_admin_query_success_tip": "リース申請の検索に成功しました！合計件数:",

    "lease_application_lease_detail_id_prompt": "申請のリース詳細IDを入力してください: ",
    "lease_application_audit_type_prompt": "審査結果を入力してください (1または2を入力、1 -> 承認 2 -> 拒否): ",
    "lease_application_audit_message_prompt": "拒否理由を入力してください (この項目をスキップするにはEnterキーを押してください): ",
    "lease_application_admin_audit_success_tip": "リース申請の審査に成功しました！",
    "lease_application_admin_audit_fail_tip": "リース申請の審査に失敗しました、入力内容を確認するかシステム管理者にお問い合わせください。",
    "lease_application_admin_input_error": "入力が無効です、確認してください。",
    "lease_application_query_user_id_prompt": "検索したいリース申請のユーザーIDを入力してください: ",
    "lease_application_query_car_id_prompt": "検索したいリース申請の車両IDを入力してください: ",
    "lease_application_query_no_result_tip": "条件に一致するリース申請はありません。",
    "lease_application_query_success_tip": "リース申請の検索に成功しました！合計件数:",

}

MANAGER_LEASE_DETAILS_PAGE = {

    "lease_details_admin_welcome_tip": "システムリース詳細の管理へようこそ！",
    "query_details_option": "1. リース詳細を検索",
    "exit_option": "2. 管理者メインページに戻る",

    "lease_details_query_user_id_prompt": "検索したいリース詳細のユーザーIDを入力してください: ",
    "lease_details_query_car_id_prompt": "検索したいリース詳細の車両IDを入力してください: ",
    "lease_details_query_no_result_tip": "条件に一致するリース詳細はありません。",
    "lease_details_query_success_tip": "リース詳細の検索に成功しました！合計件数:",

}
CUSTOMER_MAIN_PAGE = {
    "welcome_tip": "顧客システムへようこそ！",
    "view_cars_option": "1. 利用可能な車両を表示",
    "view_all_cars_option": "2. 全ての車両を表示",
    "book_car_option": "3. 車両を予約",
    "order_history_option": "4. 注文履歴を表示",
    "exit_option": "5. メインページに戻る",

    "thank_prompt": "\n顧客システムのご利用ありがとうございました、またお会いしましょう！",
    "customer_view_cars_make_prompt": "検索したい車両のメーカーを入力してください: ",
    "customer_view_cars_model_prompt": "検索したい車両のモデルを入力してください: ",
    "customer_view_cars_year_prompt": "検索したい車両の年式を入力してください: ",
    "customer_view_cars_min_mileage_prompt": "検索したい車両の最小走行距離を入力してください: ",
    "customer_view_cars_max_mileage_prompt": "検索したい車両の最大走行距離を入力してください: ",
    "customer_view_cars_min_rent_prompt": "検索したい車両の最小日額レンタル料金を入力してください: ",
    "customer_view_cars_max_rent_prompt": "検索したい車両の最大日額レンタル料金を入力してください: ",

    "customer_view_cars_no_result_tip": "条件に一致する車両はありません。",
    "customer_view_cars_success_tip": "車両の検索に成功しました！合計件数:",

    "customer_book_car_id_prompt": "予約したい車両のIDを入力してください: ",
    "customer_book_car_start_time_prompt": "リースの開始時間を入力してください (形式: dd-mm-yyyy): ",
    "customer_book_car_end_time_prompt": "リースの終了時間を入力してください (形式: dd-mm-yyyy): ",
    "customer_book_car_confirm_prompt": "予約を確定してください、合計料金は ",
    "customer_book_car_not_available_tip": "この車両は現在利用できないか、存在しません、確認してください。",
    "customer_book_car_cancel_tip": "注文をキャンセルしました。",
    "customer_book_car_success_tip": "車両予約の申請を送信しました！",
    "customer_book_car_failure_tip": "車両の予約に失敗しました、入力内容を確認するかシステム管理者にお問い合わせください。",
    "customer_book_invalid_interval_days_tip": "レンタル日数が制限を満たしていません。最小および最大日数: ",

    "customer_order_history_no_result_tip": "条件に一致する注文はありません。",
    "customer_order_history_success_tip": "注文の検索に成功しました！合計件数:",

    "customer_book_car_input_error": "入力が無効です、確認してください。",
}