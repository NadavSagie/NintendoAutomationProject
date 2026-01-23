import time

from playwright.sync_api import Page
from pages.base_page import BasePage
from playwright.sync_api import expect



class Support(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    _SUPPORT = "#support-tab"
    _MY_SUPPORT_DASHBOARD = "[data-testid='MySupportDashboardIcon']"
    _ACCOUNTS_AND_PURCHASES = "[data-testid='SupportAccountsPurchasesIcon']"
    _NINTENDO_SWITCH = "[data-testid='SupportNintendoSwitchLogoIcon']"
    _NINTENDO_SWITCH_2 = "[data-testid='SupportNintendoSwitch2LogoIcon']"
    _NINTENDO_SWITCH_ONLINE = "[data-testid='NsoIcon']"
    _APPS_AND_OTHER = "[data-testid='SupportAppsOtherProductsIcon']"
    _REPAIR = "[data-testid='SupportRepairIcon']"
    _SUPPORT_HOME = ".YSMyD"
    _NINTENDO_SWITCH_GAME_SUPPORT = "[data-ref='Game Support']"
    _SEARCH_BAR = "#rn_KeywordText_11"
    _SELECT_FIRST_RESULTS = "[start='1'] > li:nth-child(1) a"

    def click_support(self):
        self.click(self._SUPPORT)

    def click_my_support_dashboard(self):
        self.click(self._MY_SUPPORT_DASHBOARD)

    def click_account_and_purchases(self):
        self.click(self._ACCOUNTS_AND_PURCHASES)

    def click_nintendo_switch_2(self):
        self.click(self._NINTENDO_SWITCH_2)

    def click_nintendo_switch(self):
        self.click(self._NINTENDO_SWITCH)

    def click_nintendo_switch_online(self):
        self.click(self._NINTENDO_SWITCH_ONLINE)

    def click_apps_and_other(self):
        self.click(self._APPS_AND_OTHER)

    def click_repair(self):
        self.click(self._REPAIR)

    def click_support_home(self):
        self.click(self._SUPPORT_HOME)

    def full_process_for_searching_bug(self):
        self.click(self._NINTENDO_SWITCH)
        self.page.get_by_role("link", name="United States English").click()
        self.click(self._NINTENDO_SWITCH_GAME_SUPPORT)
        self.click(self._SEARCH_BAR)
        self.type(self._SEARCH_BAR, "display")
        self.page.keyboard.press("Enter")
        self.click(self._SELECT_FIRST_RESULTS)
        self.page.locator("h1").wait_for(state="visible", timeout=10_000)
        return self.verify_title()

    def verify_title(self):
        return self.page.locator("h1").inner_text().strip()

