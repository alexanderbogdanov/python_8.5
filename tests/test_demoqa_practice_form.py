import os

from selene import browser, be, have, command, by


def test_form():
    browser.open("/automation-practice-form")
    remove_footer_and_ad()
    browser.element("#firstName").should(be.blank).type("Benedict")
    browser.element("#lastName").should(be.blank).type("Cumberbatch")
    browser.element("#userEmail").should(be.blank).type("benya@mail.ru")
    browser.element("[for='gender-radio-1']").click()
    browser.element("#userNumber").should(be.blank).type("1234567890")
    browser.element("#dateOfBirthInput").click()
    browser.element(".react-datepicker__month-select").click().element(
        by.text("September")
    ).click()
    browser.element(".react-datepicker__year-select").click().element(
        by.text("1977")
    ).click()
    browser.element(".react-datepicker__day--024").click()
    scroll_to("#submit")
    browser.element("#subjectsInput").should(be.blank).type("Arts").press_enter()
    browser.element("[for='hobbies-checkbox-3']").click()
    browser.element("#uploadPicture").send_keys(
        os.path.abspath("resources/kamber.jpeg")
    )
    browser.element("#currentAddress").should(be.blank).type(
        "Manohar Chhangani home, 032"
    )
    browser.element("#state").click()
    browser.element("#react-select-3-input").should(be.blank).type("raj").press_enter()
    browser.element("#city").click()
    browser.element("#react-select-4-input").should(be.blank).type("jais").press_enter()
    browser.element("#submit").click()

    browser.element(".modal-dialog").should(be.existing)
    browser.element(".table").all("td:nth-child(2)").should(
        have.texts(
            "Benedict Cumberbatch",
            "benya@mail.ru",
            "Male",
            "1234567890",
            "24 September,1977",
            "Arts",
            "Music",
            "kamber.jpeg",
            "Manohar Chhangani home, 032",
            "Rajasthan Jaiselmer",
        )
    )


#


def scroll_to(elem):
    browser.element(elem).perform(command.js.scroll_into_view)


def remove_footer_and_ad():
    browser.execute_script('document.querySelector("#fixedban").remove()')
    browser.element("footer").execute_script("element.remove()")
