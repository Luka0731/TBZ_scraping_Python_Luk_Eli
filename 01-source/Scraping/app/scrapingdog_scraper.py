import requests
import os
from base_scraper import BaseScraper
from app.automation_utils.output import Output



class ScrapingdogScraper(BaseScraper):

    def start(self, config, query, csv_name):
        try:
            html = self._get_results(config["scrapingdog_api_key"], query)
            results = self.parse_google_results(html)
            self.save_to_csv(results, os.path.join(config["output_path"], csv_name))
            return results
        except Exception as e:
            Output.print_error(f"Error: {str(e)}")
            raise



    @staticmethod
    def _get_results(api_key, query):
        url = "https://api.scrapingdog.com/scrape"
        params = {
            "api_key": api_key,
            "url": f"https://google.com/search?q={query}",
            "dynamic": "true"
        }
        response = requests.get(url, params=params)
        credit = response.headers.get('X-RateLimit-Remaining', 'Unknown')
        Output.print_info(f"Remaining API credit: {credit}")
        response.raise_for_status()
        return response.text
