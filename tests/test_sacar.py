import pytest

def test_sacar():
    from main import sacar

    assert sacar(100, 50) == 50
    assert pytest.raises(ValueError, sacar, 100, 150)