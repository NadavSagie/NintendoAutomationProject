from time import sleep
from tests.base_test import BaseTest
import allure

@allure.epic("Nintendo Shop Games Tests")
class TestShopGames(BaseTest):

    def setup_method(self):
        self.page.goto("https://www.nintendo.com/us/store/games/")
        #self.home_page.click_start_shopping()
        #self.shop.click_games()

    @allure.title("Click Characters in Games")
    def test_click_characters_tab(self):
        self.shop_games.click_characters()
        assert "characters" in self.page.url

    @allure.title("Click New Releases")
    def test_click_new_releases(self):
        self.shop_games.click_new_releases()
        new_releases_header = self.shop_games.verify_new_releases()
        assert "new releases" in new_releases_header.lower()

    @allure.title("Click Coming Soon")
    def test_click_coming_soon(self):
        self.shop_games.click_coming_soon()
        coming_soon_header = self.shop_games.verify_coming_soon()
        assert "coming soon" in coming_soon_header.lower()

    @allure.title("Click Genre Tab")
    def test_click_genres(self):
        self.shop_games.click_genres()
        assert "genre" in self.page.content().lower()

    @allure.title("Click Nintendo Switch 2")
    def test_click_switch2(self):
        self.shop_games.click_nintendo_switch_2()
        assert "switch" in self.page.url

    @allure.title("Click Featured")
    def test_click_featured(self):
        self.shop_games.click_featured()
        assert "featured" in self.page.content().lower()

    @allure.title("Click Characters - Mario")
    def test_click_characters_mario(self):
        self.shop_games.click_characters_mario()
        sleep(1)
        super_mario_header = self.shop_games.verify_super_mario()
        assert "mario" in super_mario_header.lower()

    @allure.title("Click Characters - Zelda")
    def test_click_characters_zelda(self):
        self.shop_games.click_characters_zelda()
        zelda_header = self.shop_games.verify_zelda()
        assert "zelda" in zelda_header.lower()

    @allure.title("Click Characters - Pikachu")
    def test_click_characters_pikachu(self):
        self.shop_games.click_characters_pikachu()
        pikachu_header = self.shop_games.verify_zelda()
        assert "pokémon" in pikachu_header.lower()

    @allure.title("Filter: Platform Nintendo Switch")
    def test_filter_platform_switch(self):
        self.shop_games.scroll_to_shop()
        self.shop_games.click_table_type_dlc()
        self.shop_games.click_table_platform_tab()
        self.shop_games.click_table_platform_nintendo_switch()
        #self.shop_games.click_table_type_demo_available()
        #self.shop_games.click_table_type_demo_available()
        self.shop_games.click_table_characters_of_series_tab()
        self.shop_games.click_table_characters_animal_crossing()
        self.shop_games.click_table_price_tab()
        self.shop_games.click_table_price_10_20()
        assert "Switch" in self.page.content()

    @allure.title("Filter: Characters > Pokemon > Price $20-40")
    def test_filter_pokemon_20_40(self):
        self.shop_games.search_pokemon_game_price_max_40()
        self.shop_games.click_first_result()
        assert self.shop_games.third_tag_filter() == "$20 - $39.99"

    def test_filter_pokemon_40_plus(self):
        self.shop_games.search_pokemon_game_price_over_40()
        assert self.shop_games.third_tag_filter() == "$40+"
        self.shop_games.click_first_result()

    @allure.title("Click Save Data Cloud filter")
    def test_click_save_data_cloud_filter(self):
        self.shop_games.scroll_to_shop()
        self.shop_games.click_table_nintendo_switch_online_tab()
        self.shop_games.click_table_nintendo_save_data_cloud()
        assert "save" in self.page.content().lower()

    @allure.title("Click Online Play filter")
    def test_click_online_play_filter(self):
        self.shop_games.scroll_to_shop()
        self.shop_games.click_table_nintendo_switch_online_tab()
        self.shop_games.click_table_nintendo_online_play()
        assert "online play" in self.page.content().lower()

    @allure.title("Click Upgrade Pack filter")
    def test_click_upgrade_pack_filter(self):
        self.shop_games.scroll_to_shop()
        self.shop_games.click_table_type_upgrade_pack()
        assert "upgrade" in self.page.content().lower()