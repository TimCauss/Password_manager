import pytest
import string
from Modules.randomizer import PasswordCreator


@pytest.mark.parametrize("length, expected_length", [(10, 10), (20, 20)])
def test_generate_password(length, expected_length):
    password_creator = PasswordCreator(length=length)
    password = password_creator.generate_password()
    assert len(password) == expected_length


@pytest.mark.parametrize("use_alpha_maj, use_num, use_special_chars",
                         [(True, True, True), (True, True, False), (False, True, True)])
def test_generate_password_with_options(use_alpha_maj, use_num, use_special_chars):
    password_creator = PasswordCreator(length=10,
                                       use_alpha_maj=use_alpha_maj, use_num=use_num,
                                       use_special_chars=use_special_chars)
    password = password_creator.generate_password()

    if use_alpha_maj:
        assert any(c.isupper() for c in password)
    else:
        assert not any(c.isupper() for c in password)

    if use_num:
        assert any(c.isdigit for c in password)
    else:
        assert not any(c.isdigit for c in password)

    if use_special_chars:
        assert any(c in string.punctuation for c in password)
    else:
        assert not any(c in string.punctuation for c in password)


@pytest.fixture
def password_creator(length=10):
    return PasswordCreator(length)


def test_add_uppercase(password_creator):
    password_creator.add_uppercase()
    password = password_creator.generate_password()
    assert any(c.isupper() for c in password)


def test_remove_uppercase(password_creator):
    password_creator.add_uppercase()
    password_creator.remove_uppercase()
    password = password_creator.generate_password()
    assert not any(c.isupper() for c in password)


def test_add_numbers(password_creator):
    password_creator.add_numbers()
    password = password_creator.generate_password()
    assert any(c.isdigit() for c in password)


def test_remove_numbers(password_creator):
    password_creator.add_numbers()
    password_creator.remove_numbers()
    password = password_creator.generate_password()
    assert not any(c.isdigit() for c in password)


def test_add_special_chars(password_creator):
    password_creator.add_special_chars()
    password = password_creator.generate_password()
    assert any(c in string.punctuation for c in password)


def test_remove_special_chars(password_creator):
    password_creator.add_special_chars()
    password_creator.remove_special_chars()
    password = password_creator.generate_password()
    assert not any(c in string.punctuation for c in password)
