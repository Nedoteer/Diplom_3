import allure
from seletools.actions import drag_and_drop

from locators.recover_password import StellarBurgersLocators
from User import User
from pages.base_page import BasePage


class FunctionalPage(BasePage):

    @allure.step('Переход по клику на «Конструктор»')
    def click_constructor(self):
        self.wheit_and_click(StellarBurgersLocators.BUTTON_PERSSONAL_ACCOUNT)
        self.click_element(StellarBurgersLocators.BUTTON_CONSTRUCTOR)
        self.wheit_element_text(StellarBurgersLocators.TEXT_BURGER, 'Соберите бургер')
        return self.find_and_return_element(StellarBurgersLocators.TEXT_BURGER)

    @allure.step('Переход по клику на «Лента заказов»')
    def click_count(self):
        self.wheit_and_click(StellarBurgersLocators.BUTTON_PERSSONAL_ACCOUNT)
        self.click_element(StellarBurgersLocators.BUTTON_COUNT)
        self.wheit_element_text(StellarBurgersLocators.TEXT_DONE, 'Выполнено за сегодня:')
        return self.find_and_return_element(StellarBurgersLocators.TEXT_DONE)

    @allure.step('Если кликнуть на ингредиент, появится всплывающее окно с деталями')
    def click_ingridient(self):
        self.wheit_and_click(StellarBurgersLocators.BUTTON_IMG)
        self.wheit_element_text(StellarBurgersLocators.TEXT_DETALS, 'Детали ингредиента')
        return self.find_and_return_element(StellarBurgersLocators.TEXT_DETALS)

    @allure.step('Всплывающее окно закрывается кликом по крестику')
    def click_exit_ingridient(self):
        self.wheit_and_click(StellarBurgersLocators.BUTTON_IMG)
        self.click_element(StellarBurgersLocators.BUTTON_KRESTIC)
        self.wheit_element_click(StellarBurgersLocators.BUTTON_PERSSONAL_ACCOUNT)
        return self.find_and_return_element(StellarBurgersLocators.BUTTON_PERSSONAL_ACCOUNT)

    @allure.step('При добавлении ингредиента в заказ счётчик этого ингридиента увеличивается')
    def plus_counter(self):
        ingridient = self.find_and_return_element(StellarBurgersLocators.BUTTON_IMG)
        drag = self.find_and_return_element(StellarBurgersLocators.DRAG)
        drag_and_drop(self.driver, ingridient, drag)
        self.wheit_element_text(StellarBurgersLocators.COUNT_INGRIDIENT, '2')
        return self.find_and_return_element(StellarBurgersLocators.COUNT_INGRIDIENT)

    @allure.step('Залогиненный пользователь может оформить заказ')
    def count_login_user(self):
        self.wheit_and_click(StellarBurgersLocators.BUTTON_PERSSONAL_ACCOUNT)
        create_user = User()
        user = create_user.create_user()
        self.send_key_element(StellarBurgersLocators.EMAIL_ACCOUNT, user.json()['user']['email'])
        self.send_key_element(StellarBurgersLocators.PASSWORD_ACCOUNT, 'password')
        self.click_element(StellarBurgersLocators.BUTTON_LOGIN_IN_ACCOUNT)
        self.wheit_element_text(StellarBurgersLocators.TEXT_COUNT, 'Оформить заказ')
        ingridient = self.find_and_return_element(StellarBurgersLocators.BUTTON_IMG)
        drag = self.find_and_return_element(StellarBurgersLocators.DRAG)
        drag_and_drop(self.driver, ingridient, drag)
        self.wheit_and_click(StellarBurgersLocators.TEXT_COUNT)
        self.wheit_element_text(StellarBurgersLocators.TEXT_ORDER, 'Ваш заказ начали готовить')
        return self.find_and_return_element(StellarBurgersLocators.TEXT_ORDER)



