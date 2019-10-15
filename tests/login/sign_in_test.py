from pages.login.login_page import LoginPage
import unittest
import pytest
import utilities.custom_logger as cl
import logging


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)

    @pytest.mark.run(order=2)
    def test_login(self):
        signedIn = self.lp.loginWith('blablaUser')
        assert signedIn == True

    @pytest.mark.run(order=1)
    def test_acceptEula(self):
        eulaAccepted = self.lp.acceptEula()
        assert eulaAccepted == True

