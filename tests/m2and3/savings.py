from playwright.sync_api import Page

from tests.utils.constant import BASE_URL


def test_filtering_demo(page: Page):
    # Navigate to the savings.html page
    page.goto(f'{BASE_URL}savings.html')

    # Get all rows in the table
    rows = page.get_by_role('row')
    print(f"Total rows: {rows.count()}")

    # Filter the row with text 'Competition'
    row = page.get_by_role('row').filter(has_text='Competition')
    print(f"Text content of the filtered row: {row.text_content()}")

    cell = page.get_by_role('row').filter(has_text='Competition').get_by_role('cell').nth(1)
    print('Cell:')
    print(cell.text_content())
