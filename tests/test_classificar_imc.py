import pytest

def test_classificar_imc():
    from main import classificar_imc

    assert classificar_imc(17) == "Abaixo do peso"
    assert classificar_imc(22) == "Peso normal"
    assert classificar_imc(30) == "Acima do peso"
    assert classificar_imc(18.5) == "Peso normal"