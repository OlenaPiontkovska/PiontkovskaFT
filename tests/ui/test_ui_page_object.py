from tests.ui.page_objects.sign_in_page import SignInPage
import pytest

@pytest.mark.ui 
def test_check_incorrect_username_page_object():
    #створюємо об'єкт сторінки
    sign_in_page = SignInPage()

    # Відкриваємо сторінку https://github.com/login
    sign_in_page.go_to()

    #пробуємо увійти в систему GitHub
    sign_in_page.try_login("wrong1@wrong.com", "wrong password")

    # Перевіряємо назву сторінки, чи така як очікували
    assert sign_in_page.check_title("Sign in to GitHub · GitHub")

    #закриваємо браузер
    sign_in_page.close()
    