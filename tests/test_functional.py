import allure

from pages.functional_page import FunctionalPage



class TestFunctional:

    @allure.title('Проверка основного функционала')
    @allure.description('Переход по клику на «Конструктор»')
    def test_click_constructor(self, driver):
        click_constructor = FunctionalPage(driver)
        text_burger = click_constructor.click_constructor()
        assert text_burger.is_displayed() and text_burger.text == 'Соберите бургер'

    @allure.title('Проверка основного функционала')
    @allure.description('Переход по клику на «Лента заказов»')
    def test_click_count(self, driver):
        click_count = FunctionalPage(driver)
        text_done = click_count.click_count()
        assert text_done.is_displayed() and text_done.text == 'Выполнено за сегодня:'

    @allure.title('Проверка основного функционала')
    @allure.description('Если кликнуть на ингредиент, появится всплывающее окно с деталями')
    def test_igridient(self, driver):
        click_ingridient = FunctionalPage(driver)
        text_detals = click_ingridient.click_ingridient()
        assert text_detals.is_displayed() and text_detals.text == 'Детали ингредиента'

    @allure.title('Проверка основного функционала')
    @allure.description('Всплывающее окно закрывается кликом по крестику')
    def test_exit_ingridient(self, driver):
        click_exit_ingridient = FunctionalPage(driver)
        result = click_exit_ingridient.click_exit_ingridient()
        assert result.is_displayed() == True

    @allure.title('Проверка основного функционала')
    @allure.description('При добавлении ингредиента в заказ счётчик этого ингридиента увеличивается')
    def test_plus_counter(self, driver):
        counter = FunctionalPage(driver)
        count_ingridient = counter.plus_counter()
        assert count_ingridient.text == '2'

    @allure.title('Проверка основного функционала')
    @allure.description('Залогиненный пользователь может оформить заказ')
    def test_count_login_user(self, driver):
        count_user = FunctionalPage(driver)
        order = count_user.count_login_user()
        assert order.is_displayed() and order.text == 'Ваш заказ начали готовить'







