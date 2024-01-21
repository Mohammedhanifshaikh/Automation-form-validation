import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

@pytest.fixture
def driver():
    # Start Chrome browser using WebDriver
    driver = webdriver.Chrome()
    yield driver
    # Close the browser after the test
    driver.quit()

def test_google_search(driver):
    # Open the Google homepage
    driver.get("https://www.google.com")

    # Find the search box by its name attribute value
    search_box = driver.find_element("name", "q")

    # Type a search query
    search_box.send_keys("Selenium automation")

    # Press the Enter key to perform the search
    search_box.send_keys(Keys.RETURN)

    # Assert that the search results page title contains the search query
    assert "Selenium automation" in driver.title

    # Optionally, you can perform more assertions or validations
    # For example, check if specific search results are present
    # results = driver.find_elements_by_css_selector("h3")
    # assert len(results) > 0

if __name__ == "__main__":
    # Run the tests using pytest
    pytest.main(["-v", "test_google_search.py"])
