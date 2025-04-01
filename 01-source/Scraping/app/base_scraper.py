import os
import pandas as pd
from bs4 import BeautifulSoup
from app.automation_utils.output import Output



class BaseScraper:

    @staticmethod
    def save_to_csv(data, path):
        """Saves data to CSV with error handling"""
        try:
            os.makedirs(os.path.dirname(path), exist_ok=True)
            pd.DataFrame(data).to_csv(path, index=False)
            Output.print_success(f"Data saved to {path}")
        except Exception as e:
            Output.print_error(f"Failed to save CSV: {str(e)}")
            raise



    @staticmethod
    def parse_google_results(html):
        """Parses Google search results from HTML"""
        try:
            soup = BeautifulSoup(html, 'html.parser')
            return [{
                "title": (h3.text if (h3 := div.find("h3")) else "N/A"),
                "link": (a.get('href') if (a := div.find("a")) else "N/A"),
                "description": (desc.text if (desc := div.find("div", class_="VwiC3b")) else "N/A")
            } for div in soup.find_all("div", class_="tF2Cxc")]
        except Exception as e:
            Output.print_error(f"Parsing failed: {str(e)}")
            raise
