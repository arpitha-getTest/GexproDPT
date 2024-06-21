import time
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from pageObjects.ConsensusPlanningPage import ConsensusPlanningPage
from pageObjects.LoginPage import LoginPage
from utilities.BaseClass import BaseClass
from utilities.customLogger import LogGen
from pageObjects.LandingPage import LandingPage
from selenium.webdriver.support import expected_conditions as EC


class Test002ValidateConsensusPlanningDataSelected(BaseClass):

    logger = LogGen.loggen()

    def test_click_consensus_planning(self, setup):
        self.logger.info(" ************* Test_002_Validate_Consensus_Planning_Click *************")
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.logger.info(" *************** Login to the application ***************")
        self.lp = LoginPage(self.driver)
        self.lp.set_user_name(self.username)
        self.lp.set_password(self.password)
        self.lp.click_login()
        time.sleep(1)
        self.lp.click_ok()
        time.sleep(2)
        self.logger.info(" *************** Login successful ***************")
        self.logger.info(" *************** Click on Consensus Planning block ***************")
        self.lnp = LandingPage(self.driver)
        self.lnp.click_consensus_planning_block()
        self.logger.info(" ************* Clicked on Consensus Planning ************ ")
        time.sleep(2)
        self.driver.save_screenshot(".\\Screenshots\\"+"test_homepage_title.png")
        self.logger.error(" ************ Home page title test is failed ************* ")

    def test_select_and_validate_input_data(self):
        try:
            time.sleep(2)
            self.lnp = LandingPage(self.driver)
            self.logger.info(" ************* Select input values from dropdown ************ ")
            self.logger.info(" ********* Click on Apply without selecting Site Node and check Warning message ******* ")
            self.lnp.btn_apply_clk()

            actual_msg = self.lnp.validate_warning_message_1()
            self.logger.info(actual_msg)

            if actual_msg == "Minimum one site node is required.":
                assert True
            else:
                assert False
            time.sleep(3)

            self.logger.info(" ************* Select Site Node ************ ")
            self.lnp.dropdown_sitenode_clk()
            self.lnp.dropdown_sitenode_select()
            self.logger.info(" ************* Site Node selected successfully ************ ")

            self.logger.info(" ************* Click on Apply without selecting Customer ************ ")
            self.lnp.btn_apply_clk()
            self.logger.info(" ************* Check warning message should appear ************ ")
            actual_msg = self.lnp.validate_warning_message_1()
            self.logger.info(actual_msg)

            if actual_msg == "Minimum one customer is required.":
                assert True
            else:
                assert False
            time.sleep(4)

            self.logger.info(" ************* Select customer ************ ")
            # select customer
            self.lnp.dropdown_customer_clk()
            time.sleep(1)
            self.lnp.dropdown_customer_select()
            time.sleep(1)
            self.logger.info(" ************* Customer selected successfully ************* ")
            time.sleep(1)

            self.logger.info(" ************* Click on Apply ************* ")
            self.lnp.btn_apply_clk()
            self.logger.info(" ************* Clicked on Apply successfully ************* ")

            self.cnsp = ConsensusPlanningPage(self.driver)
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((self.cnsp.validate_text_historical_sales_column())))
            self.driver.close()

        except Exception as e:
            self.logger.info("The error is: ", e)

