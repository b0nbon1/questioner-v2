import os


class Config():
    """Parent configuration class."""
    DEBUG = False
    TESTING = False


class Development(Config):
    """Configurations for Development."""
    DEBUG = True
    TESTING = True
    DATABASE_URL = os.getenv('DATABASE_URL')


class Testing(Config):
    """Configurations for Testing, with a separate test database."""
    DEBUG = True
    TESTING = True
    DATABASE_URL = os.getenv("DATABASE_TEST_URL")


app_config = {
    "development": Development,
    "testing": Testin}
