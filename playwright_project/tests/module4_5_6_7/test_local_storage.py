from playwright.sync_api import sync_playwright, Page

from playwright_project.tests.utils.constant import BASE_URL


def test_local_storage(page: Page):
    page.goto(BASE_URL)
    name = "Andrejs"
    page.get_by_label('First name').fill(name)
    page.get_by_role('button', name='Save Input').click()

    # Validate localStorage directly using JavaScript
    local_storage_content = page.evaluate("Object.entries(localStorage)")
    print("\nLocalStorage Content:", local_storage_content)

    # Add validation (assertions)
    assert any(item[0] == 'First name' and item[1] == name for item in local_storage_content), \
        "Expected 'First name' key with the correct value in localStorage."


# Run the test using Playwright
def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        context = browser.new_context()
        page = context.new_page()
        test_local_storage(page)
        browser.close()


if __name__ == "__main__":
    run()
