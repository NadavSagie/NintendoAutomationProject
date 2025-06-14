from tests.base_test import BaseTest
import allure

@allure.epic("Nintendo Explore Page Tests")
class TestExplore(BaseTest):

    def setup_method(self):
        self.page.goto("https://www.nintendo.com/us/")
        self.home_page.click_explore()

    @allure.title("Click Nintendo Switch 2")
    def test_click_nintendo_switch_2(self):
        self.explore.click_nintendo_switch_2()
        assert "switch" in self.page.url or "hardware" in self.page.url

    @allure.title("Click Nintendo Switch")
    def test_click_nintendo_switch(self):
        self.explore.click_nintendo_switch()
        assert "switch" in self.page.url

    @allure.title("Click Games")
    def test_click_games(self):
        self.explore.click_games()
        assert "games" in self.page.url

    @allure.title("Click Nintendo Switch Online")
    def test_click_switch_online(self):
        self.explore.click_nintendo_switch_online()
        assert "switch-online" in self.page.url

    @allure.title("Click News and Events")
    def test_click_news_and_events(self):
        self.explore.click_news_and_events()
        assert "news" in self.page.url or "events" in self.page.url

    @allure.title("Click Play Nintendo")
    def test_click_play_nintendo(self):
        self.explore.click_play_nintendo()
        assert "play.nintendo.com" in self.page.url or "play" in self.page.url

    @allure.title("Click My Nintendo")
    def test_click_my_nintendo(self):
        self.explore.click_my_nintendo()
        assert "my.nintendo.com" in self.page.url or "my-nintendo" in self.page.url

    @allure.title("Click Apps")
    def test_click_apps(self):
        self.explore.click_apps()
        assert "apps" in self.page.url or "google.com" in self.page.url

    @allure.title("Click Super Mario Character")
    def test_click_super_mario(self):
        self.explore.click_super_mario()
        assert "mario" in self.page.url

    @allure.title("Click Zelda Character")
    def test_click_zelda(self):
        self.explore.click_zelda()
        assert "zelda" in self.page.url or "link" in self.page.url

    @allure.title("Click Splatoon Character")
    def test_click_splatoon(self):
        self.explore.click_splatoon()
        assert "splatoon" in self.page.url

    @allure.title("Click Kirby Character")
    def test_click_kirby(self):
        self.explore.click_kirby()
        assert "kirby" in self.page.url

    @allure.title("Click Pikmin Character")
    def test_click_pikmin(self):
        self.explore.click_pikmin()
        assert "pikmin" in self.page.url

    @allure.title("Click Animal Crossing Character")
    def test_click_animal_crossing(self):
        self.explore.click_animal_crossing()
        assert "animal-crossing" in self.page.url

    @allure.title("Click Metroid Character")
    def test_click_metroid(self):
        self.explore.click_metroid()
        assert "metroid" in self.page.url

    @allure.title("Full Explore Navigation Flow")
    def test_explore_full_navigation(self):
        self.explore.click_nintendo_switch()
        self.page.go_back()
        self.explore.click_games()
        self.page.go_back()
        self.explore.click_nintendo_switch_online()
        self.page.go_back()
        self.explore.click_news_and_events()
        assert "news" in self.page.url