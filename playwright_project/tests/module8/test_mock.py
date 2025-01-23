from playwright.sync_api import expect, Page

from playwright_project.tests.utils.constant import BASE_URL


def test_route_fulfill(page: Page):
    # Intercept requests for PDF files and respond with a 404
    page.route(
        url='**/*.pdf',
        handler=lambda route: route.fulfill(
            status=404,
            content_type='text/plain',
            body='Not Found'
        )
    )

    # Navigate to the savings page
    page.goto(f'{BASE_URL}savings.html')

    # Simulate clicking the "Download Our Offer" link
    page.get_by_text('Download Our Offer').click()

    # Take a screenshot for debugging
    page.screenshot(path='route.png')

    # Wait for the intercepted URL (PDF) to be handled
    page.wait_for_url('**/*.pdf')

    # Verify the response body contains "Not Found"
    body = page.locator('body')
    expect(body).to_contain_text('Not Found')
