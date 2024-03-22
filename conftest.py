import pytest
from selenium import webdriver

@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()  # Assuming chromedriver is in your PATH
    yield driver
    driver.quit()

# Add your test functions below using the 'driver' fixture
