from time import sleep

import pytest
from playwright.sync_api import Page, sync_playwright
from pages.explore import Explore
from pages.home_page import HomePage
from pages.characters import Characters
from pages.shop import Shop
from pages.shop_games import ShopGames
from pages.sign_up import SignUp
from pages.support import Support

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=["--start-maximized"])
        yield browser
        browser.close()

@pytest.fixture(scope="class", autouse=True)
def setup_page_class(request, browser):
    context = browser.new_context(no_viewport=True)
    page = context.new_page()
    page.goto("https://www.nintendo.com/us/")
    request.cls.page = page
    request.cls.home_page = HomePage(page)
    request.cls.characters = Characters(page)
    request.cls.explore = Explore(page)
    request.cls.shop = Shop(page)
    request.cls.shop_games = ShopGames(page)
    request.cls.support = Support(page)
    request.cls.sign_up = SignUp(page)
    yield
    sleep(1)
    page.close()
    context.close()
