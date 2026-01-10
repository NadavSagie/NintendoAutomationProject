from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def highlight(self, locator) -> None:
        script = """
           element => {
               const originalStyle = element.style.cssText;
               element.style.transition = 'all 0.2s ease-in-out';
               element.style.outline = '3px solid red';
               element.style.backgroundColor = 'yellow';
               setTimeout(() => {
                   element.style.cssText = originalStyle;
               }, 500);
           }
        """
        self.page.locator(locator).evaluate(script)

    def fill_text(self, locator, text):
        self.page.locator(locator).wait_for(state="visible")
        self.highlight(locator)
        self.page.locator(locator).fill(text)

    def click(self, locator):
        self.page.locator(locator).wait_for(state="visible")
        self.highlight(locator)
        self.page.locator(locator).click()

    def select_option(self, locator, value):
        self.page.locator(locator).wait_for(state="visible")
        self.highlight(locator)
        self.page.locator(locator).select_option(value=value)

    def press(self, locator, key):
        self.page.locator(locator).wait_for(state="visible")
        self.highlight(locator)
        self.page.locator(locator).press(key)