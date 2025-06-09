import pytest
from selene import browser
from selenium import webdriver
from utils import attach


@pytest.fixture(scope='function', autouse=True)
def browser_manager():
    browser.config.base_url = 'https://demoqa.com'
    browser.config.timeout = 2.0
    browser.config.window_width = 900
    browser.config.window_height = 900

    # вводить текст одной строкой через JS (selenium вводит текст посимвольно)
    # browser.config.type_by_js = True

    browser_options = webdriver.ChromeOptions()
    # удаление сообщения "Браузером Chrome управляет автоматизированное тестовое ПО"
    # browser_options.add_experimental_option("excludeSwitches", ['enable-automation'])
    # не выводить изображение браузера на экран
    # browser_options.add_argument('--headless=new')
    browser.config.driver_options = browser_options

    yield browser

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()
