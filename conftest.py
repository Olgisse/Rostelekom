import pytest
from selenium import webdriver


@pytest.fixture(scope='session')
def driver():
    driver = webdriver.Chrome(r'C:\Users\Olga\Desktop\SkillFactory\chrome\chromedriver.exe')
    driver.implicitly_wait(20)

    yield driver
    driver.quit()
