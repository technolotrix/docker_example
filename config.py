import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    BROWSER = "chrome"
    LOCAL_SELENIUM = False
    COMMAND_EXECUTOR = 'http://192.168.1.10:4444/wd/hub'


class DevelopmentConfig(Config):
    DEBUG = True
    LOCAL_SELENIUM = False


class ProductionConfig(Config):
    DEBUG = False


APP_SETTINGS = DevelopmentConfig if os.environ.get('TARGET') in ('dev', ) \
    else ProductionConfig