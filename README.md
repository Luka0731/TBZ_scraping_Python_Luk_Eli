
WEB SCRAPER TOOL
================


Description:
------------
This Python tool automates Google search result scraping using two different tools:
1. BeautifulSoup + Selenium (local)
2. Scrapingdog API (cloud-based)

Results are saved as CSV files.


Requirements:
-------------
1. Python 3.8 or higher installed
2. Required Python packages:
   pip install selenium beautifulsoup4 pandas requests

3. For Selenium:
   - Chrome browser installed
   - Matching ChromeDriver version downloaded and configured
   (Download: https://chromedriver.chromium.org/downloads)

4. For Scrapingdog:
   - Register for free API key at https://www.scrapingdog.com/
   - Provide API key in configuration


Initial Configuration:
------------
   - Run program: python main.py
   - Provide path to chromedriver.exe
   - Select output directory for CSV files
   - Choose scraping method (Selenium or Scrapingdog)
   - For Scrapingdog: Enter API key


Important Notes:
----------------
- When using Selenium:
  - Don't interact with browser window during scraping
  - ChromeDriver version must match Chrome browser version

- When using Scrapingdog:
  - API credits remaining are shown after each request
  - Free version has limitations

- The program saves:
  - Search result title
  - URL/link
  - Description text


Example Usage:
-------------
1. Start program: python main.py
2. Enter configuration on first run
3. Select "Scrape" in main menu
4. Enter search term (e.g. "Python Web Scraping")
5. Enter filename for CSV (e.g. "results")
6. Results are saved in configured output directory


Troubleshooting:
----------------
- The program shows detailed error messages
- For configuration issues: Use Reset Config
- For API issues: Verify Scrapingdog key
- For Selenium issues: Check ChromeDriver version
