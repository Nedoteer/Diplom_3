

import allure

from pages.string_count_page import StringCount



class TestStringCount:

    @allure.title('Раздел лента заказов')
    @allure.description('Если кликнуть на заказ, откроется всплывающее окно с деталями')
    def test_click_count(self, driver):
        click_count = StringCount(driver)
        window_count = click_count.click_count()
        assert window_count.is_displayed() == True

    @allure.title('Раздел лента заказов')
    @allure.description('Заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    def test_count_user_string(self, driver):
        count_user_string = StringCount(driver)
        count_user_string.number_new_order()
        history_order = count_user_string.get_order()
        string_order = count_user_string.get_nubmer_order_from_string_order()
        assert history_order == string_order

    @allure.title('Раздел лента заказов')
    @allure.description('При создании нового заказа счётчик Выполнено за всё время увеличивается')
    def test_count_completed_increases(self, driver):
        count_complited = StringCount(driver)
        done = count_complited.count_complited_inc()
        result = count_complited.new_user_and_create_order()
        assert done != result

    @allure.title('Раздел лента заказов')
    @allure.description('При создании нового заказа счётчик Выполнено за сегодня увеличивается')
    def test_count_complited_today(self, driver):
        count_day = StringCount(driver)
        done_today = count_day.count_complited_to_day()
        day = count_day.new_user_and_create_order_day()
        assert done_today != day

    @allure.title('Раздел лента заказов')
    @allure.description('После оформления заказа его номер появляется в разделе В работе')
    def test_order_in_work(self, driver):
        order = StringCount(driver)
        number_order = order.create_user_and_treck_number_order()
        in_work = order.count_in_work()
        assert f'0{number_order}' == in_work










