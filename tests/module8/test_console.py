from playwright.sync_api import Page

from tests.utils.constant import BASE_URL


def test_check_console(page: Page):
    # Task: Test for console.error()
    # Example alternative ways to handle console events:
    # page.on('console', lambda msg: expect(msg.text).not_to_have_text('...'))
    # page.on('console', lambda msg: assert msg.type != 'error')
    # page.on('console', check_console_event)

    console_errors = []

    # Listen for 'console' events and filter only errors
    page.on('console', lambda msg: console_errors.append(msg.text) if msg.type == 'error' else None)

    # Navigate to the base URL
    page.goto(BASE_URL)

    # Simulate interaction with a button named 'Register'
    page.get_by_role('button', name='Register').click()

    # Assert that there are no console errors
    assert len(console_errors) == 0, 'Expected 0 console errors'

def test_http_traffic(page: Page):
    # Challenge: Fail if response status code is >= 400

    traffic_errors = []

    # Listen for 'response' events and track responses with status >= 400
    page.on('response', lambda response: traffic_errors.append(response) if response.status >= 400 else None)

    # Navigate to the base URL
    page.goto(BASE_URL)

    # Assert that there are no traffic errors
    assert len(traffic_errors) == 0, 'Expected 0 traffic errors'
