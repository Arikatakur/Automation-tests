import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestNavigation(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_navigation(self):
        self.driver.get("https://example.com")  # Replace with your target URL

        # Wait for and click a navigation link
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "About Us"))
        ).click()

        # Verify the page title
        self.assertIn("About Us", self.driver.title)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
