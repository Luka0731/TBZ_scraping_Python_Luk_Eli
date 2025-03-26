from app.automation_utils.output import Output
from scraping_app import ScrapingApp

Output.print_info("sdklaskl")
Output.print_error("Etwas lief falsch")
Output.print_warning("Pass langsam auf")
Output.print_success("Juhu hat funktioniert")

Output.menu("Titleee", ["exit", "analise file", "nothing"])


app = ScrapingApp("WEB SCRAPER TOOL")
app.start()



# todo: Datenbank-Integration
# todo: Parametrisierung & Konfiguration
# todo: Fehlerbehandlung
# todo: Pagination & Mehrere Seiten Scrapen
# todo: Proxy-Rotation & User-Agent-Rotation
# todo: Erweiterte Datenanalyse
# todo: User Interface (Konsole) für alles
# todo: PowerShell-Alternative (Erweiterung)
