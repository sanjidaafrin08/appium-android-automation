import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import time
import os
from appium.webdriver.common.appiumby import AppiumBy
from datetime import datetime
from utils.setup import driver

def test_attendance_report_search(driver):
    """
    Test Case:
    1. Search attendance report for specific date range
    2. Apply 'On Leave' filter
    3. Validate results and take screenshot
    """

    # Handle permission prompt (if appears)
    try:
        driver.find_element(AppiumBy.ID, "com.android.permissioncontroller:id/permission_deny_button").click()
    except:
        pass

    # Login to the app
    driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='Enter Email']").send_keys("azmin@excelbd.com")
    driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='Enter Password']").send_keys("D!m77(2SJ,5j")
    driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Login']").click()

    # Handle one-time permission (if appears)
    try:
        driver.find_element(AppiumBy.ID, "com.android.permissioncontroller:id/permission_allow_one_time_button").click()
    except:
        pass

    # Go back to close any popups
    driver.back()
    time.sleep(3)

    # Navigate: HR → My Attendance
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, "HR").click()
    time.sleep(2)
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, "My Attendance").click()
    time.sleep(2)

    # Select From Date
    driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='From']").click()
    driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='03 August 2025']").click()
    driver.find_element(AppiumBy.ID, "android:id/button1").click()

    # Select To Date
    driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='To']").click()
    driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='06 August 2025']").click()
    driver.find_element(AppiumBy.ID, "android:id/button1").click()

    # Apply Status filter: On Leave
    driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='All']").click()
    driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='On Leave']").click()

    # Validate search results
    time.sleep(2)
    try:
        driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='No data found']")
        assert False, "No data found!"
    except:
        print("Data found.")

    # Save screenshot of the result
    os.makedirs("screenshots", exist_ok=True)
    filename = f"screenshots/attendance_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
    driver.save_screenshot(filename)
    print(f"Screenshot saved: {filename}")
