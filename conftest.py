import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
@pytest.fixture(scope="class")
def setup(request):
    print("initiating chrome driver")
    #options = Options()
    #options.add_argument('--headless')
    #options.add_argument('--disable-gpu')  # Last I checked this was necessary.
    #driver = webdriver.Chrome("/usr/lib/chromium/chromedriver", chrome_options=options)
    desiredCapabilities = DesiredCapabilities.CHROME.copy()
    driver = webdriver.Remote('http://143.244.176.53:4444/wd/hub', desired_capabilities=desiredCapabilities)

    driver.get("http://google.com")
    driver.maximize_window()
    request.cls.driver=driver

    yield driver
    driver.close()
