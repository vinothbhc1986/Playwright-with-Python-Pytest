import re

from playwright.sync_api import Page, expect

# playwright locators
def test_verify_pwlocators(page: Page):
    page.goto("https://demowebshop.tricentis.com/")

    # 1) page.get_by_alt_text()
    logo = page.get_by_alt_text("Tricentis Demo Web Shop")
    expect(logo).to_be_visible()

    # 2) page.get_by_text()
    expect(page.get_by_text("Welcome to the new Tricentis store!")).to_be_visible() #full text
    expect(page.get_by_text("Welcome to the new Tricentis")).to_be_visible()  # partial text
    expect(page.get_by_text(re.compile(".*to the new Tricentis.*"))).to_be_visible()  #using reg expression

    # 3) page.getByRole()
    page.goto("https://demowebshop.tricentis.com/register")
    page.wait_for_timeout(1000)
    expect(page.get_by_role("heading", name="Register")).to_be_visible()

    # 4) page.get_by_label()
    page.get_by_label("First name:").fill("John")
    page.get_by_label("Last name:").fill("Kenedy")
    page.get_by_label("Email:").fill("abc@gmail.com")
    page.wait_for_timeout(2000)

    # 5) page.get_by_placeholder()
    page.goto("https://www.automationexercise.com/login")
    page.get_by_placeholder("Name").fill("abc")
    page.wait_for_timeout(2000)

    # 6) page.get_by_title()
    page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")
    expect(page.get_by_title("Home page link")).to_have_text("Home")
    expect(page.get_by_title("HyperText Markup Language")).to_have_text("HTML")
    page.wait_for_timeout(1000)

    # 7) page.get_by_test_id()
    expect(page.get_by_test_id("profile-name")).to_have_text("John Doe")
    expect(page.get_by_test_id("profile-email")).to_have_text("john.doe@example.com")


