from time import sleep

import pytest

from tests.base_test import BaseTest
import allure

@allure.epic("Nintendo Home Page Tests")
class Test_Master(BaseTest):

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

    @allure.title("Search for Pokemon and validate results")
    def test_search(self):
        self.home_page.search("Pokemon")
        self.home_page.click_search_result(1)
        self.home_page.slide_show_previous()
        sleep(1)
        self.home_page.slide_show_previous()
        sleep(1)
        self.home_page.slide_show_previous()
        assert "pokemon" in self.page.url
        self.home_page.click_home_btn()

    @allure.title("Full Short Sign-Up Flow - Expected Error")
    def test_sign_up(self):
        self.sign_up.sign_up_full_process("7", "11", "2000", "tester111", "fake@gmail.com", "Test1234", "male", "Israel", "142")
        current_url = self.page.url
        print(f"[DEBUG] Final URL: {current_url}")
        assert "error" in current_url.lower()
        self.page.goto("https://www.nintendo.com/us/")

    @allure.title("Click Start Shopping")
    def test_click_start_shopping(self):
        with self.page.expect_navigation():
            self.home_page.click_start_shopping()
        assert "store" in self.page.url

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

    @allure.title("Click Best Sellers_Test")
    @pytest.mark.e2e
    def test_click_best_sellers(self):
        self.home_page.click_best_sellers()
        self.shop_games.click_table_platform_tab()
        self.shop_games.click_table_platform_nintendo_switch()
        self.shop_games.click_table_price_tab()
        self.shop_games.click_table_price_10_20()
        sleep(1)
        self.home_page.scroll_page("down", 30, 9000, 1)
        sleep(1)
        self.shop_games.click_by_name("Diablo III")
        self.shop_games.age_verification("11", "13", "1995")
        sleep(2)
        self.home_page.slide_show_previous()
        sleep(1)
        self.home_page.slide_show_previous()
        assert "diablo" in self.page.url
        self.home_page.click_home_btn()

    @allure.title("Click all characters and validate each")
    def test_click_all_characters_validation(self):
        characters = [
            (self.characters.click_super_mario, "mario"),
            (self.characters.click_zelda, "zelda"),
            (self.characters.click_kirby, "kirby"),
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

    @pytest.mark.usefixtures("setup_page_session")
    @allure.title("Log in button opens Nintendo Account popup")
    def test_log_in_popup(self):
        popup = self.home_page.click_log_in_and_get_popup()
        assert self.home_page.log_in_title(popup) == "Nintendo Account"

    @allure.title("Click Wishlist")
    def test_click_wishlist(self):
        self.home_page.click_wish_list()

