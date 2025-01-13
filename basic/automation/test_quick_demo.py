from playwright.sync_api import Page, expect

def test_quick_demo(page: Page):
    # Navigate to the correct URL
    page.goto('http://example.com')  # Replace with the correct URL
    page.get_by_label('Date of birth').fill('2024-10-10')
    page.get_by_role(role='button', name='Register').click()

    feedback = page.locator('.invalid-feedback')
    for message in feedback.all():
        expect(message).to_be_visible(timeout=1000)

def test_quick_demo_2(page: Page):
    # Ensure localhost server is running
    page.goto('http://localhost:8000/')
    page.get_by_label('Last name').fill('Andrejs')
    page.get_by_label('Date of birth').fill('2024-10-10')
    page.get_by_role(role='button', name='Register').click()

    feedback = page.locator('.invalid-feedback').first
    expect(feedback).to_be_visible()
