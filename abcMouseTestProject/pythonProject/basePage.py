from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium_stealth import stealth
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class BaseTest:
    def setup_method(self, method):
        options = Options()
        options.add_argument("start-maximized")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)


        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

        # Selenium Stealth settings
        stealth(self.driver,
                languages=["en-US", "en"],
                vendor="Google Inc.",
                platform="Win32",
                webgl_vendor="Intel Inc.",
                renderer="Intel Iris OpenGL Engine",
                fix_hairline=True,
                )

        self.driver.implicitly_wait(10)




    def teardown_method(self, method):
        self.driver.quit()

    def get_url(self, url):
        self.driver.get(url)

    def wait_for_element(self, locator):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))

    def verify_text(self, locator, expected_text):
        element = self.driver.find_element(*locator)
        assert element.text == expected_text
