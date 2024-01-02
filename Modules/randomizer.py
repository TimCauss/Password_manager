import random

# Var
alpha_min = "abcdefghijklmnopqrstuvwxyz"
alpha_maj = "ABCDEJGHIJKLMNOPQRSTUVWXYZ"
num = "0123456789"
special_char = "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~" + "\""

all_chars = f"{alpha_min}{alpha_maj}{num}{special_char}"


# Function who return a string from args
def randomizer(length: int, use_alpha_maj=True, use_num=True, use_specials=True) -> str:
    characters = alpha_min
    if use_alpha_maj:
        characters += alpha_maj
    if use_num:
        characters += num
    if use_specials:
        characters += special_char

    return ''.join(random.choice(characters) for _ in range(length))
