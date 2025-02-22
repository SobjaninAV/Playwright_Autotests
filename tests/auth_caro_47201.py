import re
from playwright.sync_api import Playwright, sync_playwright, expect


def test_auth_caro_47201(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://servicetest.b2b-logist.com/cargo/47201/ru_RU/")
    page.locator("#userName").click()
    page.locator("#userName").fill("472ulsu@gmail.com")
    page.locator("#userPassword").click()
    page.locator("#userPassword").fill("123")
    page.get_by_role("button", name="Войти").click()

    # ---------------------
    #context.close()
    #browser.close()
