import os
from flask_uploads import IMAGES
basedir = os.path.abspath(os.path.dirname(__file__))

class config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'liangzzh'

    UPLOADED_AVATAR_DEST = './app/static/avatar'
    UPLOADED_AVATAR_ALLOW = IMAGES

    MAIL_SERVER = 'smtp.qq.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or '473230218@qq.com'
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or 'babsiqflogfycafc'
    MAIL_SUBJECT_PREFIX = 'NEW USER COMING'
    MAIL_SENDER = '473230218@qq.com'
    PROJECT_ADMIN = '473230218@qq.com'

    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')

config = {
    'development' : DevelopmentConfig
}