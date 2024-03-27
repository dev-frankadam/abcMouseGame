from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SubscriptionPage:
    def __init__(self, driver):
        self.driver = driver

    def verify_text_present(self, text):
        text_script = """
        return document.querySelector("body > route-view").shadowRoot
                    .querySelector("#page-component").shadowRoot
                    .querySelector("#become-member").textContent;
        """
        actual_text = self.driver.execute_script(text_script)

        # Assert the expected text is present
        assert text in actual_text, f"Expected text '{text}' is not present on the page"

    def wait_for_element(self, locator):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
