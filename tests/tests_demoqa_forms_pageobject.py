from selene import browser
from demoqa_simp_and_comp_form.pages.application import app


def tests_demoqa_simple_form():
    # GIVEN
    app.simple_app.open_simple_page()

    # WHEN
    app.simple_app.fill_simple_form_name('Igor Deg')
    app.simple_app.fill_simple_form_email('div@novoch.ru')
    app.simple_app.fill_simple_form_cur_addr('Russia Novocherkassk')
    app.simple_app.fill_simple_form_per_addr('Russia Sochi')
    app.simple_app.fill_simple_form_submit()

    # THEN
    app.simple_app.shouid_simple_registration_form(
        'Igor Deg',
        'div@novoch.ru',
        'Russia Novocherkassk',
        'Russia Sochi',
    )


def tests_demoqa_complex_form():
    # GIVEN
    app.complex_page.open_complex_page()

    # WHET
    app.complex_page.type_first_name()
    app.complex_page.type_last_name()
    app.complex_page.type_email()
    app.complex_page.type_gender()
    app.complex_page.type_number()
    app.complex_page.type_data_birth()
    app.complex_page.type_subjects()
    app.complex_page.type_hobbi()
    app.complex_page.type_file()
    app.complex_page.type_address()
    app.complex_pagetype_state()
    app.complex_page.type_city()
    app.complex_page.clich_submit()

    # THEN
    app.complex_page.shouid_complex_registration_form()
