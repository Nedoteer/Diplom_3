from selenium.webdriver.common.by import By


class StellarBurgersLocators:

    BUTTON_PERSSONAL_ACCOUNT = (By.XPATH, "//p[contains(text(), 'Личный Кабинет')]")
    BUTTON_RECOVER = (By.XPATH, "//button[contains(text(), 'Восстановить')]")
    BUTTON_ICON = (By.XPATH, "//div[@class = 'input__icon input__icon-action']")
    BUTTON_LOGIN_IN_ACCOUNT = (By.XPATH, ".//button[contains(text(), 'Войти')]")
    BUTTON_EXIT = (By.XPATH, "//button[contains(text(), 'Выход')]")
    BUTTON_CONSTRUCTOR = (By.XPATH, "//p[contains(text(), 'Конструктор')]")
    BUTTON_COUNT = (By.XPATH, "//p[contains(text(), 'Лента Заказов')]")
    BUTTON_IMG = (By.XPATH, "//img[@src = 'https://code.s3.yandex.net/react/code/bun-02.png']")
    BUTTON_KRESTIC = (By.XPATH, "//button[contains(@class, 'close')]")
    BUTTON_SAVE = (By.XPATH, "//button[contains(text(), 'Сохранить')]")
    MODAL_OVERLAY = (By.XPATH, './/div[@class = "Modal_modal_opened__3ISw4 Modal_modal__P3_V5"]'
                               '/div[@class = "Modal_modal_overlay__x2ZCr"]')

    ORDER_READY = (By.XPATH, "//li[contains(text(), 'Все текущие заказы готовы!')]")
    IN_WORK = (By.XPATH, "//p[@class = 'text text_type_main-medium']/following-sibling::ul[@class = 'OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi']")
    DONE_TODAY = (By.XPATH, "//div[@class = 'undefined mb-15']/following::p[@class = 'OrderFeed_number__2MbrQ text text_type_digits-large']")
    DONE_ALL_TIME = (By.XPATH,  "//div[@class = 'undefined mb-15']/child::p[@class = 'OrderFeed_number__2MbrQ text text_type_digits-large']")
    IMG_STATUS = (By.CSS_SELECTOR,  "Modal_modal__loading__3534A")
    FIRST_STRING = (By.XPATH, "(//ul[@class = 'OrderFeed_list__OLh59']/child::*)[1]")
    COUNT_INGRIDIENT = (By.XPATH, "//div[@class = 'counter_counter__ZNLkj counter_default__28sqi']/descendant::p[contains(text(), '2')]")
    DRAG = (By.XPATH, "//span[contains(text(), 'Перетяните булочку сюда (верх)')]")
    STATUS_CHANGE = (By.XPATH, "//div[@class='input pr-6 pl-6 input_type_text input_size_default input_status_active']")

    PASSWORD_ACCOUNT = (By.XPATH, "//input[@type = 'password']")
    LINK_FORGOT_PASSWORD = (By.XPATH, "//a[contains(@href, '/forgot-password')]")

    EMAIL_ACCOUNT = (By.XPATH, "//div[@class = 'input__container']/descendant::label[text() = 'Email']/following-sibling::input")

    TEXT_RECOVER = (By.XPATH, "//h2[contains(text(), 'Восстановление пароля')]")
    LABEL_EMAIL = (By.XPATH, "//label[contains(text(), 'Введите код из письма')]")
    TEXT_ENTER = (By.XPATH, "//h2[text() = 'Вход']")
    TEXT_HISTORY = (By.XPATH, "//a[contains(text(), 'История заказов')]")
    TEXT_COUNT = (By.XPATH, "//button[contains(text(), 'Оформить заказ')]")
    TEXT_BURGER = (By.XPATH, "//h1[contains(text(), 'Соберите бургер')]")
    TEXT_DONE = (By.XPATH, "//p[contains(text(), 'Выполнено за сегодня:')]")
    TEXT_DETALS = (By.XPATH, "//h2[contains(text(), 'Детали ингредиента')]")
    TEXT_ORDER = (By.XPATH,  "//p[contains(text(), 'Ваш заказ начали готовить')]")
    WINDOW_COUNT =(By.XPATH, "//div[@class = 'Modal_orderBox__1xWdi Modal_modal__contentBox__sCy8X p-10']")
    TEXT_STRING = (By.XPATH,  "//p[contains(text(), 'Лента заказов')]")
    INT_COUNT = (By.XPATH, "//h2[@class = 'Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8']")
    TEXT_WHEIT = (By.XPATH, "//p[contains(text(), 'Дождитесь готовности на орбитальной станции')]")
    FULL_WINDOW = (By.XPATH,  "//div[@class = 'Modal_modal__container__Wo2l_']")
    EMPTY_WINDOW = (By.XPATH, "//section[@class = 'Modal_modal_opened__3ISw4 Modal_modal__P3_V5']")
    INVISIBL = (By.XPATH, "//div[@class = 'Modal_modal__P3_V5']")
    IMG_LOAD = (By.XPATH, "//img[@scr = './static/media/loading.89540200.svg']")