import os
from flask import Flask
import redis
from flask_debugtoolbar import DebugToolbarExtension
from flask_session import Session

from myApp.models import db
from myApp.order_view import order_blueprint
from myApp.user_views import user_blueprint
from myApp.house_views import house_blueprint
from utils.func import get_sqlalchemy_uri
from .settings import static_folder, templates_folder, MYSQL_DATABASE, REDIS_DATABASE


def create_app():

    app = Flask(__name__, static_folder=static_folder, template_folder=templates_folder)

    app.register_blueprint(house_blueprint, url_prefix='/house')
    app.register_blueprint(user_blueprint, url_prefix='/user')
    app.register_blueprint(order_blueprint, url_prefix='/order')

    # 配置mysql
    app.config['SQLALCHEMY_DATABASE_URI'] = get_sqlalchemy_uri(MYSQL_DATABASE)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # 配置redis
    app.config['SESSION_TYPE'] = 'redis'
    app.config['SESSION_REDIS'] = redis.Redis(host=REDIS_DATABASE['HOST'],
                                              port=REDIS_DATABASE['PORT'])
    # 配置debugtoolbar
    # app.config['SECRET_KEY'] = 'secret_key'
    # app.debug=True

    db.init_app(app)

    se = Session()
    se.init_app(app)

    # debug = DebugToolbarExtension()
    # debug.init_app(app)

    return app
