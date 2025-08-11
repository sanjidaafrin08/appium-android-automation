import pytest
from appium import webdriver
from appium.options.common import AppiumOptions

@pytest.fixture(scope="module")
def driver():
    """
    Pytest fixture to initialize and provide the Appium driver instance.
    Scope: module (reused for all tests in the same module)
    """

    # Desired capabilities for the mobile test environment
    desired_caps = {
        "platformName": "Android",                       # Target platform
        "appium:platformVersion": "14",                  # Android version
        "appium:deviceName": "JRZP55WOVCBAQSOJ",          # Device name (emulator/real device)
        "appium:udid": "JRZP55WOVCBAQSOJ",                # Device unique ID
        "appium:appPackage": "com.arcone.arcone",         # Application package name
        "appium:appActivity": "com.arcone.arcone.MainActivity",  # Launch activity
        "appium:noReset": True,                           # Keep app state between sessions
        "appium:automationName": "UiAutomator2",          # Automation engine
        "appium:ignoreHiddenApiPolicyError": True         # Ignore hidden API policy errors
    }

    # Appium server URL
    url = 'http://127.0.0.1:4723'

    # Initialize driver with AppiumOptions
    driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(desired_caps))

    # Implicit wait for element search
    driver.implicitly_wait(30)

    # Provide driver to tests
    yield driver

    # Quit driver after all tests in the module finish
    driver.quit()
