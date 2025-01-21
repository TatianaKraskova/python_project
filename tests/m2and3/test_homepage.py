from playwright.sync_api import sync_playwright

def test_homepage_title():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        page.goto('https://playwright.dev/python/')
        browser.close()

def test_homepage_header():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        page.goto('https://playwright.dev/python/')
        browser.close()
