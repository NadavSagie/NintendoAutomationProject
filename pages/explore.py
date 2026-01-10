<<<<<<< HEAD
from playwright.sync_api import Page
from pages.base_page import BasePage


class Explore(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    _EXPLORE = "#explore-tab"
    _NINTENDO_SWITCH_2 = ".sc-1empns-0.edpYZm.abGCC:nth-child(1)"
    _NINTENDO_SWITCH = ".sc-1empns-0.edpYZm.abGCC:nth-child(2)"
    _GAMES = ".sc-1empns-0.edpYZm.abGCC:nth-child(3)"
    _NINTENDO_SWITCH_ONLINE = ".sc-1empns-0.edpYZm.abGCC:nth-child(4)"
    _NEWS_AND_EVENTS = "a:nth-child(1) > span.sc-1k9k6ch-2.clfwsO"
    _PLAY_NINTENDO = "a:nth-child(2) > span.sc-1k9k6ch-2.clfwsO"
    _MY_NINTENDO = "a:nth-child(3) > span.sc-1k9k6ch-2.clfwsO"
    _APPS = "a:nth-child(4) > span.sc-1k9k6ch-2.clfwsO"
    _SUPER_MARIO = "div.Mb4lk > a:nth-child(2) > span"
    _ZELDA = "div.Mb4lk > a:nth-child(3) > span"
    _SPLATOON = "div.Mb4lk > a:nth-child(4) > span"
    _KIRBY = "div.Mb4lk > a:nth-child(5) > span"
    _PIKMIN = "div.Mb4lk > a:nth-child(6) > span"
    _ANIMAL_CROSSING = "div.Mb4lk > a:nth-child(7) > span"
    _METROID = "div.Mb4lk > a:nth-child(8) > span"

    def click_explore(self):
        self.click(self._EXPLORE)

    def click_nintendo_switch_2(self):
        self.click(self._NINTENDO_SWITCH_2)

    def click_nintendo_switch(self):
        self.click(self._NINTENDO_SWITCH)

    def click_games(self):
        self.click(self._GAMES)

    def click_nintendo_switch_online(self):
        self.click(self._NINTENDO_SWITCH_ONLINE)

    def click_news_and_events(self):
        self.click(self._NEWS_AND_EVENTS)

    def click_play_nintendo(self):
        self.click(self._PLAY_NINTENDO)

    def click_my_nintendo(self):
        self.click(self._MY_NINTENDO)

    def click_apps(self):
        self.click(self._APPS)

    def click_super_mario(self):
        self.click(self._SUPER_MARIO)

    def click_zelda(self):
        self.click(self._ZELDA)

    def click_splatoon(self):
        self.click(self._SPLATOON)

    def click_kirby(self):
        self.click(self._KIRBY)

    def click_pikmin(self):
        self.click(self._PIKMIN)

    def click_animal_crossing(self):
        self.click(self._ANIMAL_CROSSING)

    def click_metroid(self):
        self.click(self._METROID)
=======
from playwright.sync_api import Page
from pages.base_page import BasePage


class Explore(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    _EXPLORE = "#explore-tab"
    _NINTENDO_SWITCH_2 = ".sc-1empns-0.edpYZm.abGCC:nth-child(1)"
    _NINTENDO_SWITCH = ".sc-1empns-0.edpYZm.abGCC:nth-child(2)"
    _GAMES = ".sc-1empns-0.edpYZm.abGCC:nth-child(3)"
    _NINTENDO_SWITCH_ONLINE = ".sc-1empns-0.edpYZm.abGCC:nth-child(4)"
    _NEWS_AND_EVENTS = "a:nth-child(1) > span.sc-1k9k6ch-2.clfwsO"
    _PLAY_NINTENDO = "a:nth-child(2) > span.sc-1k9k6ch-2.clfwsO"
    _MY_NINTENDO = "a:nth-child(3) > span.sc-1k9k6ch-2.clfwsO"
    _APPS = "a:nth-child(4) > span.sc-1k9k6ch-2.clfwsO"
    _SUPER_MARIO = "div.Mb4lk > a:nth-child(2) > span"
    _ZELDA = "div.Mb4lk > a:nth-child(3) > span"
    _SPLATOON = "div.Mb4lk > a:nth-child(4) > span"
    _KIRBY = "div.Mb4lk > a:nth-child(5) > span"
    _PIKMIN = "div.Mb4lk > a:nth-child(6) > span"
    _ANIMAL_CROSSING = "div.Mb4lk > a:nth-child(7) > span"
    _METROID = "div.Mb4lk > a:nth-child(8) > span"

    def click_explore(self):
        self.click(self._EXPLORE)

    def click_nintendo_switch_2(self):
        self.click(self._NINTENDO_SWITCH_2)

    def click_nintendo_switch(self):
        self.click(self._NINTENDO_SWITCH)

    def click_games(self):
        self.click(self._GAMES)

    def click_nintendo_switch_online(self):
        self.click(self._NINTENDO_SWITCH_ONLINE)

    def click_news_and_events(self):
        self.click(self._NEWS_AND_EVENTS)

    def click_play_nintendo(self):
        self.click(self._PLAY_NINTENDO)

    def click_my_nintendo(self):
        self.click(self._MY_NINTENDO)

    def click_apps(self):
        self.click(self._APPS)

    def click_super_mario(self):
        self.click(self._SUPER_MARIO)

    def click_zelda(self):
        self.click(self._ZELDA)

    def click_splatoon(self):
        self.click(self._SPLATOON)

    def click_kirby(self):
        self.click(self._KIRBY)

    def click_pikmin(self):
        self.click(self._PIKMIN)

    def click_animal_crossing(self):
        self.click(self._ANIMAL_CROSSING)

    def click_metroid(self):
        self.click(self._METROID)
>>>>>>> master
