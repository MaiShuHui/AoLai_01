from selenium.webdriver.common.by import By

log_number = By.ID,"com.vcooline.aike:id/etxt_username"
log_password = By.ID,"com.vcooline.aike:id/etxt_pwd"
log_enter = By.ID,"com.vcooline.aike:id/btn_login"

set_shousuo = By.ID,"com.android.settings:id/search"
set_shuru = By.ID,"android:id/search_src_text"
set_fanhui = By.CLASS_NAME,"android.widget.ImageButton"

# 点击我
al_wo =  By.ID,"com.yunmall.lc:id/tab_me"
# 点击已有账号登录
al_zh = By.ID,"com.yunmall.lc:id/textView1"
# 输入账号框
al_number = By.ID,"com.yunmall.lc:id/logon_account_textview"
# 输入密码框
al_password = By.ID,"com.yunmall.lc:id/logon_password_textview"
# 点击登录按钮
al_btn = By.ID,"com.yunmall.lc:id/logon_button"
# 定位昵称
al_username =By.ID,"com.yunmall.lc:id/tv_user_nikename"
# 定位设置
al_setting = By.ID,"com.yunmall.lc:id/ymtitlebar_left_btn_image"
# 定位消息推送
al_pust = By.ID,"com.yunmall.lc:id/setting_notification"
# 定位修改密码
al_log_pwd =By.ID,"com.yunmall.lc:id/setting_modify_pwd"
# 点击退出
al_click_logout =By.ID,"com.yunmall.lc:id/setting_logout"
# 确认退出
al_logout_ok = By.ID,"com.yunmall.lc:id/ymdialog_right_button"
# 点击购物车
al_gw = By.ID,"com.yunmall.lc:id/tab_shopping_cart"


"""以下数据为 地址管理配置数据"""
# 地址管理
address_manage = By.ID,"com.yunmall.lc:id/setting_address_manage"
# 新增地址
address_add_new_btn = By.ID, "com.yunmall.lc:id/address_add_new_btn"
# 收件人
address_receipt_name = By.ID , "com.yunmall.lc:id/address_receipt_name"
# 电话
address_add_phone = By.ID, "com.yunmall.lc:id/address_add_phone"
# 所在区域
address_area = By.ID, "com.yunmall.lc:id/address_province"
# 省  id重复 只能使用text

# 市  class = "android.widget.RelativeLayout"
shi = By.ID ,"com.yunmall.lc:id/area_title"
# 区 使用 text

# 输入详细地址
address_detail_addr_info = By.ID, "com.yunmall.lc:id/address_detail_addr_info"
# 输入邮编
address_post_code = By.ID, "com.yunmall.lc:id/address_post_code"
# 设为默认地址
address_default = By.ID, "com.yunmall.lc:id/address_default"
# 保存
address_save = By.ID, "com.yunmall.lc:id/button_send"
# 获取名字和电话
address_name_phone = By.ID,"com.yunmall.lc:id/receipt_name"
# 确认删除信息
address_delete_ok = By.ID, "com.yunmall.lc:id/ymdialog_left_button"




tp_login = By.CLASS_NAME,"red"
tp_number = By.ID,"username"
tp_password = By.ID,"password"
tp_verify = By.ID,"verify_code"
tp_btn = By.CLASS_NAME,"J-login-submit"

