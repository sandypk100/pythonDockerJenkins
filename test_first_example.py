import pytest
from selenium import webdriver

from test_TestBasicTest import TestBasicTest


@pytest.mark.usefixtures("setup")
class TestExampleOne(TestBasicTest):



    def test_first_case_selenium_pytest(self):

        self.driver.get('https://www.google.com')
        assert "Google" == self.driver.title


    def test_second_case_selenium_pytest(self):

        self.driver.get('https://www.google.com')
        assert "Google" == self.driver.title


    def test_third_case_selenium_pytest(self):

        self.driver.get('https://www.google.com')
        assert "Google" == self.driver.title


    def test_fourth_case_selenium_pytest(self):

        self.driver.get('https://www.google.com')
        assert "Google" == self.driver.title
