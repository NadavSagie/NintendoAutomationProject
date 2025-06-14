from tests.base_test import BaseTest
import allure

@allure.epic("Nintendo Support Page Tests")
class TestSupport(BaseTest):

    def setup_method(self):
        self.page.goto("https://www.nintendo.com/us/")
        self.home_page.click_support()

    @allure.title("Click My Support Dashboard")
    def test_click_support_dashboard(self):
        self.support.click_my_support_dashboard()
        assert "support" in self.page.url

    @allure.title("Click Nintendo Switch Family")
    def test_click_switch_family(self):
        self.support.click_nintendo_switch_family()
        assert "switch" in self.page.url

    @allure.title("Click Other Systems")
    def test_click_other_systems(self):
        self.support.click_other_systems()
        assert "other-systems" in self.page.url or "support" in self.page.url

    @allure.title("Click Accounts and My Nintendo")
    def test_click_accounts_nintendo(self):
        self.support.click_accounts_my_nintendo()
        assert "account" in self.page.url or "nintendo" in self.page.url

    @allure.title("Click Repair Services")
    def test_click_repair_services(self):
        self.support.click_repair()
        assert "repair" in self.page.url

    @allure.title("Return to Support Home")
    def test_click_support_home(self):
        self.support.click_support_home()
        assert "support" in self.page.url

    @allure.title("Go through all support tabs")
    def test_all_support_tabs(self):
        self.support.click_my_support_dashboard()
        self.page.go_back()
        self.support.click_nintendo_switch_family()
        self.page.go_back()
        self.support.click_other_systems()
        self.page.go_back()
        self.support.click_accounts_my_nintendo()
        self.page.go_back()
        self.support.click_repair()
        self.page.go_back()
        self.support.click_support_home()
        assert "support" in self.page.url

    @allure.title("Support dashboard and return")
    def test_support_dashboard_back(self):
        self.support.click_my_support_dashboard()
        self.page.go_back()
        assert "support" in self.page.url

    @allure.title("Support flow to repair and back")
    def test_support_repair_flow(self):
        self.support.click_repair()
        self.page.go_back()
        self.support.click_support_home()
        assert "support" in self.page.url

    @allure.title("Support navigation does not crash")
    def test_support_navigation_safe(self):
        try:
            self.support.click_my_support_dashboard()
            self.support.click_nintendo_switch_family()
            self.support.click_other_systems()
            self.support.click_accounts_my_nintendo()
            self.support.click_repair()
            self.support.click_support_home()
            assert True
        except Exception:
            assert False

    @allure.title("Repeat clicking support home")
    def test_repeat_support_home(self):
        for _ in range(3):
            self.support.click_support_home()
        assert "support" in self.page.url

    @allure.title("Validate Support Home Page title exists")
    def test_support_home_text(self):
        assert self.support.page.locator(".YSMyD").is_visible()

    @allure.title("Click support dashboard then repair")
    def test_dashboard_to_repair(self):
        self.support.click_my_support_dashboard()
        self.page.go_back()
        self.support.click_repair()
        assert "repair" in self.page.url

    @allure.title("Click switch family then accounts")
    def test_switch_family_to_accounts(self):
        self.support.click_nintendo_switch_family()
        self.page.go_back()
        self.support.click_accounts_my_nintendo()
        assert "account" in self.page.url

    @allure.title("Click other systems then home")
    def test_other_systems_to_home(self):
        self.support.click_other_systems()
        self.page.go_back()
        self.support.click_support_home()
        assert "support" in self.page.url