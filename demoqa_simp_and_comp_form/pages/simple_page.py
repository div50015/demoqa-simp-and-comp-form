from selene import browser, have, command


class SimlePage:
    def __init__(self):
        self.locator_elements = browser.element('//*[text()="Elements"]').element('../..')
        self.locator_text_box = browser.element('//*[text()="Text Box"]')

        self.locator_name = browser.element('#userName')
        self.locator_email = browser.element('#userEmail')
        self.locator_cur_addr = browser.element('#currentAddress')
        self.locator_per_addr = browser.element('#permanentAddress')
        self.locator_submit = browser.element('#submit')
        self.locator_should = browser.element('#output')

    def open_simple_page(self):
        browser.open('/')
        browser.driver.execute_script("document.querySelector('.body-height').style.transform='scale(.60)'")
        self.locator_elements.click()
        self.locator_text_box.click()

    def fill_simple_form_name(self, value):
        self.locator_name.type(value)

    def fill_simple_form_email(self, value):
        self.locator_email.type(value)

    def fill_simple_form_cur_addr(self, value):
        self.locator_cur_addr.type(value)

    def fill_simple_form_per_addr(self, value):
        self.locator_per_addr.type(value)

    def fill_simple_form_submit(self):
        self.locator_submit.click()

    def shouid_simple_registration_form(self, name, email, cur_addr, per_addr):
        self.locator_should.perform(command.js.scroll_into_view).all('p').should(
            have.texts(
                f'Name:{name}',
                f'Email:{email}',
                f'Current Address :{cur_addr}',
                f'Permananet Address :{per_addr}',
            )
        )
