import re
from time import sleep

import playwright
from playwright.sync_api import Page, expect

def test_verifyPageUrl(page: Page):
    page.goto("https://www.automationexercise.com")  # passing url
    print("url: ", page.url)  # printing url
    expect(page).to_have_url("https://www.automationexercise.com/")  # expected url
    # sleep(2)
    page.wait_for_timeout(2000)
    expect(page).to_have_url(re.compile(r"https://www.automationexercise\.com/?"))  # expected url with regex

def test_verifyPageTitle(page: Page):
    page.goto("https://www.automationexercise.com")  # passing url
    print("title: ", page.title())  # printing title
    expect(page).to_have_title("Automation Exercise")  # expected title
    expect(page).to_have_title(re.compile(r"Automation Exercise"))  # expected title with regex