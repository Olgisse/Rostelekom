import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from auth_page import AuthPage
from settings import phone_number, password, email, account, login


# БЛОК 1. Вкладки аутентификации
# 1 Вкладка авторизации по номеру телефона
def test_auth_page_phone_tab():
    driver = webdriver.Chrome(r'C:\Users\Olga\Desktop\SkillFactory\chrome\chromedriver.exe')
    driver.implicitly_wait(10)
    auth_page = AuthPage(driver)
    auth_page.go_to_site()
    driver.find_element(By.ID, 't-btn-tab-phone').click()
    assert driver.find_element(By.CLASS_NAME, 'rt-input__placeholder').text == "Мобильный телефон"


# 2 Вкладка авторизации по электронной почте
def test_auth_page_email_tab():
    driver = webdriver.Chrome(r'C:\Users\Olga\Desktop\SkillFactory\chrome\chromedriver.exe')
    driver.implicitly_wait(10)
    auth_page = AuthPage(driver)
    auth_page.go_to_site()
    driver.find_element(By.ID, 't-btn-tab-mail').click()
    assert driver.find_element(By.XPATH,
                               '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/div/span[2]').text == "Электронная почта"


# 3 Вкладка авторизации по логину
def test_auth_page_login_tab():
    driver = webdriver.Chrome(r'C:\Users\Olga\Desktop\SkillFactory\chrome\chromedriver.exe')
    driver.implicitly_wait(10)
    auth_page = AuthPage(driver)
    auth_page.go_to_site()
    driver.find_element(By.ID, 't-btn-tab-login').click()
    assert driver.find_element(By.XPATH,
                               '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/div/span[2]').text == "Логин"


# 4 Вкладка авторизации по номеру лицевого счёта
def test_auth_page_LS_tab():
    driver = webdriver.Chrome(r'C:\Users\Olga\Desktop\SkillFactory\chrome\chromedriver.exe')
    driver.implicitly_wait(10)
    auth_page = AuthPage(driver)
    auth_page.go_to_site()
    driver.find_element(By.ID, 't-btn-tab-ls').click()
    assert driver.find_element(By.XPATH,
                               '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/div/span[2]').text == "Лицевой " \
                                                                                                           "счёт"


# БЛОК 2 БАЗОВЫЕ ПОЗИТИВНЫЕ ТЕСТЫ
# 5 Аутентификация по телефону, привязанному к учетной записи клиента; пароль корректный
def test_auth_page_valid_phone():
    driver = webdriver.Chrome(r'C:\Users\Olga\Desktop\SkillFactory\chrome\chromedriver.exe')
    driver.implicitly_wait(10)
    auth_page = AuthPage(driver)
    auth_page.go_to_site()
    auth_page.auth_by_phone()
    driver.find_element(By.ID, "username").send_keys(phone_number)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "kc-login").click()
    assert driver.find_element(By.XPATH, '//*[@id="app"]/main/div/div[2]/div[3]/h3').text == "Личные кабинеты"


# 6 Аутентификация по электронной почте, привязанному к учетной записи клиента; пароль корректный
def test_auth_page_valid_email():
    driver = webdriver.Chrome(r'C:\Users\Olga\Desktop\SkillFactory\chrome\chromedriver.exe')
    driver.implicitly_wait(10)
    auth_page = AuthPage(driver)
    auth_page.go_to_site()
    driver.find_element(By.ID, 't-btn-tab-mail').click()
    driver.find_element(By.ID, "username").send_keys(email)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "kc-login").click()
    assert driver.find_element(By.XPATH, '//*[@id="app"]/main/div/div[2]/div[3]/h3').text == "Личные кабинеты"


# 7 Аутентификация по логину, привязанному к учетной записи клиента; пароль корректный
def test_auth_page_valid_login():
    driver = webdriver.Chrome(r'C:\Users\Olga\Desktop\SkillFactory\chrome\chromedriver.exe')
    driver.implicitly_wait(10)
    auth_page = AuthPage(driver)
    auth_page.go_to_site()
    driver.find_element(By.ID, 't-btn-tab-login').click()
    driver.find_element(By.ID, "username").send_keys(login)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "kc-login").click()
    assert driver.find_element(By.XPATH, '//*[@id="app"]/main/div/div[2]/div[3]/h3').text == "Личные кабинеты"


# 8 Аутентификация по лицевому счету, привязанному к учетной записи клиента; пароль корректный
def test_auth_page_valid_LS():
    driver = webdriver.Chrome(r'C:\Users\Olga\Desktop\SkillFactory\chrome\chromedriver.exe')
    driver.implicitly_wait(10)
    auth_page = AuthPage(driver)
    auth_page.go_to_site()
    driver.find_element(By.ID, 't-btn-tab-ls').click()
    driver.find_element(By.ID, "username").send_keys(account)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "kc-login").click()
    assert driver.find_element(By.XPATH, '//*[@id="app"]/main/div/div[2]/div[3]/h3').text == "Личные кабинеты"


# БЛОК 3 НЕГАТИВНЫХ ТЕСТОВ - незаполненное поле username в разных способах аутентификации
# 9 Незаполненное поле "телефон"; пароль корректный
def test_auth_page_empty_phone():
    driver = webdriver.Chrome(r'C:\Users\Olga\Desktop\SkillFactory\chrome\chromedriver.exe')
    driver.implicitly_wait(10)
    auth_page = AuthPage(driver)
    auth_page.go_to_site()
    auth_page.auth_by_phone()
    driver.find_element(By.ID, 't-btn-tab-phone').click()
    driver.find_element(By.ID, "username").send_keys("")
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "kc-login").click()
    driver.implicitly_wait(10)
    assert driver.find_element(By.XPATH,
                               '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/span').text == "Введите номер " \
                                                                                                    "телефона"


# 10 Незаполненное поле "email"; пароль корректный
def test_auth_page_empty_email():
    driver = webdriver.Chrome(r'C:\Users\Olga\Desktop\SkillFactory\chrome\chromedriver.exe')
    driver.implicitly_wait(10)
    auth_page = AuthPage(driver)
    auth_page.go_to_site()
    auth_page.auth_by_email()
    driver.find_element(By.ID, 't-btn-tab-mail').click()
    driver.find_element(By.ID, "username").send_keys("")
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "kc-login").click()
    driver.implicitly_wait(10)
    assert driver.find_element(By.XPATH,
                               '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/span').text == "Введите адрес, " \
                                                                                                    "указанный при " \
                                                                                                    "регистрации"


# 11 Незаполненное поле "логин"; пароль корректный
def test_auth_page_empty_login():
    driver = webdriver.Chrome(r'C:\Users\Olga\Desktop\SkillFactory\chrome\chromedriver.exe')
    driver.implicitly_wait(10)
    auth_page = AuthPage(driver)
    auth_page.go_to_site()
    auth_page.auth_by_login()
    driver.find_element(By.ID, 't-btn-tab-login').click()
    driver.find_element(By.ID, "username").send_keys("")
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "kc-login").click()
    driver.implicitly_wait(10)
    assert driver.find_element(By.XPATH,
                               '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/span').text == "Введите логин, " \
                                                                                                    "указанный при " \
                                                                                                    "регистрации"


# 12 Незаполненное поле "лицевой счет"; пароль корректный
def test_auth_page_empty_ls():
    driver = webdriver.Chrome('/C:/Users/User/Downloads/chromedriver_win32//chromedriver.exe')
    driver.implicitly_wait(10)
    auth_page = AuthPage(driver)
    auth_page.go_to_site()
    auth_page.auth_by_LS()
    driver.find_element(By.ID, 't-btn-tab-ls').click()
    driver.find_element(By.ID, "username").send_keys("")
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "kc-login").click()
    driver.implicitly_wait(10)
    assert driver.find_element(By.XPATH,
                               '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/span').text == "Введите номер " \
                                                                                                    "вашего лицевого " \
                                                                                                    "счета"


# БЛОК 4 НЕГАТИВНЫХ ТЕСТОВ -незаполненное поле password во всех способах авторизации; пароль корректный
# 13 Незаполненное поле "пароль"; номер телефона корректный
def test_auth_page_phone_but_pass_is_empty():
    driver = webdriver.Chrome(r'C:\Users\Olga\Desktop\SkillFactory\chrome\chromedriver.exe')
    driver.implicitly_wait(10)
    auth_page = AuthPage(driver)
    auth_page.go_to_site()
    auth_page.auth_by_phone()
    driver.find_element(By.ID, 't-btn-tab-phone').click()
    driver.find_element(By.ID, "username").send_keys(phone_number)
    driver.find_element(By.ID, "password").send_keys("")
    driver.find_element(By.ID, "kc-login").click()
    driver.implicitly_wait(10)
    assert driver.find_element(By.ID, "kc-login").is_enabled()


# 14 Незаполненное поле "пароль"; email корректный
def test_auth_page_email_but_pass_is_empty():
    driver = webdriver.Chrome(r'C:\Users\Olga\Desktop\SkillFactory\chrome\chromedriver.exe')
    driver.implicitly_wait(10)
    auth_page = AuthPage(driver)
    auth_page.go_to_site()
    auth_page.auth_by_email()
    driver.find_element(By.ID, 't-btn-tab-mail').click()
    driver.find_element(By.ID, "username").send_keys(email)
    driver.find_element(By.ID, "password").send_keys("")
    driver.find_element(By.ID, "kc-login").click()
    driver.implicitly_wait(10)
    assert driver.find_element(By.ID, "kc-login").is_enabled()


# 15 Незаполненное поле "пароль"; логин корректный
def test_auth_page_login_but_pass_is_empty():
    driver = webdriver.Chrome(r'C:\Users\Olga\Desktop\SkillFactory\chrome\chromedriver.exe')
    driver.implicitly_wait(10)
    auth_page = AuthPage(driver)
    auth_page.go_to_site()
    auth_page.auth_by_login()
    driver.find_element(By.ID, 't-btn-tab-login').click()
    driver.find_element(By.ID, "username").send_keys(login)
    driver.find_element(By.ID, "password").send_keys("")
    driver.find_element(By.ID, "kc-login").click()
    driver.implicitly_wait(10)
    assert driver.find_element(By.ID, "kc-login").is_enabled()


# 16 Незаполненное поле "пароль"; лицевой счёт корректный
def test_auth_page_ls_but_pass_is_empty():
    driver = webdriver.Chrome(r'C:\Users\Olga\Desktop\SkillFactory\chrome\chromedriver.exe')
    driver.implicitly_wait(10)
    auth_page = AuthPage(driver)
    auth_page.go_to_site()
    auth_page.auth_by_LS()
    driver.find_element(By.ID, 't-btn-tab-ls').click()
    driver.find_element(By.ID, "username").send_keys(account)
    driver.find_element(By.ID, "password").send_keys("")
    driver.find_element(By.ID, "kc-login").click()
    driver.implicitly_wait(10)
    # assert auth_page.get_relative_link() != '/account_b2c/page'
    assert driver.find_element(By.ID, "kc-login").is_enabled()


# БЛОК 5 НЕГАТИВНЫХ ТЕСТОВ -некорректные данные: существующие персональные данные, но не привязанные к конкретной
# учетной записи клиента
# 17 Существующий телефонный номер, не привязанный к УЗ, пароль от УЗ
def test_auth_page_other_phone():
    driver = webdriver.Chrome(r'C:\Users\Olga\Desktop\SkillFactory\chrome\chromedriver.exe')
    driver.implicitly_wait(10)
    auth_page = AuthPage(driver)
    auth_page.go_to_site()
    auth_page.auth_by_phone()
    driver.find_element(By.ID, 't-btn-tab-phone').click()
    driver.find_element(By.ID, "username").send_keys("+7 931 0082602")
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "kc-login").click()
    driver.implicitly_wait(10)
    # assert auth_page.get_relative_link() != '/account_b2c/page'
    assert driver.find_element(By.ID, "form-error-message").text == "Неверный логин или пароль"


# 18 Существующий email, не привязанный к УЗ, пароль от УЗ
def test_auth_page_other_email():
    driver = webdriver.Chrome(r'C:\Users\Olga\Desktop\SkillFactory\chrome\chromedriver.exe')
    driver.implicitly_wait(10)
    auth_page = AuthPage(driver)
    auth_page.go_to_site()
    auth_page.auth_by_email()
    driver.find_element(By.ID, 't-btn-tab-mail').click()
    driver.find_element(By.ID, "username").send_keys("mikhi.olga@gmail.com")
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "kc-login").click()
    driver.implicitly_wait(10)
    assert driver.find_element(By.ID, "form-error-message").text == "Неверный логин или пароль"


# 19 Существующий логин, не привязанный к УЗ, пароль от УЗ
def test_auth_page_other_loginname():
    driver = webdriver.Chrome(r'C:\Users\Olga\Desktop\SkillFactory\chrome\chromedriver.exe')
    driver.implicitly_wait(10)
    auth_page = AuthPage(driver)
    auth_page.go_to_site()
    auth_page.auth_by_login()
    driver.find_element(By.ID, 't-btn-tab-login').click()
    driver.find_element(By.ID, "username").send_keys("Strelna_net")
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "kc-login").click()
    driver.implicitly_wait(10)
    assert driver.find_element(By.ID, "form-error-message").text == "Неверный логин или пароль"


# 20 Существующий лицевой счет, не привязанный к УЗ данного пользователя, пароль от УЗ
def test_auth_page_other_ls():
    driver = webdriver.Chrome(r'C:\Users\Olga\Desktop\SkillFactory\chrome\chromedriver.exe')
    driver.implicitly_wait(10)
    auth_page = AuthPage(driver)
    auth_page.go_to_site()
    auth_page.auth_by_LS()
    driver.find_element(By.ID, 't-btn-tab-ls').click()
    driver.find_element(By.ID, "username").send_keys("278010574977")
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "kc-login").click()
    driver.implicitly_wait(10)
    assert driver.find_element(By.ID, "form-error-message").text == "Неверный логин или пароль"


# БЛОК 5 НЕГАТИВНЫХ ТЕСТОВ - некорректны данные: несуществующие данные (наборы случайных символов и пр.)
# 21 Неверный номер телефона (буквы, латиница)
def test_auth_page_phone_latin():
    driver = webdriver.Chrome(r'C:\Users\Olga\Desktop\SkillFactory\chrome\chromedriver.exe')
    driver.implicitly_wait(10)
    auth_page = AuthPage(driver)
    auth_page.go_to_site()
    driver.find_element(By.ID, 't-btn-tab-phone').click()
    driver.find_element(By.ID, "username").send_keys("abcdefg")
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "kc-login").click()
    driver.implicitly_wait(10)
    assert driver.find_element(By.ID, "form-error-message").text == "Неверный логин или пароль"


# 22 Неверный email (набор специальных символов)
def test_auth_page_email_symbol():
    driver = webdriver.Chrome(r'C:\Users\Olga\Desktop\SkillFactory\chrome\chromedriver.exe')
    driver.implicitly_wait(10)
    auth_page = AuthPage(driver)
    auth_page.go_to_site()
    driver.find_element(By.ID, 't-btn-tab-mail').click()
    driver.find_element(By.ID, "username").send_keys(")(**?*?:*?:%*")
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "kc-login").click()
    driver.implicitly_wait(10)
    assert driver.find_element(By.XPATH, '//*[@id="form-error-message"]').text == 'Неверный логин или пароль'


# 23 Неверный логин (набор специальных символов)
def test_auth_page_loginname_symbol():
    driver = webdriver.Chrome(r'C:\Users\Olga\Desktop\SkillFactory\chrome\chromedriver.exe')
    driver.implicitly_wait(10)
    auth_page = AuthPage(driver)
    auth_page.go_to_site()
    driver.find_element(By.ID, 't-btn-tab-login').click()
    driver.find_element(By.ID, "username").send_keys(")(**?*?:*?:%*")
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "kc-login").click()
    driver.implicitly_wait(10)
    assert driver.find_element(By.XPATH, '//*[@id="form-error-message"]').text == 'Неверный логин или пароль'


# 24 Неверный лицевой счёт (набор специальных символов)
def test_auth_page_ls_symbol():
    driver = webdriver.Chrome(r'C:\Users\Olga\Desktop\SkillFactory\chrome\chromedriver.exe')
    driver.implicitly_wait(10)
    auth_page = AuthPage(driver)
    auth_page.go_to_site()
    driver.find_element(By.ID, 't-btn-tab-ls').click()
    driver.find_element(By.ID, "username").send_keys(")(**?*?:*?:%*")
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "kc-login").click()
    driver.implicitly_wait(10)
    assert driver.find_element(By.XPATH, '//*[@id="form-error-message"]').text == 'Неверный логин или пароль'


# 25 Неверный номер телефона, неверный пароль (набор случайных символов)
def test_auth_page_phone_but_pass_wrong():
    driver = webdriver.Chrome(r'C:\Users\Olga\Desktop\SkillFactory\chrome\chromedriver.exe')
    driver.implicitly_wait(10)
    auth_page = AuthPage(driver)
    auth_page.go_to_site()
    driver.find_element(By.ID, 't-btn-tab-phone').click()
    driver.find_element(By.ID, "username").send_keys(")*?(*?*:")
    driver.find_element(By.ID, "password").send_keys("*&*(&*(&*^&^")
    driver.find_element(By.ID, "kc-login").click()
    driver.implicitly_wait(10)
    assert driver.find_element(By.ID, "form-error-message").text == "Неверный логин или пароль"
