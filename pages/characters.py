from playwright.sync_api import Page
from pages.base_page import BasePage


class Characters(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    _SUPER_MARIO = "[aria-label='Mario']"
    _ZELDA = "[aria-label='Link']"
    _SPLATOON = "[aria-label='Splatoon']"
    _KIRBY = "[aria-label='Kirby']"
    _PIKMIN = "div:nth-child(6) > a > div.sc-bxi6rv-4.fQoaGi.hCSeY"
    _ANIMAL_CROSSING = "[aria-label='Tom Nook and Isabelle']"
    METROID = "div:nth-child(8) > a > div.sc-bxi6rv-4.fQoaGi.hCSeY"
    _POKEMON = "div:nth-child(9) > a > div.sc-bxi6rv-4.fQoaGi.hCSeY"

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
        self.click(self.METROID)

    def click_pokemon(self):
        self.click(self._POKEMON)
