import os
import time
from app.automation_utils.input import Input
from app.automation_utils.output import Output
from app.beautiful_soup_scraper import BeautifulSoupScraper
from app.config_handler import ConfigHandler
from app.scrapingdog_scraper import ScrapingdogScraper



class ScrapingApp(object):

    def __init__(self, title):
        self._is_running = True
        self._title = title
        self._CONFIG_PATH = os.path.join("configurations", "config.json")  # Verbessert Pfadhandling
        self._config_file = None
        os.makedirs("configurations", exist_ok=True)  # Erstellt Config-Verzeichnis falls nicht vorhanden



    def start(self):
        self._print_header()
        while self._is_running:
            try:  # Exception-Handling hinzugefügt
                self._make_configurations()
                self._main_menu()
            except Exception as e:
                Output.print_error(f"An error occurred: {str(e)}")
        self._print_footer()



    def _print_header(self):
        border = "//////////////////////////////////////////////////////////////////////////"
        width = len(border)
        print("\n" + border)
        print(self._title.center(width))
        print(border)
        print("\nWelcome to the Web Scraper!")
        print("\nThis tool automatically extracts and analyzes data from websites.")
        print("It can scrape search results, product listings, or any structured")
        print("information and save it to a csv file.")
        print("\nKey features:")
        print("- Multiple APIs")
        print("- Customizable queries")
        print("- CSV export")
        print("\n" + border)
        input("\nPress Enter to start the program... ")
        if not os.path.exists(self._CONFIG_PATH):
            print("\nSince you are probably opening the program for the first time, " +
                  "the scraping program needs some basic configurations")



    def _make_configurations(self):
        config_handler = ConfigHandler()
        self._config_file = config_handler.load_or_create_config(self._CONFIG_PATH)



    def _main_menu(self):
        option = Output.menu("Main Menu", ["Exit", "Scrape", "Reset Configurations"])
        if option == 0:
            self._is_running = False
        elif option == 1:
            self._scrape()
        elif option == 2:
            if os.path.exists(self._CONFIG_PATH):
                os.remove(self._CONFIG_PATH)
            self._config_file = None



    def _scrape(self):
        search_query = Input.get_string("\nSearch query: ").strip()
        if not search_query:
            Output.print_error("Search query cannot be empty")
            return

        csv_name = Input.get_string("CSV name: ").strip()
        if not csv_name:
            Output.print_error("CSV name cannot be empty")
            return

        try:  # Exception-Handling hinzugefügt
            if self._config_file["scraper_engine"] == 1:
                Output.print_warning("\nPlease do not change Pages while the browser is open, it will close after a time!")
                time.sleep(1)
                scraper = BeautifulSoupScraper()
                scraper.start(self._config_file, search_query, csv_name + ".csv")
            else:
                scraper = ScrapingdogScraper()
                scraper.start(self._config_file, search_query, csv_name + ".csv")
        except KeyError:
            Output.print_error("Invalid configuration. Please reset configurations.")
        except Exception as e:
            Output.print_error(f"Scraping failed: {str(e)}")



    def _print_footer(self):
        print("\nThank you for using the " + self._title + "!")
        print("\n//////////////////////////////////////////////////////////////////////////")
