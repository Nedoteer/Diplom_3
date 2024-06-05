import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.recover_password import StellarBurgersLocators
from pages.User import User
from urls import Urls
from seletools.actions import drag_and_drop


class TestFunctional:

    @allure.title('Проверка основного функционала')
    @allure.description('Переход по клику на «Конструктор»')
    def test_click_constructor(self, driver):
        filter_field = WebDriverWait(driver, 20).until(expected_conditions.element_to_be_clickable(StellarBurgersLocators.BUTTON_PERSSONAL_ACCOUNT))
        ActionChains(driver).move_to_element(filter_field).click().perform()

        driver.find_element(*StellarBurgersLocators.BUTTON_CONSTRUCTOR).click()

        WebDriverWait(driver, Urls.MAX_WAIT_TIME).until(expected_conditions.text_to_be_present_in_element(StellarBurgersLocators.TEXT_BURGER, 'Соберите бургер'))

        text_burger = driver.find_element(*StellarBurgersLocators.TEXT_BURGER)

        assert text_burger.is_displayed() and text_burger.text == 'Соберите бургер'

    @allure.title('Проверка основного функционала')
    @allure.description('Переход по клику на «Лента заказов»')
    def test_click_count(self, driver):
        filter_field = WebDriverWait(driver, 20).until(expected_conditions.element_to_be_clickable(StellarBurgersLocators.BUTTON_PERSSONAL_ACCOUNT))
        ActionChains(driver).move_to_element(filter_field).click().perform()

        driver.find_element(*StellarBurgersLocators.BUTTON_COUNT).click()

        WebDriverWait(driver, Urls.MAX_WAIT_TIME).until(expected_conditions.text_to_be_present_in_element(StellarBurgersLocators.TEXT_DONE, 'Выполнено за сегодня:'))

        text_done = driver.find_element(*StellarBurgersLocators.TEXT_DONE)

        assert text_done.is_displayed() and text_done.text == 'Выполнено за сегодня:'

    @allure.title('Проверка основного функционала')
    @allure.description('Если кликнуть на ингредиент, появится всплывающее окно с деталями')
    def test_igridient(self, driver):
        filter_field = WebDriverWait(driver, 20).until(expected_conditions.element_to_be_clickable(StellarBurgersLocators.BUTTON_IMG))
        ActionChains(driver).move_to_element(filter_field).click().perform()

        WebDriverWait(driver, Urls.MAX_WAIT_TIME).until(expected_conditions.text_to_be_present_in_element(StellarBurgersLocators.TEXT_DETALS, 'Детали ингредиента'))

        text_detals = driver.find_element(*StellarBurgersLocators.TEXT_DETALS)
        assert text_detals.is_displayed() and text_detals.text == 'Детали ингредиента'

    @allure.title('Проверка основного функционала')
    @allure.description('Всплывающее окно закрывается кликом по крестику')
    def test_exit_ingridient(self, driver):
        filter_field = WebDriverWait(driver, 20).until(expected_conditions.element_to_be_clickable(StellarBurgersLocators.BUTTON_IMG))
        ActionChains(driver).move_to_element(filter_field).click().perform()

        driver.find_element(*StellarBurgersLocators.BUTTON_KRESTIC).click()

        WebDriverWait(driver, Urls.MAX_WAIT_TIME).until(expected_conditions.element_to_be_clickable(StellarBurgersLocators.BUTTON_PERSSONAL_ACCOUNT))

        button_perssonal_account = driver.find_element(*StellarBurgersLocators.BUTTON_PERSSONAL_ACCOUNT)
        assert button_perssonal_account.is_displayed() == True

    @allure.title('Проверка основного функционала')
    @allure.description('При добавлении ингредиента в заказ счётчик этого ингридиента увеличивается')
    def test_plus_counter(self, driver):

        ingridient =  driver.find_element(*StellarBurgersLocators.BUTTON_IMG)
        drag = driver.find_element(*StellarBurgersLocators.DRAG)
        drag_and_drop(driver, ingridient, drag)

        WebDriverWait(driver, Urls.MAX_WAIT_TIME).until(expected_conditions.text_to_be_present_in_element(StellarBurgersLocators.COUNT_INGRIDIENT, '2'))

        count_ingridient = driver.find_element(*StellarBurgersLocators.COUNT_INGRIDIENT).text

        assert count_ingridient == '2'

    @allure.title('Проверка основного функционала')
    @allure.description('Залогиненный пользователь может оформить заказ')
    def test_count_login_user(self, driver):
        filter_field = WebDriverWait(driver, 20).until(expected_conditions.element_to_be_clickable(StellarBurgersLocators.BUTTON_PERSSONAL_ACCOUNT))
        ActionChains(driver).move_to_element(filter_field).click().perform()

        create_user = User()
        user = create_user.create_user()

        driver.find_element(*StellarBurgersLocators.EMAIL_ACCOUNT).send_keys(user.json()['user']['email'])
        driver.find_element(*StellarBurgersLocators.PASSWORD_ACCOUNT).send_keys('password')
        driver.find_element(*StellarBurgersLocators.BUTTON_LOGIN_IN_ACCOUNT).click()

        WebDriverWait(driver, Urls.MAX_WAIT_TIME).until(
            expected_conditions.text_to_be_present_in_element(StellarBurgersLocators.TEXT_COUNT, 'Оформить заказ'))

        ingridient = driver.find_element(*StellarBurgersLocators.BUTTON_IMG)
        drag = driver.find_element(*StellarBurgersLocators.DRAG)
        drag_and_drop(driver, ingridient, drag)

        filter_field = WebDriverWait(driver, 20).until(
            expected_conditions.element_to_be_clickable(StellarBurgersLocators.TEXT_COUNT))
        ActionChains(driver).move_to_element(filter_field).click().perform()

        WebDriverWait(driver, Urls.MAX_WAIT_TIME).until(expected_conditions.text_to_be_present_in_element(StellarBurgersLocators.TEXT_ORDER, 'Ваш заказ начали готовить'))

        text_order = driver.find_element(*StellarBurgersLocators.TEXT_ORDER)

        assert text_order.is_displayed() and text_order.text == 'Ваш заказ начали готовить'







