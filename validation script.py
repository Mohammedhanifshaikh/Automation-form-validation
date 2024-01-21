import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import fitz  # PyMuPDF library

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page_number in range(doc.page_count):
        page = doc[page_number]
        text += page.get_text()
    doc.close()
    return text

@pytest.fixture
def driver():
    # Specify the correct path to the newly downloaded ChromeDriver executable
    chrome_driver_path = r"C:\path\to\new\chromedriver.exe"
    
    # Start Chrome browser using WebDriver
    driver = webdriver.Chrome(executable_path=chrome_driver_path)
    yield driver
    # Close the browser after the test
    driver.quit()

def test_country_validation(driver):
    # URL of the webpage
    url = "Your Path"
    driver.get(url)

    # Find the dropdown element for countries
    dropdown_element = driver.find_element(By.ID, "country")

    # Get the list of countries from the dropdown
    select = Select(dropdown_element)
    countries = [option.text for option in select.options]

    # Iterate through each country in the dropdown
    for country in countries:
        # Select the country in the dropdown
        select.select_by_visible_text(country)

        # Validate the selected country in the PDF
        pdf_path = r # Use raw string
        pdf_text = extract_text_from_pdf(pdf_path)

        assert country in pdf_text, f"Validation failed: {country} is not present in the dropdown and/or the PDF."

if __name__ == "__main__":
    # Run the tests using pytest
    pytest.main(["-v", "your_test_script.py"])  # Replace with your actual script name
