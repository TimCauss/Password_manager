import secrets
import string


# Function who return a string from args
def randomizer(length: int, use_alpha_maj=True,
               use_num=True,
               use_specials=True) -> str:
    characters = string.ascii_lowercase
    if use_alpha_maj:
        characters += string.ascii_uppercase
    if use_num:
        characters += string.digits
    if use_specials:
        characters += string.punctuation
    return ''.join(secrets.choice(characters) for _ in range(length))


class PasswordCreator:
    """
    Represents a password generator with configurable options.
    """

    def __init__(self, length: int, use_alpha_maj=True,
                 use_num=True, use_special_chars=True) -> object:
        self.length = length
        self.use_alpha_maj = use_alpha_maj
        self.use_num = use_num
        self.use_special_chars = use_special_chars

    def generate_password(self) -> str:
        """Generates a random password based on specified options."""
        characters = string.ascii_lowercase
        if self.use_alpha_maj:
            characters += string.ascii_uppercase
        if self.use_num:
            characters += string.digits
        if self.use_special_chars:
            characters += string.punctuation
        return ''.join(secrets.choice(characters) for _ in range(self.length))

    def add_uppercase(self) -> None:
        """Enables the use of uppercase letters in generated passwords."""
        self.use_alpha_maj = True

    def remove_uppercase(self) -> None:
        """Disables the use of uppercase letters in generated passwords."""
        self.use_alpha_maj = False

    def add_numbers(self) -> None:
        """Enables the use of numbers in generated passwords."""
        self.use_num = True

    def remove_numbers(self) -> None:
        """Disables the use of numbers in generated passwords."""
        self.use_num = False

    def add_special_chars(self) -> None:
        """Enables the use of special characters in generated passwords."""
        self.use_special_chars = True

    def remove_special_chars(self) -> None:
        """Disables the use of special characters in generated passwords."""
        self.use_special_chars = False
