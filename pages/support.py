from playwright.sync_api import Page
from pages.base_page import BasePage


class Support(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    _MY_SUPPORT_DASHBOARD = "div._2-bt5 > a:nth-child(1)"
    _VERIFY_MY_SUPPORT_DASHBOARD = ".header-title"
    _ACCOUNTS_AND_PURCHASES = "div._2-bt5 > a:nth-child(2)"
    _NINTENDO_SWITCH_2 = "div._2-bt5 > a:nth-child(3)"
    _ACCOUNTS_MY_NINTENDO = "div._2-bt5 > a:nth-child(4)"
    _REPAIR = "div._2-bt5 > a:nth-child(5)"
    _SUPPORT_HOME = ".YSMyD"

    def click_my_support_dashboard(self):
        self.click(self._MY_SUPPORT_DASHBOARD)

    def verify_click_my_support_dashboard(self):
        return self.page.inner_text(self._VERIFY_MY_SUPPORT_DASHBOARD)

    def click_nintendo_switch_family(self):
        self.click(self._ACCOUNTS_AND_PURCHASES)

    def click_other_systems(self):
        self.click(self._NINTENDO_SWITCH_2)

    def click_accounts_my_nintendo(self):
        self.click(self._ACCOUNTS_MY_NINTENDO)

    def click_repair(self):
        self.click(self._REPAIR)

    def click_support_home(self):
        self.page.locator(self._SUPPORT_HOME).wait_for(state="visible", timeout=10000)
        self.page.locator(self._SUPPORT_HOME).click()