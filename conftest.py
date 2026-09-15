import random
import string
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import MainPageLocators, LoginPageLocators, RegistrationPageLocators
from constants import BASE_URL


def generate_email():
#   генерирует уникальный email для нового пользователя
    return f"test_{''.join(random.choices(string.ascii_lowercase + string.digits, k=8))}@example.com"


def registers_new_user(driver, email, password):
#   регистрирует нового пользователя
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(MainPageLocators.LOGIN_BUTTON)
    ).click()

    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(RegistrationPageLocators.REGISTER_LINK)
    ).click()

    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(RegistrationPageLocators.EMAIL_INPUT)
    ).send_keys(email)

    driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*RegistrationPageLocators.CONFIRM_PASSWORD_INPUT).send_keys(password)
    driver.find_element(*RegistrationPageLocators.CREATE_BUTTON).click()

    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(MainPageLocators.USER_AVATAR)
    )


@pytest.fixture
def driver():
#   открывает браузер и закрывает его после теста
    options = Options()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    driver.get(BASE_URL)
    yield driver
    driver.quit()


@pytest.fixture
def registered_user(driver):
#   регистрирует нового пользователя и выходит из аккаунта
    email = generate_email()
    password = "ValidPass123"

    registers_new_user(driver, email, password)

    driver.find_element(*MainPageLocators.LOGOUT_BUTTON).click()
    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(MainPageLocators.LOGIN_BUTTON)
    )

    return {"email": email, "password": password, "driver": driver}


@pytest.fixture
def authorized_user(driver):
#   регистрирует нового пользователя и оставляет его авторизованным
    email = generate_email()
    password = "ValidPass123"

    registers_new_user(driver, email, password)
    return driver
