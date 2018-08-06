from functools import wraps
from flask import session, redirect, url_for

def get_sqlalchemy_uri(MYSQL_DATABASE):

    return '%s+%s://%s:%s@%s:%s/%s' % (MYSQL_DATABASE['ENGINE'],
                                       MYSQL_DATABASE['DRIVER'],
                                       MYSQL_DATABASE['USER'],
                                       MYSQL_DATABASE['PASSWORD'],
                                       MYSQL_DATABASE['HOST'],
                                       MYSQL_DATABASE['PORT'],
                                       MYSQL_DATABASE['DB'])

def is_login(func):

    @wraps(func)
    def check_login(*args, **kwargs):
        if 'user_id' in session:
            return func(*args, **kwargs)
        else:
            return redirect(url_for('user.login'))
    return check_login
