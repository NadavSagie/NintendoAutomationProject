from playwright.sync_api import Page
from pages.explore import Explore
from pages.home_page import HomePage
from pages.characters import Characters
from pages.shop import Shop
from pages.shop_characters import ShopCharacters
from pages.shop_games import ShopGames
from pages.shop_hardware import ShopHardware
from pages.shop_merchandise import ShopMerchandise
from pages.shop_sales_and_deals import ShopSalesAndDeals
from pages.shop_store_execlusives import ShopStoreExclusives
from pages.sign_up import SignUp
from pages.support import Support


class BaseTest:
    page: Page
    home_page: HomePage
    shop: Shop
    shop_games: ShopGames
    explore: Explore
    support: Support
    characters: Characters
    sign_up: SignUp
    shop_characters : ShopCharacters
    shop_hardware: ShopHardware
    shop_merchandise: ShopMerchandise
    shop_sales_and_deals: ShopSalesAndDeals
    shop_store_exclusives: ShopStoreExclusives