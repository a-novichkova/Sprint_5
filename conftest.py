import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import MainPageLocators, LoginPageLocators, RegistrationPageLocators


BASE_URL = "https://qa-desk.education-services.ru"

EXISTING_USER_EMAIL = "test123@mailinator.com"
EXISTING_USER_PASSWORD = "qwerty1234"


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
def authorized_user(driver):
#   логинит заранее созданного пользователя 
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(MainPageLocators.LOGIN_BUTTON)
    ).click()

    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(LoginPageLocators.LOGIN_EMAIL_INPUT)
    ).send_keys(EXISTING_USER_EMAIL)

    driver.find_element(*LoginPageLocators.LOGIN_PASSWORD_INPUT).send_keys(EXISTING_USER_PASSWORD)
    driver.find_element(*LoginPageLocators.LOGIN_SUBMIT_BUTTON).click()

    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(MainPageLocators.USER_AVATAR)
    )
    return driver
