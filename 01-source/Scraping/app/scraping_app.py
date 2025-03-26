from app.automation_utils.console_style import ConsoleStyle
from app.automation_utils.output import Output

class ScrapingApp(object):

    def __init__(self, title):
        self._is_running = True
        self._title = title

    def start(self):
        self._print_header()
        while self._is_running:
            self._main_menu()
        print("Thank you for using the " + self._title + "!" )

    def _print_header(self):
        border = "//////////////////////////////////////////////////////////////////////////"
        width = len(border)

        print("\n" + border)
        print(self._title.center(width))
        print(border)
        print("\nWelcome to the Web Scraper!")
        print("\nThis tool automatically extracts and analyzes data from websites.")
        print("It can scrape search results, product listings, or any structured")
        print("information and save it to a database for further processing.")
        print("\nKey features:")
        print("- Google Search scraping")
        print("- Customizable queries")
        print("- SQLite/CSV export")
        print("- Anti-bot evasion techniques")
        print("\n" + border)
        input("\nPress Enter to start the program... ")

    def _main_menu(self):
        input = Output.menu("Main Menu", ["", "", ""])
