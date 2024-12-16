import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


@pytest.mark.ui 
def test_check_incorrect_username():
    # Створення об'єкта для керування браузером
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    # Відкриваємо сторінку https://github.com/login
    driver.get("https://github.com/login")

    #знаходимо поле, в якому буде вводитись неправильне ім'я користувача
    login_elem = driver.find_element(By.ID, "login_field")

    #вводимо неправильну електронну адресу
    login_elem.send_keys("wrong@wrong.com")

    # знаходимо поле в яке будемо вводити неправильний Пароль
    pass_elem = driver.find_element(By.ID, "password")

    #вводимо неправильний Пароль
    pass_elem.send_keys("wrong password")

    # Знаходимо кнопку Sign in
    btn_elem = driver.find_element(By.NAME, "commit")

    # Емуліємо клік лівою кнопкою мишки
    btn_elem.click()

    # Перевіряємо назву сторінки, чи така як очікували
    assert driver.title == "Sign in to GitHub · GitHub"
    
    
    #закриваємо браузер
    driver.close()
    