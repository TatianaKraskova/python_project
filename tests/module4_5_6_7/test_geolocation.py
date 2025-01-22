import pprint
from playwright.sync_api import sync_playwright

def test_geolocation():
    with sync_playwright() as playwright:
        ipad: dict = playwright.devices['iPad Pro 11']
        pprint.pprint(playwright.devices)  # Print available devices for reference

        ctx = playwright.chromium.launch(headless=False, slow_mo=1000).new_context(
            # **ipad,  # Uncomment this line if you want to simulate the iPad Pro device
            user_agent='Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) '
                       'AppleWebKit/605.1.15 (KHTML, like Gecko) '
                       'Version/18.0 Mobile/15E148 Safari/604.1',
            locale='en_GB',
            geolocation={"longitude": -0.118092, "latitude": 51.509865},  # London coordinates
            permissions=["geolocation"],
            base_url='https://maps.google.com'
        )

        page = ctx.new_page()
        page.goto('')
        page.get_by_role('button', name='Accept all').click()
        page.get_by_role('button', name='Stay on web').click()

        # Allow time to observe actions in the browser
        from time import sleep
        sleep(2)

        ctx.close()
