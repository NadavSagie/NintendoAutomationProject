from playwright.sync_api import Page
from pages.base_page import BasePage


class ShopMerchandise(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    _GAMES = ".gUkqje > a:nth-child(1) > h2"
    _HARDWARE = ".gUkqje > a:nth-child(2) > h2"
    _MERCHANDISE = ".gUkqje > a:nth-child(3) > h2"
    _STORE_EXCLUSIVES = ".gUkqje > a:nth-child(4) > h2"
    _CHARACTERS = ".gUkqje > a:nth-child(5) > h2"
    _SALES_AND_DEALS = ".gUkqje > a:nth-child(6) > h2"

    def click_games(self):
        self.click(self._GAMES)

    def click_hardware(self):
        self.click(self._HARDWARE)

    def click_merchandise(self):
        self.click(self._MERCHANDISE)

    def click_store_exclusives(self):
        self.click(self._STORE_EXCLUSIVES)

    def click_characters(self):
        self.click(self._CHARACTERS)

    def click_sales_and_deals(self):
        self.click(self._SALES_AND_DEALS)