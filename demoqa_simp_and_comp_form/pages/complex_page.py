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

        self.locator_hobbi = browser.all("[for^=hobbies-checkbox]").element_by(have.text("Sports"))

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

    def type_first_name(self):
        self.locator_first_name.type("Igor")

    def type_last_name(self):
        self.locator_last_name.type("Degt")

    def type_email(self):
        self.locator_email.type("div@novoch.ru")

    def type_gender(self):
        self.locator_gender.element_by(have.value("Male")).click()

    def type_number(self):
        self.locator_number.type("9185024041")

    def type_data_birth(self):
        self.locator_birth.send_keys(Keys.CONTROL, "a").type("04 august 1967").press_enter()

    def type_subjects(self):
        self.locator_subject.type("History").press_enter()

    def type_hobbi(self):
        self.locator_hobbi.perform(command.js.scroll_into_view).click()

    def type_file(self):
        self.locator_file.send_keys(os.path.dirname(tests.__file__), "/files/ball.jpg")

    def type_address(self):
        self.locator_address.type("Russian Novocherkassk")

    def type_state(self):
        self.locator_click_state.click()
        self.locator_enter_state.element_by(have.text("Rajasthan")).click()

    def type_city(self):
        self.locator_click_city.click()
        self.locator_enter_city.element_by(have.text("Jaipur")).click()

    def clich_submit(self):
        self.locator_submit.click()

        pass

    # THEN
    def shouid_complex_registration_form(self):
        self.locator_should.should(
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
