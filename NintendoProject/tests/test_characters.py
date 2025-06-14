from tests.base_test import BaseTest
import allure

@allure.epic("Nintendo Characters Tests")
class TestCharacters(BaseTest):

    def setup_method(self):
        self.page.goto("https://www.nintendo.com/us/")

    @allure.title("Click Super Mario Character")
    def test_click_super_mario(self):
        self.characters.click_super_mario()
        assert "mario" in self.page.url.lower()

    @allure.title("Click Zelda Character")
    def test_click_zelda(self):
        self.characters.click_zelda()
        assert "zelda" in self.page.url.lower()

    @allure.title("Click Splatoon Character")
    def test_click_splatoon(self):
        self.characters.click_splatoon()
        assert "splatoon" in self.page.url.lower()

    @allure.title("Click Kirby Character")
    def test_click_kirby(self):
        self.characters.click_kirby()
        assert "kirby" in self.page.url.lower()

    @allure.title("Click Pikmin Character")
    def test_click_pikmin(self):
        self.characters.click_pikmin()
        assert "pikmin" in self.page.url.lower()

    @allure.title("Click Animal Crossing Character")
    def test_click_animal_crossing(self):
        self.characters.click_animal_crossing()
        assert "animalcrossing" in self.page.url.lower()

    @allure.title("Click Metroid Character")
    def test_click_metroid(self):
        self.characters.click_metroid()
        assert "metroid" in self.page.url.lower()

    @allure.title("Click Pokemon Character")
    def test_click_pokemon(self):
        self.characters.click_pokemon()
        assert "pokemon" in self.page.url.lower()

    @allure.title("Click Mario then back to Characters page")
    def test_click_mario_and_return(self):
        self.characters.click_super_mario()
        self.page.go_back()
        assert "nintendo" in self.page.url.lower()

    @allure.title("Click Zelda then back")
    def test_click_zelda_and_return(self):
        self.characters.click_zelda()
        self.page.go_back()
        assert "nintendo" in self.page.url.lower()

    @allure.title("Click multiple characters in sequence")
    def test_click_multiple_characters(self):
        self.characters.click_kirby()
        self.page.go_back()
        self.characters.click_pikmin()
        self.page.go_back()
        self.characters.click_metroid()
        assert "metroid" in self.page.url.lower()

    @allure.title("Click all characters and validate each")
    def test_click_all_characters_validation(self):
        characters = [
            (self.characters.click_super_mario, "mario"),
            (self.characters.click_zelda, "link"),
            (self.characters.click_splatoon, "splatoon"),
            (self.characters.click_kirby, "kirby"),
            (self.characters.click_pikmin, "pikmin"),
            (self.characters.click_animal_crossing, "animal-crossing"),
            (self.characters.click_metroid, "metroid"),
            (self.characters.click_pokemon, "pokemon")
        ]
        for click_func, keyword in characters:
            self.page.goto("https://www.nintendo.com/us/")
            click_func()
            assert keyword in self.page.url.lower()

    @allure.title("Validate no error on all character clicks")
    def test_all_clicks_no_errors(self):
        self.characters.click_super_mario()
        self.page.go_back()
        self.characters.click_zelda()
        self.page.go_back()
        self.characters.click_splatoon()
        self.page.go_back()
        self.characters.click_kirby()
        self.page.go_back()
        self.characters.click_pikmin()
        self.page.go_back()
        self.characters.click_animal_crossing()
        self.page.go_back()
        self.characters.click_metroid()
        self.page.go_back()
        self.characters.click_pokemon()
        assert "pokemon" in self.page.url.lower()