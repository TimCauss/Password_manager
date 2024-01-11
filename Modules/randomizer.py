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

    def __init__(self, length: int, use_upper_chars=40,
                 use_num=20, use_special_chars=20) -> object:
        self.length = length
        self.use_upper_chars = use_upper_chars
        self.use_num = use_num
        self.use_special_chars = use_special_chars
        self.password_content = {}

    def calcul_password_content(self) -> None:
        """Calcul how many lowercase, uppercase, numbers and spe chars"""
        if self.use_upper_chars:
            self.password_content = {"uppers": (
                self.length * self.use_upper_chars) / 100}

    def generate_password(self) -> str:
        """Generates a random password based on specified options."""
        characters = string.ascii_lowercase
        if self.use_upper_chars:
            characters += string.ascii_uppercase
        if self.use_num:
            characters += string.digits
        if self.use_special_chars:
            characters += string.punctuation
        return ''.join(secrets.choice(characters) for _ in range(self.length))
