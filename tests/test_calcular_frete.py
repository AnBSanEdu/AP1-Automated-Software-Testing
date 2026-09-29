import pytest

def test_calcular_frete():
    from main import calcular_frete

    assert calcular_frete(0) == 10
    assert calcular_frete(5) == 10
    assert calcular_frete(9) == 20
    assert calcular_frete(10) == 20
    assert calcular_frete(30) == 35
    
    
    