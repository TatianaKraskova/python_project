from playwright.sync_api import expect, Page

from playwright_project.tests.utils.constant import BASE_URL


def test_route_abort(page: Page):
    # Navigate to the savings page
    page.goto(f'{BASE_URL}savings.html')

    # Fill in the deposit field
    page.get_by_test_id('deposit').fill('10')

    # Check if the element with test ID 'result' is not visible
    expect(page.get_by_test_id('result')).to_be_visible()
