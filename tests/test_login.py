from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators, LoginPageLocators


class TestLogin:

    def test_login_success(self, registered_user):
    #   login пользователя
        driver = registered_user["driver"]

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(MainPageLocators.LOGIN_BUTTON)
        ).click()

        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(LoginPageLocators.LOGIN_EMAIL_INPUT)
        ).send_keys(registered_user["email"])

        driver.find_element(*LoginPageLocators.LOGIN_PASSWORD_INPUT).send_keys(registered_user["password"])
        driver.find_element(*LoginPageLocators.LOGIN_SUBMIT_BUTTON).click()

        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(MainPageLocators.USER_AVATAR)
        )
        assert driver.find_element(*MainPageLocators.USER_NAME).text == "User."
