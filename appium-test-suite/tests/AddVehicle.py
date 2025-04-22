import unittest
import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.options.android import UiAutomator2Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.actions.interaction import Interaction
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.actions import interaction

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

appium_server_url = 'http://localhost:4723'

# Converts capabilities to UiAutomator2Options instance
capabilities_options = UiAutomator2Options().load_capabilities(capabilities)

class TestAppium(unittest.TestCase):
    def setUp(self):
        # Start Appium session
        self.driver = webdriver.Remote(command_executor=appium_server_url, options=capabilities_options)
        
        # Explicit wait for the app to load completely by waiting for the login button to appear
        self.wait = WebDriverWait(self.driver, 20)  # Use this wait instance throughout
        print("App Loading")

    def test_loginflow(self):
        print("Before Login click")
        
        # Wait until the Login button is clickable and then click it
        login_button = self.wait.until(
            EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.Button[@resource-id="com.eibdevel.pnc.insurance:id/btnLogin"]'))
        )
        print("On Login page")
        login_button.click()
        time.sleep(3)

        # Locate the username field and input the username
        username_field = self.wait.until(
            EC.presence_of_element_located((AppiumBy.CLASS_NAME, "android.widget.EditText"))
        )
        username_field.send_keys("trainingfile")

        # Locate the password field and input the password
        password_field = self.wait.until(
            EC.presence_of_element_located((AppiumBy.XPATH,
                '//android.webkit.WebView[@text="Log in | Jarus-XInsurance"]/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[2]/android.widget.EditText'
            ))
        )
        password_field.send_keys("Prime1234")

        # Click the "Continue" button
        continue_button = self.wait.until(
            EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.Button[@text="Continue"]'))
        )
        continue_button.click()
        time.sleep(2)

        # Wait for any potential popup and dismiss it
        popup_ok_button = self.wait.until(
            EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.Button[@resource-id="android:id/button1"]'))
        )
        time.sleep(2)
        popup_ok_button.click()
        time.sleep(2)
        
        print("On Home Page")

        # Vehicles section click action
        vehiclessection = self.wait.until(
            EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="com.eibdevel.pnc.insurance:id/cv_vehicle"]/android.view.ViewGroup/android.widget.LinearLayout[1]'))
        )
        time.sleep(2)
        vehiclessection.click()
        time.sleep(2)
        
    # Add Vehicle feature 
        addvehicle =  self.wait.until(
            EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.Button[@resource-id="com.eibdevel.pnc.insurance:id/add_vehicle"]'))
        )
        time.sleep(1)
        addvehicle.click()
        time.sleep(2)

    # Add vehicle form
        vin = self.wait.until(
            EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.EditText[@resource-id="com.eibdevel.pnc.insurance:id/edit_vin_num"]'))
        )
        vin.send_keys("SCA664S5XAUX48670")

        vinlookup = self.wait.until(
            EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.Button[@resource-id="com.eibdevel.pnc.insurance:id/vin_search"]'))
            )
        vinlookup.click()
        time.sleep(5)

        physicaldamage = self.wait.until(
            EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.RadioButton[@text="Yes"]'))
            )
        physicaldamage.click()
        time.sleep(1)

        vehvalue = self.wait.until(
            EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.EditText[@resource-id="com.eibdevel.pnc.insurance:id/text_input_edit_text" and @text="Value - Must not be zero if you require physical damage. *"]'))
            )
        vehvalue.send_keys("1254.22")

        platenum = self.wait.until(
            EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.EditText[@resource-id="com.eibdevel.pnc.insurance:id/text_input_edit_text" and @text="Medallion / Plate Number / Stock Number *"]'))
            )
        platenum.send_keys("65985")

        time.sleep(2)
        next = self.wait.until(
            EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.Button[@resource-id="com.eibdevel.pnc.insurance:id/button"]'))
            )
        time.sleep(2)
        next.click()
        time.sleep(5)
        submit = self.wait.until(
            EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.Button[@resource-id="com.eibdevel.pnc.insurance:id/button"]'))
            )
        submit.click()
        time.sleep(5)
        popuptext = self.wait.until(
            EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.TextView[@resource-id="android:id/message"]'))
            )
        popuptextmsg = popuptext.text
        print(popuptextmsg)
        actualpopupmsg = "Request to add vehicle successful.  Please allow up to 48 hours to process."
        if actualpopupmsg == popuptextmsg:
            print("Vehicle add req success")
        else:
            print("Add Vehicle req FAILED")
        confirmpopup = self.wait.until(
            EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.Button[@resource-id="android:id/button1"]'))
            )
        confirmpopup.click()
        time.sleep(3)
        
        

    #Home page 
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
