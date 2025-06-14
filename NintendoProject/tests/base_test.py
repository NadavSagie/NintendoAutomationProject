from playwright.sync_api import Page
from pages.explore import Explore
from pages.home_page import HomePage
from pages.characters import Characters
from pages.shop import Shop
from pages.shop_games import ShopGames
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
