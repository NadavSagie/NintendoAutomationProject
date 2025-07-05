from tests.base_test import BaseTest
import allure

class Test1(BaseTest):

    @allure.description("Search series and than click join us")
    @allure.title("Search series and Join")
    def test_01_nintendo_click_explore(self):
        self.home_page.click_explore()
        explore_msg = self.home_page.verify_explore()
        assert explore_msg == "Meet the characters:"

    def test_02_nintendo_click_shop_tab(self):
        self.home_page.click_shop()
        shop_msg = self.home_page.get_shop_text()
        assert shop_msg == "My Nintendo Store"

    def test_03_nintendo_click_support_tab(self):
        self.home_page.click_support()
        support_msg = self.home_page.get_support_text()
        assert support_msg == "Support Home"

    def test_04_nintendo_search(self):
        self.home_page.search("Pokemon")
        headline = self.home_page.result_title()
        assert "Pokemon" in headline

    def test_05_nintendo_log_in(self):
        popup_page = self.home_page.click_log_in_and_get_popup()
        headline = self.home_page.log_in_title(popup_page)
        assert headline == "Nintendo Account"

    def test_06_nintendo_click_online_store(self):
        self.home_page.click_start_shopping()
        self.shop.click_games()

    def test_07_nintendo_click_shop_games(self):
        self.shop_games.click_characters()

    def test_08_nintendo_search_pokemon_game_max_40(self):
        self.home_page.click_start_shopping()
        self.shop.click_games()
        self.shop_games.scroll_to_shop()
        self.shop_games.search_pokemon_game_price_max_40()
        max_40_msg = self.shop_games.max_40_filter()
        assert max_40_msg == "$20 - $39.99"

    def test_09_nintendo_sign_up(self):
        self.sign_up.sign_up_full_process("7", "11", "2001", "genadizen11", "test@test.com", "Bdika123", "male", "Israel", "142")
        account_need_verification = self.sign_up.account_sign_up_error()
        assert account_need_verification == "An error has occurred. Please try again later."