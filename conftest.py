import pytest
import mysql.connector
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os


# Database connection fixture
@pytest.fixture(scope="class")
def db_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='rpa',
            password='rpa!1111',
            database='rpa-test'
        )
        cursor = connection.cursor(dictionary=True)
        yield cursor
    finally:
        cursor.close()
        connection.close()


# Fixture to initialize WebDriver
@pytest.fixture(scope="class")
def setup(request):
    options = Options()
    options.add_experimental_option("detach", True)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument('start-maximized')

    # Set ChromeDriver path
    chromedriver_path = os.getenv('CHROME_DRIVER_PATH', 'E:\\KTAlphaTestAutomation\\chromedriver.exe')
    service = Service(executable_path=chromedriver_path)

    # Initialize WebDriver
    driver = webdriver.Chrome(service=service, options=options)
    base_url = "https://m.kshop.co.kr/display/ec/display/main"
    driver.get(base_url)
    request.cls.driver = driver

    yield

    driver.quit()


# Fixture to perform dynamic login using DB account
@pytest.fixture(scope="class")
def login(request, setup, db_connection):
    driver = request.cls.driver
    cursor = db_connection

    # Fetch test account from the database
    cursor.execute("SELECT username, password FROM test_accounts LIMIT 1")
    account = cursor.fetchone()

    if account:
        username = account['username']
        password = account['password']

        # Perform login
        driver.get("https://example.com/login")  # Replace with your login URL
        driver.find_element("id", "username").send_keys(username)
        driver.find_element("id", "password").send_keys(password)
        driver.find_element("id", "login_button").click()
        print(f"Login successful with user: {username}")
    else:
        print("No test account found in the database.")


# Hook to capture screenshots on test failure
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield  # Run the test and capture the result
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.cls.driver  # Access the WebDriver from the test class
        screenshot_path = f"screenshots/{item.name}.png"
        driver.save_screenshot(screenshot_path)
        print(f"Screenshot saved: {screenshot_path}")
