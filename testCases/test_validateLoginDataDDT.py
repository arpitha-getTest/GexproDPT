import os.path

import time
from selenium.webdriver.common.by import By

from pageObjects.LoginPage import LoginPage
from utilities import XLUtils
# from pageObjects.LoginPage import LoginPage
from utilities.BaseClass import BaseClass
from utilities.customLogger import LogGen
from utilities.ActionClass import Actions


class TestLoginDDT(BaseClass):
    logger = LogGen.loggen()
    path = os.path.abspath(os.curdir) + "\\TestData\\GexproDPT_LoginDetails.xlsx"

    def test_login_ddt(self, setup):
        self.logger.info(" ************* Verifying Login test by DDT ************* ")
        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        lst_status = []
        self.lp = LoginPage(self.driver)

        time.sleep(2)
        self.driver.get(self.baseURL)
        for r in range(2, self.rows + 1):
            self.username = XLUtils.readData(self.path, "Sheet1", r, 1)
            time.sleep(2)
            self.password = XLUtils.readData(self.path, "Sheet1", r, 2)
            self.exp = XLUtils.readData(self.path, "Sheet1", r, 3)
            time.sleep(2)
            self.lp.set_user_name(self.username)
            self.lp.set_password(self.password)
            time.sleep(2)
            self.lp.click_login()
            time.sleep(3)

            if self.exp == 'Valid':
                # if self.lp.click_ok_btn:
                lst_status.append('Pass')
                b = self.driver.find_element(By.XPATH,"//button[contains(text(),'Cancel')]")
                self.driver.execute_script("arguments[0].click();", b)
                self.logger.info("Logged in with Valid creds")

            elif self.exp == 'Invalid':
                self.logger.info("Logged in with Invalid creds")
                self.logger.info(str(self.lp.click_ok_btn)+"Testing")
                if self.lp.click_ok_btn is True:

                    lst_status.append('Fail')
                else:
                    lst_status.append('Pass')

        # final validation
            if "Fail" not in lst_status:
                assert True
            else:
                assert False
