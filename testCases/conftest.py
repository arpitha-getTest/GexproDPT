import os.path
from datetime import datetime

from selenium import webdriver
import pytest


@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Edge()
    # driver.get(url="https://gexproservices-asterisksc-uat.ey.com/auth/login")
    driver.maximize_window()
    request.cls.driver = driver
    yield


def pytest_addoption(parser):
    parser.addoption("--browser")


# @pytest.fixture()
# def browser(request):
#     return request.config.getoption("--browser")


# It is a hook to delete/modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)

# Specifying report folder location and Save with timestamp
@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    config.option.htmlpath = os.path.abspath(os.curdir)+"\\Reports\\"+datetime.now().strftime("%d-%m-%Y %H-%M-%S")+".html"