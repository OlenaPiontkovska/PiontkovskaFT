from tests.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By

class SignInPage(BasePage):
    URL = "https://github.com/login"

    def init(self):
        super().init()
    
    def go_to(self):
        self.driver.get(SignInPage.URL)

    def try_login(self, username, password):
        #знаходимо поле, в якому буде вводитись неправильне ім'я користувача
        login_elem = self.driver.find_element(By.ID, "login_field")

        #вводимо неправильну електронну адресу
        login_elem.send_keys(username)

        # знаходимо поле в яке будемо вводити неправильний Пароль
        pass_elem = self.driver.find_element(By.ID, "password")

        #вводимо неправильний Пароль
        pass_elem.send_keys(password)

        # Знаходимо кнопку Sign in
        btn_elem = self.driver.find_element(By.NAME, "commit")

        # Емуліємо клік лівою кнопкою мишки
        btn_elem.click()

    def check_title(self, expected_title):
        return self.driver.title == expected_title