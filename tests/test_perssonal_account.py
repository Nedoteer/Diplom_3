import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.recover_password import StellarBurgersLocators
from pages.User import User
from urls import Urls


class TestPerssonalAccount:

    @allure.title('Личный кабинет')
    @allure.description('Переход по клику на «Личный кабинет»')
    def test_click_perssonal_account(self, driver):
        filter_field = WebDriverWait(driver, 20).until(expected_conditions.element_to_be_clickable(StellarBurgersLocators.BUTTON_PERSSONAL_ACCOUNT))
        ActionChains(driver).move_to_element(filter_field).click().perform()

        WebDriverWait(driver, Urls.MAX_WAIT_TIME).until(expected_conditions.text_to_be_present_in_element(StellarBurgersLocators.TEXT_ENTER, 'Вход'))

        text_enter = driver.find_element(*StellarBurgersLocators.TEXT_ENTER)

        assert text_enter.is_displayed() and text_enter.text == 'Вход'

    @allure.title('Личный кабинет')
    @allure.description('Переход в раздел «История заказов»')
    def test_click_history_count(self, driver):
        filter_field = WebDriverWait(driver, 20).until(expected_conditions.element_to_be_clickable(StellarBurgersLocators.BUTTON_PERSSONAL_ACCOUNT))
        ActionChains(driver).move_to_element(filter_field).click().perform()

        create_user = User()
        user = create_user.create_user()

        driver.find_element(*StellarBurgersLocators.EMAIL_ACCOUNT).send_keys(user.json()['user']['email'])
        driver.find_element(*StellarBurgersLocators.PASSWORD_ACCOUNT).send_keys('password')
        driver.find_element(*StellarBurgersLocators.BUTTON_LOGIN_IN_ACCOUNT).click()

        WebDriverWait(driver, Urls.MAX_WAIT_TIME).until(expected_conditions.text_to_be_present_in_element(StellarBurgersLocators.TEXT_COUNT, 'Оформить заказ'))

        filter_field = WebDriverWait(driver, 20).until(
            expected_conditions.element_to_be_clickable(StellarBurgersLocators.BUTTON_PERSSONAL_ACCOUNT))
        ActionChains(driver).move_to_element(filter_field).click().perform()

        WebDriverWait(driver, Urls.MAX_WAIT_TIME).until(expected_conditions.element_to_be_clickable(StellarBurgersLocators.TEXT_HISTORY))
        driver.find_element(*StellarBurgersLocators.TEXT_HISTORY).click()
        assert driver.current_url == Urls.HISTORY

    @allure.title('Личный кабинет')
    @allure.description('Выход из аккаунта')
    def test_exit(self, driver):
        filter_field = WebDriverWait(driver, 20).until(expected_conditions.element_to_be_clickable(StellarBurgersLocators.BUTTON_PERSSONAL_ACCOUNT))
        ActionChains(driver).move_to_element(filter_field).click().perform()

        create_user = User()
        user = create_user.create_user()

        driver.find_element(*StellarBurgersLocators.EMAIL_ACCOUNT).send_keys(user.json()['user']['email'])
        driver.find_element(*StellarBurgersLocators.PASSWORD_ACCOUNT).send_keys('password')
        driver.find_element(*StellarBurgersLocators.BUTTON_LOGIN_IN_ACCOUNT).click()

        WebDriverWait(driver, Urls.MAX_WAIT_TIME).until(
            expected_conditions.text_to_be_present_in_element(StellarBurgersLocators.TEXT_COUNT, 'Оформить заказ'))

        filter_field = WebDriverWait(driver, 20).until(expected_conditions.element_to_be_clickable(StellarBurgersLocators.BUTTON_PERSSONAL_ACCOUNT))
        ActionChains(driver).move_to_element(filter_field).click().perform()

        WebDriverWait(driver, Urls.MAX_WAIT_TIME).until(
            expected_conditions.element_to_be_clickable(StellarBurgersLocators.TEXT_HISTORY))

        driver.find_element(*StellarBurgersLocators.BUTTON_EXIT).click()
        WebDriverWait(driver, Urls.MAX_WAIT_TIME).until(expected_conditions.text_to_be_present_in_element(StellarBurgersLocators.TEXT_ENTER, 'Вход'))

        assert driver.current_url == Urls.LOGIN

