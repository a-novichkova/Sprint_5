import random
import string
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators, RegistrationPageLocators


class TestRegistration:

    def test_registration_success(self, driver):
    #   регистрация пользователя
        email = f"test_{''.join(random.choices(string.ascii_lowercase + string.digits, k=8))}@example.com"
        password = "ValidPass123"

        driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(RegistrationPageLocators.REGISTER_LINK)
        ).click()

        driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*RegistrationPageLocators.CONFIRM_PASSWORD_INPUT).send_keys(password)
        driver.find_element(*RegistrationPageLocators.CREATE_BUTTON).click()

        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(MainPageLocators.USER_AVATAR)
        )
        assert driver.find_element(*MainPageLocators.USER_NAME).text == 'User.'

    def test_registration_invalid_email(self, driver):
    #   регистрация пользователя c email не по маске
        invalid_email = "invalid_email"
        driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(RegistrationPageLocators.REGISTER_LINK)
        ).click()

        driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys(invalid_email)
        driver.find_element(*RegistrationPageLocators.CREATE_BUTTON).click()

        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(RegistrationPageLocators.EMAIL_ERROR)
        )
        assert driver.find_element(*RegistrationPageLocators.EMAIL_FIELD_ERROR).is_displayed()
        assert driver.find_element(*RegistrationPageLocators.PASSWORD_FIELD_ERROR).is_displayed()
        assert driver.find_element(*RegistrationPageLocators.CONFIRM_FIELD_ERROR).is_displayed()

    def test_registration_existing_user(self, driver):
    #   регистрация уже существующего пользователя
        email = f"test_{''.join(random.choices(string.ascii_lowercase + string.digits, k=8))}@example.com"
        password = "ValidPass123"

        # создание нового пользователя с уникальным email
        driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(RegistrationPageLocators.REGISTER_LINK)
        ).click()

        driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*RegistrationPageLocators.CONFIRM_PASSWORD_INPUT).send_keys(password)
        driver.find_element(*RegistrationPageLocators.CREATE_BUTTON).click()

        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(MainPageLocators.USER_AVATAR)
        )

        # выход из аккаунта, чтобы снова открыть форму регистрации
        driver.find_element(*MainPageLocators.LOGOUT_BUTTON).click()
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(MainPageLocators.LOGIN_BUTTON)
        )

        # попытка зарегистрироваться повторно с теми же данными
        driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(RegistrationPageLocators.REGISTER_LINK)
        ).click()

        driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*RegistrationPageLocators.CONFIRM_PASSWORD_INPUT).send_keys(password)
        driver.find_element(*RegistrationPageLocators.CREATE_BUTTON).click()

        # проверка, что поля выделены красным и есть сообщение об ошибке
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(RegistrationPageLocators.EMAIL_ERROR)
        )
        assert driver.find_element(*RegistrationPageLocators.EMAIL_FIELD_ERROR).is_displayed()
        assert driver.find_element(*RegistrationPageLocators.PASSWORD_FIELD_ERROR).is_displayed()
        assert driver.find_element(*RegistrationPageLocators.CONFIRM_FIELD_ERROR).is_displayed()
