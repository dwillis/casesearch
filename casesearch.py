from playwright.sync_api import sync_playwright
import os

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
    'sec-ch-device-memory': '8',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
    'sec-ch-ua-arch': '"x86"',
    'sec-ch-ua-full-version-list': '" Not A;Brand";v="99.0.0.0", "Chromium";v="102.0.5005.115", "Google Chrome";v="102.0.5005.115"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
}

def main():
    url = "https://casesearch.courts.state.md.us/casesearch/"
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.set_extra_http_headers(headers)
        page.goto(url)

        # Check the checkbox using JavaScript
        checkbox = page.query_selector("input[name='disclaimer']")
        if checkbox:
            page.evaluate("document.querySelector('input[name=\"disclaimer\"]').checked = true;")

        # Click the "I Agree" button
        button = page.get_by_role("button", name="I Agree")
        button.click()

        print(page.url)

        # Find the single h3 tag and print its text
        h3_element = page.query_selector("h3")
        if h3_element:
            print(h3_element.inner_text())
        else:
            print("No h3 tag found.")

        browser.close()

if __name__ == "__main__":
    main()
