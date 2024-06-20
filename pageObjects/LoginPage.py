from selenium.webdriver.common.by import By


class LoginPage:
    textbox_username = "//input[@type='text']"
    textbox_password = "//input[@type='password']"
    button_login = "//button[contains(text(),' Login ')]"
    button_ok = "//button[contains(text(),'Ok')]"
    container_consensus_planning = "//div[contains(text(),'Consensus Planning')]"
    cancel_btn = "//button[contains(text(),'Cancel')]"
    ok_btn = "//h2[contains(text(),'User Action Required')]"

    def __init__(self, driver):
        self.driver = driver

    def set_user_name(self, username):
        self.driver.find_element(By.XPATH, self.textbox_username).clear()
        self.driver.find_element(By.XPATH, self.textbox_username).send_keys(username)

    def set_password(self, password):
        self.driver.find_element(By.XPATH, self.textbox_password).clear()
        self.driver.find_element(By.XPATH, self.textbox_password).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH, self.button_login).click()

    def click_ok(self):
        self.driver.find_element(By.XPATH, self.button_ok).click()

    def click_cancel_btn(self):
        self.driver.find_element(By.XPATH, self.cancel_btn).click()

    def click_ok_btn(self):
        Dis = self.driver.find_element(By.XPATH, self.ok_btn).is_displayed

    # def click_ok_exists(self):
    #     self.driver.find_element(By.XPATH, self.ok_btn).isExists()

    def click_ok_(self):
        self.driver.find_element(By.XPATH, self.button_ok)
