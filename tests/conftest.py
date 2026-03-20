import os
import pytest
from playwright.sync_api import sync_playwright

from pages.explore import Explore
from pages.home_page import HomePage
from pages.characters import Characters
from pages.shop import Shop
from pages.shop_games import ShopGames
from pages.sign_up import SignUp
from pages.support import Support


BASE_URL = "https://www.nintendo.com/us/"


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        is_ci = os.getenv("CI", "").lower() == "true"

        if is_ci:
            browser = p.chromium.launch(
                headless=True,
                args=["--autoplay-policy=no-user-gesture-required"],
            )
        else:
            browser = p.chromium.launch(
                channel="chrome",   # 👈 Chrome אמיתי
                headless=False,
                args=["--start-maximized"],
            )

        yield browser
        browser.close()


@pytest.fixture(scope="class", autouse=True)
def setup_page_class(request, browser):
    context = browser.new_context(
        viewport={"width": 1440, "height": 900}
    )
    page = context.new_page()

    page.goto(BASE_URL, wait_until="domcontentloaded")
    page.wait_for_load_state("networkidle")

    request.cls.page = page
    request.cls.home_page = HomePage(page)
    request.cls.characters = Characters(page)
    request.cls.explore = Explore(page)
    request.cls.shop = Shop(page)
    request.cls.shop_games = ShopGames(page)
    request.cls.support = Support(page)
    request.cls.sign_up = SignUp(page)

    yield

    page.close()
    context.close()


@pytest.fixture(scope="session", autouse=False)
def setup_page_session(request, browser):
    context = browser.new_context(
        viewport={"width": 1440, "height": 900}
    )
    page = context.new_page()

    page.goto(BASE_URL, wait_until="domcontentloaded")
    page.wait_for_load_state("networkidle")

    request.session.page = page
    request.session.home_page = HomePage(page)
    request.session.characters = Characters(page)
    request.session.explore = Explore(page)
    request.session.shop = Shop(page)
    request.session.shop_games = ShopGames(page)
    request.session.support = Support(page)
    request.session.sign_up = SignUp(page)

    yield

    page.close()
    context.close()