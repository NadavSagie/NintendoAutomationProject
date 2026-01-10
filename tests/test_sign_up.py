import allure
from tests.base_test import BaseTest


@allure.epic("Nintendo Sign Up Tests")
class TestSignUp(BaseTest):

    #def setup_method(self):
        #self.page.goto("https://www.nintendo.com/us/")

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

    @allure.title("Full Short Sign-Up Flow - Expected Error")
    def test_sign_up(self):
        self.sign_up.sign_up_short_process("7", "11", "2000", "tester111", "fake@gmail.com", "Test1234", "male", "Israel", "142")
        current_url = self.page.url
        print(f"[DEBUG] Final URL: {current_url}")
        assert "error" in current_url.lower()

    @allure.title("Full Sign-Up Flow - Expected Error")
    def test_sign_up_with_invalid_email(self):
        self.sign_up.sign_up_full_process("7", "11", "2000", "tester111", "fake@invalid.com", "Test1234", "male", "Israel", "142")
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
        self.sign_up.fill_text(self.sign_up._SIGN_UP_PASSWORD, "Blue1234")
        self.sign_up.fill_text(self.sign_up._SIGN_UP_CONFIRM_PASSWORD, "Blue1234")
        self.sign_up.select_option(self.sign_up._SIGN_UP_COUNTRY, "Israel")
        self.sign_up.select_option(self.sign_up._SIGN_UP_TIME_ZONE, "142")
        self.sign_up.click(self.sign_up._SIGN_UP_CONTINUE_BUTTON)
        assert "required" in self.page.content().lower()

    @allure.title("Error message appears for duplicate nickname/email")
    def test_signup_error_messages(self):
        self.sign_up.sign_up_full_process("6", "9", "2000", "usednickname", "test@test.com", "Test1234", "male", "Israel", "142")
        error_msg = self.sign_up.account_sign_up_error()
        assert error_msg is not None and error_msg != ""