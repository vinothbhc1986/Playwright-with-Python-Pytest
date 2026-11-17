from playwright.sync_api import Page, expect


def test_checkbox(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    # 1. select specific checkbox (Sunday)
    sunday_checkbox = page.get_by_label("Sunday")
    sunday_checkbox.check()
    expect(sunday_checkbox).to_be_checked()
    page.wait_for_timeout(5000)

    # 2. count number of check boxes

    # step1:
    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    checkboxes = []

    # step2
    # for day in days:
    #     checkbox = page.get_by_label(day)
    #     checkboxes.append(checkbox)

    checkboxes = [page.get_by_label(day) for day in days]
    print("total number of checkboxes:", len(checkboxes))

    # 3 . select all the checkboxes and assert each check box is selected
    for checkbox in checkboxes:
        checkbox.check()
        expect(checkbox).to_be_checked()

    page.wait_for_timeout(5000)
