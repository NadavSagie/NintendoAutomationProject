import time
from time import sleep

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

    @allure.title("Click Best Sellers")
    def test_click_best_sellers(self):
        self.home_page.click_best_sellers()
        self.home_page.scroll_to_bottom_and_top()
        assert "best-sellers" in self.page.url
        self.home_page.click_home_btn()

    @allure.title("Click New Releases")
    def test_click_new_releases(self):
        self.home_page.click_digital_new_releases()
        self.home_page.scroll_to_bottom_and_top()
        assert "new-releases" in self.page.url
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
        assert "lang" in self.page.url or "country" in self.page.url
        self.home_page.click_home_btn()

    @allure.title("Full home page click-through test")
    def test_full_navigation(self):
        self.home_page.click_explore()
        self.page.go_back()
        self.home_page.click_shop()
        self.page.go_back()
        self.home_page.click_support()
        self.page.go_back()
        self.home_page.click_all_news()
        assert "news" in self.page.url

    @allure.title("Search for Pokemon and validate results")
    def test_search_pokemon(self):
        self.home_page.search("Pokemon")
        assert "Pokemon" in self.home_page.result_title()

    #@allure.title("Log in button opens Nintendo Account popup")
    #def test_log_in_popup(self):
     #   popup = self.home_page.click_log_in_and_get_popup()
      #  assert self.home_page.log_in_title(popup) == "Nintendo Account"

    #@allure.title("Click Wishlist")
    #def test_click_wishlist(self):
     #   self.home_page.click_wish_list()
      #  assert "wishlist" in self.page.url