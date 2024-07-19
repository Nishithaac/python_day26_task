import pytest

# Importing data and locators from respective modules
from TestData.HomepageData import Data
from TestLocators.HomepageLocators import Locators

# Importing necessary Selenium components
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Define the test class
class Test_IMDB:

    # Fixture to set up the browser instance

    @pytest.fixture
    def booting_function(self):
        # Initialize Chrome WebDriver with WebDriver Manager
        self.driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        # Maximize the browser window
        self.driver.maximize_window()
        # Initialize WebDriverWait
        self.wait=WebDriverWait(self.driver,10)
        # Test execution happens here
        yield
        # Teardown: Close the browser instance after tests
        self.driver.close()

    # Test to verify the web page title
    def test_get_title(self,booting_function):
        # Open the URL from test data
        self.driver.get(Data().url)
        # Assert the page title matches expected
        assert self.driver.title==Data().title
        # Print success message
        print("Success : Web Page title is verified")

    # Test to verify the current URL matches expected URL
    def test_verify_url(self,booting_function):
        # Open the URL from test data
        self.driver.get(Data().url)
        # Assert current URL matches expected URL
        assert self.driver.current_url==Data().url
        # Print success message
        print("SUCCESS : Home page URL verified")

    # Test to perform a search operation
    def test_search(self,booting_function):
        try:
            # Open the URL from test data
            self.driver.get(Data().url)
            # Scroll the page
            self.driver.execute_script('window.scrollBy(0, 500)')

            # Click on the name option
            name_option = self.wait.until(EC.element_to_be_clickable((By.XPATH,Locators().name_option)))
            self.driver.execute_script("arguments[0].click();", name_option)

            # Enter name input
            name_input = self.wait.until(EC.visibility_of_element_located((By.XPATH, Locators().name_input)))
            name_input.send_keys(Data().name_input)

            # Click on birth option
            birth_option = self.wait.until(EC.element_to_be_clickable((By.XPATH, Locators().birth_option)))
            self.driver.execute_script("arguments[0].click();", birth_option)

            # Enter birth inputs
            birth_input1 = self.wait.until(EC.visibility_of_element_located((By.XPATH, Locators().birth_input1)))
            birth_input1.send_keys(Data().birth_input1)

            birth_input2 = self.wait.until(EC.visibility_of_element_located((By.XPATH, Locators().birth_input2)))
            birth_input2.send_keys(Data().birth_input2)

            # Click on birthday
            birthday = self.wait.until(EC.element_to_be_clickable((By.XPATH, Locators().birthday)))
            self.driver.execute_script("arguments[0].click();", birthday)

            # Enter birthday input
            birthday_input = self.wait.until(EC.visibility_of_element_located((By.XPATH, Locators().birthday_input)))
            birthday_input.send_keys(Data.birthday_input)

            # Click on awards option
            awards_option = self.wait.until(EC.element_to_be_clickable((By.XPATH, Locators().awards_option)))
            self.driver.execute_script("arguments[0].click();", awards_option)

            # Click on awards input
            awards_input = self.wait.until(EC.visibility_of_element_located((By.XPATH, Locators().awards_input)))
            self.driver.execute_script("arguments[0].click();", awards_input)

            # Click on search box
            search_box = self.wait.until(EC.element_to_be_clickable((By.XPATH, Locators().search_box)))
            self.driver.execute_script("arguments[0].click();", search_box)

            # Verify search results are displayed
            search_results=self.wait.until(EC.visibility_of_element_located((By.XPATH,Locators().search_results)))
            assert search_results.is_displayed()
            # Print the message
            print("SUCCESS : Result displayed")



        except NoSuchElementException as e:
            # Print any NoSuchElementException encountered
            print(e)
