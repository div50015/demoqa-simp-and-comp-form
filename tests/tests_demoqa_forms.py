import pytest
import os
from selene import browser, have, command
from selenium.webdriver import Keys
import allure


def test_demoqa_simple_registration_form():
    # GIVEN
    with allure.step('Open registration form'):
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
    with allure.step('Fill form'):
        browser.element('#userName').type('Igor Deg')
        browser.element('#userEmail').type('div@novoch.ru')
        browser.element('#currentAddress').perform(command.js.scroll_into_view).type('Russian Novocherkassk')
        browser.element('#permanentAddress').type('Russian Sochi')
        browser.element('#submit').click()

    # THEN
    with allure.step('Check form results'):
        browser.element('#output').perform(command.js.scroll_into_view).all('p').should(
            have.texts(
                'Name:Igor Deg',
                'Email:div@novoch.ru',
                'Current Address :Russian Novocherkassk',
                'Permananet Address :Russian Sochi',
            )
        )


def test_demoqa_complex_registration_form():
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

    browser.element('//*[text()="Forms"]').element('../..').click()
    browser.element('//*[text()="Practice Form"]').click()

    # WHEN
    browser.element("#firstName").type("Igor")
    browser.element("#lastName").type("Degt")
    browser.element("#userEmail").type("div@novoch.ru")
    # bad selector (find for text)
    # browser.all('[for^=gender-radio]').element_by(have.text('Male')).click()
    # good selector (find for value)
    browser.all("[name=gender]").element_by(have.value("Male")).element("..").click()
    browser.element("#userNumber").type("9185024041")
    browser.element("#dateOfBirthInput").send_keys(Keys.CONTROL, "a").type("04 august 1967").press_enter()
    browser.element("#subjectsInput").type("History").press_enter()
    # browser.all('[for^=hobbies-checkbox]').element_by(have.text('Sports')).click() # клик на элементе без прокрутви
    # поиск элемента, прокрутка скрола и клик
    browser.all("[for^=hobbies-checkbox]").element_by(have.text("Sports")).perform(
        command.js.scroll_into_view
    ).click()
    import tests

    browser.element("#uploadPicture").send_keys(os.path.dirname(tests.__file__), "/files/ball.jpg")
    browser.element("#currentAddress").type("Russian Novocherkassk")
    browser.element("#state").click()
    browser.all("[id^=react-select]").element_by(have.text("Rajasthan")).click()
    browser.element("#city").click()
    browser.all("[id^=react-select]").element_by(have.text("Jaipur")).click()
    browser.element("#submit").click()
    # time.sleep(3)

    # THEN
    browser.element(".table").all("td").should(
        have.texts(
            ('Student Name', 'Igor Degt'),
            ('Student Email', 'div@novoch.ru'),
            ('Gender', 'Male'),
            ('Mobile', '9185024041'),
            ('Date of Birth', '04 August,1967'),
            ('Subjects', 'History'),
            ('Hobbies', 'Sports'),
            ('Picture', 'ball.jpg'),
            ('Address', 'Russian Novocherkassk'),
            ('State and City', 'Rajasthan Jaipur'),
        )
    )
