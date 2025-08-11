import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import time
import os
import random
from datetime import datetime, timedelta
from appium.webdriver.common.appiumby import AppiumBy
from utils.setup import driver

def test_checkin_and_leave_application(driver):
    """
    Test Case:
    1. Perform HR module Check-IN
    2. Submit a new Leave Application
    3. Capture screenshots of the confirmation
    """

    # Handle initial permission prompt (if appears)
    try:
        driver.find_element(AppiumBy.ID, "com.android.permissioncontroller:id/permission_deny_button").click()
    except:
        pass

    # Login to the app
    driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='Enter Email']").send_keys("azmin@excelbd.com")
    driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='Enter Password']").send_keys("D!m77(2SJ,5j")
    driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Login']").click()

    # Handle location/camera permission prompt (if appears)
    try:
        driver.find_element(AppiumBy.ID, "com.android.permissioncontroller:id/permission_allow_one_time_button").click()
    except:
        pass

    # Go back to close any popup screen
    driver.back()
    time.sleep(3)

    # Navigate: HR → Check-IN
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, "HR").click()
    time.sleep(1)
    driver.find_element(AppiumBy.XPATH, "//android.view.ViewGroup[@content-desc='Check-IN']").click()
    time.sleep(1)

    # Handle camera permission (if appears)
    try:
        driver.find_element(AppiumBy.ID, "com.android.permissioncontroller:id/permission_allow_one_time_button").click()
    except:
        pass

    # Confirm check-in with OK button
    time.sleep(2)
    driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@content-desc='OK']").click()
    time.sleep(2)
    driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Check-IN']").click()
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("OK")').click()

    # Navigate: HR → Leave Application
    driver.back()
    time.sleep(1)
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, "HR").click()
    driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Leave Application']").click()
    driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Application']").click()

    # Select Leave Type
    driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Leave Type*']").click()
    driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Leave Without Pay']").click()

    # Generate random leave dates
    start_date = datetime.today()
    from_date = start_date + timedelta(days=random.randint(0, 7))
    to_date = from_date + timedelta(days=random.randint(1, 7))
    from_str = from_date.strftime('%d %B %Y')
    to_str = to_date.strftime('%d %B %Y')

    # Select From Date
    driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='From Date*']").click()
    driver.find_element(AppiumBy.XPATH, f"//android.view.View[@content-desc='{from_str}']").click()
    driver.find_element(AppiumBy.ID, "android:id/button1").click()

    # Select To Date
    driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[contains(@text, 'To Date')]").click()
    driver.find_element(AppiumBy.XPATH, f"//android.view.View[@content-desc='{to_str}']").click()
    driver.find_element(AppiumBy.ID, "android:id/button1").click()

    # Enter reason and apply
    driver.find_element(AppiumBy.XPATH, "//android.widget.EditText").send_keys("I am sick")
    driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Apply']").click()

    # Confirm leave submission if confirmation appears
    try:
        driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='OK']").click()
    except:
        pass

    # Save screenshot of the result
    os.makedirs("screenshots", exist_ok=True)
    filename = f"screenshots/leave_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
    driver.save_screenshot(filename)
    print(f"Screenshot saved: {filename}")
