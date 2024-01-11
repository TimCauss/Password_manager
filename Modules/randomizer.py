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
        self.password = self.generate_password()

    def generate_password(self) -> str:
        """Generates a random password based on specified options."""
        password_tmp = ''
        password_tmp_mixed = ''
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
        password_tmp_mixed = self.mix_password(password_tmp)

        return password_tmp_mixed

    def get_password_config(self) -> dict:
        """Return the config dict"""
        return self.password_content

    def password(self) -> str:
        return self.password

    def mix_password(self, word=None) -> str:
        if word is None:
            word = self.password
        list_word = list(word)
        tmp_word = ''
        while len(list_word) > 0:
            tmp_word += list_word.pop(secrets.choice(range(len(list_word))))
        return tmp_word
