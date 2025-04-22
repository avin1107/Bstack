import unittest
import pytest   
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
        time.sleep(5)

    def test_loginflow(self):
        print("Before Login click")
        
        # Wait until the Login button is clickable and then click it
        login_button = self.wait.until(
            EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.Button[@resource-id="com.eibdevel.pnc.insurance:id/btnLogin"]'))
        )
        print("On Login page")
        time.sleep(1)
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
        time.sleep(1)
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
        
        # Vehicle click
        vehicleclick = self.wait.until(
        EC.element_to_be_clickable((AppiumBy.XPATH, '(//android.widget.ImageView[@content-desc="Arrow"])[1]'))
)
        time.sleep(2)
        vehicleclick.click()
        time.sleep(2)

        # Clicking Veh Id card 

        viewidcard = self.wait.until(
        EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.Button[@resource-id="com.eibdevel.pnc.insurance:id/get_certificate"]'))
        )
        time.sleep(2)
        viewidcard.click()
        time.sleep(3)

        # Swipe back 
        print("THIS IS SWIPE BACK BLOCK")
        actions = ActionChains(self.driver)
        actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(60, 1156)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(766, 1170)
        actions.w3c_actions.pointer_action.release()
        time.sleep(1)
        actions.perform()
        print("Completed swipe")
        time.sleep(2)
    # Pending tab
        vehpending = self.wait.until(
        EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.TextView[@text="PENDING"]'))
        )
        vehpending.click()
        time.sleep(2)

    #InActive tab
        vehinactive = self.wait.until(
        EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.TextView[@text="INACTIVE"]'))
        )
        vehinactive.click()
        time.sleep(4)

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
