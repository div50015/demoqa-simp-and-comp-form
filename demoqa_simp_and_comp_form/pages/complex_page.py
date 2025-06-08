from selene import browser, have, command
from selenium.webdriver import Keys
import tests
import os


class ComplexPage:
    def __init__(self):
        self.locator_elements = browser.element('//*[text()="Forms"]').element('../..')
        self.locator_practice_form = browser.element('//*[text()="Practice Form"]')

        self.locator_first_name = browser.element("#firstName")
        self.locator_last_name = browser.element("#lastName")
        self.locator_email = browser.element("#userEmail")
        self.locator_gender = browser.all("[name=gender]")
        self.locator_number = browser.element("#userNumber")
        self.locator_birth = browser.element("#dateOfBirthInput")
        self.locator_subject = browser.element("#subjectsInput")

        self.locator_hobbi = browser.all("[for^=hobbies-checkbox]")

        self.locator_file = browser.element("#uploadPicture")
        self.locator_address = browser.element("#currentAddress")
        self.locator_click_state = browser.element("#state")
        self.locator_enter_state = browser.all("[id^=react-select]")
        self.locator_click_city = browser.element("#city")
        self.locator_enter_city = browser.all("[id^=react-select]")
        self.locator_submit = browser.element("#submit")
        self.locator_should = browser.element(".table").all("td")

    def open_complex_page(self):
        browser.open('/')
        browser.driver.execute_script("document.querySelector('.body-height').style.transform='scale(.50)'")
        self.locator_elements.click()
        self.locator_practice_form.click()

    def type_first_name(self, value):
        self.locator_first_name.type(value)

    def type_last_name(self, value):
        self.locator_last_name.type(value)

    def type_email(self, value):
        self.locator_email.type(value)

    def type_gender(self, value):
        self.locator_gender.element_by(have.value(value)).element("..").click()

    def type_number(self, value):
        self.locator_number.type(value)

    def type_data_birth(self, value):
        self.locator_birth.send_keys(Keys.CONTROL, "a").type(value).press_enter()

    def type_subjects(self, value):
        self.locator_subject.type(value).press_enter()

    def type_hobbi(self, value):
        self.locator_hobbi.element_by(have.text(value)).perform(command.js.scroll_into_view).click()

    def type_file(self, value):
        self.locator_file.send_keys(os.path.dirname(tests.__file__), f'/files/{value}')

    def type_address(self, value):
        self.locator_address.type(value)

    def type_state(self, value):
        self.locator_click_state.click()
        self.locator_enter_state.element_by(have.text(value)).click()

    def type_city(self, value):
        self.locator_click_city.click()
        self.locator_enter_city.element_by(have.text(value)).click()

    def clich_submit(self):
        self.locator_submit.click()

        pass

    # THEN
    def shouid_complex_registration_form(
        self, fullname, email, gender, number, birth, subject, hobbi, file, address, state_city
    ):
        self.locator_should.should(
            have.texts(
                ('Student Name', fullname),
                ('Student Email', email),
                ('Gender', gender),
                ('Mobile', number),
                ('Date of Birth', birth),
                ('Subjects', subject),
                ('Hobbies', hobbi),
                ('Picture', file),
                ('Address', address),
                ('State and City', state_city),
            )
        )
