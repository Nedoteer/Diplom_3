import time

import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from seletools.actions import drag_and_drop

from locators.recover_password import StellarBurgersLocators
from pages.User import User
from pages.base_page import BasePage
from pages.string_count_page import StringCount
from urls import Urls


class TestStringCount:

    @allure.title('Раздел лента заказов')
    @allure.description('Если кликнуть на заказ, откроется всплывающее окно с деталями')
    def test_click_count(self, driver):
        filter_field = WebDriverWait(driver, 20).until(
            expected_conditions.element_to_be_clickable(StellarBurgersLocators.BUTTON_COUNT))
        ActionChains(driver).move_to_element(filter_field).click().perform()

        WebDriverWait(driver, Urls.MAX_WAIT_TIME).until(expected_conditions.invisibility_of_element(StellarBurgersLocators.ORDER_READY))

        filter_field = WebDriverWait(driver, 20).until(
            expected_conditions.element_to_be_clickable(StellarBurgersLocators.FIRST_STRING))
        ActionChains(driver).move_to_element(filter_field).click().perform()


        WebDriverWait(driver, Urls.MAX_WAIT_TIME).until(
            expected_conditions.text_to_be_present_in_element(StellarBurgersLocators.WINDOW_COUNT, 'Выполнен'))

        window_count = driver.find_element(*StellarBurgersLocators.WINDOW_COUNT)

        assert window_count.is_displayed()

    @allure.title('Раздел лента заказов')
    @allure.description('Заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    def test_count_user_string(self, driver):
        filter_field = WebDriverWait(driver, 20).until(
            expected_conditions.element_to_be_clickable(StellarBurgersLocators.BUTTON_PERSSONAL_ACCOUNT))
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

        string_count = StringCount(driver)
        string_count.test(StellarBurgersLocators.BUTTON_KRESTIC)

        img_status = driver.find_element(*StellarBurgersLocators.BUTTON_KRESTIC)
        img_status.is_displayed()
        WebDriverWait(driver, timeout=10).until(
            expected_conditions.invisibility_of_element(StellarBurgersLocators.IMG_STATUS))
        time.sleep(2)
        number_order = driver.find_element(*StellarBurgersLocators.INT_COUNT).text

        filter_field = WebDriverWait(driver, 20).until(
            expected_conditions.element_to_be_clickable(StellarBurgersLocators.BUTTON_KRESTIC))
        ActionChains(driver).move_to_element(filter_field).click().perform()

        filter_field = WebDriverWait(driver, 20).until(
            expected_conditions.element_to_be_clickable(StellarBurgersLocators.BUTTON_PERSSONAL_ACCOUNT))
        ActionChains(driver).move_to_element(filter_field).click().perform()

        WebDriverWait(driver, Urls.MAX_WAIT_TIME).until(expected_conditions.text_to_be_present_in_element(StellarBurgersLocators.BUTTON_SAVE, 'Сохранить'))

        filter_field = WebDriverWait(driver, 20).until(
            expected_conditions.element_to_be_clickable(StellarBurgersLocators.TEXT_HISTORY))
        ActionChains(driver).move_to_element(filter_field).click().perform()

        order = BasePage(driver)
        result = order.order_displayed(number_order)

        filter_field = WebDriverWait(driver, 20).until(
            expected_conditions.element_to_be_clickable(StellarBurgersLocators.BUTTON_COUNT))
        ActionChains(driver).move_to_element(filter_field).click().perform()

        result_2 = order.order_displayed(number_order)
        assert result == result_2

    @allure.title('Раздел лента заказов')
    @allure.description('При создании нового заказа счётчик Выполнено за всё время увеличивается')
    def test_count_completed_increases(self, driver):
        filter_field = WebDriverWait(driver, 20).until(
            expected_conditions.element_to_be_clickable(StellarBurgersLocators.BUTTON_COUNT))
        ActionChains(driver).move_to_element(filter_field).click().perform()

        WebDriverWait(driver, Urls.MAX_WAIT_TIME).until(expected_conditions.element_to_be_clickable(StellarBurgersLocators.FIRST_STRING))
        done = driver.find_element(*StellarBurgersLocators.DONE_ALL_TIME).text

        filter_field = WebDriverWait(driver, 20).until(
            expected_conditions.element_to_be_clickable(StellarBurgersLocators.BUTTON_PERSSONAL_ACCOUNT))
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

        time.sleep(2)
        filter_field = WebDriverWait(driver, 20).until(
            expected_conditions.element_to_be_clickable(StellarBurgersLocators.BUTTON_KRESTIC))
        ActionChains(driver).move_to_element(filter_field).click().perform()

        WebDriverWait(driver, Urls.MAX_WAIT_TIME).until(expected_conditions.element_to_be_clickable(StellarBurgersLocators.TEXT_COUNT))

        filter_field = WebDriverWait(driver, 20).until(
            expected_conditions.element_to_be_clickable(StellarBurgersLocators.BUTTON_COUNT))
        ActionChains(driver).move_to_element(filter_field).click().perform()

        WebDriverWait(driver, Urls.MAX_WAIT_TIME).until(
            expected_conditions.element_to_be_clickable(StellarBurgersLocators.FIRST_STRING))

        result = driver.find_element(*StellarBurgersLocators.DONE_ALL_TIME).text

        assert done != result

    @allure.title('Раздел лента заказов')
    @allure.description('При создании нового заказа счётчик Выполнено за сегодня увеличивается')
    def test_count_complited_today(self, driver):
        filter_field = WebDriverWait(driver, 20).until(
            expected_conditions.element_to_be_clickable(StellarBurgersLocators.BUTTON_COUNT))
        ActionChains(driver).move_to_element(filter_field).click().perform()

        WebDriverWait(driver, Urls.MAX_WAIT_TIME).until(
            expected_conditions.element_to_be_clickable(StellarBurgersLocators.FIRST_STRING))
        done_today = driver.find_element(*StellarBurgersLocators.DONE_TODAY).text

        filter_field = WebDriverWait(driver, 20).until(
            expected_conditions.element_to_be_clickable(StellarBurgersLocators.BUTTON_PERSSONAL_ACCOUNT))
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

        time.sleep(2)
        filter_field = WebDriverWait(driver, 20).until(
            expected_conditions.element_to_be_clickable(StellarBurgersLocators.BUTTON_KRESTIC))
        ActionChains(driver).move_to_element(filter_field).click().perform()

        WebDriverWait(driver, Urls.MAX_WAIT_TIME).until(
            expected_conditions.element_to_be_clickable(StellarBurgersLocators.TEXT_COUNT))

        filter_field = WebDriverWait(driver, 20).until(
            expected_conditions.element_to_be_clickable(StellarBurgersLocators.BUTTON_COUNT))
        ActionChains(driver).move_to_element(filter_field).click().perform()

        WebDriverWait(driver, Urls.MAX_WAIT_TIME).until(
            expected_conditions.element_to_be_clickable(StellarBurgersLocators.FIRST_STRING))
        time.sleep(2)
        day = driver.find_element(*StellarBurgersLocators.DONE_TODAY).text

        assert done_today != day

    @allure.title('Раздел лента заказов')
    @allure.description('После оформления заказа его номер появляется в разделе В работе')
    def test_order_in_work(self, driver):
        filter_field = WebDriverWait(driver, 20).until(
            expected_conditions.element_to_be_clickable(StellarBurgersLocators.BUTTON_PERSSONAL_ACCOUNT))
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

        string_count = StringCount(driver)
        string_count.test(StellarBurgersLocators.BUTTON_KRESTIC)

        img_status = driver.find_element(*StellarBurgersLocators.BUTTON_KRESTIC)
        img_status.is_displayed()
        WebDriverWait(driver, timeout=10).until(
            expected_conditions.invisibility_of_element(StellarBurgersLocators.IMG_STATUS))
        time.sleep(2)
        number_order = driver.find_element(*StellarBurgersLocators.INT_COUNT).text

        filter_field = WebDriverWait(driver, 20).until(
            expected_conditions.element_to_be_clickable(StellarBurgersLocators.BUTTON_KRESTIC))
        ActionChains(driver).move_to_element(filter_field).click().perform()

        filter_field = WebDriverWait(driver, 20).until(
            expected_conditions.element_to_be_clickable(StellarBurgersLocators.BUTTON_COUNT))
        ActionChains(driver).move_to_element(filter_field).click().perform()

        WebDriverWait(driver, Urls.MAX_WAIT_TIME).until(
            expected_conditions.element_to_be_clickable(StellarBurgersLocators.FIRST_STRING))

        WebDriverWait(driver, Urls.MAX_WAIT_TIME).until(expected_conditions.invisibility_of_element(StellarBurgersLocators.ORDER_READY))
        in_work = driver.find_element(*StellarBurgersLocators.IN_WORK).text


        assert f'0{number_order}' == in_work












