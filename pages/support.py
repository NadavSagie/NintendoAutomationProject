from playwright.sync_api import Page
from pages.base_page import BasePage


class Support(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    _MY_SUPPORT_DASHBOARD = "div._2-bt5 > a:nth-child(1)"
    _NINTENDO_SWITCH_FAMILY = "div._2-bt5 > a:nth-child(2)"
    _OTHER_SYSTEMS = "div._2-bt5 > a:nth-child(3)"
    _ACCOUNTS_MY_NINTENDO = "div._2-bt5 > a:nth-child(4)"
    _REPAIR = "div._2-bt5 > a:nth-child(5)"
    _SUPPORT_HOME = ".YSMyD"
    

    def click_my_support_dashboard(self):
        self.click(self._MY_SUPPORT_DASHBOARD)

    def click_nintendo_switch_family(self):
        self.click(self._NINTENDO_SWITCH_FAMILY)

    def click_other_systems(self):
        self.click(self._OTHER_SYSTEMS)

    def click_accounts_my_nintendo(self):
        self.click(self._ACCOUNTS_MY_NINTENDO)

    def click_repair(self):
        self.click(self._REPAIR)

    def click_support_home(self):
        self.click(self._SUPPORT_HOME)