import pytest
import string
from Modules.randomizer import PasswordCreator


def test_password_length():
    length = 15
    password = PasswordCreator(15)
    assert len(password.password) == length
