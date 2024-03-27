import time
from PageObjects.homePage import HomePage
from PageObjects.registerPage import RegisterPage
from PageObjects.subscriptionPage import SubscriptionPage
from basePage import BaseTest
import config
from faker import Faker

class TestAbcMouseSignup(BaseTest):
    def test_signup_flow(self):
        fake = Faker()
        fake_email = fake.email()

        home_page = HomePage(self.driver)
        home_page.get_url(config.URL)  # Moved URL access to HomePage
        home_page.click_signup_button()

        time.sleep(10)

        register_page = RegisterPage(self.driver)
        register_page.assert_url(config.ASSERT_REGISTRATION_URL)
        register_page.enter_email(fake_email)
        time.sleep(10)
        register_page.click_submit_button()
        time.sleep(10)


        subscription_page = SubscriptionPage(self.driver)
        register_page.assert_url(config.ASSERT_SUBSCRIPTION_URL)
        subscription_page.verify_text_present(config.ASSERT_TEXT)
