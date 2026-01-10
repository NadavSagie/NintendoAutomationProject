from playwright.sync_api import Page
from pages.base_page import BasePage


class Characters(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    _SUPER_MARIO = "[alt='Super Mario site']"
    _ZELDA = "[alt='The Legend of Zelda site']"
    _SPLATOON = "[alt='Splatoon site']"
    _KIRBY = "[alt='Kirby site']"
    _PIKMIN = "[alt='Pikmin site']"
    _ANIMAL_CROSSING = "[alt='Animal Crossing site']"
    _METROID = "[alt='Metroid site']"
    _POKEMON = "[alt='Pokémon site']"

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

    def click_pokemon(self):
        self.click(self._POKEMON)