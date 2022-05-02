class ProdConfig():
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False

class DevConfig():
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True

CORP_SERVER = "https://corp.applifting.cz/api" # dev/prod
# CORP_SERVER = "https://staging.corp.applifting.cz/api" # testing