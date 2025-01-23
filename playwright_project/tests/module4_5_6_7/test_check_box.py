from playwright.sync_api import Page, expect

from playwright_project.tests.utils.constant import BASE_URL

def test_check(page: Page):
    page.goto(BASE_URL)
    checkbox = page.get_by_role('checkbox')
    textarea = page.locator('#referralText')
    message = 'msg'
    checkbox.check()
    expect(checkbox).to_be_checked()
    textarea.fill(message)
    expect(textarea).to_have_value(message)
