from playwright.sync_api import sync_playwright, Playwright
from rich import print


def run(playwright: Playwright):
    start_url = "https://www.oddsportal.com/football/spain/laliga/"
    firefox = playwright.firefox
    browser = firefox.launch(headless=False)
    page = browser.new_page()
    page.goto(start_url)

    while True:
        for link in page.locator("a[data-selenium='miniProductPageDetailsGridViewNameLink']").all():
            p = browser.new_page(base_url="https://www.oddsportal.com")
            url = link.get_attribute("href")

            if url is not None:
                p.goto(url)
            else:
                p.close()
    

with sync_playwright() as playwright:
    run(playwright)