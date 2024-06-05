import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage


class StringCount(BasePage):

    @allure.step('Отображение елемента на странице')
    def test(self, locator):

        WebDriverWait(self.driver, timeout=5).until(expected_conditions.element_to_be_clickable(locator))
        test = self.driver.find_element(*locator)
        test.is_displayed()



