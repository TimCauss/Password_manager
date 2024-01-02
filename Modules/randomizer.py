import random

# Var
alpha_min = "abcdefghijklmnopqrstuvwxyz"
alpha_maj = "ABCDEJGHIJKLMNOPQRSTUVWXYZ"
num = "0123456789"
special_char = "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~" + "\""

all_chars = f"{alpha_min}{alpha_maj}{num}{special_char}"


# Function who return a string from args
def randomizer(lenght: int, alpha_maj=True, num=True, specials=True) -> str:
    word = ''
    while len(word) < lenght:
        if not (alpha_maj or num or specials):
            word.append(random.choice(alpha_min))
        if not (num or special_char):
            word.append(random.choice(alpha_min+alpha_min))
        if not (special_char):
            word.append(random.choice(alpha_min+alpha_maj+num))
        else:
            word.append(random.choice(alpha_min+alpha_maj+num+special_char))
    return word
