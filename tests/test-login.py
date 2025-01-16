import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()  # Ensure chromedriver.exe is in PATH or the same directory

    def test_login(self):
        self.driver.get("https://example.com/login")  # Replace with your target URL

        # Locate and interact with elements
        self.driver.find_element(By.ID, "username").send_keys("test_user")
        self.driver.find_element(By.ID, "password").send_keys("secure_password")
        self.driver.find_element(By.ID, "login-button").click()

        # Assert that login is successful
        welcome_message = self.driver.find_element(By.ID, "welcome-message")
        self.assertIn("Welcome", welcome_message.text)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
