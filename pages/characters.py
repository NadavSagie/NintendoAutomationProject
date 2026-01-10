from playwright.sync_api import Page
from pages.base_page import BasePage


class Characters(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    _SUPER_MARIO = "[aria-label='Super Mario site']"
    _ZELDA = "[aria-label='The Legend of Zelda site']"
    _SPLATOON = "[aria-label='Splatoon site']"
    _KIRBY = "[aria-label='Kirby site']"
    _PIKMIN = "[aria-label='Pikmin site']"
    _ANIMAL_CROSSING = "[aria-label='Animal Crossing site']"
    METROID = "[aria-label='Metroid site']"
    _POKEMON = "[aria-label='Pokémon site']"

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