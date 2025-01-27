import html

class HtmlPagesConverter:
    def __init__(self, open_file):
        self.open_file = open_file
        self._find_page_breaks()

    def _find_page_breaks(self):
        """Read the file and note the positions of the page breaks so we can access them quickly"""
        self.breaks = [0]
        while True:
            line = self.open_file.readline()
            if not line:
                break
            if "PAGE_BREAK" in line:
                self.breaks.append(self.open_file.tell())
        self.breaks.append(self.open_file.tell())  # To handle the end of the file

    def get_html_page(self, page, html_converter=None):
        """Return HTML page with the given number (zero indexed)"""
        page_start = self.breaks[page]
        page_end = self.breaks[page + 1]  # Correctly reference the next page

        html_output = ""
        self.open_file.seek(page_start)

        # If no html_converter is provided, use the built-in html module
        if html_converter is None:
            html_converter = html  # Use the built-in `html` module here

        while self.open_file.tell() != page_end:
            line = self.open_file.readline()
            if "PAGE_BREAK" in line:
                continue
            line = line.strip()  # Strip any extra spaces or newlines
            html_output += html_converter.escape(line, quote=False)  # Escape the HTML content
            html_output += "<br />"  # Append the <br /> tag for line break

        return html_output
