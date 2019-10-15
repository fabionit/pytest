import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
from utilities.util import Util
from pages.home.home_page import HomePage


class LoginPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.util = Util
        self.homePage = HomePage

    # Locators
    _agree_button = "agree"
    _create_new_user = "createUserInputinput"
    _text_area_input = "prc-custom-textarea"
    _next_button = "create-user-btn"
    _unity_vocabs_modal = "tile-3"
    _unity_84_vocab_btn = "btn-system-selection-control-38"
    _get_started_btn = "finish-selecting-default-vocabulary"
    _keyboard_finished_btn = "keyboard-enter-button"


    def userName(self, name):

        return f"//*[contains(text(),'{name}')]"

    def acceptEula(self):
        eulaAccepted = False
        self.waitForElement(self._agree_button)
        while self.isElementPresent(self._agree_button):
            self.elementClick(self._agree_button)
            eulaAccepted = True
        return eulaAccepted


    def giveUserName(self, name):
        noUsers = self.isElementPresent(self._create_new_user)
        if (noUsers) :
            self.waitForElement(self._create_new_user)
            self.elementClick(self._create_new_user)
            self.waitForElement(self._text_area_input)
            self.sendKeys(data=name, locator=self._text_area_input)
            self.elementClick(self._keyboard_finished_btn)
            self.elementClick(self._next_button)
        return noUsers

    def selectVocabForNewUser(self):
        self.waitForElement(self._unity_vocabs_modal)
        self.elementClick(self._unity_vocabs_modal)
        self.elementClick(self._unity_84_vocab_btn)
        self.elementClick(self._get_started_btn)


    def loginWith(self, username):
        user = self.giveUserName(username)
        if user:
            self.selectVocabForNewUser()
        else:
            user = self.userName(username)
            self.elementClick(locator=user, locatorType="xpath")
            self.waitForElement(locator=self.homePage._vocab_grid, locatorType="css")

        return self.isElementPresent(locator=self.homePage._vocab_grid, locatorType="css")

