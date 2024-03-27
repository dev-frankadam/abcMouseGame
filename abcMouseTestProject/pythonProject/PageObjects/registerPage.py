from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import configparser

class RegisterPage:
    def __init__(self, driver):
        self.driver = driver
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')

    def assert_url(self, expected_url):
        actual_url = self.driver.current_url
        assert actual_url == expected_url, f"Expected URL: {expected_url}, Actual URL: {actual_url}"

    def enter_email(self, email):
        shadow_host = self.driver.find_element(By.CSS_SELECTOR, "body > route-view")

        shadow_root_1 = self.driver.execute_script("return arguments[0].shadowRoot", shadow_host)

        shadow_host_2 = shadow_root_1.find_element(By.CSS_SELECTOR, "#page-component")

        shadow_root_2 = self.driver.execute_script("return arguments[0].shadowRoot", shadow_host_2)

        email_field = shadow_root_2.find_element(By.CSS_SELECTOR, "#email")

        # Send keys to the email field
        email_field.send_keys(email)

    def click_submit_button(self):
        # Execute JavaScript to locate the submit button within the shadow DOM
        submit_button_script = """
        return document.querySelector("body > route-view").shadowRoot
                    .querySelector("#page-component").shadowRoot
                    .querySelector("#submit-button");
        """
        submit_button = self.driver.execute_script(submit_button_script)

        submit_button.click()

    def wait_for_element(self, locator):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
