import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import StellarData
from urls import Urls
from locators.recover_password import StellarBurgersLocators



class TestRecoverPassword:

    @allure.title('Восстановление пароля')
    @allure.description('Переход на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_click_button_recover_password(self, driver):

        filter_field = WebDriverWait(driver, 20).until(expected_conditions.element_to_be_clickable(StellarBurgersLocators.BUTTON_PERSSONAL_ACCOUNT))
        ActionChains(driver).move_to_element(filter_field).click().perform()


        driver.find_element(*StellarBurgersLocators.LINK_FORGOT_PASSWORD).click()

        WebDriverWait(driver, Urls.MAX_WAIT_TIME).until(expected_conditions.text_to_be_present_in_element(StellarBurgersLocators.TEXT_RECOVER, 'Восстановление пароля'))

        text_recover = driver.find_element(*StellarBurgersLocators.TEXT_RECOVER)

        assert text_recover.is_displayed() and text_recover.text == 'Восстановление пароля'

    @allure.title('Восстановление пароля')
    @allure.description('Ввод почты и клик по кнопке «Восстановить»')
    def test_put_email_click_buton_recover(self, driver):


        filter_field = WebDriverWait(driver, 20).until(expected_conditions.element_to_be_clickable(StellarBurgersLocators.BUTTON_PERSSONAL_ACCOUNT))
        ActionChains(driver).move_to_element(filter_field).click().perform()

        driver.find_element(*StellarBurgersLocators.LINK_FORGOT_PASSWORD).click()

        driver.find_element(*StellarBurgersLocators.EMAIL_ACCOUNT).send_keys(StellarData.EMAIL)

        driver.find_element(*StellarBurgersLocators.BUTTON_RECOVER).click()

        WebDriverWait(driver, Urls.MAX_WAIT_TIME).until(
            expected_conditions.text_to_be_present_in_element(StellarBurgersLocators.LABEL_EMAIL,
                                                              'Введите код из письма'))

        label_email = driver.find_element(*StellarBurgersLocators.LABEL_EMAIL)

        assert label_email.is_displayed() and label_email.text == 'Введите код из письма'

    @allure.title('Восстановление пароля')
    @allure.description('Клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    def test_click_button_show(self, driver):

        filter_field = WebDriverWait(driver, 20).until(expected_conditions.element_to_be_clickable(StellarBurgersLocators.BUTTON_PERSSONAL_ACCOUNT))
        ActionChains(driver).move_to_element(filter_field).click().perform()

        driver.find_element(*StellarBurgersLocators.LINK_FORGOT_PASSWORD).click()

        driver.find_element(*StellarBurgersLocators.EMAIL_ACCOUNT).send_keys(StellarData.EMAIL)
        driver.find_element(*StellarBurgersLocators.BUTTON_RECOVER).click()

        WebDriverWait(driver, Urls.MAX_WAIT_TIME).until(expected_conditions.element_to_be_clickable(StellarBurgersLocators.PASSWORD_ACCOUNT))

        driver.find_element(*StellarBurgersLocators.PASSWORD_ACCOUNT).send_keys(StellarData.PASSWORD)
        filter_field = WebDriverWait(driver, 20).until(
            expected_conditions.element_to_be_clickable(StellarBurgersLocators.BUTTON_ICON))
        ActionChains(driver).move_to_element(filter_field).click().perform()

        status_change = driver.find_element(*StellarBurgersLocators.STATUS_CHANGE)

        assert status_change.is_displayed() == True






