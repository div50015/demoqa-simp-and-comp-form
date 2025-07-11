from selene import browser
from demoqa_simp_and_comp_form.pages.application import app
import allure


def tests_demoqa_simple_form():
    # GIVEN
    with allure.step('Open registration form'):
        app.simple_app.open_simple_page()

    # WHEN
    with allure.step('Fill form'):
        app.simple_app.fill_simple_form_name('Igor Deg')
        app.simple_app.fill_simple_form_email('div@novoch.ru')
        app.simple_app.fill_simple_form_cur_addr('Russia Novocherkassk')
        app.simple_app.fill_simple_form_per_addr('Russia Sochi')
        app.simple_app.fill_simple_form_submit()

    # THEN
    with allure.step('Check form results'):
        app.simple_app.shouid_simple_registration_form(
            'Igor Deg',
            'div@novoch.ru',
            'Russia Novocherkassk',
            'Russia Sochi',
        )


def tests_demoqa_complex_form():
    # GIVEN
    with allure.step('Open registration form'):
        app.complex_page.open_complex_page()

    # WHET
    with allure.step('Fill form'):
        app.complex_page.type_first_name('Igor')
        app.complex_page.type_last_name('Deg')
        app.complex_page.type_email('div@novoch.ru')
        app.complex_page.type_gender('Male')
        app.complex_page.type_number('9185024041')
        app.complex_page.type_data_birth('04 August 1967')
        app.complex_page.type_subjects('History')
        app.complex_page.type_hobbi('Sports')
        app.complex_page.type_file('ball.jpg')
        app.complex_page.type_address('Russia Novocherkassk')
        app.complex_page.type_state('Rajasthan')
        app.complex_page.type_city('Jaipur')
        app.complex_page.clich_submit()

    # THEN
    with allure.step('Check form results'):
        app.complex_page.shouid_complex_registration_form(
            'Igor Deg',
            'div@novoch.ru',
            'Male',
            '9185024041',
            '04 August,1967',
            'History',
            'Sports',
            'ball.jpg',
            'Russia Novocherkassk',
            'Rajasthan Jaipur',
        )
