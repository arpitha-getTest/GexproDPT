from selenium.webdriver.common.by import By


class ConsensusPlanningPage:
    def __init__(self, driver):
        self.driver = driver

    all_columns_header = "//div[@style='width: 302.2px;']"
    circle_loader = "//div[@class='circle-loader']"
    text_historical_sales_column = "//span[text()='Historical Sales']"
    btn_download_filtered_data = "//button[@title='Download Filtered Data']"

    def all_columns_header_names(self):
        return self.driver.find_elements(By.XPATH, self.all_columns_header)

    def validate_text_historical_sales_column(self):
        return self.driver.find_element(By.XPATH, self.text_historical_sales_column)

    def clk_download_filtered_data(self):
        return self.driver.find_element(By.XPATH, self.btn_download_filtered_data)

    def wait_for_circle_loader(self):
        return self.driver.find_element(By.XPATH, self.circle_loader)
