from playwright.sync_api import Page, expect

from tests.utils.constant import BASE_URL


def test_screenshot_demo(page: Page):
    # Navigate to the base URL
    page.goto(BASE_URL)

    # Fill in the "First name" field
    name_input = page.get_by_label('First name')
    name_input.fill('Andrejs')

    # Click the "Register" button
    page.get_by_role('button', name='Register').click()

    # Take a screenshot
    page.screenshot(path='screenshots/screenshot.png')
    elements_to_mask = page.locator('.form-control').all()
    page.screenshot(
        path='screenshots/screenshot-advanced1.jpeg',
        full_page=True,
        mask=elements_to_mask,
        mask_color='red'
    )

    # Locate feedback messages
    feedback = page.locator('.invalid-feedback')

    # Ensure all feedback messages are not visible
    for message in feedback.all():
        expect(message).not_to_be_visible()
