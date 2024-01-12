from Modules.PasswordCreator import randomizer, PasswordCreator
import re
import sys


word_lenght = 5


def test_randomizer_with_min_alpha_only():
    result = randomizer(word_lenght, False, False, False)
    match = re.fullmatch(r'\b[a-z]{5}\b', result)
    assert match is not None


for _ in range(10):
    print(f"Password {_}: {randomizer(25)}")

for _ in range(10):
    password = PasswordCreator(25)
    print(f"Password {_}: {password.password}")
