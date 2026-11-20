"""
valid - s - passed
valid - u - failed

invalid - s - failed
invalid - u -- passed
"""

login_test_Data=[ ("laura.taylor1234@example.com", "test123", "valid"),
                  ("invaliduser@example.com", "test321", "invalid"),
                  ("validuser@example.com", "testxyz", "invalid"),
                  ("", "", "invalid")
                ]


import pytest
from playwright.sync_api import expect,Page

@pytest.mark.parametrize("email,password, validity", login_test_Data)
def test_login_data_driven(email,password, validity, page:Page):
    page.goto("https://demowebshop.tricentis.com/login")

    #fill the login form
    page.locator("#Email").fill(email)  # email id
    page.locator("#Password").fill(password) #password
    page.locator("input[value='Log in']").click()

    # validation
    if validity == "valid":
        logout_link = page.locator("a[href='/logout']")
        expect(logout_link).to_be_visible(timeout=5000)
    else:
        error_message = page.locator(".validation-summary-errors")
        expect(error_message).to_be_visible(timeout=2000)  # checking error message
        expect(page).to_have_url("https://demowebshop.tricentis.com/login")  # checking same login page
