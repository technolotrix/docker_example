import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    BROWSER = "chrome"
    LOCAL_SELENIUM = False
    #COMMAND_EXECUTOR = os.environ['IP']


class DevelopmentConfig(Config):
    DEBUG = True
    LOCAL_SELENIUM = False


class ProductionConfig(Config):
    DEBUG = False


APP_SETTINGS = DevelopmentConfig if os.environ.get('TARGET') in ('dev', ) \
    else ProductionConfig