from time import sleep
from playwright.sync_api import Page
from pages.base_page import BasePage


class SignUp(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    _ACCOUNT = "._9eU-h"
    _ACCOUNT_LOG_IN = ".sc-1h06vbw-0.iDyxyN > button"
    _ACCOUNT_SIGN_UP = ".Mc7qX.aqpwZ"
    _SIGN_UP_MONTH = "#birth-month-field"
    _SIGN_UP_DAY = "#birth-day-field"
    _SIGN_UP_YEAR = "#birth-year-field"
    _SIGN_UP_SUBMIT = "#authorize-age-gate-us-form_pc_button_0"
    _NINTENDO_HOME_SIGN_UP = "#common-header_pc_a_0"
    _CREATE_NINTENDO_ACCOUNT = "#common-header_pc_a_2"
    _ACCOUNT_UNDER_16 = "#authorize-age-gate_pc_a_0"
    _ACCOUNT_OVER_16 = "#authorize-age-gate_pc_a_1"
    _SIGN_UP_NICKNAME = "#register-form_pc_input_0"
    _SIGN_UP_EMAIL = "#email"
    _SIGN_UP_PASSWORD = "#register-form_pc_input_1"
    _SIGN_UP_CONFIRM_PASSWORD = "#register-form_pc_input_2"
    _SIGN_UP_GENDER = "#register-form_pc_select_0"
    _SIGN_UP_COUNTRY = "#country-field"
    _SIGN_UP_TIME_ZONE = "#timezone-field"
    _SIGN_UP_USER_AGREEMENT_CHECKBOX = "label[for='form-terms_consented']"
    _SIGN_UP_PRIVACY_POLICY_CHECKBOX = "label[for='form-policy_consented']"
    _SIGN_UP_CONTINUE_BUTTON = "#register-form_pc_button_5"
    _SIGN_UP_UNRECEIVED_EMAIL = "#email_opted_in_unreceive"
    _SIGN_UP_REGISTER_BUTTON = "[value='register']"
    _SIGN_UP_ACCOUNT_CREATION_UNMADE_MSG = ".c-attention_inner"
    _SIGN_UP_ACCOUNT_CREATION_ERROR = "data-template-id=['cdn-display-error']"
    _SIGN_UP_HOME_BTN = ".logo-nintendo"

    def sign_up_short_process(self, month, day, year, nickname, email, password, gender, country, timezone):
        self.click(self._ACCOUNT)
        self.click(self._ACCOUNT_SIGN_UP)
        self.select_option(self._SIGN_UP_MONTH, month)
        self.select_option(self._SIGN_UP_DAY, day)
        self.select_option(self._SIGN_UP_YEAR, year)
        self.click(self._SIGN_UP_SUBMIT)

        self.fill_text(self._SIGN_UP_NICKNAME, nickname)
        self.fill_text(self._SIGN_UP_EMAIL, email)
        self.fill_text(self._SIGN_UP_PASSWORD, password)
        self.fill_text(self._SIGN_UP_CONFIRM_PASSWORD, password)

        self.select_option(self._SIGN_UP_MONTH, month)
        self.select_option(self._SIGN_UP_DAY, day)
        self.select_option(self._SIGN_UP_YEAR, year)
        self.select_option(self._SIGN_UP_GENDER, gender)
        self.select_option(self._SIGN_UP_COUNTRY, country)
        self.select_option(self._SIGN_UP_TIME_ZONE, timezone)

        self.click(self._SIGN_UP_USER_AGREEMENT_CHECKBOX)
        self.click(self._SIGN_UP_PRIVACY_POLICY_CHECKBOX)
        sleep(2)
        self.click(self._SIGN_UP_CONTINUE_BUTTON)

        if "register" in self.page.url:
            try:
                if self.page.locator(self._SIGN_UP_UNRECEIVED_EMAIL).is_visible():
                    self.click(self._SIGN_UP_UNRECEIVED_EMAIL)
            except:
                print("[INFO] UNRECEIVED EMAIL button not visible or missing")

        else:
            print(f"[ERROR] Unexpected URL: {self.page.url}")

    def sign_up_full_process(self, month, day, year, nickname, email, password, gender, country, timezone):
        self.click(self._ACCOUNT)
        self.click(self._ACCOUNT_SIGN_UP)
        self.select_option(self._SIGN_UP_MONTH, month)
        self.select_option(self._SIGN_UP_DAY, day)
        self.select_option(self._SIGN_UP_YEAR, year)
        self.click(self._SIGN_UP_SUBMIT)
        self.click(self._NINTENDO_HOME_SIGN_UP)
        self.click(self._CREATE_NINTENDO_ACCOUNT)
        self.click(self._ACCOUNT_OVER_16)
        self.fill_text(self._SIGN_UP_NICKNAME, nickname)
        self.fill_text(self._SIGN_UP_EMAIL, email)
        self.fill_text(self._SIGN_UP_PASSWORD, password)
        self.fill_text(self._SIGN_UP_CONFIRM_PASSWORD, password)
        self.select_option(self._SIGN_UP_MONTH, month)
        self.select_option(self._SIGN_UP_DAY, day)
        self.select_option(self._SIGN_UP_YEAR, year)
        self.select_option(self._SIGN_UP_GENDER, gender)
        self.select_option(self._SIGN_UP_COUNTRY, country)
        self.select_option(self._SIGN_UP_TIME_ZONE, timezone)
        self.click(self._SIGN_UP_USER_AGREEMENT_CHECKBOX)
        self.click(self._SIGN_UP_PRIVACY_POLICY_CHECKBOX)
        self.click(self._SIGN_UP_CONTINUE_BUTTON)
        self.click(self._SIGN_UP_UNRECEIVED_EMAIL)
        self.click(self._SIGN_UP_REGISTER_BUTTON)

    def account_sign_up_not_created_msg(self):
        return self.page.inner_text(self._SIGN_UP_ACCOUNT_CREATION_UNMADE_MSG)

    def account_sign_up_error(self):
        return self.page.inner_text(self._SIGN_UP_ACCOUNT_CREATION_ERROR)

    def click_sign_up_home_btn(self):
        self.click(self._SIGN_UP_HOME_BTN)