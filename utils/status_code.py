
OK = 200
SUCCESS = {'code': 200, 'msg': '请求成功'}
DATABASE_ERROR = {'code': 500, 'msg': '数据库卵了'}

# 用户模块
USER_REGISTER_CODE_ERROR = {'code': 1000, 'msg': '验证码错误'}
USER_REGISTER_PARAMS_VALID_ERROR = {'code': 1001, 'msg': '请填写完整的注册参数'}
USER_REGISTER_MOBILE_INVALID = {'code': 1003, 'msg': '手机号不正确'}
USER_REGISTER_PASSWORD_SAME = {'code': 1004, 'msg': '两次密码不同'}
USER_REGISTER_MOBILE_EXSITS = {'code': 1004, 'msg': '手机号已存在'}

USER_REGISTER_PASSWORD_INVALID = {'code': 1005, 'msg': '手机号不正确'}
USER_REGISTER_LOGIN_PARAMS_VALID = {'code': 1006, 'msg': '请填写完整的登录信息'}
USER_REGISTER_PASSWORD_VALID = {'code': 1007, 'msg': '密码错误'}

USER_USERINFO_PROFILE_AVATOR_INVALID = {'code': 1008, 'msg': '请上传正确图片格式'}
USER_USERINFO_NAME_EXSITS = {'code': 1009, 'msg': '用户名已存在'}
USER_USERINFO_CARD_INVALID = {'code': 1010, 'msg': '身份证不合法'}

# 房屋模块
HOUSE_USER_INFO_VERIFIED = {'code': 1100, 'msg':'用户未实名认证'}