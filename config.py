import os


class Config:
    DEBUG = True
    SECRET_KEY = os.urandom(24)
    TESTING = False
    # DATABASE_URL=postgresql://postgres@localhost:{port}/{dbname}
    SQLALCHEMY_DATABASE_URI = f"postgresql://{os.getenv('DB_USER')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
    # os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    pass


class TestingConfig(Config):
    pass


class ProductionConfig(Config):
    pass


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
