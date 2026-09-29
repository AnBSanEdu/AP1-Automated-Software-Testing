import pytest

def test_senha_valida():
    from main import senha_valida

    assert senha_valida("Abcdef1!") is True
    assert senha_valida("Abcde1") is False
    assert senha_valida("Abcdefgh!") is False
    assert senha_valida("Abcde123") is True