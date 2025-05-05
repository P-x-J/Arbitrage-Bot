from playwright.sync_api import sync_playwright

def scrape_odds():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)  # Set True if you don't want to see the browser
        page = browser.new_page()

        # Step 1: Go to La Liga odds page
        page.goto("https://www.oddsportal.com/soccer/spain/laliga/")

        # Step 2: Click on the first match listed
        page.wait_for_selector("table.table-main")
        match_links = page.query_selector_all("table.table-main a[href*='/soccer/spain/laliga/']")
        if not match_links:
            print("No match links found.")
            browser.close()
            return

        match_links[0].click()

        # Step 3: Wait and extract odds
        page.wait_for_selector("table#odds-data-table")
        odds_rows = page.query_selector_all("table#odds-data-table tbody tr")

        odds_data = []
        for row in odds_rows[:5]:  # Limit to top 5 bookmakers
            try:
                bookmaker = row.query_selector("td.bookmaker-name").inner_text()
                odds = row.query_selector_all("td.odds")
                home = float(odds[0].inner_text())
                draw = float(odds[1].inner_text())
                away = float(odds[2].inner_text())
                odds_data.append({
                    "bookmaker": bookmaker,
                    "home": home,
                    "draw": draw,
                    "away": away
                })
            except:
                continue

        browser.close()
        return odds_data


# Run it
odds = scrape_odds()
for o in odds:
    print(o)