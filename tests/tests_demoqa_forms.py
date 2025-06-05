import pytest
from selene import browser


def test_demoqa_simple_registration_form():
    #GIVEN
    browser.open('/')
    # удаление элемента с id=fixeban и поиском елемента в JS
    # browser.execute_script('document.querySelector(#fixeban).remove')

    # удалениме элемента с тегом footer и поиском элемента в selene
    # browser.element('footer').execute_script('element.remove()')

    # уменьшение масштаба страници до 65%
    # browser.driver.execute_script("document.querySelector('.body-height').style.transform='scale(.65)'")

    # ожидание в течение 10 секунд 3х реклпмных банеров и их удаление (вторая строка)
    # browser.all('[id^google_ads][id$=container__]').with_(timeout=10).wait_until(have.size_less_than_or_equal(3))
    # browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)

    #WHEN
    pass

    #THEN