import allure

from data import StellarData
from locators.recover_password import StellarBurgersLocators
from pages.base_page import BasePage


class RecoverPassword(BasePage):

    @allure.step('Переход на страницу восстановления пароля по кнопке «Восстановить пароль')
    def click_button_recover_password(self):
        self.wheit_and_click(StellarBurgersLocators.BUTTON_PERSSONAL_ACCOUNT)
        self.click_element(StellarBurgersLocators.LINK_FORGOT_PASSWORD)
        self.wheit_element_text(StellarBurgersLocators.TEXT_RECOVER, 'Восстановление пароля')
        return self.find_and_return_element(StellarBurgersLocators.TEXT_RECOVER)

    @allure.step('Ввод почты и клик по кнопке «Восстановить»')
    def put_email_click_buton_recover(self):
        self.wheit_and_click(StellarBurgersLocators.BUTTON_PERSSONAL_ACCOUNT)
        self.click_element(StellarBurgersLocators.LINK_FORGOT_PASSWORD)
        self.send_key_element(StellarBurgersLocators.EMAIL_ACCOUNT, StellarData.EMAIL)
        self.click_element(StellarBurgersLocators.BUTTON_RECOVER)
        self.wheit_element_text(StellarBurgersLocators.LABEL_EMAIL,
                                                              'Введите код из письма')
        return self.find_and_return_element(StellarBurgersLocators.LABEL_EMAIL)

    @allure.step('Клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    def click_button_show(self):
        self.wheit_and_click(StellarBurgersLocators.BUTTON_PERSSONAL_ACCOUNT)
        self.click_element(StellarBurgersLocators.LINK_FORGOT_PASSWORD)
        self.send_key_element(StellarBurgersLocators.EMAIL_ACCOUNT, StellarData.EMAIL)
        self.click_element(StellarBurgersLocators.BUTTON_RECOVER)
        self.wheit_and_click(StellarBurgersLocators.PASSWORD_ACCOUNT)
        self.send_key_element(StellarBurgersLocators.PASSWORD_ACCOUNT, StellarData.PASSWORD)
        self.wheit_and_click(StellarBurgersLocators.BUTTON_ICON)
        return self.find_and_return_element(StellarBurgersLocators.STATUS_CHANGE)



