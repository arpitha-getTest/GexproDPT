from selenium.webdriver.common.by import By


class LandingPage:
    def __init__(self, driver):
        self.driver = driver

    btn_Apply = "//button[contains(text(),'Apply')]"
    warning_message_1 = "(//h2[contains(@id,'swal2-title')])[1]"
    clk_siteNode = "//span[contains(text(),'Select Site')]"
    select_siteNode = "//li/span[contains(text(),'AT01')]"
    container_consensus_planning = "//div[contains(text(),'Consensus Planning')]"
    clk_customer = "//span[contains(text(),'Select Cus')]"
    select_customer = "//span[contains(text(),'ACME')]"


    def click_consensus_planning_block(self):
        self.driver.find_element(By.XPATH, self.container_consensus_planning).click()

    def btn_apply_clk(self):
        self.driver.find_element(By.XPATH, self.btn_Apply).click()

    def validate_warning_message_1(self):
        return self.driver.find_element(By.XPATH, self.warning_message_1).text

    def dropdown_sitenode_clk(self):
        return self.driver.find_element(By.XPATH, self.clk_siteNode).click()

    def dropdown_sitenode_select(self):
        return self.driver.find_element(By.XPATH, self.select_siteNode).click()

    def dropdown_customer_clk(self):
        return self.driver.find_element(By.XPATH, self.clk_customer).click()

    def dropdown_customer_select(self):
        return self.driver.find_element(By.XPATH, self.select_customer).click()


