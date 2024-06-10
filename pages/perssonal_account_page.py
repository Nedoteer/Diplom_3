import allure

from locators.recover_password import StellarBurgersLocators
from User import User
from pages.base_page import BasePage


class PerssonalAccount(BasePage):

     @allure.step('Переход по клику на «Личный кабинет»')
     def click_perssonal_account(self):
         self.wheit_and_click(StellarBurgersLocators.BUTTON_PERSSONAL_ACCOUNT)
         self.wheit_element_text(StellarBurgersLocators.TEXT_ENTER, 'Вход')
         return self.find_and_return_element(StellarBurgersLocators.TEXT_ENTER)

     @allure.step('Переход в раздел «История заказов»')
     def click_history_count(self):
         self.wheit_and_click(StellarBurgersLocators.BUTTON_PERSSONAL_ACCOUNT)
         create_user = User()
         user = create_user.create_user()
         self.send_key_element(StellarBurgersLocators.EMAIL_ACCOUNT, user.json()['user']['email'])
         self.send_key_element(StellarBurgersLocators.PASSWORD_ACCOUNT, 'password')
         self.click_element(StellarBurgersLocators.BUTTON_LOGIN_IN_ACCOUNT)
         self.wheit_element_text(StellarBurgersLocators.TEXT_COUNT, 'Оформить заказ')
         self.wheit_and_click(StellarBurgersLocators.BUTTON_PERSSONAL_ACCOUNT)
         self.wheit_element_click(StellarBurgersLocators.TEXT_HISTORY)
         self.click_element(StellarBurgersLocators.TEXT_HISTORY)

     @allure.step('Выход из аккаунта')
     def exit_account(self):
         self.wheit_and_click(StellarBurgersLocators.BUTTON_PERSSONAL_ACCOUNT)
         create_user = User()
         user = create_user.create_user()
         self.send_key_element(StellarBurgersLocators.EMAIL_ACCOUNT, user.json()['user']['email'])
         self.send_key_element(StellarBurgersLocators.PASSWORD_ACCOUNT, 'password')
         self.click_element(StellarBurgersLocators.BUTTON_LOGIN_IN_ACCOUNT)
         self.wheit_element_text(StellarBurgersLocators.TEXT_COUNT, 'Оформить заказ')
         self.wheit_and_click(StellarBurgersLocators.BUTTON_PERSSONAL_ACCOUNT)
         self.wheit_element_click(StellarBurgersLocators.TEXT_HISTORY)
         self.click_element(StellarBurgersLocators.BUTTON_EXIT)
         self.wheit_element_text(StellarBurgersLocators.TEXT_ENTER, 'Вход')




