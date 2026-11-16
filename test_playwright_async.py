from playwright.async_api import async_playwright, Page, expect
import pytest

@pytest.mark.asyncio
async def test_verifyPageUrl():
    async with async_playwright() as p:
        browser=await p.chromium.launch()
        mypage=await browser.new_page()
        await mypage.goto("https://www.automationexercise.com") # passing url
        await expect(mypage).to_have_url("https://www.automationexercise.com/") # expected url