from tests.base_test import BaseTest
import allure

@allure.epic("Nintendo Shop Games Tests")
class TestShopGames(BaseTest):

    def setup_method(self):
        self.page.goto("https://www.nintendo.com/us/")
        self.home_page.click_start_shopping()
        self.shop.click_games()

    @allure.title("Click Characters in Games")
    def test_click_characters_tab(self):
        self.shop_games.click_characters()
        assert "characters" in self.page.url

    @allure.title("Click New Releases")
    def test_click_new_releases(self):
        self.shop_games.click_new_releases()
        assert "new-releases" in self.page.url

    @allure.title("Click Coming Soon")
    def test_click_coming_soon(self):
        self.shop_games.click_coming_soon()
        assert "coming-soon" in self.page.url

    @allure.title("Click Shop All")
    def test_click_shop_all(self):
        self.shop_games.click_shop_all()
        assert "all" in self.page.url or "browse" in self.page.url

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
        assert "mario" in self.page.url

    @allure.title("Click Characters - Zelda")
    def test_click_characters_zelda(self):
        self.shop_games.click_characters_zelda()
        assert "zelda" in self.page.url or "link" in self.page.url

    @allure.title("Click Characters - Pikachu")
    def test_click_characters_pikachu(self):
        self.shop_games.click_characters_pikachu()
        assert "pokemon" in self.page.url or "pikachu" in self.page.url

    @allure.title("Filter: Platform Nintendo Switch")
    def test_filter_platform_switch(self):
        self.shop_games.click_shop_all()
        self.shop_games.click_table_platform_tab()
        self.shop_games.click_table_platform_nintendo_switch()
        assert "Switch" in self.page.content()

    @allure.title("Filter: Characters > Pokemon > Price $20-40")
    def test_filter_pokemon_20_40(self):
        self.shop_games.search_pokemon_game_price_max_40()
        assert self.shop_games.max_40_filter() == "$20 - $39.99"

    @allure.title("Click Save Data Cloud filter")
    def test_click_save_data_cloud_filter(self):
        self.shop_games.click_shop_all()
        self.shop_games.click_table_nintendo_switch_online_tab()
        self.shop_games.click_table_nintendo_save_data_cloud()
        assert "save" in self.page.content().lower()

    @allure.title("Click Online Play filter")
    def test_click_online_play_filter(self):
        self.shop_games.click_shop_all()
        self.shop_games.click_table_nintendo_switch_online_tab()
        self.shop_games.click_table_nintendo_online_play()
        assert "online play" in self.page.content().lower()

    @allure.title("Click Upgrade Pack filter")
    def test_click_upgrade_pack_filter(self):
        self.shop_games.click_shop_all()
        self.shop_games.click_table_type_upgrade_pack()
        assert "upgrade" in self.page.content().lower()