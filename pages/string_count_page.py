import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from seletools.actions import drag_and_drop

from locators.recover_password import StellarBurgersLocators
from pages.User import User
from pages.base_page import BasePage


class StringCount(BasePage):

    @allure.step('Отображение елемента на странице')
    def displayed_element(self, locator):

        WebDriverWait(self.driver, timeout=5).until(expected_conditions.element_to_be_clickable(locator))
        test = self.driver.find_element(*locator)
        test.is_displayed()

    @allure.step('Клик по заказу, откроется всплывающее окно с деталями')
    def click_count(self):
        self.wheit_and_click(StellarBurgersLocators.BUTTON_COUNT)
        self.wheit_element_off(StellarBurgersLocators.ORDER_READY)
        self.wheit_and_click(StellarBurgersLocators.FIRST_STRING)
        self.wheit_element_text(StellarBurgersLocators.WINDOW_COUNT, 'Выполнен')
        return self.find_and_return_element(StellarBurgersLocators.WINDOW_COUNT)

    @allure.step('Создание заказа и получение его номера')
    def number_new_order(self):
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
        self.displayed_element(StellarBurgersLocators.BUTTON_KRESTIC)
        self.find_and_return_element(StellarBurgersLocators.BUTTON_KRESTIC)
        self.wheit_element_off(StellarBurgersLocators.MODAL_OVERLAY)
        self.wheit_element_click(StellarBurgersLocators.BUTTON_KRESTIC)
        self.wheit_all_element(StellarBurgersLocators.EMPTY_WINDOW)
        order = self.find_and_return_element(StellarBurgersLocators.INT_COUNT)
        self.wheit_and_click(StellarBurgersLocators.BUTTON_KRESTIC)
        self.wheit_and_click(StellarBurgersLocators.BUTTON_PERSSONAL_ACCOUNT)
        self.wheit_element_text(StellarBurgersLocators.BUTTON_SAVE, 'Сохранить')
        self.wheit_and_click(StellarBurgersLocators.TEXT_HISTORY)
        return order.text

    @allure.step('Получение заказа из истории заказа')
    def get_order(self, number_order):
        history_order = self.order_displayed(number_order)
        self.wheit_and_click(StellarBurgersLocators.BUTTON_COUNT)
        return history_order

    @allure.step('Получение номера заказа из ленты заказов')
    def get_nubmer_order_from_string_order(self, number_order):
        string_order = self.order_displayed(number_order)
        return string_order

    @allure.step('Количество сделаных заказов')
    def count_complited_inc(self):
        self.wheit_and_click(StellarBurgersLocators.BUTTON_COUNT)
        self.wheit_element_click(StellarBurgersLocators.FIRST_STRING)
        done = self.find_and_return_element(StellarBurgersLocators.DONE_ALL_TIME)
        return done.text

    @allure.step('Регистрация нового пользователя и создание заказа')
    def new_user_and_create_order(self):
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
        self.wheit_element_off(StellarBurgersLocators.MODAL_OVERLAY)
        self.wheit_and_click(StellarBurgersLocators.BUTTON_KRESTIC)
        self.wheit_element_click(StellarBurgersLocators.TEXT_COUNT)
        self.wheit_and_click(StellarBurgersLocators.BUTTON_COUNT)
        self.wheit_element_click(StellarBurgersLocators.FIRST_STRING)
        return self.find_and_return_element(StellarBurgersLocators.DONE_ALL_TIME).text


    @allure.step('Количество сделаных заказов за сегодня')
    def count_complited_to_day(self):
        self.wheit_and_click(StellarBurgersLocators.BUTTON_COUNT)
        self.wheit_element_click(StellarBurgersLocators.FIRST_STRING)
        done_today = self.find_and_return_element(StellarBurgersLocators.DONE_TODAY)
        return done_today.text

    @allure.step('Создание нового пользователя и заказа')
    def new_user_and_create_order_day(self):
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
        self.wheit_element_off(StellarBurgersLocators.MODAL_OVERLAY)
        self.wheit_and_click(StellarBurgersLocators.BUTTON_KRESTIC)
        self.wheit_element_click(StellarBurgersLocators.TEXT_COUNT)
        self.wheit_and_click(StellarBurgersLocators.BUTTON_COUNT)
        self.wheit_element_click(StellarBurgersLocators.FIRST_STRING)
        return self.find_and_return_element(StellarBurgersLocators.DONE_TODAY).text

    @allure.step('Создание пользователя и отслеживание номера заказа')
    def create_user_and_treck_number_order(self):
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
        self.wheit_element_off(StellarBurgersLocators.MODAL_OVERLAY)
        self.wheit_and_click(StellarBurgersLocators.BUTTON_KRESTIC)
        return self.find_and_return_element(StellarBurgersLocators.INT_COUNT).text

    @allure.step('Информация о заказе что он в работе')
    def count_in_work(self):
        self.wheit_and_click(StellarBurgersLocators.BUTTON_COUNT)
        self.wheit_and_click(StellarBurgersLocators.FIRST_STRING)
        self.wheit_element_off(StellarBurgersLocators.ORDER_READY)
        return self.find_and_return_element(StellarBurgersLocators.IN_WORK).text










