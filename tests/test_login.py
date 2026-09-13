from locators import MainPageLocators


class TestLogin:

    def test_login_success(self, authorized_user):
    #   login пользователя
        assert authorized_user.find_element(*MainPageLocators.USER_NAME).text == "User."
