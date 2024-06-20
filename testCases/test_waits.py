import time
from selenium.webdriver.common.by import By

from pageObjects.LoginPage import LoginPage
from utilities.BaseClass import BaseClass
from utilities.customLogger import LogGen
from utilities.ActionClass import Actions


class Test001Login(BaseClass):

    logger = LogGen.loggen()

    # def test_homepage_title(self):
    #
    #     self.logger.info("*********** Test_001_Login ***********")
    #     self.logger.info(" ************* Verifying Home Page Title ************* ")
    #     # self.driver = setup
    #     self.driver.get(self.baseURL)
    #     actual_title = self.driver.title
    #     if actual_title == "Asterisk":
    #         assert True
    #         self.logger.info(" ************** Home page title test is passed ************* ")
    #     else:
    #         self.driver.save_screenshot(".\\Screenshots\\"+"test_homepage_title.png")
    #         self.logger.error(" ************ Home page title test is failed ************* ")
    #         assert False

    def test_login(self, setup):
        self.logger.info(" ************* Verifying Login test ************* ")
        # self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.set_user_name(self.username)
        self.lp.set_password(self.password)
        time.sleep(2)
        self.lp.click_login()
        # time.sleep(2)
        ac = Actions.wait_and_click_element(self.driver, 10, By.XPATH, self.lp.button_ok)
        # self.lp.click_ok()
        time.sleep(2)
        # self.lp.click_consensus_planning_block()
        act_title = self.driver.title
        if act_title == "Asterisk":
            assert True
            self.logger.info(" *************** Login test is passed ************* ")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.logger.error(" ************** Login test is failed ************** ")
            assert False
        self.driver.close()



