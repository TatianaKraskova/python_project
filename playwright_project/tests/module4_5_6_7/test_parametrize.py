import pytest
from playwright.sync_api import sync_playwright, expect
from playwright_project.tests.utils.constant import BASE_URL

@pytest.mark.parametrize('name, last_name, is_active, id', [
    ('Bob', 'Smith', False, 123),
    ('Alexandrina', 'Johnson', True, 456),
])
def test_single_param(name: str, last_name: str, is_active: bool, id: int):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)  # Добавляем slow_mo здесь
        context = browser.new_context()
        page = context.new_page()

        page.goto(BASE_URL)

        name_input = page.get_by_label("First name")
        name_input.fill(name)
        expect(name_input).to_have_value(name)

        browser.close()
