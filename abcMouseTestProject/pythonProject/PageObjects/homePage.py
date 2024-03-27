from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def get_url(self, url):
        self.driver.get(url)

    def click_signup_button(self):
        shadow_host = self.driver.find_element(By.CSS_SELECTOR, "body > route-view")

        # Get the first shadow root
        shadow_root_1 = self.driver.execute_script("return arguments[0].shadowRoot", shadow_host)

        # Find the second shadow host
        shadow_host_2 = shadow_root_1.find_element(By.CSS_SELECTOR, "#page-component")

        # Get the second shadow root
        shadow_root_2 = self.driver.execute_script("return arguments[0].shadowRoot", shadow_host_2)

        # Find the desired element within the shadow DOM
        desired_element = shadow_root_2.find_element(By.CSS_SELECTOR,
                                                     "main-layout > header > home-header > authstate-context:nth-child(3) > signup-button")

        # Click on the desired element
        desired_element.click()

    def wait_for_element(self, locator):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
