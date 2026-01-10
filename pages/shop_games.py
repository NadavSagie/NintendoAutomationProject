<<<<<<< HEAD
from playwright.sync_api import Page
from pages.base_page import BasePage

class ShopGames(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    _NINTENDO_SWITCH_2   = "div:nth-child(2) > section > div > div > div.OIFpM > div.P8EbW > div > div.sziGh > div:nth-child(1)"
    _GENRES = "div:nth-child(2) > section > div > div > div.OIFpM > div.P8EbW > div > div.sziGh > div:nth-child(2)"
    _FEATURED = "div:nth-child(2) div.OIFpM div:nth-child(3)"
    _CHARACTERS = "div:nth-child(2) div.OIFpM div:nth-child(4)"
    _BEST_SELLERS = "div:nth-child(2) div.OIFpM div:nth-child(5)"
    _COMING_SOON = "div:nth-child(2) div.OIFpM div:nth-child(6)"
    _VERIFY_COMING_SOON = ".sc-14s4g00-7 > h1"
    _NEW_RELEASES = "div:nth-child(2) div.OIFpM div:nth-child(7)"
    _VERIFY_NEW_RELEASES = "div.sc-14s4g00-2.jKoniT > h1"
    _CHARACTERS_MARIO = "#games-with-nintendo-characters div:nth-child(1) > a"
    _VERIFY_SUPER_MARIO = "div.sc-14s4g00-2.jKoniT > h1"
    _CHARACTERS_ZELDA = "#games-with-nintendo-characters div:nth-child(2) > a"
    _VERIFY_ZELDA = "div.sc-14s4g00-2.jKoniT > h1"
    _CHARACTERS_KIRBY = "#games-with-nintendo-characters div:nth-child(3) > a"
    _CHARACTERS_DONKEY_KONG = "#games-with-nintendo-characters div:nth-child(4) > a"
    _CHARACTERS_PIKACHU = "#games-with-nintendo-characters div:nth-child(5) > a"
    _VERIFY_PIKACHU = ".s954l._3TUsN._39p7O.sXEHt"
    _TABLE_SHOP_CLEAR_ALL_BUTTON = ".kAkyvX > div > button"
    _TABLE_SHOP_TYPE_DEALS = "div:nth-child(19) [aria-label='Deals']:"
    _TABLE_SHOP_TYPE_DEMO_AVAILABLE = "div:nth-child(19) [aria-label='Demo available']"
    _TABLE_SHOP_TYPE_DLC = "div:nth-child(19) [aria-label='DLC']"
    _TABLE_SHOP_TYPE_GAMES_VOUCHER = "div:nth-child(19) [aria-label='Game Voucher eligible']"
    _TABLE_SHOP_TYPE_GAMES_WITH_DLC = "div:nth-child(19) [aria-label='Games with DLC']"
    _TABLE_SHOP_TYPE_UPGRADE_PACK = "div:nth-child(19) [aria-label='Upgrade pack']"
    _TABLE_SHOP_NINTENDO_ONLINE_FEATURES_TAB = "h3:has-text('Nintendo Switch Online features')"
    _TABLE_SHOP_NINTENDO_ONLINE_FEATURES_ONLINE_PLAY = "div:nth-child(19) [aria-label='Online play']"
    _TABLE_SHOP_NINTENDO_ONLINE_FEATURES_SAVE_DATA_CLOUD = "div:nth-child(19) [aria-label='Save Data Cloud']:"
    _TABLE_SHOP_PLATFORM_TAB = "h3:has-text('Platform')"
    _TABLE_SHOP_PLATFORM_IOS_ANDROID = "div:nth-child(19) [aria-label='iOS / Android']"
    _TABLE_SHOP_PLATFORM_NINTENDO_SWITCH = "input[aria-label='Nintendo Switch']"
    _TABLE_SHOP_PLATFORM_NINTENDO_SWITCH_2 = "input[aria-label='Nintendo Switch 2']"
    _TABLE_SHOP_CHARACTERS_OF_SERIES_TAB = "h3:has-text('Character or series')"
    _TABLE_SHOP_PLATFORM_SHOW_MORE_BUTTON = ".kAkyvX > div > div.sc-1at2kvx-0.cslSfM > div > div > button"
    _TABLE_SHOP_CHARACTERS_ANIMAL_CROSSING = "input[aria-label='Animal Crossing']"
    _TABLE_SHOP_CHARACTERS_BOWSER = "input[aria-label='Bowser']"
    _TABLE_SHOP_CHARACTERS_DIDDY_KONG = "input[aria-label='Diddy Kong']"
    _TABLE_SHOP_CHARACTERS_DONKEY_KONG = "input[aria-label='Donkey Kong']"
    _TABLE_SHOP_CHARACTERS_FIRE_EMBLEM = "input[aria-label='Fire Emblem']"
    _TABLE_SHOP_CHARACTERS_KIRBY = "input[aria-label='Kirby']"
    _TABLE_SHOP_CHARACTERS_LINK = "input[aria-label='Link']"
    _TABLE_SHOP_CHARACTERS_LUIGI = "input[aria-label='Luigi']"
    _TABLE_SHOP_CHARACTERS_MARIO = "input[aria-label='Mario']"
    _TABLE_SHOP_CHARACTERS_POKEMON = "input[aria-label='Pokémon']"
    _TABLE_SHOP_CHARACTERS_TLO_ZELDA = "input[aria-label='The Legend of Zelda']"
    _TABLE_SHOP_CHARACTERS_ZELDA = "input[aria-label='Zelda']"
    _TABLE_SHOP_PRICE_TAB = "h3:has-text('Price')"
    _TABLE_SHOP_PRICE_FREE = "input[aria-label='Free to start']"
    _TABLE_SHOP_PRICE_0_5 = "input[aria-label='$0 - $4.99']"
    _TABLE_SHOP_PRICE_5_10 = "input[aria-label='$5 - $9.99']"
    _TABLE_SHOP_PRICE_10_20 = "input[aria-label='$10 - $19.99']"
    _TABLE_SHOP_PRICE_20_40 = "input[aria-label='$20 - $39.99']"
    _TABLE_SHOP_PRICE_40_PLUS = "section:has(h3:has-text('Price')) input[aria-label='$40+']"
    _THIRD_TAG = "div > button:nth-child(3) > span.ZovBS"
    _TABLE_SHOP_FIRST_RESULT = ".sc-1dskkk7-3.ljMhgM > div:nth-child(1)"
    _RESULTS = ".sc-1dskkk7-3.ljMhgM > div"


    def click_nintendo_switch_2(self):
        self.click(self._NINTENDO_SWITCH_2)

    def click_genres(self):
        self.click(self._GENRES)

    def click_featured(self):
        self.click(self._FEATURED)

    def click_characters(self):
        self.click(self._CHARACTERS)

    def click_coming_soon(self):
        self.click(self._COMING_SOON)

    def verify_coming_soon(self):
        return self.page.inner_text(self._VERIFY_COMING_SOON)

    def click_new_releases(self):
        self.click(self._NEW_RELEASES)

    def verify_new_releases(self):
        return self.page.inner_text(self._VERIFY_NEW_RELEASES)

    def scroll_to_shop(self):
        self.page.evaluate("""window.scrollTo(0, document.body.scrollHeight * 0.4)""")

    def click_table_clear_all(self):
        self.click(self._TABLE_SHOP_CLEAR_ALL_BUTTON)

    def click_table_type_deals(self):
        self.click(self._TABLE_SHOP_TYPE_DEALS)

    def click_table_type_dlc(self):
        self.click(self._TABLE_SHOP_TYPE_DLC)

    def click_table_type_demo_available(self):
        self.click(self._TABLE_SHOP_TYPE_DEMO_AVAILABLE)

    def click_table_type_game_voucher(self):
        self.click(self._TABLE_SHOP_TYPE_GAMES_VOUCHER)

    def click_table_type_games_with_dlc(self):
        self.click(self._TABLE_SHOP_TYPE_GAMES_WITH_DLC)

    def click_table_type_upgrade_pack(self):
        self.click(self._TABLE_SHOP_TYPE_UPGRADE_PACK)

    def click_table_nintendo_switch_online_tab(self):
        self.click(self._TABLE_SHOP_NINTENDO_ONLINE_FEATURES_TAB)

    def click_table_nintendo_online_play(self):
        self.click(self._TABLE_SHOP_NINTENDO_ONLINE_FEATURES_ONLINE_PLAY)

    def click_table_nintendo_save_data_cloud(self):
        self.click(self._TABLE_SHOP_NINTENDO_ONLINE_FEATURES_SAVE_DATA_CLOUD)

    def click_characters_mario(self):
        self.click(self._CHARACTERS_MARIO)

    def verify_super_mario(self):
        return self.page.inner_text(self._VERIFY_SUPER_MARIO)

    def click_characters_zelda(self):
        self.click(self._CHARACTERS_ZELDA)

    def verify_zelda(self):
        return self.page.inner_text(self._VERIFY_ZELDA)

    def click_characters_kirby(self):
        self.click(self._CHARACTERS_KIRBY)

    def click_characters_donkey_kong(self):
        self.click(self._CHARACTERS_DONKEY_KONG)

    def click_characters_pikachu(self):
        self.click(self._CHARACTERS_PIKACHU)

    def verify_pikachu(self):
        return self.page.inner_text(self._VERIFY_PIKACHU)

    def click_table_platform_tab(self):
        self.click(self._TABLE_SHOP_PLATFORM_TAB)

    def click_table_platform_ios_android(self):
        self.click(self._TABLE_SHOP_PLATFORM_IOS_ANDROID)

    def click_table_platform_nintendo_switch(self):
        self.page.locator(self._TABLE_SHOP_PLATFORM_NINTENDO_SWITCH).first.click()

    def click_table_platform_nintendo_switch_2(self):
        self.page.locator(self._TABLE_SHOP_PLATFORM_NINTENDO_SWITCH_2).first.click()

    def click_table_characters_of_series_tab(self):
        self.click(self._TABLE_SHOP_CHARACTERS_OF_SERIES_TAB)

    def click_table_platform_show_more(self):
        self.click(self._TABLE_SHOP_PLATFORM_SHOW_MORE_BUTTON)

    def click_table_characters_animal_crossing(self):
        self.page.locator(self._TABLE_SHOP_CHARACTERS_ANIMAL_CROSSING).first.click()

    def click_table_characters_bowser(self):
        self.click(self._TABLE_SHOP_CHARACTERS_BOWSER)

    def click_table_characters_diddy_kong(self):
        self.click(self._TABLE_SHOP_CHARACTERS_DIDDY_KONG)

    def click_table_characters_donkey_kong(self):
        self.click(self._TABLE_SHOP_CHARACTERS_DONKEY_KONG)

    def click_table_characters_fire_emblem(self):
        self.click(self._TABLE_SHOP_CHARACTERS_FIRE_EMBLEM)

    def click_table_characters_kirby(self):
        self.click(self._TABLE_SHOP_CHARACTERS_KIRBY)

    def click_table_characters_link(self):
        self.click(self._TABLE_SHOP_CHARACTERS_LINK)

    def click_table_characters_luigi(self):
        self.click(self._TABLE_SHOP_CHARACTERS_LUIGI)

    def click_table_characters_mario(self):
        self.click(self._TABLE_SHOP_CHARACTERS_MARIO)

    def click_table_characters_pokemon(self):
        self.click(self._TABLE_SHOP_CHARACTERS_POKEMON)

    def click_table_characters_tlo_zelda(self):
        self.click(self._TABLE_SHOP_CHARACTERS_TLO_ZELDA)

    def click_table_characters_zelda(self):
        self.click(self._TABLE_SHOP_CHARACTERS_ZELDA)

    def click_table_price_tab(self):
        self.click(self._TABLE_SHOP_PRICE_TAB)

    def click_table_price_free(self):
        self.click(self._TABLE_SHOP_PRICE_FREE)

    def click_table_price_0_5(self):
        self.click(self._TABLE_SHOP_PRICE_0_5)

    def click_table_price_5_10(self):
        self.click(self._TABLE_SHOP_PRICE_5_10)

    def click_table_price_10_20(self):
        self.page.locator(self._TABLE_SHOP_PRICE_10_20).first.click()

    def click_table_price_20_40(self):
        self.page.locator(self._TABLE_SHOP_PRICE_20_40).first.click()

    def click_table_price_40_plus(self):
        self.click(self._TABLE_SHOP_PRICE_40_PLUS)

    def search_pokemon_game_price_max_40(self):
        self.scroll_to_shop()
        self.click_table_platform_tab()
        self.click_table_platform_nintendo_switch()
        self.click_table_characters_of_series_tab()
        self.click_table_platform_show_more()
        self.click_table_characters_pokemon()
        self.click_table_price_tab()
        self.click_table_price_20_40()

    def search_pokemon_game_price_over_40(self):
         self.scroll_to_shop()
         self.click_table_platform_tab()
         self.click_table_platform_nintendo_switch()
         self.click_table_characters_of_series_tab()
         self.click_table_platform_show_more()
         self.click_table_characters_pokemon()
         self.click_table_price_tab()
         self.click_table_price_40_plus()

    def third_tag_filter(self):
        return self.page.inner_text(self._THIRD_TAG)

    def click_first_result(self):
        self.click(self._TABLE_SHOP_FIRST_RESULT)

    def click_by_name(self, name: str, timeout: int = 5000):
        item = self.page.locator(self._RESULTS).filter(has_text=name).first
        item.wait_for(state="visible", timeout=timeout)
        item.scroll_into_view_if_needed(timeout=timeout)
        item.click(timeout=timeout)
=======
from playwright.sync_api import Page
from pages.base_page import BasePage

class ShopGames(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    _NINTENDO_SWITCH_2   = "div:nth-child(2) > section > div > div > div.OIFpM > div.P8EbW > div > div.sziGh > div:nth-child(1)"
    _GENRES = "div:nth-child(2) > section > div > div > div.OIFpM > div.P8EbW > div > div.sziGh > div:nth-child(2)"
    _FEATURED = "div:nth-child(2) div.OIFpM div:nth-child(3)"
    _CHARACTERS = "div:nth-child(2) div.OIFpM div:nth-child(4)"
    _BEST_SELLERS = "div:nth-child(2) div.OIFpM div:nth-child(5)"
    _COMING_SOON = "div:nth-child(2) div.OIFpM div:nth-child(6)"
    _VERIFY_COMING_SOON = ".sc-14s4g00-7 > h1"
    _NEW_RELEASES = "div:nth-child(2) div.OIFpM div:nth-child(7)"
    _VERIFY_NEW_RELEASES = "div.sc-14s4g00-2.jKoniT > h1"
    _CHARACTERS_MARIO = "#games-with-nintendo-characters div:nth-child(1) > a"
    _VERIFY_SUPER_MARIO = "div.sc-14s4g00-2.jKoniT > h1"
    _CHARACTERS_ZELDA = "#games-with-nintendo-characters div:nth-child(2) > a"
    _VERIFY_ZELDA = "div.sc-14s4g00-2.jKoniT > h1"
    _CHARACTERS_KIRBY = "#games-with-nintendo-characters div:nth-child(3) > a"
    _CHARACTERS_DONKEY_KONG = "#games-with-nintendo-characters div:nth-child(4) > a"
    _CHARACTERS_PIKACHU = "#games-with-nintendo-characters div:nth-child(5) > a"
    _VERIFY_PIKACHU = ".s954l._3TUsN._39p7O.sXEHt"
    _TABLE_SHOP_CLEAR_ALL_BUTTON = ".kAkyvX > div > button"
    _TABLE_SHOP_TYPE_DEALS = "div:nth-child(19) [aria-label='Deals']:"
    _TABLE_SHOP_TYPE_DEMO_AVAILABLE = "div:nth-child(19) [aria-label='Demo available']"
    _TABLE_SHOP_TYPE_DLC = "div:nth-child(19) [aria-label='DLC']"
    _TABLE_SHOP_TYPE_GAMES_VOUCHER = "div:nth-child(19) [aria-label='Game Voucher eligible']"
    _TABLE_SHOP_TYPE_GAMES_WITH_DLC = "div:nth-child(19) [aria-label='Games with DLC']"
    _TABLE_SHOP_TYPE_UPGRADE_PACK = "div:nth-child(19) [aria-label='Upgrade pack']"
    _TABLE_SHOP_NINTENDO_ONLINE_FEATURES_TAB = "h3:has-text('Nintendo Switch Online features')"
    _TABLE_SHOP_NINTENDO_ONLINE_FEATURES_ONLINE_PLAY = "div:nth-child(19) [aria-label='Online play']"
    _TABLE_SHOP_NINTENDO_ONLINE_FEATURES_SAVE_DATA_CLOUD = "div:nth-child(19) [aria-label='Save Data Cloud']:"
    _TABLE_SHOP_PLATFORM_TAB = "h3:has-text('Platform')"
    _TABLE_SHOP_PLATFORM_IOS_ANDROID = "div:nth-child(19) [aria-label='iOS / Android']"
    _TABLE_SHOP_PLATFORM_NINTENDO_SWITCH = "input[aria-label='Nintendo Switch']"
    _TABLE_SHOP_PLATFORM_NINTENDO_SWITCH_2 = "input[aria-label='Nintendo Switch 2']"
    _TABLE_SHOP_CHARACTERS_OF_SERIES_TAB = "h3:has-text('Character or series')"
    _TABLE_SHOP_PLATFORM_SHOW_MORE_BUTTON = ".kAkyvX > div > div.sc-1at2kvx-0.cslSfM > div > div > button"
    _TABLE_SHOP_CHARACTERS_ANIMAL_CROSSING = "input[aria-label='Animal Crossing']"
    _TABLE_SHOP_CHARACTERS_BOWSER = "input[aria-label='Bowser']"
    _TABLE_SHOP_CHARACTERS_DIDDY_KONG = "input[aria-label='Diddy Kong']"
    _TABLE_SHOP_CHARACTERS_DONKEY_KONG = "input[aria-label='Donkey Kong']"
    _TABLE_SHOP_CHARACTERS_FIRE_EMBLEM = "input[aria-label='Fire Emblem']"
    _TABLE_SHOP_CHARACTERS_KIRBY = "input[aria-label='Kirby']"
    _TABLE_SHOP_CHARACTERS_LINK = "input[aria-label='Link']"
    _TABLE_SHOP_CHARACTERS_LUIGI = "input[aria-label='Luigi']"
    _TABLE_SHOP_CHARACTERS_MARIO = "input[aria-label='Mario']"
    _TABLE_SHOP_CHARACTERS_POKEMON = "input[aria-label='Pokémon']"
    _TABLE_SHOP_CHARACTERS_TLO_ZELDA = "input[aria-label='The Legend of Zelda']"
    _TABLE_SHOP_CHARACTERS_ZELDA = "input[aria-label='Zelda']"
    _TABLE_SHOP_PRICE_TAB = "h3:has-text('Price')"
    _TABLE_SHOP_PRICE_FREE = "input[aria-label='Free to start']"
    _TABLE_SHOP_PRICE_0_5 = "input[aria-label='$0 - $4.99']"
    _TABLE_SHOP_PRICE_5_10 = "input[aria-label='$5 - $9.99']"
    _TABLE_SHOP_PRICE_10_20 = "input[aria-label='$10 - $19.99']"
    _TABLE_SHOP_PRICE_20_40 = "input[aria-label='$20 - $39.99']"
    _TABLE_SHOP_PRICE_40_PLUS = "section:has(h3:has-text('Price')) input[aria-label='$40+']"
    _THIRD_TAG = "div > button:nth-child(3) > span.ZovBS"
    _TABLE_SHOP_FIRST_RESULT = ".sc-1dskkk7-3.ljMhgM > div:nth-child(1)"
    _RESULTS = ".sc-1dskkk7-3.ljMhgM > div"
    _VERIFY_SELECTED_GAME_HEADER = ".kpUJEX > h1"


    def click_nintendo_switch_2(self):
        self.click(self._NINTENDO_SWITCH_2)

    def click_genres(self):
        self.click(self._GENRES)

    def click_featured(self):
        self.click(self._FEATURED)

    def click_characters(self):
        self.click(self._CHARACTERS)

    def click_coming_soon(self):
        self.click(self._COMING_SOON)

    def verify_coming_soon(self):
        return self.page.inner_text(self._VERIFY_COMING_SOON)

    def click_new_releases(self):
        self.click(self._NEW_RELEASES)

    def verify_new_releases(self):
        return self.page.inner_text(self._VERIFY_NEW_RELEASES)

    def verify_selected_game_header(self):
        return self.page.inner_text(self._VERIFY_SELECTED_GAME_HEADER)

    def scroll_to_shop(self):
        self.page.evaluate("""window.scrollTo(0, document.body.scrollHeight * 0.4)""")

    def click_table_clear_all(self):
        self.click(self._TABLE_SHOP_CLEAR_ALL_BUTTON)

    def click_table_type_deals(self):
        self.click(self._TABLE_SHOP_TYPE_DEALS)

    def click_table_type_dlc(self):
        self.click(self._TABLE_SHOP_TYPE_DLC)

    def click_table_type_demo_available(self):
        self.click(self._TABLE_SHOP_TYPE_DEMO_AVAILABLE)

    def click_table_type_game_voucher(self):
        self.click(self._TABLE_SHOP_TYPE_GAMES_VOUCHER)

    def click_table_type_games_with_dlc(self):
        self.click(self._TABLE_SHOP_TYPE_GAMES_WITH_DLC)

    def click_table_type_upgrade_pack(self):
        self.click(self._TABLE_SHOP_TYPE_UPGRADE_PACK)

    def click_table_nintendo_switch_online_tab(self):
        self.click(self._TABLE_SHOP_NINTENDO_ONLINE_FEATURES_TAB)

    def click_table_nintendo_online_play(self):
        self.click(self._TABLE_SHOP_NINTENDO_ONLINE_FEATURES_ONLINE_PLAY)

    def click_table_nintendo_save_data_cloud(self):
        self.click(self._TABLE_SHOP_NINTENDO_ONLINE_FEATURES_SAVE_DATA_CLOUD)

    def click_characters_mario(self):
        self.click(self._CHARACTERS_MARIO)

    def verify_super_mario(self):
        return self.page.inner_text(self._VERIFY_SUPER_MARIO)

    def click_characters_zelda(self):
        self.click(self._CHARACTERS_ZELDA)

    def verify_zelda(self):
        return self.page.inner_text(self._VERIFY_ZELDA)

    def click_characters_kirby(self):
        self.click(self._CHARACTERS_KIRBY)

    def click_characters_donkey_kong(self):
        self.click(self._CHARACTERS_DONKEY_KONG)

    def click_characters_pikachu(self):
        self.click(self._CHARACTERS_PIKACHU)

    def verify_pikachu(self):
        return self.page.inner_text(self._VERIFY_PIKACHU)

    def click_table_platform_tab(self):
        self.click(self._TABLE_SHOP_PLATFORM_TAB)

    def click_table_platform_ios_android(self):
        self.click(self._TABLE_SHOP_PLATFORM_IOS_ANDROID)

    def click_table_platform_nintendo_switch(self):
        self.page.locator(self._TABLE_SHOP_PLATFORM_NINTENDO_SWITCH).first.click()

    def click_table_platform_nintendo_switch_2(self):
        self.page.locator(self._TABLE_SHOP_PLATFORM_NINTENDO_SWITCH_2).first.click()

    def click_table_characters_of_series_tab(self):
        self.click(self._TABLE_SHOP_CHARACTERS_OF_SERIES_TAB)

    def click_table_platform_show_more(self):
        self.click(self._TABLE_SHOP_PLATFORM_SHOW_MORE_BUTTON)

    def click_table_characters_animal_crossing(self):
        self.page.locator(self._TABLE_SHOP_CHARACTERS_ANIMAL_CROSSING).first.click()

    def click_table_characters_bowser(self):
        self.click(self._TABLE_SHOP_CHARACTERS_BOWSER)

    def click_table_characters_diddy_kong(self):
        self.click(self._TABLE_SHOP_CHARACTERS_DIDDY_KONG)

    def click_table_characters_donkey_kong(self):
        self.click(self._TABLE_SHOP_CHARACTERS_DONKEY_KONG)

    def click_table_characters_fire_emblem(self):
        self.click(self._TABLE_SHOP_CHARACTERS_FIRE_EMBLEM)

    def click_table_characters_kirby(self):
        self.click(self._TABLE_SHOP_CHARACTERS_KIRBY)

    def click_table_characters_link(self):
        self.click(self._TABLE_SHOP_CHARACTERS_LINK)

    def click_table_characters_luigi(self):
        self.click(self._TABLE_SHOP_CHARACTERS_LUIGI)

    def click_table_characters_mario(self):
        self.click(self._TABLE_SHOP_CHARACTERS_MARIO)

    def click_table_characters_pokemon(self):
        self.click(self._TABLE_SHOP_CHARACTERS_POKEMON)

    def click_table_characters_tlo_zelda(self):
        self.click(self._TABLE_SHOP_CHARACTERS_TLO_ZELDA)

    def click_table_characters_zelda(self):
        self.click(self._TABLE_SHOP_CHARACTERS_ZELDA)

    def click_table_price_tab(self):
        self.click(self._TABLE_SHOP_PRICE_TAB)

    def click_table_price_free(self):
        self.click(self._TABLE_SHOP_PRICE_FREE)

    def click_table_price_0_5(self):
        self.click(self._TABLE_SHOP_PRICE_0_5)

    def click_table_price_5_10(self):
        self.click(self._TABLE_SHOP_PRICE_5_10)

    def click_table_price_10_20(self):
        self.page.locator(self._TABLE_SHOP_PRICE_10_20).first.click()

    def click_table_price_20_40(self):
        self.page.locator(self._TABLE_SHOP_PRICE_20_40).first.click()

    def click_table_price_40_plus(self):
        self.click(self._TABLE_SHOP_PRICE_40_PLUS)

    def search_pokemon_game_price_max_40(self):
        self.scroll_to_shop()
        self.click_table_platform_tab()
        self.click_table_platform_nintendo_switch()
        self.click_table_characters_of_series_tab()
        self.click_table_platform_show_more()
        self.click_table_characters_pokemon()
        self.click_table_price_tab()
        self.click_table_price_20_40()

    def search_pokemon_game_price_over_40(self):
         self.scroll_to_shop()
         self.click_table_platform_tab()
         self.click_table_platform_nintendo_switch()
         self.click_table_characters_of_series_tab()
         self.click_table_platform_show_more()
         self.click_table_characters_pokemon()
         self.click_table_price_tab()
         self.click_table_price_40_plus()

    def third_tag_filter(self):
        return self.page.inner_text(self._THIRD_TAG)

    def click_first_result(self):
        self.click(self._TABLE_SHOP_FIRST_RESULT)

    def click_by_name(self, name: str, timeout: int = 5000):
        item = self.page.locator(self._RESULTS).filter(has_text=name).first
        item.wait_for(state="visible", timeout=timeout)
        item.scroll_into_view_if_needed(timeout=timeout)
        item.click(timeout=timeout)
>>>>>>> master
