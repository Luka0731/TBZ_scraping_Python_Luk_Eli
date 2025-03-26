from app.automation_utils.console_style import ConsoleStyle

class Output:

    @staticmethod
    def print_error(text: str):
        print(ConsoleStyle.BRIGHT_RED.format(f"✘ {text}"))

    @staticmethod
    def print_success(text: str):
        print(ConsoleStyle.BRIGHT_GREEN.format(f"✓ {text}"))

    @staticmethod
    def print_warning(text: str):
        print(ConsoleStyle.BRIGHT_YELLOW.format(f"⚠ {text}"))

    @staticmethod
    def print_info(text: str):
        print(ConsoleStyle.BRIGHT_CYAN.format(f"ℹ {text}"))

    @staticmethod
    # generates automatically a menu gets the right input
    def menu(title: str, options: list[str]) -> int:
        # Build the options string
        option_text = "| "
        for index, option in enumerate(options):
            option_text += f"{index} = {option} | "

        # Create the decorative bars
        upper_bar_text = f"/// {title} ///" + "/" * (len(option_text) - 8 - len(title))
        lower_bar_text = "/" * len(option_text)

        # Print the menu
        print(f"\n{upper_bar_text}")
        print("Please select an option:")
        print(option_text)
        print(lower_bar_text)

        # Get valid user input
        while True:
             try:
                choice = int(input(": "))
                if 0 <= choice < len(options):
                    return choice
                Output.print_error(f"Please enter a number between 0 and {len(options) - 1}")
             except ValueError:
                 Output.print_error("Please enter a valid number")
