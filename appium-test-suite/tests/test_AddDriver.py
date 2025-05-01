import os
from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
import unittest
import time 

# Ensure BrowserStack credentials are set
BROWSERSTACK_USERNAME = os.getenv("BROWSERSTACK_USERNAME")
BROWSERSTACK_ACCESS_KEY = os.getenv("BROWSERSTACK_ACCESS_KEY")

if not BROWSERSTACK_USERNAME or not BROWSERSTACK_ACCESS_KEY:
    raise unittest.SkipTest("BROWSERSTACK_USERNAME and BROWSERSTACK_ACCESS_KEY are not set.")

# BrowserStack Appium server URL
appium_server_url = f"https://{BROWSERSTACK_USERNAME}:{BROWSERSTACK_ACCESS_KEY}@hub-cloud.browserstack.com/wd/hub"

# BrowserStack desired capabilities
capabilities = {
    "platformName": "Android",
    "automationName": "uiautomator2",
    "deviceName": "Google Pixel 9",
    "platformVersion": "15.0",
    "app": os.getenv("APP_URL", "bs://defaultfallbackvalue"),
    "appActivity": "com.jarus.insurance.android.agentapp.activities.spashscreen.SplashScreen",
    "language": "en",
    "locale": "US",
    "autoGrantPermissions": "true", 
    "browserstackDebug": "true"
}

class TestAppium(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Remote(
            command_executor=appium_server_url,
            options=UiAutomator2Options().load_capabilities(capabilities) 
        )
        self.wait = WebDriverWait(self.driver, 5)
        print("App Loaded on BrowserStack")

    def safe_click(self, locator, retries=3):
        for attempt in range(retries):
            try:
                element = self.wait.until(EC.element_to_be_clickable(locator))
                element.click()
                return
            except (StaleElementReferenceException, TimeoutException):
                print(f"Attempt {attempt + 1}: Retrying click on {locator}...")
                time.sleep(1)
        raise Exception(f"Failed to interact with element {locator} after {retries} retries.")

    def test_loginflow(self):
        print("On Login page")
        
        # Click Login Button
        #self.safe_click((AppiumBy.CLASS_NAME, 'android.widget.Button'))
        self.safe_click((AppiumBy.ID, 'com.eibdev.pnc.insurance:id/btnLogin'))
        
        # Enter Username
        username_field = self.wait.until(EC.presence_of_element_located((AppiumBy.CLASS_NAME, "android.widget.EditText")))
        username_field.send_keys("trainingfile")
        
        # Enter Password
        password_field = self.wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.EditText[@resource-id="password"]')))
        password_field.send_keys("Prime1234")
        
        # Click Continue
        self.safe_click((AppiumBy.XPATH, '//android.widget.Button[@text="Continue"]'))
        
        # Handle Popup
        self.safe_click((AppiumBy.XPATH, '//android.widget.Button[@resource-id="android:id/button2"]'))
        
        # Navigate to Vehicles Section
        self.safe_click((AppiumBy.XPATH, '(//android.view.ViewGroup[@resource-id="com.eibdev.pnc.insurance:id/navigation_bar_item_labels_group"])[5]'))
        
        # Click Add Vehicle
        self.safe_click((AppiumBy.CLASS_NAME, "android.widget.Button"))
        
        # Enter VIN Number
        #vin_field = self.wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.eibdev.pnc.insurance:id/edit_vin_num")')))
        #vin_field.send_keys("SCA664S5XAUX48670")

        # Year
        Year = self.wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.EditText[@resource-id="com.eibdev.pnc.insurance:id/text_input_edit_text" and @text="Year *"]')))
        Year.click()
        Year.send_keys("2002")
        self.driver.hide_keyboard()
        Make = self.wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.EditText[@resource-id="com.eibdev.pnc.insurance:id/text_input_edit_text" and @text="Make *"]')))
        Make.click()
        Make.send_keys("Volvo")
        self.driver.hide_keyboard()
        Model = self.wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.EditText[@resource-id="com.eibdev.pnc.insurance:id/text_input_edit_text" and @text="Model *"]')))
        Model.click()
        Model.send_keys("XC 90")
        self.driver.hide_keyboard()
        
        # Select Physical Damage
        Phydamage=self.wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.RadioButton[@text="Yes"]')))
        Phydamage.click()
        
        # Enter Vehicle Value
        veh_value_field = self.wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.EditText[@text="Value - Must not be zero if you require physical damage. *"]')))
        veh_value_field.send_keys("1254.22")
        
        # Enter Plate Number
        plate_field = self.wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.EditText[@text="Medallion / Plate Number / Stock Number *"]')))
        plate_field.send_keys("65985")

      
        # Click Next button 
   
        Next = self.wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.Button[@resource-id="com.eibdev.pnc.insurance:id/button"]')))
        Next.click()

       

        Submit = self.wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.Button[@text="SUBMIT"]')))
        Submit.click()

        Okbutton = self.wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.Button[@text="OK"]')))
        time.sleep(2)
        Okbutton.click()


                                                                                
        
        # Navigate to Home Page
        self.safe_click((AppiumBy.XPATH, '(//android.widget.ImageView[@content-desc="App Icon"])'))

        
        # Open Context Menu
        self.safe_click((AppiumBy.ID, 'com.eibdev.pnc.insurance:id/app_context_menu_icon'))
        
        # Click Logout
        self.safe_click((AppiumBy.XPATH, '//android.widget.TextView[@text="Logout"]'))
        print("Logout button clicked")
        
        # Confirm Logout
        self.safe_click((AppiumBy.XPATH, '//android.widget.Button[@text="OK"]'))
        print("Logged out successfully!")

    def tearDown(self):
        if self.driver: 
            self.driver.quit()


if __name__ == "__main__":
    unittest.main()
