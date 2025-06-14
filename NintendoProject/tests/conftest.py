import pytest
from playwright.sync_api import Page
from pages.explore import Explore
from pages.home_page import HomePage
from pages.characters import Characters
from pages.shop import Shop
from pages.shop_games import ShopGames
from pages.sign_up import SignUp
from pages.support import Support


@pytest.fixture(scope="class", autouse=True)
def setup_page_class(request, browser):
    request.cls.page = browser.new_page()
    request.cls.page.goto("https://www.nintendo.com/us/")
    request.cls.home_page = HomePage(request.cls.page)
    request.cls.characters = Characters(request.cls.page)
    request.cls.explore = Explore(request.cls.page)
    request.cls.shop = Shop(request.cls.page)
    request.cls.shop_games = ShopGames(request.cls.page)
    request.cls.support = Support(request.cls.page)
    request.cls.sign_up = SignUp(request.cls.page)
    yield
    request.cls.page.close()
    browser.close()

"""
@pytest.fixture(scope="class", autouse=True)
def setup_page_class(request, page: Page):
    request.cls.page = browser.new_page()
    request.cls.page.goto("https://galmatalon.github.io/tutorials/indexNoID.html")
    request.cls.wizard1_page = Wizard1Page(request.cls.page)
    request.cls.wizard2_page = Wizard2Page(request.cls.page)
    request.cls.wizard3_page = Wizard3Page(request.cls.page)
    yield
    request.cls.page.close()
    browser.close()

"""