import json
import os
import requests
from app.automation_utils.input import Input
from app.automation_utils.output import Output



class ConfigHandler(object):

    def load_or_create_config(self, config_path):
        """Loads the configuration file or prompts user input and creates it"""
        try:
            if os.path.exists(config_path):
                with open(config_path, "r") as config_file:
                    config = json.load(config_file)
                    self._validate_config(config)
                    return config
            return self._configurate_new_file(config_path)
        except Exception as e:
            Output.print_error(f"Error handling configuration: {str(e)}")
            raise



    @staticmethod
    def _validate_config(config):
        """Validates the loaded configuration"""
        required_keys = ["chromedriver_path", "output_path", "scraper_engine", "scrapingdog_api_key"]
        for key in required_keys:
            if key not in config:
                raise ValueError(f"Missing required config key: {key}")

        if not os.path.exists(config["chromedriver_path"]):
            raise FileNotFoundError(f"ChromeDriver path does not exist: {config['chromedriver_path']}")

        if not os.path.exists(config["output_path"]):
            raise FileNotFoundError(f"Output path does not exist: {config['output_path']}")

        if config["scraper_engine"] not in [1, 2]:
            raise ValueError(f"Invalid scraper engine: {config['scraper_engine']}")



    @staticmethod
    def _validate_chromedriver_path(path):
        """Validates the ChromeDriver path"""
        if not os.path.exists(path):
            raise FileNotFoundError(f"The specified ChromeDriver path does not exist: {path}")

        if not path.lower().endswith("chromedriver.exe"):
            raise ValueError("The specified path does not point to a ChromeDriver executable")

        # Optional: Check if the file is actually executable
        if not os.access(path, os.X_OK):
            raise PermissionError(f"No execute permissions for ChromeDriver at: {path}")



    @staticmethod
    def _configurate_new_file(config_path):
        """Gets the user input and creates new configuration file"""
        try:
            # ChromeDriver path configuration
            while True:
                try:
                    chromedriver_path = Input.get_string("Enter the path to ChromeDriver: ").strip()
                    ConfigHandler._validate_chromedriver_path(chromedriver_path)
                    break
                except Exception as e:
                    Output.print_error(f"Invalid ChromeDriver path: {str(e)}")

            # Output path configuration
            while True:
                output_path = Input.get_string("Enter the output path for the CSV files: ").strip()
                if not output_path:
                    Output.print_error("Output path cannot be empty.")
                    continue
                try:
                    if not os.path.exists(output_path):
                        create_dir = Input.get_boolean("Path does not exist. Create it now? (y/n): ")
                        if create_dir:
                            os.makedirs(output_path)
                            break
                        continue
                    break
                except Exception as e:
                    Output.print_error(f"Error with output path: {str(e)}")

            # Scraper engine selection
            print("\nOptions: [0 = More Information, 1 = BeautifulSoup and Selenium, 2 = Scrapingdog]")
            scraper_engine = Input.get_integer_range("Which tool would you like to use for scraping: ", 0, 2)

            if scraper_engine == 0:
                print(
                    "\nSelenium + BeautifulSoup offers full control but can get blocked when scraping large amounts of "
                    "\ndata. Scrapingdog handles restrictions automatically, making it more reliable for large-scale "
                    "\nscraping, but it requires an account and has API limits. Choose based on flexibility vs. ease "
                    "\nof use.")
                print("\nOptions: [1 = BeautifulSoup and Selenium, 2 = Scrapingdog]")
                scraper_engine = Input.get_integer_range("Which tool would you like to use for scraping: ", 1, 2)

            # API key configuration if needed
            scrapingdog_api_key = "None"
            if scraper_engine == 2:
                while True:
                    try:
                        scrapingdog_api_key = input("Enter the Scrapingdog API key: ").strip()
                        if not scrapingdog_api_key:
                            raise ValueError("API key cannot be empty")

                        test_url = "https://api.scrapingdog.com/google/"
                        test_params = {"api_key": scrapingdog_api_key, "query": "test", "results": 1}
                        response = requests.get(test_url, params=test_params, timeout=10)

                        if response.status_code != 200:
                            raise ValueError(f"API test failed with status code {response.status_code}")

                        Output.print_success("API key is valid.")
                        break
                    except requests.RequestException as e:
                        Output.print_error(f"Network error testing API key: {str(e)}")
                    except Exception as e:
                        Output.print_error(f"Invalid API key: {str(e)}")

            # Create config data
            config_data = {
                "chromedriver_path": os.path.normpath(chromedriver_path).replace("\\", "/"),
                "output_path": os.path.normpath(output_path).replace("\\", "/"),
                "scraper_engine": scraper_engine,
                "scrapingdog_api_key": scrapingdog_api_key
            }

            # Save config file
            with open(config_path, "w") as config_file:
                json.dump(config_data, config_file, indent=4)

            Output.print_success("\nConfiguration was successfully created")
            return config_data

        except Exception as e:
            Output.print_error(f"Error creating configuration: {str(e)}")
            raise
