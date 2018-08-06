import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 配置静态文件地址
static_folder = os.path.join(BASE_DIR, 'static')

# 配置模板地址
templates_folder = os.path.join(BASE_DIR, 'templates')

# 配置图片保存地址
media_folder = os.path.join(static_folder, 'media')
upload_folder = os.path.join(media_folder, 'upload')

# 配置mysql
MYSQL_DATABASE = {
    'USER': 'root',
    'PASSWORD': 'zxc4141567',
    'HOST': '127.0.0.1',
    'PORT': '3306',
    'DB': 'ihome',
    'ENGINE': 'mysql',
    'DRIVER': 'pymysql',
}

# 配置redis-
REDIS_DATABASE = {
    'HOST': '127.0.0.1',
    'PORT': '6379',
}
