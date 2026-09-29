import pytest

def test_aplicar_desconto():
    from main import aplicar_desconto

    assert aplicar_desconto(100, 10) == 90
    assert aplicar_desconto(200, 0) == 200
    assert aplicar_desconto(50, 100) == 0
    assert pytest.raises(ValueError, aplicar_desconto, 100, -10)