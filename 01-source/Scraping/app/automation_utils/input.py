from typing import *
from app.automation_utils.output import Output

class Comparable(Protocol):
    def __lt__(self, other: Any) -> bool: ...
    def __gt__(self, other: Any) -> bool: ...

T = TypeVar('T', bound=Comparable)

class Input:
    """A utility class for handling various types of user input with validation."""

    # Generic input reader with validation
    @staticmethod
    def _read_input(
            prompt: str,
            input_type: Callable[[str], T],
            min_val: Optional[T] = None,
            max_val: Optional[T] = None,
            allowed_values: Optional[List[T]] = None
    ) -> T:
        while True:
            try:
                user_input = input(prompt)
                value = input_type(user_input)

                # Check against allowed values if specified
                if allowed_values and value not in allowed_values:
                    Output.print_error(f"Error: Value must be one of {allowed_values}")
                    continue

                # Check min/max bounds
                if (min_val is not None and value < min_val) or \
                        (max_val is not None and value > max_val):
                    Output.print_error(f"Error: Value must be between {min_val} and {max_val}")
                    continue

                return value

            except ValueError:
                Output.print_error("Error: Invalid input type. Please try again.")



    # |------- Basic type inputs -------|

    @staticmethod
    def get_integer(prompt: str) -> int:
        return Input._read_input(prompt, int)

    @staticmethod
    def get_boolean(prompt: str) -> bool:
        """Accepts various true/false inputs including yes/no, y/n, 1/0"""
        true_values = {'true', 'yes', 'y', 't', '1', 'ja', 'j', 'wahr', 'w'}
        false_values = {'false', 'no', 'n', 'f', '0', 'falsch', 'nein'}

        while True:
            user_input = input(prompt).strip().lower()
            if user_input in true_values:
                return True
            if user_input in false_values:
                return False
            Output.print_error("Error: Please enter a boolean value (true/false, yes/no, y/n)")

    @staticmethod
    def get_string(prompt: str) -> str:
        return input(prompt).strip()



    # |------- Range-constrained inputs -------|

    @staticmethod
    def get_integer_range(prompt: str, min_val: int, max_val: int) -> int:
        return Input._read_input(prompt, int, min_val, max_val)

    @staticmethod
    def get_float_range(prompt: str, min_val: float, max_val: float) -> float:
        return Input._read_input(prompt, float, min_val, max_val)



    # |------- Allowed values inputs -------|

    @staticmethod
    def get_integer_options(prompt: str, allowed_values: List[int]) -> int:
        return Input._read_input(prompt, int, None, None, allowed_values)

    @staticmethod
    def get_string_options(prompt: str, allowed_values: List[str]) -> str:
        while True:
            user_input = input(prompt).strip()
            if user_input in allowed_values:
                return user_input
            Output.print_error(f"Error: Value must be one of {allowed_values}")



    # |------- Length-constrained strings -------|

    @staticmethod
    def get_string_length(prompt: str, min_len: int, max_len: int) -> str:
        while True:
            user_input = input(prompt).strip()
            if min_len <= len(user_input) <= max_len:
                return user_input
            Output.print_error(f"Error: Input must be between {min_len} and {max_len} characters")

    @staticmethod
    def get_string_exact_length(prompt: str, length: int) -> str:
        return Input.get_string_length(prompt, length, length)
