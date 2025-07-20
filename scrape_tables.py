from playwright.sync_api import sync_playwright
import re

def scrape_and_sum(url):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url)
        
        total = 0
        tables = page.query_selector_all("table")
        for table in tables:
            rows = table.query_selector_all("tr")
            for row in rows:
                cells = row.query_selector_all("td,th")
                for cell in cells:
                    text = cell.inner_text()
                    numbers = re.findall(r'-?\d+\.?\d*', text)
                    for num in numbers:
                        total += float(num)
        
        browser.close()
        return total

if __name__ == "__main__":
    urls = [f"https://sanand0.github.io/tdsdata/js_table/?seed={i}" for i in range(38, 48)]
    grand_total = sum(scrape_and_sum(url) for url in urls)
    print(f"GRAND_TOTAL={grand_total}")
