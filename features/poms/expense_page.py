from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class ExpensePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def login_button(self):
        element: WebElement = self.driver.find_element_by_id("login_button")
        return element

    def login_email(self):
        element: WebElement = self.driver.find_element_by_id(
            "form-email-input")
        return element

    def login_password(self):
        element: WebElement = self.driver.find_element_by_id(
            "form-password-input")
        return element

    def submit_button(self):
        element: WebElement = self.driver.find_element_by_id(
            "form-submit-button")
        return element

    def reset_button(self):
        element: WebElement = self.driver.find_element_by_id(
            "form-reset-button")
        return element
