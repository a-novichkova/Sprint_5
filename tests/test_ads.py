from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators, AdFormLocators, ProfilePageLocators

from constants import PROFILE_URL

class TestAds:

    def test_create_ad_unauthorized(self, driver):
    #   создание объявления неавторизованным пользователем
        driver.find_element(*MainPageLocators.POST_AD_BUTTON).click()
        modal = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(MainPageLocators.MODAL_WINDOW)
        )
        assert "Чтобы разместить объявление, авторизуйтесь" in modal.text

    def test_create_ad_authorized(self, authorized_user):
    #   создание объявления авторизованным пользователем
        driver = authorized_user
        title = "test объявление"
        description = "test описание товара"
        price = "100500"

        driver.find_element(*MainPageLocators.POST_AD_BUTTON).click()
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(AdFormLocators.TITLE_INPUT)
        )

        driver.find_element(*AdFormLocators.TITLE_INPUT).send_keys(title)
        driver.find_element(*AdFormLocators.DESCRIPTION_INPUT).send_keys(description)
        driver.find_element(*AdFormLocators.PRICE_INPUT).send_keys(price)

        driver.find_element(*AdFormLocators.CATEGORY_DROPDOWN).click()
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(AdFormLocators.CATEGORY_AUTO)
        ).click()
        driver.find_element(*AdFormLocators.CITY_DROPDOWN).click()
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(AdFormLocators.CITY_MOSCOW)
        ).click()

        driver.find_element(*AdFormLocators.CONDITION_RADIO).click()
        driver.find_element(*AdFormLocators.PUBLISH_BUTTON).click()

        WebDriverWait(driver, 5).until(
            EC.invisibility_of_element_located(AdFormLocators.PUBLISH_BUTTON)
        )

        driver.get(PROFILE_URL)

        ad_locator = ProfilePageLocators.ad_title_by_text(title)
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(ad_locator)
        )
        assert driver.find_element(*ad_locator).is_displayed()
