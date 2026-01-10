from tests.base_test import BaseTest
import allure

@allure.epic("Nintendo All Tests")
class TestAll(BaseTest):

    #def setup_method(self):
        #self.page.goto("https://www.nintendo.com/us/")

    @allure.title("Click Super Mario Character")
    def test_click_super_mario(self):
        self.characters.click_super_mario()
        assert "mario" in self.page.url.lower()

    @allure.title("Click Zelda Character")
    def test_click_zelda(self):
        self.characters.click_zelda()
        assert "zelda" in self.page.url.lower()

    @allure.title("Click Splatoon Character")
    def test_click_splatoon(self):
        self.characters.click_splatoon()
        assert "splatoon" in self.page.url.lower()

    @allure.title("Click Kirby Character")
    def test_click_kirby(self):
        self.characters.click_kirby()
        assert "kirby" in self.page.url.lower()

    @allure.title("Click Pikmin Character")
    def test_click_pikmin(self):
        self.characters.click_pikmin()
        assert "pikmin" in self.page.url.lower()

    @allure.title("Click Animal Crossing Character")
    def test_click_animal_crossing(self):
        self.characters.click_animal_crossing()
        assert "animalcrossing" in self.page.url.lower()

    @allure.title("Click Metroid Character")
    def test_click_metroid(self):
        self.characters.click_metroid()
        assert "metroid" in self.page.url.lower()

    @allure.title("Click Pokemon Character")
    def test_click_pokemon(self):
        self.characters.click_pokemon()
        assert "pokemon" in self.page.url.lower()

    @allure.title("Click Mario then back to Characters page")
    def test_click_mario_and_return(self):
        self.characters.click_super_mario()
        self.page.go_back()
        assert "nintendo" in self.page.url.lower()

    @allure.title("Click Zelda then back")
    def test_click_zelda_and_return(self):
        self.characters.click_zelda()
        self.page.go_back()
        assert "nintendo" in self.page.url.lower()

    @allure.title("Click multiple characters in sequence")
    def test_click_multiple_characters(self):
        self.characters.click_kirby()
        self.page.go_back()
        self.characters.click_pikmin()
        self.page.go_back()
        self.characters.click_metroid()
        assert "metroid" in self.page.url.lower()

    @allure.title("Click all characters and validate each")
    def test_click_all_characters_validation(self):
        characters = [
            (self.characters.click_super_mario, "mario"),
            (self.characters.click_zelda, "link"),
            (self.characters.click_splatoon, "splatoon"),
            (self.characters.click_kirby, "kirby"),
            (self.characters.click_pikmin, "pikmin"),
            (self.characters.click_animal_crossing, "animal-crossing"),
            (self.characters.click_metroid, "metroid"),
            (self.characters.click_pokemon, "pokemon")
        ]
        for click_func, keyword in characters:
            self.page.goto("https://www.nintendo.com/us/")
            click_func()
            assert keyword in self.page.url.lower()

    @allure.title("Validate no error on all character clicks")
    def test_all_clicks_no_errors(self):
        self.characters.click_super_mario()
        self.page.go_back()
        self.characters.click_zelda()
        self.page.go_back()
        self.characters.click_splatoon()
        self.page.go_back()
        self.characters.click_kirby()
        self.page.go_back()
        self.characters.click_pikmin()
        self.page.go_back()
        self.characters.click_animal_crossing()
        self.page.go_back()
        self.characters.click_metroid()
        self.page.go_back()
        self.characters.click_pokemon()
        assert "pokemon" in self.page.url.lower()

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

    @allure.title("Open Sign Up from account menu")
    def test_open_sign_up(self):
        self.sign_up.click(self.sign_up._ACCOUNT)
        self.sign_up.click(self.sign_up._ACCOUNT_SIGN_UP)
        assert "sign-up" in self.page.url or "account" in self.page.url

    @allure.title("Try underage sign up")
    def test_underage_sign_up_block(self):
        self.sign_up.click(self.sign_up._ACCOUNT)
        self.sign_up.click(self.sign_up._ACCOUNT_SIGN_UP)
        self.sign_up.select_option(self.sign_up._SIGN_UP_MONTH, "12")
        self.sign_up.select_option(self.sign_up._SIGN_UP_DAY, "31")
        self.sign_up.select_option(self.sign_up._SIGN_UP_YEAR, "2015")
        self.sign_up.click(self.sign_up._SIGN_UP_SUBMIT)
        assert "under 16" in self.page.content().lower() or "parent" in self.page.content().lower()

    @allure.title("Select birthdate and continue")
    def test_birthday_step(self):
        self.sign_up.click(self.sign_up._ACCOUNT)
        self.sign_up.click(self.sign_up._ACCOUNT_SIGN_UP)
        self.sign_up.select_option(self.sign_up._SIGN_UP_MONTH, "7")
        self.sign_up.select_option(self.sign_up._SIGN_UP_DAY, "11")
        self.sign_up.select_option(self.sign_up._SIGN_UP_YEAR, "2000")
        self.sign_up.click(self.sign_up._SIGN_UP_SUBMIT)
        assert "sign" in self.page.content().lower()

    @allure.title("Full Sign-Up Flow - Expected Error")
    def test_sign_up_with_invalid_email(self):
        self.sign_up.sign_up_full_process("7", "11", "2000", "tester111", "fake@invalid.com", "Test1234", "male",
                                          "Israel", "142")
        error = self.sign_up.account_sign_up_error()
        assert "error" in error.lower()

    @allure.title("Click Create Nintendo Account link")
    def test_click_create_account_link(self):
        self.sign_up.click(self.sign_up._ACCOUNT)
        self.sign_up.click(self.sign_up._ACCOUNT_SIGN_UP)
        self.sign_up.select_option(self.sign_up._SIGN_UP_MONTH, "6")
        self.sign_up.select_option(self.sign_up._SIGN_UP_DAY, "9")
        self.sign_up.select_option(self.sign_up._SIGN_UP_YEAR, "2001")
        self.sign_up.click(self.sign_up._SIGN_UP_SUBMIT)
        self.sign_up.click(self.sign_up._NINTENDO_HOME_SIGN_UP)
        self.sign_up.click(self.sign_up._CREATE_NINTENDO_ACCOUNT)
        assert "register" in self.page.url

    @allure.title("Try signing up without checking checkboxes")
    def test_sign_up_missing_checkboxes(self):
        self.sign_up.click(self.sign_up._ACCOUNT)
        self.sign_up.click(self.sign_up._ACCOUNT_SIGN_UP)
        self.sign_up.select_option(self.sign_up._SIGN_UP_MONTH, "6")
        self.sign_up.select_option(self.sign_up._SIGN_UP_DAY, "9")
        self.sign_up.select_option(self.sign_up._SIGN_UP_YEAR, "2000")
        self.sign_up.click(self.sign_up._SIGN_UP_SUBMIT)
        self.sign_up.click(self.sign_up._NINTENDO_HOME_SIGN_UP)
        self.sign_up.click(self.sign_up._CREATE_NINTENDO_ACCOUNT)
        self.sign_up.click(self.sign_up._ACCOUNT_OVER_16)
        self.sign_up.fill_text(self.sign_up._SIGN_UP_NICKNAME, "noCheckTest")
        self.sign_up.fill_text(self.sign_up._SIGN_UP_EMAIL, "test@testing.com")
        self.sign_up.fill_text(self.sign_up._SIGN_UP_PASSWORD, "Test1234")
        self.sign_up.fill_text(self.sign_up._SIGN_UP_CONFIRM_PASSWORD, "Test1234")
        self.sign_up.select_option(self.sign_up._SIGN_UP_COUNTRY, "Israel")
        self.sign_up.select_option(self.sign_up._SIGN_UP_TIME_ZONE, "142")
        self.sign_up.click(self.sign_up._SIGN_UP_CONTINUE_BUTTON)
        assert "required" in self.page.content().lower()

    @allure.title("Error message appears for duplicate nickname/email")
    def test_signup_error_messages(self):
        self.sign_up.sign_up_full_process("6", "9", "2000", "usednickname", "test@test.com", "Buff1234", "male",
                                          "Israel", "142")
        error_msg = self.sign_up.account_sign_up_error()
        assert error_msg is not None and error_msg != ""

