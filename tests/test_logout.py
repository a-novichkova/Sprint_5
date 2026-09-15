from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators


class TestLogout:

    def test_logout(self, authorized_user):
    #   logout пользователя
        driver = authorized_user

        driver.find_element(*MainPageLocators.LOGOUT_BUTTON).click()

        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(MainPageLocators.LOGIN_BUTTON)
        )
        assert not driver.find_elements(*MainPageLocators.USER_AVATAR)
        assert not driver.find_elements(*MainPageLocators.USER_NAME)
