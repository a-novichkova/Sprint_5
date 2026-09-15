from selenium.webdriver.common.by import By


class MainPageLocators:
#   локаторы главной страницы
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Вход и регистрация']")
    POST_AD_BUTTON = (By.XPATH, "//button[text()='Разместить объявление']")
    USER_AVATAR = (By.CLASS_NAME, "svgSmall")
    USER_NAME = (By.CSS_SELECTOR, "h3.profileText.name")
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выйти']")
    MODAL_WINDOW = (By.XPATH, "//div[contains(@class, 'modal')]")


class RegistrationPageLocators:
#   локаторы страницы регистрации
    REGISTER_LINK = (By.XPATH, "//button[text()='Нет аккаунта']")
    EMAIL_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.NAME, "password")
    CONFIRM_PASSWORD_INPUT = (By.NAME, "submitPassword")
    CREATE_BUTTON = (By.XPATH, "//button[text()='Создать аккаунт']")
    EMAIL_ERROR = (By.XPATH, "//span[contains(@class, 'input_span') and text()='Ошибка']")
    EMAIL_FIELD_ERROR = (By.XPATH, "//div[contains(@class, 'input_inputError__fLUP9') and .//input[@name='email']]")
    PASSWORD_FIELD_ERROR = (By.XPATH, "//div[contains(@class, 'input_inputError__fLUP9') and .//input[@name='password']]")
    CONFIRM_FIELD_ERROR = (By.XPATH, "//div[contains(@class, 'input_inputError__fLUP9') and .//input[@name='submitPassword']]")


class LoginPageLocators:
#   локаторы страницы входа
    LOGIN_EMAIL_INPUT = (By.NAME, "email")
    LOGIN_PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_SUBMIT_BUTTON = (By.XPATH, "//button[text()='Войти']")


class AdFormLocators:
#   локаторы страницы для размещения объявлений
    TITLE_INPUT = (By.NAME, "name")
    DESCRIPTION_INPUT = (By.XPATH, "//textarea[@placeholder='Описание товара']")
    PRICE_INPUT = (By.NAME, "price")
    CATEGORY_DROPDOWN = (By.XPATH, ".//div/div[2]/div/form/div[2]/div[2]/div[1]/button")
    CATEGORY_AUTO = (By.XPATH, "//button[.//span[text()='Авто']]")
    CITY_DROPDOWN = (By.XPATH, ".//div/div[2]/div/form/div[3]/div[1]/button")
    CITY_MOSCOW = (By.XPATH, "//button[.//span[text()='Москва']]")
    CONDITION_RADIO = (By.CLASS_NAME, "radioUnput_inputRegular__FbVbr")
    PUBLISH_BUTTON = (By.XPATH, "//button[text()='Опубликовать']")


class ProfilePageLocators:

    @staticmethod
    def ad_title_by_text(title):
    #   локатор заголовка объявления по его тексту
        return (By.XPATH, f"//h2[text()='{title}']")
