from playwright.sync_api import sync_playwright

from playwright_project.tests.utils.constant import BASE_URL


def test_download():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        context = browser.new_context(accept_downloads=True)
        page = context.new_page()

        page.goto(f"{BASE_URL}savings.html")

        try:
            with page.expect_download() as download_info:
                page.locator("a.btn-download").click()
            download = download_info.value

            print(f"Download triggered successfully.")
            print(f"Download path: {download.path()}")
            print(f"Suggested filename: {download.suggested_filename}")

            assert download.suggested_filename == "dummy.zip", f"Expected 'dummy.zip', got {download.suggested_filename}"
        except Exception as e:
            print(f"Error: {e}")
            raise

        browser.close()

if __name__ == "__main__":
    test_download()