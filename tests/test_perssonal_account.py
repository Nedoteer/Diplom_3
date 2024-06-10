import allure

from pages.perssonal_account_page import PerssonalAccount
from urls import Urls


class TestPerssonalAccount:

    @allure.title('Личный кабинет')
    @allure.description('Переход по клику на «Личный кабинет»')
    def test_click_perssonal_account(self, driver):
        pessonal_account = PerssonalAccount(driver)
        result = pessonal_account.click_perssonal_account()
        assert result.is_displayed() and result.text == 'Вход'


    @allure.title('Личный кабинет')
    @allure.description('Переход в раздел «История заказов»')
    def test_click_history_count(self, driver):
        history_count = PerssonalAccount(driver)
        history_count.click_history_count()
        assert driver.current_url == Urls.HISTORY

    @allure.title('Личный кабинет')
    @allure.description('Выход из аккаунта')
    def test_exit(self, driver):
        exit_account = PerssonalAccount(driver)
        exit_account.exit_account()
        assert driver.current_url == Urls.LOGIN

