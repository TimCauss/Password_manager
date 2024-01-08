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
