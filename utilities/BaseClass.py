import time

import pytest
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig


@pytest.mark.usefixtures("setup")
class BaseClass:
    baseURL = ReadConfig.get_application_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()

