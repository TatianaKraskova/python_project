from playwright.sync_api import sync_playwright, Page, expect, BrowserType

from tests.utils.constant import BASE_URL

def test_headless_and_slow():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        context = browser.new_context()
        page = context.new_page()

        recommended_locators(page)
        browser.close()

        # page = browser_type.launch(headless=False, slow_mo=1000) // from the course


def recommended_locators(page: Page):
    #page.goto(BASE_URL)
    page.goto(f'{BASE_URL}index.html')
    first_name = page.get_by_label('First name')
    first_name.fill('Sofia')
    first_name.clear()

    page.get_by_label('First name').fill('Andrea')
    page.get_by_role('button', name='Register').click()
    warning = page.get_by_text('Valid last name is required')
    expect(warning).to_be_visible()

if __name__ == "__main__":
    test_headless_and_slow()

