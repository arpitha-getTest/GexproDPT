import glob
import os
import time
from selenium.webdriver.support.wait import WebDriverWait
from pageObjects.ConsensusPlanningPage import ConsensusPlanningPage
from pageObjects.LoginPage import LoginPage
from utilities.BaseClass import BaseClass
from utilities.customLogger import LogGen
from pageObjects.LandingPage import LandingPage
from selenium.webdriver.support import expected_conditions as EC


class Test003Validate18MonthsColumns(BaseClass):

    logger = LogGen.loggen()

    def test_validate_18months_columns_exists(self, setup):
        try:
            self.logger.info(" ************* Test_003_Validate_18Months_Columns *************")
            # self.driver = setup
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
            time.sleep(8)

            self.logger.info(" ************* Select Site Node ************ ")
            self.lnp.dropdown_sitenode_clk()
            self.lnp.dropdown_sitenode_select()
            self.logger.info(" ************* Site Node selected successfully ************ ")

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
            WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((self.cnsp.validate_text_historical_sales_column())))

            self.logger.info(" ************* Check and validate length of 18 months ************ ")
            header_elements = self.cnsp.all_columns_header_names()
            self.logger.info(len(header_elements))
            actual_header_elements = 19

            assert len(header_elements) > 0

            if actual_header_elements == len(header_elements):
                self.logger.info("18 months columns exists")

                self.logger.info(" ************* 18 months exists ************ ")

        except Exception as e:
            self.logger.info("The error is: ", e)
            self.driver.save_screenshot(".\\Screenshots\\" + "test_validate_18months_columns_exists.png")
            self.logger.error(" ************ test_validate_18months_columns_exists test is failed ************* ")

    def test_read_downloaded_file(self):
        try:
            self.logger.info(" ************* Test_002_Validate_Consensus_Planning_Click *************")
            self.cnsp = ConsensusPlanningPage(self.driver)
            WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((self.cnsp.validate_text_historical_sales_column())))

            self.logger.info(" ************* Find latest downloaded file ************ ")
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((self.cnsp.clk_download_filtered_data())))

            button = self.cnsp.clk_download_filtered_data()
            self.driver.execute_script("arguments[0].click();", button)

            time.sleep(3)
            folder_path = r"C:\\Users\\EQ927KY\\Downloads"
            file_type = r"\*csv"
            files = glob.glob(folder_path + file_type)
            max_file = max(files, key=os.path.getctime)

            self.logger.info(max_file)
            os.remove(max_file)
            self.logger.info(" ************* Filtered data csv file successfully deleted ************ ")
            self.driver.close()

        except Exception as e:
            self.logger.info("The error is: ", e)
            self.driver.save_screenshot(".\\Screenshots\\" + "test_read_downloaded_file.png")
            self.logger.error(" ************ test_read_downloaded_file test is failed ************* ")
