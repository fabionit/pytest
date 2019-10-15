from pages.home.home_page import HomePage
from pages.login.login_page import LoginPage
import unittest
import pytest
import utilities.custom_logger as cl
import logging

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def login(self, oneTimeSetUp):
        self.home = HomePage(self.driver)
        self.login = LoginPage(self.driver)
        self.login.acceptEula()
        self.login.loginWith("blablaUser")

    @pytest.mark.run(order=1)
    def test_sequenceInTheGrid(self):
        wordsToClick = ["are", "is"]
        writtenText = self.home.writeInTheTextAreaByClickingOnTheGrid(wordsToClick)
        assert writtenText == wordsToClick


