import allure
from selenium.webdriver import ActionChains

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.recover_password import StellarBurgersLocators
from urls import Urls


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Ожидание прогрузки елемента")
    def wait_and_find_element(self, locator):
        WebDriverWait(self.driver, Urls.MAX_WAIT_TIME).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step("Получение урл")
    def url_stellar(self):
        return self.driver.current_url

    @allure.step('Отображение заказа')
    def order_displayed(self, locator):
        WebDriverWait(self.driver, Urls.MAX_WAIT_TIME).until(expected_conditions.visibility_of_element_located(locator))
        displayed = self.driver.find_element(*locator)
        result = displayed.is_displayed()
        return result

    @allure.step('Ожидание и нажатие на элемент')
    def wheit_and_click(self, locator):
        filter_field = WebDriverWait(self.driver, Urls.MAX_WAIT_TIME).until(
            expected_conditions.element_to_be_clickable(locator))
        ActionChains(self.driver).move_to_element(filter_field).click().perform()

    @allure.step('Клик по элементу')
    def click_element(self, locator):
       self.driver.find_element(*locator).click()

    @allure.step('Ожидание текста')
    def wheit_element_text(self, locator, text):
        WebDriverWait(self.driver, Urls.MAX_WAIT_TIME).until(
            expected_conditions.text_to_be_present_in_element(locator,
                                                              text))

    @allure.step('Найти и вернуть элемент')
    def find_and_return_element(self, locator):
        return self.driver.find_element(*locator)

    @allure.step('Ввод данных')
    def send_key_element(self, locator, key):
        self.driver.find_element(*locator).send_keys(key)

    @allure.step('Одижание элемента пока он станет активным')
    def wheit_element_click(self, locator):
        WebDriverWait(self.driver, Urls.MAX_WAIT_TIME).until(
            expected_conditions.element_to_be_clickable(locator))

    @allure.step('Ожидание пока эелемент исчезнет')
    def wheit_element_off(self, locator):
        WebDriverWait(self.driver, Urls.MAX_WAIT_TIME).until(
            expected_conditions.invisibility_of_element(locator))

    @allure.step('Ожидает прогрузки всех елементов локатора')
    def wheit_all_element(self, locator):
        WebDriverWait(self.driver, Urls.MAX_WAIT_TIME).until(
            expected_conditions.visibility_of_all_elements_located(locator))

    @allure.step('Отображение елемента на странице')
    def displayed_element(self, locator):

        WebDriverWait(self.driver, timeout=5).until(expected_conditions.element_to_be_clickable(locator))
        test = self.driver.find_element(*locator)
        test.is_displayed()