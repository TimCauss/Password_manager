import pytest
import string
import random
from Modules.PasswordCreator import PasswordCreator


class TestPasswordCreator:

    def test_init(self):
        password_creator = PasswordCreator(length=10)
        assert password_creator.length == 10
        assert password_creator.uppers == 4
        assert password_creator.numbers == 2
        assert password_creator.special_chars == 2
        assert password_creator.lowers == 2
