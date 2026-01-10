import time
from asyncio import wait_for
from time import sleep
import pytest
from tests.base_test import BaseTest
import allure

@allure.epic("Nintendo Home Page Tests")
class TestBdika(BaseTest):

    @allure.title("Click Explore tab and validate text")
    def test_click_explore(self):
        self.home_page.click_explore()
        assert "Meet the characters:" in self.home_page.verify_explore()

    @allure.title("Click Shop tab and validate title")
    def test_click_shop(self):
        self.home_page.click_shop()
        assert self.home_page.get_shop_text() == "My Nintendo Store"

    @allure.title("Click Support tab and validate title")
    def test_click_support(self):
        self.home_page.click_support()
        assert self.home_page.get_support_text() == "Support Home"

    @allure.title("Click Cart")
    def test_click_cart(self):
        self.home_page.click_cart()
        assert "cart" in self.page.url

    @allure.title("Click My Account")
    def test_click_my_account(self):
        self.home_page.click_my_account()
        assert self.page.url.startswith("https://www.nintendo.com/")
        self.home_page.click_home_btn()

    @allure.title("Click News")
    def test_click_news(self):
        self.home_page.click_all_news()
        all_news_header = self.home_page.verify_click_all_news()
        assert "news" in all_news_header.lower()
        self.home_page.click_home_btn()

    @allure.title("Click Best Sellers")
    def test_click_best_sellers(self):
        try:
            with self.page.expect_navigation(timeout=10000):
                self.home_page.click_best_sellers()
            assert "best-sellers" in self.page.url.lower()
            self.home_page.click_home_btn()
        except Exception as e:
            self.home_page.click_home_btn()
            pytest.fail(str(e))

    @allure.title("Click Start Shopping")
    def test_click_start_shopping(self):
        with self.page.expect_navigation():
            self.home_page.click_start_shopping()
        self.shop.click_games()
        self.home_page.scroll_page("down", 70, 7000, 0)
        self.shop_games.click_table_platform_tab()
        self.shop_games.click_table_platform_nintendo_switch()
        self.shop_games.click_table_characters_of_series_tab()
        self.shop_games.click_table_platform_show_more()
        self.shop_games.click_table_characters_pokemon()
        self.shop_games.click_table_price_tab()
        self.shop_games.click_table_price_40_plus()
        sleep(1)
        self.shop_games.click_by_name("Pokémon™: Let’s Go, Pikachu!")
        sleep(2)
        self.page.go_back()
        sleep(2)
        self.home_page.scroll_page("up", 15, 7000, 0)
        self.shop_games.click_by_name("Pokémon™ Violet")
        assert "Violet" in self.shop_games.verify_selected_game_header()
        self.home_page.click_home_btn()


    @allure.title("Click all characters and validate each")
    def test_click_all_characters_validation(self):
        characters = [
            (self.characters.click_super_mario, "mario"),
            (self.characters.click_zelda, "zelda"),
            (self.characters.click_splatoon, "splatoon"),
            (self.characters.click_kirby, "kirby"),
            (self.characters.click_pikmin, "pikmin"),
            (self.characters.click_animal_crossing, "animalcrossing"),
            (self.characters.click_metroid, "metroid"),
            (self.characters.click_pokemon, "pokemon")
        ]
        for click_func, keyword in characters:
            click_func()
            assert keyword in self.page.url.lower()
            sleep(3)
            self.page.go_back()

    @allure.title("Click Gaming Systems")
    def test_click_gaming_systems(self):
        with self.page.expect_navigation():
            self.home_page.click_gaming_systems()
        assert "switch" in self.page.url or "gaming" in self.page.url
        self.home_page.click_home_btn()

    @allure.title("Click Nintendo Switch Online")
    def test_click_nintendo_switch_online(self):
        self.home_page.click_nintendo_switch_online()
        assert "online" in self.page.url
        self.home_page.click_home_btn()

    @allure.title("Language Change Navigation")
    def test_change_language(self):
        self.home_page.change_language()
        assert "region" in self.page.url
        self.page.go_back()

    @allure.title("Search for Pokemon and validate results")
    def test_search_pokemon(self):
        self.home_page.search("Pokemon")
        assert "Pokemon" in self.home_page.result_title()
        self.home_page.click_home_btn()

    @allure.title("Full Short Sign-Up Flow - Expected Error")
    def test_sign_up(self):
        self.sign_up.sign_up_short_process("7", "11", "2000", "tester111", "fake@gmail.com", "Test1234", "male", "Israel", "142")
        current_url = self.page.url
        print(f"[DEBUG] Final URL: {current_url}")
        assert "error" in current_url.lower()
        self.page.goto("https://www.nintendo.com/us/")

    import allure

    @allure.title("Click all characters in one test")
    def test_click_all_characters_in_explore_tab(self):
        cases = [
            (self.explore.click_super_mario, lambda u: "mario" in u),
            (self.explore.click_zelda, lambda u: "zelda" in u or "link" in u),
            (self.explore.click_splatoon, lambda u: "splatoon" in u),
            (self.explore.click_kirby, lambda u: "kirby" in u),
            (self.explore.click_pikmin, lambda u: "pikmin" in u),
            (self.explore.click_animal_crossing, lambda u: "animal-crossing" in u or "animalcrossing" in u),
            (self.explore.click_metroid, lambda u: "metroid" in u),
        ]

        for click, check in cases:
            self.home_page.click_explore()
            click()
            sleep(1)
            url = self.page.url.lower()
            assert check(url), f"URL mismatch: {url}"
            self.page.go_back()
            self.page.wait_for_load_state("domcontentloaded")

    @allure.title("Under 'Support' tab click on 'Home' button ")
    def test_support_home(self):
        self.page.wait_for_load_state("networkidle")
        self.home_page.click_support()
        self.support.click_my_support_dashboard()
        sleep(3)
        assert "My Support Dashboard" in self.support.verify_click_my_support_dashboard()
        self.page.go_back()

    #@allure.title("Log in button opens Nintendo Account popup")
    #def test_log_in_popup(self):
        #popup = self.home_page.click_log_in_and_get_popup()
        #assert self.home_page.log_in_title(popup) == "Nintendo Account"

    #@allure.title("Click Wishlist")
    #def test_click_wishlist(self):
     #   self.home_page.click_wish_list()
      #  assert "wishlist" in self.page.url