from playwright.sync_api import Page, expect

def test_homepage_title(page: Page):
        page.goto('https://localhost:8000/')

def test_homepage_header(page: Page):
    page.goto('http://localhost:8000/index.html')  # Add 'index.html'
    header = page.locator('h1')  # Correct header locator
    assert header.text_content() == 'Register to become a member'
    expect(page).to_have_url('http://localhost:8000/index.html')

