from Modules.randomizer import randomizer
import re

word_lenght = 5


def test_randomizer_with_min_alpha_only():
    result = randomizer(word_lenght, False, False, False)
    match = re.fullmatch(r'\b[a-z]{5}\b', result)
    assert match is not None
