import allure

from pages.recover_password_page import RecoverPassword




class TestRecoverPassword:

    @allure.title('Восстановление пароля')
    @allure.description('Переход на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_click_button_recover_password(self, driver):
        wheit_and_click = RecoverPassword(driver)
        result = wheit_and_click.click_button_recover_password()
        assert result.is_displayed() and result.text == 'Восстановление пароля'


    @allure.title('Восстановление пароля')
    @allure.description('Ввод почты и клик по кнопке «Восстановить»')
    def test_put_email_click_buton_recover(self, driver):
        wheit_and_click = RecoverPassword(driver)
        result = wheit_and_click.put_email_click_buton_recover()
        assert result.is_displayed() and result.text == 'Введите код из письма'


    @allure.title('Восстановление пароля')
    @allure.description('Клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    def test_click_button_show(self, driver):
        wheit_and_click = RecoverPassword(driver)
        result = wheit_and_click.click_button_show()
        assert result.is_displayed() == True







