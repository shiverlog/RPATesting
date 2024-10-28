from selenium.webdriver.common.action_chains import ActionChains


# Function to Scroll to a specific element
def scroll_to_element(driver, element):
    try:
        actions = ActionChains(driver)
        actions.move_to_element(element).perform()
        print(f"Scrolled to element: {element}")
    except Exception as e:
        print(f"Scroll failed - Error: {e}")


# Function to Scroll to the bottom of the page
def scroll_to_bottom(driver):
    try:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        print("Scrolled to the bottom of the page.")
    except Exception as e:
        print(f"Scroll to bottom failed - Error: {e}")


# Function to Scroll by a specific amount of pixels
def scroll_by_amount(driver, x, y):
    try:
        driver.execute_script(f"window.scrollBy({x}, {y});")
        print(f"Scrolled by ({x}, {y}) pixels.")
    except Exception as e:
        print(f"Scroll by amount failed - Error: {e}")


# Function to take a Screenshot
def save_screenshot(driver, file_path):
    try:
        driver.save_screenshot(file_path)
        print(f"Screenshot saved: {file_path}")
    except Exception as e:
        print(f"Screenshot save failed - Error: {e}")


# Function to handle Pop-up alerts
def handle_alert(driver, action="accept"):
    try:
        alert = driver.switch_to.alert
        if action == "accept":
            alert.accept()
            print("Alert accepted.")
        else:
            alert.dismiss()
            print("Alert dismissed.")
    except Exception as e:
        print(f"Alert handling failed - Error: {e}")


# Function to validate text of an element
def validate_element_text(element, expected_text):
    actual_text = element.text
    if actual_text == expected_text:
        print(f"Text matches: {actual_text}")
    else:
        print(f"Text mismatch - Expected: {expected_text}, Found: {actual_text}")


# Function to perform keyboard actions
def send_keys_to_element(element, keys):
    try:
        element.send_keys(keys)
        print(f"Keys sent: {keys}")
    except Exception as e:
        print(f"Sending keys failed - Error: {e}")