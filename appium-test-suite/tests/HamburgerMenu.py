import os
import unittest
import time
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium import webdriver
from appium.options.android import UiAutomator2Options


class TestAppium(unittest.TestCase):
    def setUp(self):
        # BrowserStack credentials
        browserstack_user = os.getenv("shekard_3whjMa")
        browserstack_key = os.getenv("pgTv2S841Tz77ZYqzds3")

        # BrowserStack-specific capabilities
        capabilities = dict(
            platformName='Android',
            automationName='uiautomator2',
            deviceName='Google Pixel 7',
            app='bs://4447d6732192fafbc24d8fa5467e3ff325269736',  # Replace with your uploaded app's ID on BrowserStack
            language='en',
            locale='US',
            project='Appium Test Project',
            build='GitHub Actions Build',
            name='Login Flow Test',
            browserstack.debug=True,  # Optional: Enables debugging
            browserstack.networkLogs=True,  # Optional: Captures network logs
        )

        # Appium server URL for BrowserStack
        appium_server_url = 'http://hub-cloud.browserstack.com/wd/hub'
        capabilities_options = UiAutomator2Options().load_capabilities(capabilities)

        # Initialize driver
        self.driver = webdriver.Remote(command_executor=appium_server_url, options=capabilities_options)
        self.wait = WebDriverWait(self.driver, 40)
        print("App Loading")

    def test_loginflow(self):
        print("Before Login click")

        # Login Button
        login_button = self.wait.until(
            EC.element_to_be_clickable(
                (AppiumBy.XPATH, '//android.widget.Button[@resource-id="com.eibdevel.pnc.insurance:id/btnLogin"]')
            )
        )
        login_button.click()
        print("On Login page")
        time.sleep(2)

        # Check the URL
        auth0 = self.driver.find_element(
            AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.android.chrome:id/url_bar"]'
        )
        dev_url = auth0.text
        actual_url = "id-dev.xinsurance.com"

        if dev_url == actual_url:
            print("DEV ENV")
        else:
            print("UAT ENV")

        time.sleep(1)

        # Username
        username_field = self.wait.until(
            EC.presence_of_element_located((AppiumBy.CLASS_NAME, "android.widget.EditText"))
        )
        username_field.send_keys("trainingfile")

        # Password
        password_field = self.wait.until(
            EC.presence_of_element_located(
                (
                    AppiumBy.XPATH,
                    '//android.webkit.WebView[@text="Log in | Jarus-XInsurance"]/android.view.View/android.view.View/'
                    'android.view.View/android.view.View/android.view.View[2]/android.view.View[2]/android.widget.EditText',
                )
            )
        )
        password_field.send_keys("Prime1234")

        # Continue Button
        continue_button = self.wait.until(
            EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.Button[@text="Continue"]'))
        )
        continue_button.click()

        # Handle Popup
        popup_ok_button = self.wait.until(
            EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.Button[@resource-id="android:id/button1"]'))
        )
        popup_ok_button.click()
        print("On Home Page")

        self.driver.save_screenshot("homepage.png")
        time.sleep(5)

        # Interact with tabs (Policies, Submit a Claim, Drivers, Vehicles, etc.)
        tabs_xpath = [
            '(//android.widget.ImageView[@resource-id="com.eibdevel.pnc.insurance:id/navigation_bar_item_icon_view"])[2]',
            '(//android.widget.ImageView[@resource-id="com.eibdevel.pnc.insurance:id/navigation_bar_item_icon_view"])[3]',
            '(//android.widget.ImageView[@resource-id="com.eibdevel.pnc.insurance:id/navigation_bar_item_icon_view"])[4]',
            '(//android.widget.ImageView[@resource-id="com.eibdevel.pnc.insurance:id/navigation_bar_item_icon_view"])[5]',
        ]

        for tab_xpath in tabs_xpath:
            tab = self.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, tab_xpath)))
            tab.click()
            time.sleep(3)

        # Logout
        hamburger_menu = self.wait.until(
            EC.element_to_be_clickable(
                (AppiumBy.XPATH, '//android.widget.ImageView[@resource-id="com.eibdevel.pnc.insurance:id/app_context_menu_icon"]')
            )
        )
        hamburger_menu.click()
        time.sleep(2)

        logout_popup_button = self.wait.until(
            EC.element_to_be_clickable(
                (AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.eibdevel.pnc.insurance:id/menu_text" and @text="Logout"]')
            )
        )
        logout_popup_button.click()
        time.sleep(1)

        logout_button = self.wait.until(
            EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.Button[@resource-id="android:id/button1"]'))
        )
        logout_button.click()
        time.sleep(1)
        print("Logged out!")

    def tearDown(self):
        if self.driver:
            self.driver.quit()


if __name__ == "__main__":
    unittest.main()
