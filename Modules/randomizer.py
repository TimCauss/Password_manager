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
        self.uppers = int((self.length * use_upper_chars) / 100)
        self.numbers = int((self.length * use_num) / 100)
        self.special_chars = int((self.length * use_special_chars) / 100)
        self.lowers = int(self.length - (self.uppers +
                          self.numbers + self.special_chars))
        self.password_content = {
            "upper": self.uppers, "numbers": self.numbers,
            "special chars": self.special_chars
        }

    def calcul_password_content(self) -> dict:
        """return password config"""
        return self.password_content

    def generate_password(self) -> str:
        """Generates a random password based on specified options."""
        password_tmp = ''
        password_tmp_mixed = []
        for _ in range(self.lowers):
            password_tmp += password_tmp.join(
                secrets.choice(string.ascii_lowercase))
        for _ in range(self.uppers):
            password_tmp += password_tmp.join(
                secrets.choice(string.ascii_uppercase))
        for _ in range(self.numbers):
            password_tmp += password_tmp.join(
                secrets.choice(string.digits))
        for _ in range(self.special_chars):
            password_tmp += password_tmp.join(
                secrets.choice(string.punctuation))
        list_password_tmp = list(password_tmp)
        while len(list_password_tmp) > 0:
            password_tmp_mixed += list_password_tmp.pop(
                secrets.choice(range(len(list_password_tmp))))
        print(f"pass not mixed: {password_tmp}\n")
        return (password_tmp_mixed)

    def show_config(self) -> dict:
        """Return the config dict"""
        return self.password_content
