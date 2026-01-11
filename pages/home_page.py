import time

from playwright.sync_api import Page
from pages.base_page import BasePage

class HomePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    _EXPLORE = "#explore-tab"
    _VERIFY_EXPLORE = ".Mb4lk > p"
    _SUPPORT = "#support-tab"
    _SUPPORT_HOME = ".YSMyD"
    _SHOP = "#shop-tab"
    _SHOP_TAB_MSG = ".YSMyD"
    _SEARCH = "#search"
    _SEARCH_LINE = "[data-testid='desktop-nav'] input[placeholder='Search games, hardware, news, etc']"
    _SEARCH_RESULTS = "#all-tab a"
    _SEARCH_FIRST_RESULT_TITLE = ".sc-qyho57-0.eccGkq > h2"
    _WISH_LIST = "[aria-label='Wish List']"
    _CART = "[aria-label='Cart']"
    _ACCOUNT = "._9eU-h"
    _ACCOUNT_LOG_IN = ".sc-1h06vbw-0.iDyxyN > button"
    _ACCOUNT_SIGN_UP = ".Mc7qX.aqpwZ"
    _ACCOUNT_LOG_IN_PAGE_TITLE = ".c-header_siteLogo"
    _LANGUAGES = "div.sc-14wlync-1.hhYTBR > a._8L3UE > span"
    _HOME_BTN = "div.sc-14wlync-1.jaBTVj > a > span"
    _START_SHOPPING = "section:nth-child(5) span.Mc7qX"
    _GAMING_SYSTEM = "section:nth-child(7) span.Mc7qX"
    _NINTENDO_SWITCH_ONLINE = "section.sc-1bfhtts-0.ierIgL.op-nso-banner a.MFcmt.G0A6l._3LMnG.xN-5A > span.Mc7qX"
    _NEWS = "[data-testid='NewsIcon']"
    _DIGITAL_BEST_SELLERS = "div:nth-child(1) > div._67AVi > a"
    _DIGITAL_NEW_RELEASES = "div:nth-child(2) > div._67AVi > a"
    _FEATURES_PREVIOUS_BTN = "section:nth-child(3) > div.mBL2V > div > div._1vq-b.IydHV"
    _FEATURES_NEXT_BTN = "section:nth-child(3) > div.mBL2V > div > div._1vq-b.IydHV > button.TcDZK.y8-wO._9Nqbd.SUqIq"
    _SHOP_GAMES = " a:nth-child(1) > span.sc-1k9k6ch-2.clfwsO"
    _SHOP_HARDWARE = " a:nth-child(2) > span.sc-1k9k6ch-2.clfwsO"
    _SHOP_MERCHANDISE = " a:nth-child(3) > span.sc-1k9k6ch-2.clfwsO"
    _SHOP_SALES_AND_DEALS = " a:nth-child(4) > span.sc-1k9k6ch-2.clfwsO"
    _SHOP_EXCLUSIVES = " a:nth-child(5) > span.sc-1k9k6ch-2.clfwsO"
    _SHOP_CHARACTERS = " a:nth-child(6) > span.sc-1k9k6ch-2.clfwsO"
    _SHOP_NINTENDO_STORE = "._5jHgU"
    _VERIFY_WHATSNEW = " div.sc-wswg5a-0.byNSlr > h1"
    _CLOSE_EXPLORE = "#explore-panel button > svg"
    _CLOSE_SHOP = "#shop-panel div > button"
    _CLOSE_SUPPORT = "#support-panel div > button"
    _SLIDE_SHOW_NEXT = "[aria-label='Next']"
    _SLIDE_SHOW_PREVIOUS = "[aria-label='Previous']"



    def click_explore(self):
        self.click(self._EXPLORE)
        self.click(self._CLOSE_EXPLORE)

    def verify_explore(self):
        return self.page.inner_text(self._VERIFY_EXPLORE)

    def click_support(self):
        self.click(self._SUPPORT)
        self.click(self._CLOSE_SUPPORT)

    def get_support_text(self):
        return self.page.inner_text(self._SUPPORT_HOME)

    def change_language(self):
        self.click(self._LANGUAGES)

    def click_home_btn(self):
        self.click(self._HOME_BTN)

    def click_shop(self):
        self.click(self._SHOP)
        self.click(self._CLOSE_SHOP)

    def get_shop_text(self):
        return self.page.inner_text(self._SHOP_TAB_MSG)

    def click_cart(self):
        self.click(self._CART)

    def search(self, text):
        self.click(self._SEARCH)
        self.type(self._SEARCH_LINE, text)
        self.press(self._SEARCH_LINE, "Enter")

    def click_first_search_result(self):
        self.click(self._SEARCH_LINE_RESULT_FIRST)

    def result_title(self):
        return self.page.inner_text(self._SEARCH_FIRST_RESULT_TITLE)

    def click_wish_list(self):
        self.page.wait_for_selector(self._WISH_LIST)
        self.page.locator(self._WISH_LIST).first.click()

    def click_my_account(self):
        self.click(self._ACCOUNT)
        self.page.click(".sc-12ilsja-0.afISW")

    def click_sign_up(self):
        self.click(self._ACCOUNT)
        self.click(self._ACCOUNT_SIGN_UP)

    def click_log_in_and_get_popup(self):
        with self.page.expect_popup() as popup_info:
            self.click(self._ACCOUNT)
            self.click(self._ACCOUNT_LOG_IN)
        new_page = popup_info.value
        new_page.wait_for_load_state("domcontentloaded")
        return new_page

    def log_in_title(self, popup_page):
        popup_page.locator("h1.c-pageTitle").wait_for(state="visible")
        return popup_page.inner_text("h1.c-pageTitle")

    def click_start_shopping(self):
        self.click(self._START_SHOPPING)

    def click_gaming_systems(self):
        self.click(self._GAMING_SYSTEM)

    def click_nintendo_switch_online(self):
        self.click(self._NINTENDO_SWITCH_ONLINE)

    def click_all_news(self):
        self.click(self._NEWS)

    def verify_click_all_news(self):
        return self.page.inner_text(self._VERIFY_WHATSNEW)

    def click_best_sellers(self):
        self.click(self._DIGITAL_BEST_SELLERS)

    def scroll_to_bottom_and_top(self):
        # Scroll slowly to bottom
        self.page.evaluate("""
                () => {
                    return new Promise((resolve) => {
                        let totalHeight = 0;
                        const distance = 100; // כמה פיקסלים לזוז כל פעם
                        const timer = setInterval(() => {
                            window.scrollBy(0, distance);
                            totalHeight += distance;

                            if (totalHeight >= document.body.scrollHeight) {
                                clearInterval(timer);
                                resolve();
                            }
                        }, 100); // כל כמה מילישניות לזוז - ערך גבוה = יותר איטי
                    });
                }
            """)
        # אפשר להוסיף הפסקה קטנה אם רוצים
        import time
        time.sleep(1)

        # Scroll slowly back to top
        self.page.evaluate("""
                () => {
                    return new Promise((resolve) => {
                        let totalHeight = document.body.scrollHeight;
                        const distance = 100;
                        const timer = setInterval(() => {
                            window.scrollBy(0, -distance);
                            totalHeight -= distance;

                            if (totalHeight <= 0) {
                                clearInterval(timer);
                                resolve();
                            }
                        }, 100);
                    });
                }
            """)

    def scroll_page(self, direction: str = "down", percent: float = 50.0, duration_ms: int = 12000, stops: int = 2,
                    dwell_ms: int = 1250):
        self.page.evaluate(
            """
            ({ direction, percent, duration, stops, dwell }) => new Promise((resolve) => {
                const dir = (String(direction || "down").toLowerCase() === "up") ? "up" : "down";
                const doc = document.documentElement, body = document.body;

                const scrollHeight = Math.max(doc.scrollHeight, body.scrollHeight);
                const startY  = window.scrollY || window.pageYOffset || 0;
                const delta   = Math.max(0, scrollHeight * (Math.max(0, percent) / 100));
                const maxY    = Math.max(0, scrollHeight - window.innerHeight);
                const endY    = dir === "down" ? Math.min(startY + delta, maxY) : Math.max(startY - delta, 0);

                // יעדי ביניים (waypoints): תחנות עצירה + יעד סופי
                const stopsCount = Math.max(0, Math.floor(stops || 0));
                const waypoints = [startY];
                for (let i = 1; i <= stopsCount; i++) {
                    const frac = i / (stopsCount + 1);
                    waypoints.push(dir === "down" ? startY + delta * frac : startY - delta * frac);
                }
                waypoints.push(endY);

                if (waypoints.length <= 1 || startY === endY) { resolve(); return; }

                // חלוקת הזמן שווה בין המקטעים
                const segDuration = Math.max(1, Math.floor(duration / (waypoints.length - 1)));
                const dwellTime   = Math.max(0, dwell);

                const easeInOut = (t) => (t < 0.5) ? (2 * t * t) : (1 - Math.pow(-2 * t + 2, 2) / 2);

                let segIndex = 0;

                const animateSegment = () => {
                    const y0 = waypoints[segIndex];
                    const y1 = waypoints[segIndex + 1];
                    const distance = y1 - y0;
                    const t0 = performance.now();

                    const step = (now) => {
                        const t = Math.min(1, (now - t0) / segDuration);
                        const y = y0 + distance * easeInOut(t);
                        window.scrollTo(0, y);
                        if (t < 1) {
                            requestAnimationFrame(step);
                        } else {
                            segIndex++;
                            if (segIndex < waypoints.length - 1) {
                                if (dwellTime > 0) {
                                    setTimeout(() => requestAnimationFrame(animateSegment), dwellTime);
                                } else {
                                    requestAnimationFrame(animateSegment);
                                }
                            } else {
                                resolve();
                            }
                        }
                    };
                    requestAnimationFrame(step);
                };

                requestAnimationFrame(animateSegment);
            })
            """,
            {"direction": direction, "percent": percent, "duration": duration_ms, "stops": stops, "dwell": dwell_ms}
        )

    def click_digital_new_releases(self):
        self.click(self._DIGITAL_NEW_RELEASES)
        time.sleep(1)

    def click_search_result(self, index: int):
        result = self.page.locator(self._SEARCH_RESULTS).nth(index)
        result.wait_for(state="visible")
        result.click()

    def slide_show_next(self):
        self.click(self._SLIDE_SHOW_NEXT)

    def slide_show_previous(self):
        self.click(self._SLIDE_SHOW_PREVIOUS)