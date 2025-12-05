import os
import allure
from selene import browser, have, be
from selene.support.shared import browser


@allure.title("Регистрация нового пользователя")
def test_registration_form(config_browser):
    with allure.step('Open form'):
        browser.open('/automation-practice-form')



    with allure.step('Fill form'):
        browser.element('#firstName').should(be.visible).should(be.clickable).type('Иван')
        browser.element('#lastName').should(be.visible).should(be.clickable).type('Иванов')
        browser.element('#userEmail').should(be.visible).should(be.clickable).type('ivanov@example.com')
        browser.all('.custom-radio').should(have.texts('Male', 'Female', 'Other'))
        browser.element('label[for="gender-radio-1"]').click()
        browser.element('#userNumber').should(be.visible).should(be.clickable).type('7929100500')
        browser.element('#dateOfBirthInput').should(be.visible).should(be.clickable).click()
        browser.element('.react-datepicker__month-select').click()
        browser.element('option[value="10"]').click()
        browser.element('.react-datepicker__year-select').click()
        browser.element('option[value="1986"]').click()
        browser.element('.react-datepicker__day.react-datepicker__day--025').click()
        browser.element('#subjectsInput').type('Maths').press_enter()
        browser.element('label[for="hobbies-checkbox-1"]').click()
        browser.element('#currentAddress').should(be.visible).should(be.clickable).type('Moscow, st.Lenina, 23')
        browser.element('#state').click()
        browser.element('#react-select-3-input').type('NCR').press_enter()
        browser.element('#city').click()
        browser.element('#react-select-4-input').type('Delhi').press_enter()
        browser.element('#submit').should(be.visible).should(be.clickable).click()
        browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))

    with allure.step("Check form results"):
        browser.all('.table td').should(have.exact_texts(
        'Student Name', 'Иван Иванов',
        'Student Email', 'ivanov@example.com',
        'Gender', 'Male',
        'Mobile', '7929100500',
        'Date of Birth', '25 November,1986',
        'Subjects', 'Maths',
        'Hobbies', 'Sports',
        'Address', 'Moscow, st.Lenina, 23',
        'State and City', 'NCR Delhi'
        ))
