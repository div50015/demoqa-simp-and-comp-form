import pytest
from selene import browser, have, command


def test_demoqa_simple_registration_form():
    # GIVEN
    browser.open('/')
    # удаление элемента с id=fixeban и поиском елемента в JS
    # browser.execute_script('document.querySelector(#fixeban).remove')

    # удалениме элемента с тегом footer и поиском элемента в selene
    # browser.element('footer').execute_script('element.remove()')

    # уменьшение масштаба страници до 50%
    browser.driver.execute_script("document.querySelector('.body-height').style.transform='scale(.50)'")

    # ожидание в течение 10 секунд 3х реклпмных банеров и их удаление (вторая строка)
    # browser.all('[id^google_ads][id$=container__]').with_(timeout=10).wait_until(have.size_less_than_or_equal(3))
    # browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)

    browser.element('//*[text()="Elements"]').element('../..').click()
    browser.element('//*[text()="Text Box"]').click()

    # WHEN
    browser.element('#userName').type('Igor Deg')
    browser.element('#userEmail').type('div@novoch.ru')
    browser.element('#currentAddress').perform(command.js.scroll_into_view).type('Russian Novocherkassk')
    browser.element('#permanentAddress').type('Russian Sochi')
    browser.element('#submit').click()

    # THEN
    browser.element('#output').perform(command.js.scroll_into_view).all('p').should(
        have.texts(
            'Name:Igor Deg',
            'Email:div@novoch.ru',
            'Current Address :Russian Novocherkassk',
            'Permananet Address :Russian Sochi',
        )
    )

