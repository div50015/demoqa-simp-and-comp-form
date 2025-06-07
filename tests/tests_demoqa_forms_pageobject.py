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
