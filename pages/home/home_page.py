import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
from utilities.util import Util


class HomePage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.utilities = Util

    # Locators
    _vocab_grid = ".vocabulary-grid"
    _text_area = ".input.textarea"

    def _button_with_text(self, text):
        return f"//span[contains(text(),'{text}')]"

    def _activity_btn_id(self,id):
        return f"button[id*=item-{id}]"

    def writeInTheTextAreaByClickingOnTheGrid(self, stringToWrite):
        wordsWritten = []
        self.waitForElement(self._vocab_grid, "css", 30)
        for string in stringToWrite:
            stringLocator = self._button_with_text(string)
            self.elementClick(locator=stringLocator, locatorType="xpath")
            wordsWritten.append(string)
        return wordsWritten

    def clickRandomlyInActivity(self):
        self.waitForElement(self._vocab_grid, "css", 30)
        idsToClick = []
        btnsText = []
        while (len(idsToClick) < 3):
            randomNr = self.util.getAlphaNumeric(1, "digits")
            idsToClick.extend(randomNr)

        for id in idsToClick:
            buttonId = self._activity_btn_id(id)
            self.waitForElement(self._activity_btn_id, "css")
            text = self.getText(locator=buttonId, locatorType="css")
            btnsText.append(text)
            self.elementClick(buttonId, "css")
        return btnsText







