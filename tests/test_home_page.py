from tests.base_test import BaseTest
import allure

@allure.epic("Nintendo Home Page Tests")
class TestHomePage(BaseTest):

    #def setup_method(self):
        #self.page.goto("https://www.nintendo.com/us/")

    @allure.title("Click Explore tab and validate text")
    def test_click_explore(self):
        self.home_page.click_explore()
        assert "Meet the characters:" in self.home_page.verify_explore()

    @allure.title("Click Support tab and validate title")
    def test_click_support(self):
        self.home_page.click_support()
        assert self.home_page.get_support_text() == "Support Home"

    @allure.title("Click Shop tab and validate title")
    def test_click_shop(self):
        self.home_page.click_shop()
        assert self.home_page.get_shop_text() == "My Nintendo Store"

    @allure.title("Search for Pokemon and validate results")
    def test_search_pokemon(self):
        self.home_page.search("Pokemon")
        assert "Pokemon" in self.home_page.result_title()

    @allure.title("Log in button opens Nintendo Account popup")
    def test_log_in_popup(self):
        popup = self.home_page.click_log_in_and_get_popup()
        assert self.home_page.log_in_title(popup) == "Nintendo Account"

    @allure.title("Click Start Shopping")
    def test_click_start_shopping(self):
        self.home_page.click_start_shopping()
        assert "store" in self.page.url

    @allure.title("Click Wishlist")
    def test_click_wishlist(self):
        self.home_page.click_wish_list()
        assert "wish-list" in self.page.url

    @allure.title("Click Cart")
    def test_click_cart(self):
        self.home_page.click_cart()
        assert "cart" in self.page.url

    @allure.title("Click My Account")
    def test_click_my_account(self):
        self.home_page.click_my_account()
        assert self.page.url.startswith("https://www.nintendo.com/")

    @allure.title("Click News")
    def test_click_news(self):
        self.home_page.click_all_news()
        assert "news" in self.page.url

    @allure.title("Click Best Sellers")
    def test_click_best_sellers(self):
        self.home_page.click_best_sellers()
        assert "best-sellers" in self.page.url

    @allure.title("Click New Releases")
    def test_click_new_releases(self):
        self.home_page.click_digital_new_releases()
        assert "new-releases" in self.page.url

    @allure.title("Click Gaming Systems")
    def test_click_gaming_systems(self):
        self.home_page.click_gaming_systems()
        assert "switch" in self.page.url or "gaming" in self.page.url

    @allure.title("Click Nintendo Switch Online")
    def test_click_nintendo_switch_online(self):
        self.home_page.click_nintendo_switch_online()
        assert "switch-online" in self.page.url

    @allure.title("Language Change Navigation")
    def test_change_language(self):
        self.home_page.change_language()
        assert "lang" in self.page.url or "country" in self.page.url

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