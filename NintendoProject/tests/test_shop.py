from tests.base_test import BaseTest
import allure

@allure.epic("Nintendo Shop Tab Tests")
class TestShop(BaseTest):

    def setup_method(self):
        self.page.goto("https://www.nintendo.com/us/")
        self.home_page.click_start_shopping()

    @allure.title("Click Games Category")
    def test_click_games(self):
        self.shop.click_games()
        assert "games" in self.page.url

    @allure.title("Click Hardware Category")
    def test_click_hardware(self):
        self.shop.click_hardware()
        assert "hardware" in self.page.url

    @allure.title("Click Merchandise Category")
    def test_click_merchandise(self):
        self.shop.click_merchandise()
        assert "merch" in self.page.url or "products" in self.page.url

    @allure.title("Click Store Exclusives")
    def test_click_store_exclusives(self):
        self.shop.click_store_exclusives()
        assert "exclusive" in self.page.url

    @allure.title("Click Characters Category")
    def test_click_characters(self):
        self.shop.click_characters()
        assert "characters" in self.page.url

    @allure.title("Click Sales and Deals")
    def test_click_sales_and_deals(self):
        self.shop.click_sales_and_deals()
        assert "deals" in self.page.url

    @allure.title("Navigate through all shop categories")
    def test_click_all_categories(self):
        self.shop.click_games()
        self.page.go_back()
        self.shop.click_hardware()
        self.page.go_back()
        self.shop.click_merchandise()
        self.page.go_back()
        self.shop.click_store_exclusives()
        self.page.go_back()
        self.shop.click_characters()
        self.page.go_back()
        self.shop.click_sales_and_deals()
        assert "deals" in self.page.url

    @allure.title("Stress test: repeat navigation")
    def test_shop_navigation_loop(self):
        for _ in range(3):
            self.shop.click_games()
            self.page.go_back()
            self.shop.click_characters()
            self.page.go_back()
        assert "nintendo.com" in self.page.url

    @allure.title("Click categories and validate no crashes")
    def test_all_shop_clicks_safe(self):
        try:
            self.shop.click_games()
            self.shop.click_hardware()
            self.shop.click_merchandise()
            self.shop.click_store_exclusives()
            self.shop.click_characters()
            self.shop.click_sales_and_deals()
            assert True
        except Exception:
            assert False

    @allure.title("Shop tab with direct URL")
    def test_direct_shop_url(self):
        self.page.goto("https://www.nintendo.com/us/store/")
        assert "store" in self.page.url

    @allure.title("Click characters after hardware")
    def test_hardware_then_characters(self):
        self.shop.click_hardware()
        self.page.go_back()
        self.shop.click_characters()
        assert "characters" in self.page.url

    @allure.title("Click merchandise after deals")
    def test_deals_then_merchandise(self):
        self.shop.click_sales_and_deals()
        self.page.go_back()
        self.shop.click_merchandise()
        assert "merch" in self.page.url or "products" in self.page.url

    @allure.title("Shop tab full sequential flow")
    def test_shop_sequential_flow(self):
        self.shop.click_games()
        self.page.go_back()
        self.shop.click_store_exclusives()
        self.page.go_back()
        self.shop.click_sales_and_deals()
        assert "deals" in self.page.url

    @allure.title("Validate store page integrity")
    def test_store_page_integrity(self):
        self.page.goto("https://www.nintendo.com/us/store/")
        assert self.page.locator("h1").first.is_visible()