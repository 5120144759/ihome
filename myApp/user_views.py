import re
import random
import os

from flask import Blueprint, render_template, request, jsonify, session

from myApp.models import User
from utils import status_code
from utils.func import is_login
from utils.settings import upload_folder

user_blueprint = Blueprint('user', __name__)


@user_blueprint.route('/register/', methods=['get'])
def register():
    if request.method == 'GET':
        return render_template('register.html')


@user_blueprint.route('/get_verification/', methods=['get'])
def get_verification():
    code = ''
    s = '1234567890qwertyuiopasdfghjklzxcvbnm'
    for i in range(4):
        code += random.choice(s)
    session['code'] = code
    return jsonify(code=200, msg='请求成功', data=code)


@user_blueprint.route('/register/', methods=['post'])
def my_register():
    mobile = request.form.get('mobile')
    imageCode = request.form.get('imageCode')
    passwd = request.form.get('passwd')
    passwd2 = request.form.get('passwd2')

    # 验证参数是否完整
    if not all([mobile, imageCode, passwd, passwd2]):
        return jsonify(status_code.USER_REGISTER_PARAMS_VALID_ERROR)

    # 验证验证码是否输入正确
    if session.get('code') != imageCode:
        return jsonify(status_code.USER_REGISTER_CODE_ERROR)
    user = User()

    # 验证手机号是否符合规则
    if not re.match(r'^1\d{10}$', mobile):
        return jsonify(status_code.USER_REGISTER_MOBILE_INVALID)

    # 验证两次密码是否输入一直
    if not passwd == passwd2:
        return jsonify(status_code.USER_REGISTER_PASSWORD_SAME)

    # 验证手机号码是否存在
    if User.query.filter(User.phone == mobile).count():
        return jsonify(status_code.USER_REGISTER_MOBILE_EXSITS)

    user = User()
    user.username = mobile
    user.phone = mobile
    user.password = passwd
    try:
        user.add_update()
        return jsonify(status_code.SUCCESS)
    except:
        return jsonify(status_code.DATABASE_ERROR)


@user_blueprint.route('/login/', methods=['get'])
def login():
    return render_template('login.html')


@user_blueprint.route('/login/', methods=['post'])
def my_login():
    mobile = request.form.get('mobile')
    password = request.form.get('password')
    # 校验参数是否完整
    if not all([mobile, password]):
        return jsonify(status_code.USER_REGISTER_LOGIN_PARAMS_VALID)

    # 验证手机号是否符合规则
    if not re.match(r'^1\d{10}$', mobile):
        return jsonify(status_code.USER_REGISTER_MOBILE_INVALID)

    user = User.query.filter(User.phone == mobile).first()
    # 校验用户是否存在
    if user:
        if user.check_pwd(password):
            # 校验密码成功
            session['user_id'] = user.id
            return jsonify(status_code.SUCCESS)
        return jsonify(status_code.USER_REGISTER_PASSWORD_VALID)


@user_blueprint.route('/my/', methods=['get'])
@is_login
def my():
    return render_template('my.html')


@user_blueprint.route('/user_info/', methods=['get'])
@is_login
def user_info():
    user_id = session['user_id']
    user = User.query.get(user_id)
    user_info = user.to_basic_dict()
    return jsonify(code=status_code.OK, user_info=user_info)


@user_blueprint.route('/profile/', methods=['get'])
@is_login
def profile():
    return render_template('profile.html')


@user_blueprint.route('/logout/', methods=['get'])
def logout():
    session.clear()
    return jsonify(status_code.SUCCESS)


@user_blueprint.route('/profile/', methods=['patch'])
@is_login
def my_profile():
    # 获取头像
    avatar = request.files.get('avatar')
    # 获取用户名
    username = request.form.get('name')
    if avatar:
        # 验证图片格式是否正确
        if not re.match(r'image/*', avatar.mimetype):
            return jsonify(status_code.USER_USERINFO_PROFILE_AVATOR_INVALID)
        # 保存图片
        user_id = session['user_id']
        # 图片保存路径'static/media/upload/xxx.xxx'
        avatar.save(os.path.join(upload_folder, avatar.filename))
        # 修改用户acatar字段
        user = User.query.get(user_id)
        avatar_addr = os.path.join('upload', avatar.filename)
        user.avatar = avatar_addr
        try:
            user.add_update()
            return jsonify(code=status_code.OK, avatar=avatar_addr)
        except:
            return jsonify(status_code.DATABASE_ERROR)
    if username:
        if User.query.filter(User.username == username).count():
            return jsonify(status_code.USER_USERINFO_NAME_EXSITS)
        user = User.query.get(session['user_id'])
        user.username = username
        user.add_update()
        return jsonify(code=status_code.OK, username=user.username)


@user_blueprint.route('/auth/', methods=['get'])
@is_login
def auth():
    return render_template('auth.html')


@user_blueprint.route('/auth/', methods=['patch'])
@is_login
def my_auth():
    id_name = request.form.get('real_name')
    id_card = request.form.get('id_card')
    # 判断是否输入完整
    if not all([id_card, id_name]):
        return jsonify(status_code.USER_REGISTER_PARAMS_VALID_ERROR)
    # 判断身份证号合法
    if not re.match(r'^[1-9]\d{5}(18|19|([23]\d))\d{2}((0[1-9])|(10|11|12))(([0-2][1-9])|10|20|30|31)\d{3}[0-9Xx]$',
                    id_card):
        return jsonify(status_code.USER_USERINFO_CARD_INVALID)

    user = User.query.get(session['user_id'])
    user.id_name = id_name
    user.id_card = id_card
    try:
        user.add_update()
        return jsonify(code=status_code.OK)
    except:
        return jsonify(status_code.DATABASE_ERROR)


@user_blueprint.route('/ready_auth/', methods=['get'])
@is_login
def is_auth():
    user = User.query.get(session['user_id'])
    user = user.to_auth_dict()
    return jsonify(code=status_code.OK, user=user)
