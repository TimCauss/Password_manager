
# Var
alpha_min = "abcdefghijklmnopqrstuvwxyz"
alpha_maj = "ABCDEJGHIJKLMNOPQRSTUVWXYZ"
num = "0123456789"
special_char = "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~" + "\""

all_chars = f"{alpha_min}{alpha_maj}{num}{special_char}"


# Function who return a string from args
def randomizer(lenght: int, alpha=True, num=True, specials=True) -> str:
    pass
