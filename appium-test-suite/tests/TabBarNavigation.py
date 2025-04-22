import unittest
import time
from appium.options.android.common.app.auto_grant_premissions_option import AutoGrantPermissionsOption
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from appium.options.android import UiAutomator2Options
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver




# Capabilities for the Appium session
capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='pixel 7 Jarus',
    appPackage='com.eibdevel.pnc.insurance',
    appActivity='com.jarus.insurance.android.agentapp.activities.spashscreen.SplashScreen',
    language='en',
    locale='US'

)

appium_server_url = 'http://localhost:4723/'
#appium_server_url = 'http://localhost:4723/wd/hub'
capabilities_options = UiAutomator2Options().load_capabilities(capabilities)


class TestAppium(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Remote(command_executor=appium_server_url, options=capabilities_options)
        self.wait = WebDriverWait(self.driver, 40)
        print("App Loading")

    def test_loginflow(self):
        print("Before Login click")

        # Login Button
        login_button = self.wait.until(
            EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.Button[@resource-id="com.eibdevel.pnc.insurance:id/btnLogin"]'))
        )
        login_button.click()
        print("On Login page")
        time.sleep(2)

        #check the URL

        Auth0 = self.driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.android.chrome:id/url_bar"]')
        devurl = Auth0.text
        print(repr(devurl))
        actualurl = "id-dev.xinsurance.com"

        if  devurl == actualurl:
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
            EC.presence_of_element_located((AppiumBy.XPATH,
                '//android.webkit.WebView[@text="Log in | Jarus-XInsurance"]/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[2]/android.widget.EditText'
            ))
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

        #Policies Tab

        policies = self.wait.until(
            EC.element_to_be_clickable((AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="com.eibdevel.pnc.insurance:id/navigation_bar_item_icon_view"])[2]'))
        )
        policies.click()
        time.sleep(4)

        #Submit a Claim
        submitclaims = self.wait.until(
        EC.element_to_be_clickable((AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="com.eibdevel.pnc.insurance:id/navigation_bar_item_icon_view"])[3]'))
        )
        submitclaims.click()
        time.sleep(1)

        #Drivers Tab
        drivers = self.wait.until(
            EC.element_to_be_clickable((AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="com.eibdevel.pnc.insurance:id/navigation_bar_item_icon_view"])[4]'))
        )
        drivers.click()
        time.sleep(3)

        #Vehicles Tab
        vehicles = self.wait.until(
            EC.element_to_be_clickable((AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="com.eibdevel.pnc.insurance:id/navigation_bar_item_icon_view"])[5]'))
        )
        vehicles.click()
        time.sleep(3)

# Home tab clicking 
        hometab = self.wait.until(
        EC.element_to_be_clickable((AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="com.eibdevel.pnc.insurance:id/navigation_bar_item_icon_view"])[1]'))
        )
        hometab.click()        
        time.sleep(2)

         #Clicking on context menu icon 
        hamburgermenu = self.wait.until(
        EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.ImageView[@resource-id="com.eibdevel.pnc.insurance:id/app_context_menu_icon"]'))
)
        hamburgermenu.click()
        time.sleep(2)
        
        logout_popup_button = self.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.eibdevel.pnc.insurance:id/menu_text" and @text="Logout"]'))
)
        logout_popup_button.click()
        print("Logout button clicked")
        time.sleep(1)
        
        #Clicking on Log out button 
        logout_button = self.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.Button[@resource-id="android:id/button1"]'))
)
        time.sleep(1)
        logout_button.click()
        time.sleep(1)
        print("Loged out !!")
        
    def tearDown(self):
        if self.driver:
            self.driver.quit()

if __name__ == "__main__":
    unittest.main()

