import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Ожидание прогрузки елемента")
    def wait_and_find_element(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step("Получение урл")
    def url_stellar(self):
        return self.driver.current_url

    @allure.step('Отображение заказа')
    def order_displayed(self, Num):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, f"//p[contains(text(), '{Num}')]")))
        displayed = self.driver.find_element(By.XPATH, f"//p[contains(text(), '{Num}')]")
        result = displayed.is_displayed()
        return result