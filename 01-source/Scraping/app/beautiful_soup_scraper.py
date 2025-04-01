import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from base_scraper import BaseScraper
from app.automation_utils.output import Output



class BeautifulSoupScraper(BaseScraper):

    def start(self, config, query, csv_name):
        try:
            driver = self._init_driver(config["chromedriver_path"])
            html = self._get_results(driver, query)
            results = self.parse_google_results(html)
            self.save_to_csv(results, os.path.join(config["output_path"], csv_name))
            return results
        except Exception as e:
            Output.print_error(f"Error: {str(e)}")
            raise
        finally:
            if 'driver' in locals():
                driver.quit()



    @staticmethod
    def _init_driver(driver_path):
        service = Service(driver_path)
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-blink-features=AutomationControlled")
        return webdriver.Chrome(service=service, options=options)



    @staticmethod
    def _get_results(driver, query):
        driver.get(f"https://google.com/search?q={query}")
        time.sleep(2)
        return driver.page_source
