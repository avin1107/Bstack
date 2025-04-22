import unittest
import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.options.android import UiAutomator2Options

# Capabilities for the Appium session
capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='pixel 7 Jarus',
    appPackage='com.eibdevel.pnc.insurance',
    appActivity='com.jarus.insurance.android.agentapp.activities.spashscreen.SplashScreen',
    language='en',
    locale='US' ,
    app= 'bs://4447d6732192fafbc24d8fa5467e3ff325269736'    
)

appium_server_url = 'http://localhost:4723'
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
            EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.Button[@resource-id="android:id/button2"]'))
        )
        btnname = popup_ok_button.text
        print(btnname)
        popup_ok_button.click()
        time.sleep(2)
        print("On Home Page")

        # Driver Add
        drivertab = self.wait.until(
            EC.element_to_be_clickable((AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="com.eibdevel.pnc.insurance:id/navigation_bar_item_icon_view"])[4]'))
        )
        drivertab.click()

        driveradd = self.wait.until(
            EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.Button[@resource-id="com.eibdevel.pnc.insurance:id/add_driver"]'))
        )
        driveradd.click()

        # Fill Driver Details
        drivername = self.wait.until(
            EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.EditText[@resource-id="com.eibdevel.pnc.insurance:id/text_input_edit_text" and @text="Name *"]'))
        )
        drivername.send_keys("Driver Add Test")

        dateofbirth = self.wait.until(
            EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.EditText[@resource-id="com.eibdevel.pnc.insurance:id/text_input_edit_text" and @text="Date of Birth *"]'))
        )
    
        time.sleep(2)
        dateofbirth.send_keys("11/04/2000")
        self.driver.press_keycode(66)
        dateofbirth.click()
        
        
        calendarokbtn = self.wait.until(
            EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.Button[@resource-id="android:id/button1"]'))
        )
        calendarokbtn.click()
        time.sleep(1)

        license = self.wait.until(
            EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.EditText[@resource-id="com.eibdevel.pnc.insurance:id/text_input_edit_text" and @text="License Number *"]'))
        )
        license.send_keys("DLFAP1234456")

        stateofissue = self.wait.until(
            EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.EditText[@resource-id="com.eibdevel.pnc.insurance:id/text_input_edit_text" and @text="State of Issue"]'))
        )
        stateofissue.send_keys("Colorado")

        next_button = self.wait.until(
            EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.Button[@resource-id="com.eibdevel.pnc.insurance:id/button"]'))
        )
        time.sleep(2)
        next_button.click()

        time.sleep(2)
        adddriversubmit = self.wait.until(
            EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.Button[@resource-id="com.eibdevel.pnc.insurance:id/button"]'))
        )
        adddriversubmit.click()
        time.sleep(3)

        confirmmsg = self.wait.until(
            EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.eibdevel.pnc.insurance:id/page_label"]'))
        )
        confirmmsgtext = confirmmsg.text
        actualmsg = "Add Driver Request Submission"
        
        if actualmsg == confirmmsgtext:
            print("Driver add req success")
        else:
            print("Driver add req FAILED")

        
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
