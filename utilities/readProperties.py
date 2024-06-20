import configparser

import pytest

config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")


# @pytest.fixture()
class ReadConfig:
    @staticmethod
    def get_application_url():
        url = config.get('access info', 'baseURL')
        return url

    @staticmethod
    def get_username():
        username = config.get('access info', 'username')
        return username

    @staticmethod
    def get_password():
        password = config.get('access info', 'password')
        return password

