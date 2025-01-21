from playwright.sync_api import sync_playwright, Page

def test_cookies():
    with sync_playwright() as p:
        # Launch the browser in non-headless mode
        browser = p.chromium.launch(headless=False, slow_mo=500)
        context = browser.new_context()
        page = context.new_page()

        # Navigate to the domain associated with the cookie
        page.goto('https://playwright.dev/python/')

        # Print cookies before adding any
        print("Before adding cookies:", page.context.cookies())

        # Add a new cookie
        page.context.add_cookies([{
            'name': 'cookie1',
            'value': 'abc',
            'url': 'https://playwright.dev/python/'
        }])

        # Assertions
        cookies = page.context.cookies()
        assert len(cookies) == 1, "Expected 1 cookie, but found a different number."

        cookie = next((c for c in cookies if c['name'] == 'cookie1'), None)
        assert cookie is not None, "Cookie 'cookie1' was not found."
        assert cookie['value'] == 'abc', f"Expected cookie value 'abc', but got '{cookie['value']}'."
        assert cookie['domain'] == 'playwright.dev', f"Expected domain 'playwright.dev', but got '{cookie['domain']}'."

        # Check JavaScript access
        cookie_value = page.evaluate("document.cookie")
        assert 'cookie1=abc' in cookie_value, "Cookie 'cookie1' is not accessible in JavaScript."

        # Print cookies after adding
        print("After adding cookies:", page.context.cookies())

        # Clear all cookies
        page.context.clear_cookies()

        # Print cookies after clearing
        print("After clearing cookies:", page.context.cookies())

        # Close the browser
        browser.close()

if __name__ == "__main__":
    test_cookies()
